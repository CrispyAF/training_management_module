# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Stages(models.Model):
    _name = 'stages.stages'
    _description = 'stages'

    _rec_name = 'stages'
    stages = fields.Char()
    available_on_batch = fields.Boolean("Available on Batch")
    available_on_training_record = fields.Boolean("Available on Training Record")
    stages_status = fields.Selection([('draft', 'Draft'),
                                      ('progress', 'Progress'),
                                      ('done', 'Done')],
                                     string="Status")
