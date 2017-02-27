# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Bhavesh Odedra (<bhavesh.b.odedra@gmail.com>)
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
###############################################################################

from openerp import models, fields

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    
    cash_turnover_addition = fields.Boolean(string='Cash Turnover')
    goods_turnover_addition = fields.Boolean(string='Goods Turnover')
