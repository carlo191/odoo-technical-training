from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Tipo di Proprieta"
    _order = "name"
    _sql_constraints = [
        ('unique_name_type', 'UNIQUE("name")', 'Il nome del tipo deve essere unico.'),
    ]

    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id")