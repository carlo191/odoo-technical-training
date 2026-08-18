from odoo import _, api, models, fields
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = "estate.property"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Proprieta Immobiliare"
    _order = "id desc"
    _sql_constraints = [
        ('expected_price_positive', 'CHECK(expected_price > 0)', 'Il prezzo previsto deve essere strettamente positivo.'),
        ('selling_price_positive', 'CHECK(selling_price >= 0)', 'Il prezzo di vendita deve essere positivo.'),
    ]

    def _default_date(self):
        return fields.Date.today() + relativedelta(months=3)

    name = fields.Char(required=True)
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    date_availability = fields.Date(copy=False, default=_default_date)
    bedrooms = fields.Integer(default=2)
    active = fields.Boolean(default=True)
    postcode = fields.Char()
    living_area = fields.Integer()
    description = fields.Text()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'Nord'),
            ('south', 'Sud'),
            ('east', 'Est'),
            ('west', 'Ovest'),
        ],
    )
    facades = fields.Integer()
    state = fields.Selection(
        selection=[
            ('new', 'Nuova'),
            ('offer_received', 'Offerta Ricevuta'),
            ('offer_accepted', 'Offerta Accettata'),
            ('sold', 'Venduta'),
            ('canceled', 'Annullata'),
        ],
        required=True,
        copy=False,
        default='new',
    )
    property_type_id = fields.Many2one("estate.property.type", string="Tipo di Proprieta")
    salesperson_id = fields.Many2one("res.users", string="Commerciale")
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    tag_ids = fields.Many2many("estate.property.tag")
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    buyer_id = fields.Many2one("res.partner", copy=False)

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            prices = record.offer_ids.mapped('price')
            record.best_price = max(prices) if prices else 0


    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def azione_venduta(self):
        for propriety in self:
            if propriety.state == "canceled":
                raise UserError(_("Una proprieta annullata non puo essere venduta."))
            propriety.state = "sold"

    def azione_annullata(self):
        for proprieta in self:
            if proprieta.state == "sold":
                raise UserError(_("Una proprieta venduta non puo essere annullata."))
            proprieta.state = "canceled"

    @api.ondelete(at_uninstall=False)
    def _check_delete_state(self):
        for record in self:
            if record.state not in ('new', 'canceled'):
                raise UserError(_("Non puoi eliminare una proprieta che non sia in stato 'New' o 'Canceled'."))
