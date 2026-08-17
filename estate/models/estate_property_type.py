from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _sql_constraints = [
        ('unique_name_type', 'UNIQUE("name")', 'Il nome del tipo deve essere unico.'),
    ]

    name = fields.Char(required=True)
    