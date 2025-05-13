from odoo import models, fields

class Person(models.Model):
    _name = 'my_module.person'
    _description = 'Person'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    is_active = fields.Boolean(string='Active', default=True)
   