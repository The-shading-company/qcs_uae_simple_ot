import frappe

def check_dis(self, event):
	user = frappe.db.get_value("User", {"email": frappe.session.user}, "name")
	roles = frappe.get_roles(user)
	required_role = "Sales User"
	if required_role not in roles:
		required_role1 = "Sales Manager"
		if required_role1 not in roles:
			pass
		else:
			com = frappe.get_doc("Company", self.company)
			sales_manager_dis = com.custom_sales_manager_max_discount
			sale_dis = sales_manager_dis/100
			tab = self.items
			for i in range(0, len(tab)):
				if (tab[i].get("price_list_rate")):
					price_amount = tab[i].get("price_list_rate")
					dis_amount = price_amount-(price_amount * sale_dis)
					if (dis_amount < tab[i].get("rate")):
						pass
					else:
						frappe.throw("Set Rate Greater than Discount Amount {0} for {1}".format(dis_amount, tab[i].get("item_code")))
	  
			if self.discount_amount:
				total = self.total
				grand_total = self.grand_total
				to_dis_amount = total-(total * sale_dis)
				if (to_dis_amount < grand_total):
					pass
				else:
					frappe.throw("Make Sure Grand Total Greater than Total Discount Amount {0}".format(to_dis_amount))

	else:
		com = frappe.get_doc("Company", self.company)
		sales_man_dis = com.custom_sales_man_max_discount
		sale_dis = sales_man_dis/100
		tab = self.items
		for i in range(0, len(tab)):
			if (tab[i].get("price_list_rate")):
				price_amount = tab[i].get("price_list_rate")
				dis_amount = price_amount-(price_amount * sale_dis)
				if (dis_amount < tab[i].get("rate")):
					pass
				else:
					frappe.throw("Set Rate Greater than Discount Amount {0} for {1}".format(dis_amount, tab[i].get("item_code")))
	 
		if self.discount_amount:
			total = self.total
			grand_total = self.grand_total
			to_dis_amount = total-(total * sale_dis)
			if (to_dis_amount < grand_total):
				pass
			else:
				frappe.throw("Make Sure Grand Total Greater than Total Discount Amount {0}".format(to_dis_amount))
