# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Batch(models.Model):
    _name = 'batch.batch'
    _description = 'batch'

    _rec_name = 'batch'
    batch = fields.Char()
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(default=fields.Date.today)
    location = fields.Many2one('location.location', string="Location")
    trainees = fields.One2many('bt_management.bt_management', 'trainee', string="Trainees")
    trainers = fields.One2many('trainer.trainer', 'trainer', string="Trainers")
    stages = fields.Many2one('stages.stages', string="Stages")
    training_topics = fields.Many2many('topic.topic', string="Training Topics")

    # creating different state for status bar:-
    state = fields.Selection([('draft', 'Draft'),
                              ('progress', 'Progress'),
                              ('done', 'Done')],
                             string="Status", readonly=True, default='draft', tracking=1)
