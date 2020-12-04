# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HrEmployeePrivate(models.Model):
    # we inherit the existing odoo model
    _inherit = "hr.employee"

    # our custom field name
    is_trainee = fields.Boolean("Trainee")
