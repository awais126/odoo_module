#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.openacademy'
    _description = 'openacademy.openacademy'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
