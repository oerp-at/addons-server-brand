from odoo.tests.common import TransactionCase


class TestDummy(TransactionCase):
    def test_dummy(self):
        """Dummy test to avoid warnings"""
        self.assertTrue(True)

    def test_brand_promotion_message_removed(self):
        """With the view active, the website footer promotion renders empty."""
        # post_init_hook deactivates the view when tests are enabled
        self.env.ref("website_debranding.layout_footer_copyright").active = True
        html = self.env["ir.ui.view"]._render_template(
            "web.brand_promotion_message",
            values={"_message": "Create a free website", "_utm_medium": "website"},
        )
        self.assertNotIn("Powered by", html)
        self.assertNotIn("odoo.com", html)
