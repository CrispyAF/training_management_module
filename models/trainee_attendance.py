# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Attendance(models.Model):
    _name = 'attendance.attendance'
    _description = 'attendance'

    _rec_name = 'trainee_attendance_name'
    trainee_attendance_name = fields.Char(compute='_comp_from_date')
    date = fields.Date(default=fields.Date.today)
    trainee = fields.Many2one('bt_management.bt_management', string="Trainee")
    login_time = fields.Datetime(default=fields.Datetime.today, tracking=1)
    logout_time = fields.Datetime(default=fields.Datetime.today, tracking=1)
    hours = fields.Float(compute='_compute_hours', string="Hours")

    # training_record = fields.Many2one('training_record_line.training_record_line', string="Training Record",
    #                                   options="{'invisible' : True}")

    # to fill the record title
    @api.depends('date')
    def _comp_from_date(self):
        for rec in self:
            rec.trainee_attendance_name = 'Training Attendance Record of ' + str(rec.date)

    @api.depends('login_time', 'logout_time')
    def _compute_hours(self):
        for attendance in self:
            if attendance.logout_time:
                delta = attendance.logout_time - attendance.login_time
                attendance.hours = delta.total_seconds() / 3600.0
            else:
                attendance.hours = False