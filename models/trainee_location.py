# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Location(models.Model):
    _name = 'location.location'
    _description = 'Location'

    _rec_name = 'location'
    location = fields.Char("Location", required=1)
    state_id = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')
    city = fields.Char('City', help='Enter City')

    # Dependent picklist code to show State based on selected Country E.g India -> Gujarat, Maharashtra, Rajasthan, etc..
    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            return {'domain': {'state_id': [('country_id', '=', self.country_id.id)]}}
        else:
            return {'domain': {'state_id': []}}