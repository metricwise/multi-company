# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    country_id = fields.Many2one(store=True)
    street = fields.Char(store=True)
    street2 = fields.Char(store=True)
    zip = fields.Char(store=True)
    city = fields.Char(store=True)
    state_id = fields.Many2one(store=True)
