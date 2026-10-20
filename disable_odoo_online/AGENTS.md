# disable_odoo_online

## Purpose

Removes bindings to odoo.com from the backend.

## What it changes

- `publisher_warranty.contract.update_notification()` returns `True` without contacting
  odoo.com on Community; on Enterprise (`version_info[5] == "e"`) the core call stays.
- Menus: Apps store, theme store and third-party apps move under Settings > Technical >
  Parameters; the Apps menu opens the local module list (`base.open_module_tree`).
- User menu: the `support` ("Help") item is removed (`user_menu_items.esm.js`).

## Pitfalls

- 20.0 core no longer has the `documentation` and `odoo_account` user menu items, so
  only `support` is removed.
- 20.0 adds the auto-installed core module `mysubscription` with a "My Subscription"
  user menu item and links to odoo.com pricing; this module does not hide it.
