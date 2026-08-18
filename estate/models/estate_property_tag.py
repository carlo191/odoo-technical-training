from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag Proprieta"
    _order = "name"

    _unique_name_tag = models.Constraint(
        'UNIQUE(name)',
        'Il nome del tag deve essere unico.',
    )

    name = fields.Char(required=True)
    color = fields.Integer()