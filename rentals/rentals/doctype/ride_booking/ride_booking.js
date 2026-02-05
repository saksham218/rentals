// Copyright (c) 2026, saksham and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
    refresh(frm) {

    },
    rate(frm) {
        frm.trigger("update_total_amount");
    },
    update_total_amount(frm) {
        frm.set_value("total_amount", frm.doc.rate * frm.doc.items.map(i => i.distance || 0).reduce((a, b) => a + b, 0));
    }
});

frappe.ui.form.on('Ride Booking Item', {
    refresh(frm) {
        // your code here
    },
    distance(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    },
    items_remove(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    }
});

