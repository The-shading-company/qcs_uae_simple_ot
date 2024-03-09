// Copyright (c) 2024, QCS and contributors
// For license information, please see license.txt

frappe.ui.form.on('TSC  Awning Pricing', {
	awning_item: function(frm) {
		frappe.call({
            method: 'qcs_uae_simple_ot.qcs_uae_simple_ot.doctype.tsc__awning_pricing.tsc__awning_pricing.awning_item_cost',
            args: {
                "awning_item": cur_frm.doc.awning_item,
            },
			callback: function(r) {
				frm.set_value("awning_bom_cost", r.message);
			}
        });
	},
	canopy_item: function(frm) {
		frappe.call({
            method: 'qcs_uae_simple_ot.qcs_uae_simple_ot.doctype.tsc__awning_pricing.tsc__awning_pricing.canopy_item_cost',
            args: {
                "canopy_item": cur_frm.doc.canopy_item,
            },
			callback: function(r) {
				frm.set_value("canopy_bom_cost", r.message);
			}
        });
	},
	copy: function(frm) {
		if(cur_frm.doc.product_description){
			const show_success_alert = () => {
				frappe.show_alert({
					indicator: "green",
					message: __("Copied to clipboard."),
				});
			};
			if (navigator.clipboard && window.isSecureContext) {
				navigator.clipboard.writeText(cur_frm.doc.product_description).then(show_success_alert);
			} else {
				let input = $("<textarea>");
				$("body").append(input);
				input.val(cur_frm.doc.product_description).select();
	
				document.execCommand("copy");
				show_success_alert();
				input.remove();
			}

		}
	}
});
