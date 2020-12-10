# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Batch(models.Model):
    _name = 'batch.batch'
    _description = 'batch'

    _rec_name = 'batch'
    batch = fields.Char(string="Batch Name")
    start_date = fields.Date(default=fields.Date.today, string="Start Date")
    end_date = fields.Date(default=fields.Date.today, string="End Date")
    batch_location = fields.Many2one('location.location', string="Location")

    # co models for trainees and trainee
    trainees = fields.One2many('trainee_batch_co.trainee_batch_co', 'co_model_trainee', string="Trainees")
    trainers = fields.One2many('trainer_batch_co.trainer_batch_co', 'co_model_trainer', string="Trainers")

    training_topics = fields.Many2many('topic.topic', string="Training Topics")

    stage_id = fields.Many2one('stages.stages', string="Stages")

    # creating different state for status bar:-
    # related="*our field*.*other model field*"
    state = fields.Selection(string="State", related='stage_id.stages_status')


class Trainee_batch_line(models.Model):
    _name = 'trainee_batch_co.trainee_batch_co'
    _description = "Co-model for trainee batch"

    trainee_name_line = fields.Many2one('bt_management.bt_management', string="Name")
    co_model_trainee = fields.Many2one('batch.batch', string="Co-model_Trainee")


class Trainer_batch_line(models.Model):
    _name = 'trainer_batch_co.trainer_batch_co'
    _description = "Co-model for trainer batch"

    trainer_name_line = fields.Many2one('trainer.trainer', string="Trainer Name")
    co_model_trainer = fields.Many2one('batch.batch', string="Co-model_Trainer")
