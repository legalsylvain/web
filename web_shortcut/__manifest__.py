# Copyright 2010-2011 Odoo SA (<http://odoo.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Shortcut Menu',
    'version': '12.0.1.0.1',
    'category': 'Web',
    'author': 'GRAP,Odoo SA,Odoo Community Association (OCA)',
    'website': 'https://github.com/web',
    'depends': [
        'base',
        'web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'templates/assets.xml',
    ],
    'qweb': [
        'static/src/xml/web_shortcut.xml'
    ],
    'installable': True,
    'license': 'AGPL-3',
}
