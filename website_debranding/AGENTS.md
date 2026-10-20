# website_debranding

## Purpose

Removes the "Powered by Odoo - Create a free website" promotion from the website footer.
Views only, no models.

## Views

- `layout_footer_copyright` inherits `web.brand_promotion_message` and empties
  `final_message`, so the whole message renders as nothing. It is a `customize_show`
  view, so users can switch it back on in the website editor.

## Pitfalls

- `post_init_hook` deactivates the view when Odoo runs with tests enabled, so other
  modules' website tests still find the core footer. Tests of this module must activate
  the view themselves.
- The view inherits the shared `web.brand_promotion_message`, so it also empties the
  promotion on other pages that use it (e.g. the portal footer).
