# Copyright (c) 2026, saksham and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""

	frappe.errprint("Executing Revenue by Make Report with filters:" + str(filters))
	columns = get_columns()
	data = get_data()

	chart={
		"data": {
			"labels": [row.make for row in data],
			"datasets": [{"values": [row.total_revenue for row in data]}]
		},
		"type": "pie"
	}

	return columns, data, "Message about the report", chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return  [{
				"fieldname": "make", 
				"label": "Make", 
				"fieldtype": "Data" 
			},
			{
				"fieldname": "total_revenue",
				"label": "Total Revenue", 
				"fieldtype": "Currency",
				"options": "USD" 
			}] 


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return frappe.get_all("Ride Booking", fields=[{"SUM":"total_amount","as":"total_revenue"}, "vehicle.make"], filters={"docstatus": 1},group_by="vehicle.make")
