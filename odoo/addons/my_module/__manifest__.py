{
    'name': 'My Module',
    'version': '1.0.0',
    'summary': 'Contoh modul kustom Odoo 18',
    'description': 'Modul ini membuat model Person sederhana.',
    'author': 'Kang Tatang',
    'website': 'https://my-module.com',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/person_views.xml',
    ],
    'installable': True,
    'application': True,
}