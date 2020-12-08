# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Record(models.Model):
    _name = 'record.record'
    _description = 'record'

    _rec_name = 'record_name'
    record_name = fields.Char(compute='_comp_record_name')
    record_date = fields.Date(default=fields.Date.today)

    batch = fields.Many2one('batch.batch', string="Training Batch",
                            options="{'no_quick_create': True, 'no_create_edit' : True}")

    training_lines = fields.One2many('training_record_line.training_record_line', 'training_lines',
                                     string="Training Record Line")
    topics_covered = fields.One2many('training_topic_line.training_topic_line', 'topics_covered',
                                     string="Topics Covered")
    attendance = fields.One2many('attendance.attendance', 'attendance',
                                 string="Attendance")

    # creating different state for status bar:-
    stages = fields.Many2one('stages.stages', string="Stages",
                             options="{'no_quick_create': True, 'no_create_edit' : True}")

    # to fill the record title
    @api.depends('record_date')
    def _comp_record_name(self):
        for rec in self:
            rec.record_name = 'Training Attendance Record of ' + str(rec.record_date)
