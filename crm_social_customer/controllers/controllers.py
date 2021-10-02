# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CrmSocialCustomer(http.Controller):

    @http.route('/', auth='user', website=True)
    def checkouts(self, **kwargs ):
        Partner = request.env['res.partner']
        if kwargs.get('name'):
            partners = Partner.search(["|",('name','ilike',kwargs.get('name')),
                                       "|",('facebook_account','ilike',kwargs.get('name')),
                                       "|", ('linkedin_account','ilike',kwargs.get('name')),
                                            ('twitter_account','ilike',kwargs.get('name'))
                                       ])
        else:
            partners = Partner.search([])

        return request.render('crm_social_customer.index',{'docs': partners})

    @http.route('/customer/<model("res.partner"):doc>',auth="user", website=True)
    def checkout(self, doc, **kwargs):
        return http.request.render( 'crm_social_customer.customer',{'doc': doc})

    @http.route('/crm_social_customer/',  auth='user', website=True)
    def index(self, **kw):
        
        return request.render('crm_social_customer.helloworld')

    @http.route('/hellocms/<page>', auth='public', website=True)
    def hello(self, page, **kwargs):
        return http.request.render(page)
        #return "Hello, world"

#     @http.route('/crm_social_customer/crm_social_customer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_social_customer.listing', {
#             'root': '/crm_social_customer/crm_social_customer',
#             'objects': http.request.env['crm_social_customer.crm_social_customer'].search([]),
#         })

#     @http.route('/crm_social_customer/crm_social_customer/objects/<model("crm_social_customer.crm_social_customer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_social_customer.object', {
#             'object': obj
#         })
