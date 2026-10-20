"""Portal debranding tests.

Validates that this module removes Odoo branding from portal pages.
"""

# Copyright 2024 level4 (https://level4.es)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import common


class TestPortalOdooDebranding(common.TransactionCase):
    def test_brand_promotion_hidden(self):
        """web.brand_promotion should render nothing after debranding.

        The view sets t-if="False" on the .o_brand_promotion container,
        so the whole block must be skipped at render time.
        """
        html = self.env["ir.ui.view"]._render_template("web.brand_promotion", values={})
        self.assertEqual(html.strip(), "", "Brand promotion block should be removed")

    def test_portal_record_sidebar_no_powered_by(self):
        """The 'Powered by Odoo' notice in portal sidebar must be removed."""
        html = self.env["ir.ui.view"]._render_template(
            "portal.portal_record_sidebar", values={"classes": ""}
        )
        self.assertNotIn("Powered by", html)
        self.assertNotIn("odoo.com?utm_medium=portal", html)

    def test_portal_record_sidebar_keeps_title(self):
        """Only the branding block is hidden, not the title block."""
        html = self.env["ir.ui.view"]._render_template(
            "portal.portal_record_sidebar",
            values={"classes": "", "title": "Sidebar Title"},
        )
        self.assertIn("Sidebar Title", html)

    def test_login_no_powered_by(self):
        """The 'Powered by Odoo' link in the login footer must be removed."""
        # Rendering the full login layout needs a request, check the arch instead
        arch = self.env.ref("web.login_layout")._get_combined_arch()
        links = arch.xpath("//a[contains(@href, 'utm_medium=auth')]")
        self.assertTrue(links)
        for link in links:
            self.assertEqual(link.get("t-if"), "False")
