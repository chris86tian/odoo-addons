# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Equitania Product Template",

    'summary': """
        This module explains the exemplary Structure of the product product and the product template views.""",

    'description': """
        
    """,

    'author': "Equitania Software GmbH",
    'website': "www.myodoo.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0.0',
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'eq_product_template_view.xml',
        'eq_product_product_view.xml'
    ],
    # demodata - only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}