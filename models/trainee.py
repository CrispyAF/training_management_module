# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BtManagement(models.Model):
    _name = 'bt_management.bt_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Trainee Management'

    name = fields.Char(compute='comp_name', tracking=1)
    first_name = fields.Char("First Name", required=1, tracking=1)
    last_name = fields.Char("Last Name", tracking=1)
    trainee_id = fields.Char(string='Trainee ID', required=True, copy=False, readonly=True, index=True,
                             default=lambda self: _('New'), tracking=1)
    emp_code = fields.Char("Employee Code", tracking=1)
    email = fields.Char(compute='_onchange_name_update_email_field', string="Email", required=1, tracking=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=1, tracking=1)
    dob = fields.Date(default=fields.Date.today, tracking=1)
    date_of_joining = fields.Date(default=fields.Date.today, tracking=1)
    trainee_designation = fields.Many2one('designation.designation', string="Designation", tracking=1,
                                          options="{'no_quick_create': True, 'no_create_edit' : True}")
    trainee_location = fields.Many2one('location.location', string="Location", tracking=1,
                                       options="{'no_quick_create': True, 'no_create_edit' : True}")
    image = fields.Binary("Profile Image", tracking=1)

    # new many2one field to link our trainees with hr.employee model
    employee_id = fields.Many2one('hr.employee', string="Employee")

    # to concatenate the first and last name
    @api.depends('first_name', 'last_name')
    def comp_name(self):
        for rec in self:
            rec.name = str(rec.first_name or '') + ' ' + str(rec.last_name or '')

    #   updating the email thingy as we type name
    @api.onchange('first_name', 'last_name')
    def _onchange_name_update_email_field(self):
        for rec in self:
            rec.email = str(rec.first_name).lower() + str(rec.last_name).lower() + '@gmail.com'

    # to generate unique and sequential trainee id
    @api.model
    def create(self, vals):
        if vals.get('trainee_id', _('New')) == _('New'):
            vals['trainee_id'] = self.env['ir.sequence'].next_by_code('bista_training.seq') or _('New')
        result = super(BtManagement, self).create(vals)
        return result

    # Verifying unique Employee code using Function Constraint

    @api.constrains('emp_code')
    def check_emp_code(self):
        for record in self:
            obj = self.search([('emp_code', '=', record.emp_code), ('id', '!=', record.id)])
            if obj:
                raise ValidationError(_('Employee Code is already in use'))

      #  To duplicate a unique fields

    @api.returns('self', lambda trainee_id: trainee_id.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(
            email=_("%s (copy)") % (self.email or ''))
        default.update(
            emp_code=_("%s (copy)") % (self.emp_code or ''))
        return super(BtManagement, self).copy(default)

    # Verifying unique Email using Function Constraint

    _sql_constraints = [
        ('email_unique',
         'unique(email)',
         'Email ID is already in use')
    ]

    # creating different state for status bar:-
    state = fields.Selection([('new', 'New'),
                              ('training', 'Training'),
                              ('rejected', 'Rejected'),
                              ('employed', 'Employed')],
                             string="Status", readonly=True, default='new', tracking=1)

    # defining action function for training button:-
    def confirm(self):
        for rec in self:
            rec.state = "training"

    # defining action function for rejected button:-
    def action_rejected(self):
        for rec in self:
            rec.state = "rejected"

    # defining action function for employed button:-
    def action_employed(self):
        for rec in self:
            rec.state = "employed"

            # Creating action for the button to reflect our employee in HR.employee
            employee_details = {

                # {variable of hr model: our variable }
                'name': rec.name,
                'image_1920': rec.image,
                'private_email': rec.email,
                'is_trainee': True
            }
            employee = self.env['hr.employee'].create(employee_details)
            rec.employee_id = employee
