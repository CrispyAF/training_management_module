# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Training_Topic_Line(models.Model):
    _name = 'topic_line.topic_line'
    _description = 'topic_line'

    _rec_name = 'training_topic'

    training_topic = fields.Many2one('topic.topic', string="Topic")
    topic_line_name = fields.Char(string="Topic Line Name")
    remarks = fields.Text(string='Remarks')
