from odoo.addons.web_enterprise.models.ir_http import Http

class HttpModel(Http):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(HttpModel,self).session_info()
        del res['warning']
        del res['expiration_date']
        del res['expiration_reason']
        return res
