from odoo import models, api


class IrUiView(models.Model):
    _inherit = 'ir.ui.menu'

    @api.multi
    def unlink(self):
        res = super().unlink()
        shortcuts = self.env['web.shortcut'].search([('menu_id', '=', False)])
        shortcuts.unlink()
        return res
