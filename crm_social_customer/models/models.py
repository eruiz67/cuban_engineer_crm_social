# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

# class crm_social_customer(models.Model):
#     _name = 'crm_social_customer.crm_social_customer'
#     _description = 'crm_social_customer.crm_social_customer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class CRMSocial(models.Model):
    _inherit = 'res.partner'

    facebook_account = fields.Char(string="Facebook")
    linkedin_account = fields.Char(string="LinkedIn")
    twitter_account = fields.Char(string="Twitter")

    

    is_profile_complete = fields.Boolean(compute='_compute_is_profile_complete', search='_search_is_profile_complete', string='Perfil completado?')
    

    @api.depends('facebook_account','linkedin_account','twitter_account')
    def _compute_is_profile_complete(self):
        for record in self:
            record.is_profile_complete = (record.facebook_account and record.linkedin_account and record.twitter_account)

    def _search_is_profile_complete(self, operator, value):
        partners = self.env['res.partner'].search([])
        list_imcomplete=[]
        for record in partners:
            if not (record.facebook_account and record.linkedin_account and record.twitter_account):
                list_imcomplete.append(record.id)
        return [('id','in', list_imcomplete)]

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    facebook_account = fields.Char(string="Facebook", related="partner_id.facebook_account")
    linkedin_account = fields.Char(string="LinkedIn", related="partner_id.linkedin_account")
    twitter_account = fields.Char(string="Twitter", related="partner_id.twitter_account")
