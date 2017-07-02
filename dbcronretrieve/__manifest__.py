# -*- coding: utf-8 -*-
{
    'name': "dbcronretrieve",

    'summary': """
        This module will store tables of of others DB in our database""",

    'description': """
        This module will store data from others DB(maybe Mysql or postgres or others) in our database.
     """,

    'author': "Mohamed Mostafa Kamel",
    'website': "http://www.kg-m.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
