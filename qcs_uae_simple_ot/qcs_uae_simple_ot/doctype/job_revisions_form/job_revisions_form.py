# Copyright (c) 2024, QCS and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class JobRevisionsForm(Document):
	def validate(self):
		over_total = self.labour_cost + self.transport_cost + self.fabric_cost + self.stitching_cost + self.other_cost
		self.total = over_total

