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

import time
from openerp.osv import osv
from openerp.report import report_sxw
from openerp import SUPERUSER_ID


class od_report_sessionsummary(report_sxw.rml_parse):

    # variables for save of all possible vat categories
    vat_0   = 0        # 0% MwSt
    vat_7   = 0        # 7% MwSt
    vat_19  = 0        # 19% Mwst
    vat_total = 0      # 0% MwSt + 7% MwSt + 19%MwSt

    def __init__(self, cr, uid, name, context):
        """
            Initialization of all functions that can be called from our report
            @cr: cursor
            @uid: user id
            @name: name
            @context: context
        """
        
        super(od_report_sessionsummary, self).__init__(cr, uid, name, context=context)        
        
        self.localcontext.update({
            'get_cash_turnover': self.get_cash_turnover,
            'get_goods_turnover': self.get_goods_turnover,
            'get_vat_sum_19': self.get_vat_sum_19,
            'get_saled_vouchers': self.get_saled_vouchers,
            'get_warenumsatz': self.get_warenumsatz,
            'get_hole_summary': self.get_hole_summary,
        })
        
    def get_hole_summary(self, pos_session):
    
        cash_value = 0.00
        currency_symbol = ''
        kartenz_value = 0.00
        first_index = True
        for statement in pos_session.statement_ids:
        
            if first_index:
            
                kartenz_value += statement.balance_end_real
                first_index = False
        
            currency_symbol = statement.currency.symbol
            
            if statement.journal_id and statement.journal_id.cash_turnover_addition:
            
                cash_value += statement.balance_end_real
                
        hole_summary = kartenz_value + cash_value
                
        return format(hole_summary, '.2f') + ' ' + currency_symbol
        
    def get_warenumsatz(self, pos_session):
        cash_value = 0.00
        currency_symbol = ''
        
        for statement in pos_session.statement_ids:
        
            currency_symbol = statement.currency.symbol
            
            if statement.journal_id and statement.journal_id.cash_turnover_addition:
            
                cash_value += statement.balance_end_real 
                
        result_value = self._get_saled_vouchers_value(pos_session)
        value = cash_value - result_value
        
        return format(value, '.2f') + ' ' + currency_symbol

    def get_cash_turnover(self, pos_session):
        """
            Get turnover and convert it to string- Umsatz
            @pos_session: actual pos session
            @return: formated turnover with currency symbol
        """
        
        cash_value = 0.00
        currency_symbol = ''
        
        for statement in pos_session.statement_ids:
        
            currency_symbol = statement.currency.symbol
            
            if statement.journal_id and statement.journal_id.cash_turnover_addition:
            
                cash_value += statement.balance_end_real    
                
        return format(cash_value, '.2f') + ' ' + currency_symbol
        
    def _get_cash_turnover_value(self, pos_session):
        """
            Get turnover as float value - Umsatz
            @pos_session: actual pos session
            @return: formated turnover with currency symbol
        """
        result = 0.00
        for pos in pos_session.order_ids:
            for line in pos.lines:
                result += line.price_subtotal_incl

        return float(result)
        
    def get_redeem_vouchers(self, pos_session):
        """
            Get sum of all reddemed vouchers as float - Gutscheineinlösung
            @pos_session: actual pos session
            @return: sum of all reddemed vouchers
        """
        result = 0.00
        #coupon_journal = self.pool.get('account.journal').search(self.cr, self.uid, [('code', '=', 'CPNJ')])                                                # old version
        coupon_journal = self.pool.get('account.journal').search(self.cr, self.uid, [ '|', ('code', '=', 'CPNJ'), ('code', '=', 'GuEin')])  #HIER                   # new version
        
        bank_account_statment_obj = self.pool.get("account.bank.statement")
        line_ids = bank_account_statment_obj.search(self.cr, self.uid, [('pos_session_id', '=', pos_session.id), ('journal_id', '=', coupon_journal[0])], None)
        for line_id in line_ids:
            line = bank_account_statment_obj.browse(self.cr, self.uid, line_id, None)
            result += line.total_entry_encoding

        return result
        
    def _get_saled_vouchers_value(self, pos_session):
        """
            Summ of all saled vouchers as float - Gutscheinverkauf
            @pos_session: actual pos session
            @return: total price of all saled vouchers
        """
        result = 0.00
        # traverse all pos_order_lines and check if linked product is a voucher
        for pos in pos_session.order_ids:
            for line in pos.lines:
                if line.product_id.product_tmpl_id.is_coupon:       # check if linked position..and it's product is defined as voucher
                  #print "line: ", line
                  result += line.price_subtotal_incl #line.price_unit; geändert 14.04.

        return float(result)
        
    def get_saled_vouchers(self, pos_session):
        """
            Summ of all saled vouchers converted into string - Gutscheinverkauf
            @pos_session: actual pos session
            @return: total price of all saled vouchers
        """
        result_value = self._get_saled_vouchers_value(pos_session)
        currency_symbol = ''

        for statement in pos_session.statement_ids:

            currency_symbol = statement.currency.symbol

        return format(result_value, '.2f') + ' ' + currency_symbol

    def get_goods_turnover(self, pos_session):
        """
            Get and calculate goods turnover - Warenumsatz
            This value is calculated like with this formel:
            Warenumsatz = Kassenumsatz + Gutschriftseinlösung - Gutscheinverkauf
            @pos_session: actual pos session
            @return: formated goods turnover with currency symbol
        """
        turnover = self._get_cash_turnover_value(pos_session)
        #print "Kassenumsatz: ", turnover
        voucher_redem = self.get_redeem_vouchers(pos_session)       # Gutscheineinlösung
        #print "Gutschriftseinlösung: ", voucher_redem
        voucher_sale = self._get_saled_vouchers_value(pos_session)        # Gutscheinverkauf
        #print "Gutscheinverkauf: ", voucher_sale
        #print "Warenumsatz = Kassenumsatz + Gutschriftseinlösung - Gutscheinverkauf"
        goods_turnover_result = turnover + voucher_redem - voucher_sale
        #print "**** Warenumsatz: ", goods_turnover_result
        currency_symbol = ''

        for statement in pos_session.statement_ids:

            currency_symbol = statement.currency.symbol
            break

        return format(goods_turnover_result, '.2f') + ' ' + currency_symbol


    def get_vat_sum_19(self, pos_session):
        """
            Get 19% VAT sum, convert it to string and add currency symbol (Umsatz 19%)
            @pos_session: actual pos_session
            @return: 19%VAT formated as string together with currency symbol
        """        
        
        cash_value = 0.00
        currency_symbol = ''
        kartenz_value = 0.00
        first_index = True
        for statement in pos_session.statement_ids:
        
            if first_index:
            
                kartenz_value += statement.balance_end_real
                first_index = False
        
            currency_symbol = statement.currency.symbol
            
            if statement.journal_id and statement.journal_id.cash_turnover_addition:
            
                cash_value += statement.balance_end_real
                
        hole_summary = kartenz_value + cash_value
                
        if hole_summary > 0.0:
        
            hole_summary = ((hole_summary / 119.0) * 19)
                
        return format(hole_summary, '.2f') + ' ' + currency_symbol

class report_lunchorder_short(osv.AbstractModel):
    _name = 'report.od_pos_customization.od_report_sessionsummary_short'
    _inherit = 'report.abstract_report'
    _template = 'od_pos_customization.od_report_sessionsummary_short'
    _wrapped_report_class = od_report_sessionsummary    
