# -*- coding: utf-8 -*-

from odoo import models, fields


class Topic(models.Model):
    _name = 'topic.topic'
    _description = 'Topic'

    _rec_name = 'topic_name'
    topic_name = fields.Char("Name", required=1)
    subject = fields.Many2one('subjects.subjects', string="Subject", options="{'no_quick_create': True, 'no_create_edit': True}")