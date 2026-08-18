{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real estate management module',
    'depends': ['base', 'mail'],
    'author': 'Carlo',
    'license': 'OPL-1',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'estate/static/src/css/estate.css',
        ],
    },
}
