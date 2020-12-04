# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Trainer(models.Model):
    _name = 'trainer.trainer'
    _description = 'Trainer Management'

    _rec_name = 'trainer_name'
    trainer_name = fields.Char(compute='comp_name')
    trainer_first_name = fields.Char("First Name", required=1)
    trainer_last_name = fields.Char("Last Name")

    @api.depends('trainer_first_name', 'trainer_last_name')
    def comp_name(self):
        for rec in self:
            rec.trainer_name = str(rec.trainer_first_name or '') + ' ' + str(rec.trainer_last_name or '')