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
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    def action_open_offer_ids(self):
        return {
            "name": "Offers",
            "type": "ir.actions.act_window",
            "view_mode": "list,form",
            "res_model": "estate.property.offer",
            "target": "current",
            "domain": [("property_type_id", "=", self.id)],
            "context": {"default_property_type_id": self.id},
        }