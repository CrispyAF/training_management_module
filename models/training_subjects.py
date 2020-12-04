# -*- coding: utf-8 -*-

from odoo import models, fields


class Subjects(models.Model):
    _name = 'subjects.subjects'
    _description = 'Subjects'

    _rec_name = 'subject_name'
    subject_name = fields.Char("Subject Name", required=1)
    description = fields.Html("Description")
    topic = fields.One2many('topic.topic', 'subject', string="Topic")
    trainers = fields.Many2many('trainer.trainer', string="Trainers")