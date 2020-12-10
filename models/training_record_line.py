# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Training_Record_Line(models.Model):
    _name = 'training_record_line.training_record_line'
    _description = 'training_record_line'

    _rec_name = 'training_record_line_trainee'

    training_record_line_trainee = fields.Many2one('bt_management.bt_management', string="Trainee")
    training_record_line_name = fields.Char(string="Trainee")

    training_record = fields.Many2one('record.record', string="Training record")
    remarks = fields.Text(string='Remarks')

    # attendance

    # to fill the record title
    # @api.depends('trainee')
    # def _comp_trainee_name(self):
    #     for rec in self:
    #         rec.training_record_line_name = rec.trainee
