import frappe

#checking to see if it is called. i dont think it is but test. was already commented out in hooks

def check_dis(self, event):
    frappe.msgprint("⚠️ check_dis function was called — but validation is currently disabled.")

    # validation is skipped intentionally
    return

    # -------------------------------
    # Below is the original validation logic
    # -------------------------------

    user = frappe.db.get_value("User", {"email": frappe.session.user}, "name")
    roles = frappe.get_roles(user)

    if "Sales User" in roles:
        role_key = "custom_sales_man_max_discount"
    elif "Sales Manager" in roles:
        role_key = "custom_sales_manager_max_discount"
    else:
        return  # no relevant role, skip

    com = frappe.get_doc("Company", self.company)
    allowed_discount = com.get(role_key, 0) / 100

    for item in self.items:
        if not item.get("price_list_rate"):
            continue

        price_list_rate = item.get("price_list_rate")
        allowed_rate = price_list_rate * (1 - allowed_discount)

        if item.get("rate") < allowed_rate:
            frappe.throw(
                f"Set Rate Greater than Discount Amount {allowed_rate} for {item.get('item_code')}"
            )

    if self.discount_amount:
        allowed_total = self.total * (1 - allowed_discount)
        if self.grand_total < allowed_total:
            frappe.throw(
                f"Make Sure Grand Total Greater than Total Discount Amount {allowed_total}"
            )