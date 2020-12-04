# -*- coding: utf-8 -*-

from odoo import models, fields


class Designation(models.Model):
    _name = 'designation.designation'
    _description = 'Designation'

    _rec_name = 'designation'
    designation = fields.Char("Designation", required=1)

