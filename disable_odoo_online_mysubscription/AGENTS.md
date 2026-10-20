# disable_odoo_online_mysubscription

## Purpose

Bridge between `disable_odoo_online` and the core module `mysubscription` (new in 20.0,
auto-installed). Removes the "My Subscription" user menu item on Community; its
dashboard links to odoo.com pricing and editions. Auto-installed with both modules.

## Rules

- Enterprise keeps the item (`session.server_version_info[5] == "e"`), same rule as the
  update notifier in `disable_odoo_online`.
- Only the user menu entry is removed; the client action `mysubscription.dashboard`
  stays reachable by URL.

## Pitfalls

- The script must load after `mysubscription/static/src/user_menu.js`, otherwise the
  item is added again after the removal. The explicit
  `import "@mysubscription/user_menu"` and the dependency guarantee the order;
  `test_script_in_backend_assets` checks it.
