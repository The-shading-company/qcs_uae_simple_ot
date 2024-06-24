# Copyright (c) 2024, Quark Cyber Systems FZC and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data


def get_columns(filters):
	columns = [
		{
			"label": ("Employee"),
			"fieldname": "employee",
			"fieldtype": "Link",
			"options": "Employee",
		},
		{
			"label": ("Basic Salary"),
			"fieldname": "basic",
			"fieldtype": "Currency",
		},
		{
			"label": ("Total Hrs"),
			"fieldname": "total_hrs",
			"fieldtype": "Float",
		},
		{
			"label": ("Holiday Hrs"),
			"fieldname": "ho_hrs",
			"fieldtype": "Float",
		},
		{
			"label": ("Holiday Amount 50%"),
			"fieldname": "ho_amount",
			"fieldtype": "Currency",
			"width": 100,
		},
		# {
		# 	"label": ("Friday Hrs"),
		# 	"fieldname": "fri_hrs",
		# 	"fieldtype": "Float",
		# },
		# {
		# 	"label": ("Friday Amount 50%"),
		# 	"fieldname": "fri_amount",
		# 	"fieldtype": "Currency",
		# },
  		{
			"label": ("Normal Day Hrs"),
			"fieldname": "nor_hrs",
			"fieldtype": "Float",
		},
		{
			"label": ("Normal Day Amount 25%"),
			"fieldname": "nor_amount",
			"fieldtype": "Currency",
		},
		{
			"label": ("Total"),
			"fieldname": "total",
			"fieldtype": "Currency",
		},
		{
			"label": ("Food Expenses"),
			"fieldname": "food_ex",
			"fieldtype": "Currency",
		},
		{
			"label": ("Grand Total"),
			"fieldname": "grand_total",
			"fieldtype": "Currency",
		},
	]
	
	return columns


