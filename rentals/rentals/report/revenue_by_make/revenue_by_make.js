// Copyright (c) 2026, saksham and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Make"] = {
	"filters": [
		{
			"fieldname": "my_filter",
			"label": "My Filter",
			"fieldtype": "Link",
			"options": "Vehicle"
		}
	]
};