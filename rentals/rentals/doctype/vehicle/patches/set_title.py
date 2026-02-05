import frappe

def execute():
    vehicles = frappe.get_all("Vehicle", pluck="name")
    for vehicle in vehicles:
        doc = frappe.get_doc("Vehicle", vehicle)
        doc.title = f"{doc.make} {doc.model} {doc.year}"
        doc.save()

    frappe.db.commit()