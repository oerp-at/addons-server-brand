# mail_debranding

## Purpose

Removes Odoo branding from sent emails: every `<a>` pointing to odoo.com is removed
together with the text right before it ("Powered by") and its own tail text.

## Models

- `mail.render.mixin`: `remove_href_odoo()` cleans rendered templates in
  `_render_template()`; the message body itself (`to_keep`) is never touched.
- `mail.mail`: debrands the final body before sending.

## Rules

- Links to dev.odoo.com (odoo.sh) are kept.
- Values shorter than 20 characters are returned unchanged.

## Pitfalls

- Named `mail_debrand` in OCA/mail up to 18.0; renamed to `mail_debranding` in
  OCA/server-brand 19.0. Databases still on `mail_debrand` need a module rename
  (`openupgradelib.update_module_names`) or uninstall/install, and dependents must
  depend on `mail_debranding`.
- The anchor's tail text is removed too. In the 20.0 auth_signup invitation ("<company>
  uses <a>Odoo</a> to run its business. You have been invited by ...") this cuts the
  inviter sentence.
