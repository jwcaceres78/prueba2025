# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'course'
    _description = 'Course Model'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    student_count = fields.Integer(string='Number of Students', default=0)
    teacher_id = fields.Many2one('teacher', string='Teacher', required=True)
