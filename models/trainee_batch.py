# -*- coding: utf-8 -*-

from odoo import models, fields


class Batch(models.Model):
    _name = 'batch.batch'
    _description = 'batch'

    _rec_name = 'batch'
    batch = fields.Char()
    start_date = fields.Date(default=fields.Date.today, tracking=1)
    end_date = fields.Date(default=fields.Date.today, tracking=1)
    location = fields.Many2one('location.location', string="Location", tracking=1,
                               options="{'no_quick_create': True, 'no_create_edit' : True}")
    trainees = fields.One2many('bt_management.bt_management', 'trainee', string="Trainees")
    trainers = fields.One2many('trainer.trainer', 'trainer', string="Trainers")
    stages = fields.Many2one('stages.stages', string="Stages", tracking=1,
                             options="{'no_quick_create': True, 'no_create_edit' : True}")
    training_topics = fields.Many2many('topic.topic', string="Training Topics")
