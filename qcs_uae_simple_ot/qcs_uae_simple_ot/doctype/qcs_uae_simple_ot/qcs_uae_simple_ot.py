# Copyright (c) 2024, QCS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class QCSUAESimpleOT(Document):
	def before_submit(self):
		if (self.time_entries):
			tab = self.time_entries
			emp_doc = frappe.get_doc("Employee", self.employee)
			ot_setup = frappe.get_doc("QCS UAE Simple OT Setup")
			s_com = frappe.get_doc("Salary Component", ot_setup.basic_salary_component)
			basic_amount = s_com.amount
			for i in range(0, len(tab)):
       
		# OverTime
  
				amount = []
				if (emp_doc.holiday_list):
					leave_doc = frappe.get_doc("Holiday List", emp_doc.holiday_list)
					if leave_doc.holidays:
						h_tab = leave_doc.holidays
						h_dates = []
						for j in range(0, len(h_tab)):
							h_date = h_tab[j].get("holiday_date")
							formatted_date = h_date.strftime('%Y-%m-%d')
							h_dates.append(formatted_date)
						dt = tab[i].get("date")
						if (dt in h_dates):
							h_amo = basic_amount * 12/365/8 * tab[i].get("total_hours") * ot_setup.holiday_ot_multiplier
							amount.append(h_amo)
						else:
							n_amo = basic_amount * 12/365/8 * tab[i].get("total_hours") * ot_setup.normal_ot_multiplier
							amount.append(n_amo)
					else:
						n_amo = basic_amount * 12/365/8 * tab[i].get("total_hours") * ot_setup.normal_ot_multiplier
						amount.append(n_amo)
				else:
					n_amo = basic_amount * 12/365/8 * tab[i].get("total_hours") * ot_setup.normal_ot_multiplier
					amount.append(n_amo)
					
				doc = frappe.new_doc("Additional Salary")
				doc.update({
					"employee": self.employee,
					"payroll_date": tab[i].get("date"),
					"salary_component": "Over Time",
					"overwrite_salary_structure_amount": 0,
					"amount": amount[0]
				})
				doc.insert(ignore_permissions=True)
				doc.submit()
				frappe.msgprint("Additional Salary Created Based on Over Time")
    
		# Food OT
  
				if (tab[i].get("territory")):
					tm_doc = frappe.get_doc("QCS UAE Simple OT Timeslots", tab[i].get("timeslot"))
					tm_tab = tm_doc.exclude_territories
					if (tm_tab):
						tm_tt = []
						for t in range(0, len(tm_tab)):
							tm_tt.append(tm_tab[t].get("territory"))
												
						doc_tt = tab[i].get("territory")
						if (doc_tt in tm_tt):
							pass
						else:
							doc = frappe.new_doc("Additional Salary")
							doc.update({
								"employee": self.employee,
								"payroll_date": tab[i].get("date"),
								"salary_component": "OT Food",
								"overwrite_salary_structure_amount": 0,
								"amount": tm_doc.food_allowance
							})
							doc.insert(ignore_permissions=True)
							doc.submit()
							frappe.msgprint("Additional Salary Created Based on OT Food")
							
