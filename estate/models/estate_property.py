from odoo import models, fields
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    def default_date(self):
        return fields.Date.today() + relativedelta(months=3)

    name = fields.Char(required=True)
    price = fields.Float()
    selling_price = fields.Float(readonly=True,copy=False)
    date_availability = fields.Date(copy=False, default=default_date)
    bedrooms = fields.Integer(default=2)
    active = fields.Boolean(default=True)
    state = fields.Selection(
    selection=[
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ],
    required=True,
    copy=False,
    default='new',
)
