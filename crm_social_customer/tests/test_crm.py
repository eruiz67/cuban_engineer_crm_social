from odoo.tests.common import TransactionCase
from odoo import models, fields, api, _
import logging
from odoo.tests import tagged
from datetime import datetime, date
import calendar
import math
import unicodedata
_logger = logging.getLogger(__name__)

@tagged('post_install')
class TestCRMSocial(TransactionCase):
    
    def setUp(self, *args, **kwargs):
        super(TestCRMSocial, self).setUp(*args, **kwargs)
        self.Customers = self.env['res.partner']
       
        self.customer1 = self.Customers.sudo().create({
                        'name':"Juan Perez",
                        'company_type':"person",
                        'facebook_account': "www.facebook.com",
                        "linkedin_account":"www.linkedin.com",
                        "twitter_account":"www.twitter.com"})
        self.customer2 = self.Customers.sudo().create({
                        'name':"Pedro Lopez",
                        'company_type':"person",
                        'facebook_account': "www.facebook.com",
                        "linkedin_account":"www.linkedin.com",
                        "twitter_account":"www.twitter.com"})
        self.customer3 = self.Customers.sudo().create({
                        'name':"Roberto Perez",
                        'company_type':"person",
                        'facebook_account': "www.facebook.com",
                        "linkedin_account":"www.linkedin.com",
                        "twitter_account":"www.twitter.com"})
        self.customer4 = self.Customers.sudo().create({
                        'name':"Juan Enrique Ruiz",
                        'company_type':"person",
                        'facebook_account': "www.facebook.com",
                        })
        self.customer5 = self.Customers.sudo().create({
                        'name':"Juan Enrique Ruiz",
                        'company_type':"person",
                       
                        })





    def test_is_profile_complete(self):
        """--- Tests if a customer's profile is incomplete ---"""

        self.assertEqual(self.customer1.is_profile_complete, True, "Customer 1 profile shows 'incomplete', wich is wrong")
        self.assertEqual(self.customer2.is_profile_complete, True, "Customer 2 profile shows 'incomplete', wich is wrong")
        self.assertEqual(self.customer3.is_profile_complete, True, "Customer 3 profile shows 'incomplete', wich is wrong")
        self.assertEqual(self.customer4.is_profile_complete, False, "Customer 4 profile shows 'complete', wich is wrong")
        self.assertEqual(self.customer5.is_profile_complete, False, "Customer 5 profile shows 'complete', wich is wrong")


   