def get_data(filters):
	data = []
 
	if filters.get("employee"):
		query_filters = []
		if filters.get("company"):
			query_filters.append(["company", "=", filters["company"]])
	
		if filters.get("employee"):
			query_filters.append(["employee", "=", filters["employee"]])
		
		if filters.get("from_date"):
			query_filters.append(["payroll_date", ">=", filters["from_date"]])

		if filters.get("to_date"):
			query_filters.append(["payroll_date", "<=", filters["to_date"]])

		query_filters.append(["docstatus", "=", 1])
		query_filters.append(["salary_component", "=", "Over Time"])
  
		add_dict = {"employee": filters["employee"]}
			
		emp_doc = frappe.get_doc("Employee", filters["employee"])
		h_dates = []
		if (emp_doc.holiday_list):
			leave_doc = frappe.get_doc("Holiday List", emp_doc.holiday_list)
			if leave_doc.holidays:
				h_tab = leave_doc.holidays
				for j in range(0, len(h_tab)):
					h_date = h_tab[j].get("holiday_date")
					formatted_date = h_date.strftime('%Y-%m-%d')
					h_dates.append(formatted_date)
	
		total_hrs = [0]
		hol_hrs = [0]
		hol_amount = [0]
		no_hrs = [0]
		no_amount = [0]
		add_salary_doc = frappe.get_all("Additional Salary", filters=query_filters, fields=["name"])
		if (add_salary_doc):
			for k in add_salary_doc:
				add_doc = frappe.get_doc("Additional Salary", k)

				add_dict["basic"] = add_doc.custom_basic_salary
				total_hrs.append(add_doc.custom_ot_hours)

				# dt = add_doc.payroll_date
				dt = add_doc.payroll_date.strftime('%Y-%m-%d')
				if (dt in h_dates):
					hol_hrs.append(add_doc.custom_ot_hours)
					hol_amount.append(add_doc.amount)
				else:
					no_hrs.append(add_doc.custom_ot_hours)
					no_amount.append(add_doc.amount)	
	
		add_dict["total_hrs"] = sum(total_hrs)
		add_dict["ho_hrs"] = sum(hol_hrs)
		add_dict["ho_amount"] = sum(hol_amount)
		add_dict["nor_hrs"] = sum(no_hrs)
		add_dict["nor_amount"] = sum(no_amount)
		add_dict["total"] = sum(no_amount) + sum(hol_amount)
  
		# Food Allowance
  
		query_filters3 = []
		if filters.get("company"):
			query_filters3.append(["company", "=", filters["company"]])
	
		if filters.get("employee"):
			query_filters3.append(["employee", "=", filters["employee"]])
		
		if filters.get("from_date"):
			query_filters3.append(["payroll_date", ">=", filters["from_date"]])

		if filters.get("to_date"):
			query_filters3.append(["payroll_date", "<=", filters["to_date"]])

		query_filters3.append(["docstatus", "=", 1])
		query_filters3.append(["salary_component", "=", "OT Food"])

		food_amount = [0]
		add_salary_doc = frappe.get_all("Additional Salary", filters=query_filters3, fields=["name"])
		if (add_salary_doc):
			for n in add_salary_doc:
				add_doc = frappe.get_doc("Additional Salary", n)
				food_amount.append(add_doc.amount)

		add_dict["food_ex"] = sum(food_amount)
		add_dict["grand_total"] = sum(food_amount) + sum(no_amount) + sum(hol_amount)

		data.append(add_dict)
	else:
		emp_list = []
		employee = frappe.get_all("Employee", filters={"company": filters["company"]}, fields=["name"])
		for emp in employee:
			emp_list.append(emp.get("name"))
   
		for i in emp_list:
			query_filters1 = []
			if filters.get("company"):
				query_filters1.append(["company", "=", filters["company"]])
		
			query_filters1.append(["employee", "=", i])
			
			if filters.get("from_date"):
				query_filters1.append(["payroll_date", ">=", filters["from_date"]])

			if filters.get("to_date"):
				query_filters1.append(["payroll_date", "<=", filters["to_date"]])

			query_filters1.append(["docstatus", "=", 1])
			query_filters1.append(["salary_component", "=", "Over Time"])

			add_dict = {"employee": i}
			
			emp_doc = frappe.get_doc("Employee", i)
			h_dates = []
			if (emp_doc.holiday_list):
				leave_doc = frappe.get_doc("Holiday List", emp_doc.holiday_list)
				if leave_doc.holidays:
					h_tab = leave_doc.holidays
					for j in range(0, len(h_tab)):
						h_date = h_tab[j].get("holiday_date")
						formatted_date = h_date.strftime('%Y-%m-%d')
						h_dates.append(formatted_date)
       
			total_hrs = [0]
			hol_hrs = [0]
			hol_amount = [0]
			no_hrs = [0]
			no_amount = [0]
			add_salary_doc = frappe.get_all("Additional Salary", filters=query_filters1, fields=["name"])
			if (add_salary_doc):
				for k in add_salary_doc:
					add_doc = frappe.get_doc("Additional Salary", k)
		
					add_dict["basic"] = add_doc.custom_basic_salary
					total_hrs.append(add_doc.custom_ot_hours)

					# dt = add_doc.payroll_date
					dt = add_doc.payroll_date.strftime('%Y-%m-%d')
					if (dt in h_dates):
						hol_hrs.append(add_doc.custom_ot_hours)
						hol_amount.append(add_doc.amount)
					else:
						no_hrs.append(add_doc.custom_ot_hours)
						no_amount.append(add_doc.amount)	
		
			add_dict["total_hrs"] = sum(total_hrs)
			add_dict["ho_hrs"] = sum(hol_hrs)
			add_dict["ho_amount"] = sum(hol_amount)
			add_dict["nor_hrs"] = sum(no_hrs)
			add_dict["nor_amount"] = sum(no_amount)
			add_dict["total"] = sum(no_amount) + sum(hol_amount)
	# Food Allowance
			query_filters2 = []
			if filters.get("company"):
				query_filters2.append(["company", "=", filters["company"]])
		
			query_filters2.append(["employee", "=", i])
			
			if filters.get("from_date"):
				query_filters2.append(["payroll_date", ">=", filters["from_date"]])

			if filters.get("to_date"):
				query_filters2.append(["payroll_date", "<=", filters["to_date"]])

			query_filters2.append(["docstatus", "=", 1])
			query_filters2.append(["salary_component", "=", "OT Food"])
   
			food_amount = [0]
			add_salary_doc = frappe.get_all("Additional Salary", filters=query_filters2, fields=["name"])
			if (add_salary_doc):
				for n in add_salary_doc:
					add_doc = frappe.get_doc("Additional Salary", n)
					food_amount.append(add_doc.amount)
    
			add_dict["food_ex"] = sum(food_amount)
			add_dict["grand_total"] = sum(food_amount) + sum(no_amount) + sum(hol_amount)

			data.append(add_dict)
   
	return data
