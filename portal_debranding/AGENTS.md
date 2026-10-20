# portal_debranding

## Purpose

Removes Odoo branding from portal pages and the login screen. Views only, no models.

## Views

- `web.brand_promotion`: the `o_brand_promotion` block gets `t-if="False"` (portal
  footer "Powered by Odoo").
- `portal.portal_record_sidebar`: the "Powered by Odoo" block below the sidebar entries
  is hidden.
- `web.login_layout`: the "Powered by Odoo" link (`utm_medium=auth`) in the login footer
  is hidden.

## Pitfalls

- 20.0 added a title block with class `d-none` in `portal.portal_record_sidebar` before
  the branding block. The 19.0 xpath `//div[hasclass('d-none')]` therefore hid the
  document title and kept the branding. The xpath now selects the `d-none` div that
  holds the `utm_medium=portal` link; `test_portal_record_sidebar_keeps_title` guards
  this.
- `web.login_layout` cannot be rendered in a test without a request, so the test checks
  the combined arch instead.
