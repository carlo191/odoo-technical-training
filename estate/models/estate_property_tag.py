from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _sql_constraints = [
            ('unique_name_tag', 'UNIQUE("name")', 'Il nome del tag  deve essere unico .'),
          
        ]

    name = fields.Char(required=True)