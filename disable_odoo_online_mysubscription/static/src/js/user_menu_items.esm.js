import {registry} from "@web/core/registry";
import {session} from "@web/session";
// Needed so that this is run after adding the menu entry
import "@mysubscription/user_menu";

// Same rule as the update notifier in disable_odoo_online: keep it on Enterprise
if (session.server_version_info?.[5] !== "e") {
    registry.category("user_menuitems").remove("mysubscription_user_menu");
}
