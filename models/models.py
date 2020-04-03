# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tttt(models.Model):
    _name = 'tttt.tttt'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    lines = fields.One2many(comodel_name="lines", inverse_name="p")

    @api.depends('lines')
    def _value_pc(self):
        for i in self:
            for line in i.lines:
                i.value2 =line.t*5

class lines(models.Model):
    _name='lines'
    name = fields.Char(string="", required=False)
    t = fields.Float(string="", required=False)
    p = fields.Many2one(comodel_name="tttt.tttt", string="", required=False)
