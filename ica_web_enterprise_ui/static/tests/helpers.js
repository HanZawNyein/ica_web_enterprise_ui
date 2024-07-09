/** @odoo-module */

import { createWebClient } from "@web/../tests/webclient/helpers";
import { WebClientEnterprise } from "@ica_web_enterprise_ui/webclient/webclient";

export function createEnterpriseWebClient(params) {
    params.WebClientClass = WebClientEnterprise;
    return createWebClient(params);
}
