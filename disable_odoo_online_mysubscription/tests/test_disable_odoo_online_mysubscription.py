# Copyright 2026 Weboffice IT und Marketing GmbH & CoKG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestDisableOdooOnlineMysubscription(common.TransactionCase):
    def test_script_in_backend_assets(self):
        """The menu patch is loaded in the backend bundle, after mysubscription."""
        paths = [
            path
            for path, *_rest in self.env["ir.asset"]._get_asset_paths(
                "web.assets_backend", {}
            )
        ]
        ours = next(
            i
            for i, path in enumerate(paths)
            if path.endswith(
                "disable_odoo_online_mysubscription/static/src/js/"
                "user_menu_items.esm.js"
            )
        )
        theirs = next(
            i
            for i, path in enumerate(paths)
            if path.endswith("mysubscription/static/src/user_menu.js")
        )
        self.assertGreater(ours, theirs)
