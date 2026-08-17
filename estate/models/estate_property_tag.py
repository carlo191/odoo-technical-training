from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag Proprieta"
    _order = "name"
    _sql_constraints = [
            ('unique_name_tag', 'UNIQUE("name")', 'Il nome del tag  deve essere unico .'),
          
        ]

    name = fields.Char(required=True)
    color = fields.Integer()