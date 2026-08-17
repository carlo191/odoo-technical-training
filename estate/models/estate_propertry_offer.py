from odoo import _, api, models, fields
from odoo.exceptions import UserError
from datetime import timedelta
from dateutil.relativedelta import relativedelta




class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Offerta Proprieta Immobiliare"
    _order = "price desc"
    _sql_constraints = [
            ('price_positive', 'CHECK(price > 0)', 'Il prezzo deve essere strettamente positivo.'),
        ]

    price = fields.Float()

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    status = fields.Selection(
        selection=[
            ('accepted', 'Accettata'),
            ('refused', 'Rifiutata'),
        ],
        copy=False,
    )
    partner_id = fields.Many2one("res.partner", required=True, string="Compratore")
    property_id = fields.Many2one("estate.property", required=True, string="Proprieta")
    property_type_id = fields.Many2one(
        "estate.property.type",
        string="Tipo di Proprieta",
        related="property_id.property_type_id",
        store=True,
    )

    @api.depends('validity',)
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - fields.Date.today()).days

    def action_accept(self):
        for offer in self:
            if offer.status == 'refused':
                raise UserError(_("Un'offerta gia rifiutata non puo essere accettata."))
            offer.status = 'accepted'
            offer.property_id.selling_price = offer.price
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.state = 'offer_accepted'

    def action_refuse(self):
        for offer in self:
            if offer.status == 'accepted':
                raise UserError(_("Un'offerta gia accettata non puo essere rifiutata."))
            offer.status = 'refused'
