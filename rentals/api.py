import frappe

@frappe.whitelist()
def hello():
    return "Hello"

def demo_background_task():
    print("Demo background task executed")