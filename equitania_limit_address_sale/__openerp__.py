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
    'name': 'Equitania Erweiterungsmodul Addresslimitierung',
    'license': 'AGPL-3',
    'version': '1.0.1',
    'description': """
        Equitania Software GmbH
    """,
    'author': 'Equitania Software GmbH',
    'website': 'www.myodoo.de',
    'depends': [
                'equitania' ],
    'category' : 'General Improvements',
    'summary': 'Sale, Account, Product, Mail, Report, CRM, Purchase',
    #'init': [
    #         'eq_install_func.xml',
    #         ],
    'data': ['sale_view.xml'],
    'demo': [],
    'css': ['static/src/css/eq_style.css'],
    'installable': True,
    'auto_install': False,
}
