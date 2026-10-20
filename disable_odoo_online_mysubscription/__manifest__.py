# Copyright 2026 Weboffice IT und Marketing GmbH & CoKG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Remove odoo.com Bindings - My Subscription",
    "summary": "Hide the My Subscription user menu item on Community",
    "version": "20.0.1.0.0",
    "category": "Hidden",
    "author": "Weboffice IT und Marketing GmbH & CoKG,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-brand",
    "license": "AGPL-3",
    "development_status": "Beta",
    "depends": ["disable_odoo_online", "mysubscription"],
    "assets": {
        "web.assets_backend": [
            "disable_odoo_online_mysubscription/static/src/js/user_menu_items.esm.js",
        ],
    },
    "auto_install": True,
    "installable": True,
}
