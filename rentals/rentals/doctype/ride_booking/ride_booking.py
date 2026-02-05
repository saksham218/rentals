# Copyright (c) 2026, saksham and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.rate:
			frappe.throw("Rate is required.")

		self.total_amount=(sum([item.distance for item in self.items])) * self.rate

