{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real estate management module',
    'depends': ['base'],
    'author': 'Carlo',
    'license': 'OPL-1',
'data': [
    'security/security.xml',
    'security/ir.model.access.csv',
    'views/estate_property_views.xml',
    'views/estate_property_offer_views.xml',
    'views/estate_property_tag_views.xml',
    'views/estate_menus.xml',
],
    'demo': [
        'demo/demo.xml',
    ],
}