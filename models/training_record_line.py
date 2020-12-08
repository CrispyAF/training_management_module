# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Training_Record_Line(models.Model):
    _name = 'training_record_line.training_record_line'
    _description = 'training_record_line'

    _rec_name = 'training_record_line_trainee'

    training_record_line_trainee = fields.Many2one('bt_management.bt_management', string="Trainee",
                                                   options="{'no_quick_create': True, 'no_create_edit' : True}")
    training_record_line_name = fields.Char(compute='_comp_trainee_name')

    #
    # remark
    # attendance
    # record

    # to fill the record title
    @api.depends('trainee')
    def _comp_trainee_name(self):
        for rec in self:
            rec.training_record_line_name = rec.trainee
