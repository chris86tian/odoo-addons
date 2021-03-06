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

from openerp import models, fields, api, _

class eq_crm_claim(models.Model):
 
    _inherit = 'crm.claim'
    
    
    eq_costs = fields.Float('Costs')
    
    eq_waste_parts = fields.Float('Waste')#Ausschussteile
    eq_good_parts = fields.Float('Good parts')#"Gut-Teile"
    
    sub_categ_id = fields.Many2one('eq.crm.claim.sub.category', 
                                   'Sub-category', required=False)
    
    
    