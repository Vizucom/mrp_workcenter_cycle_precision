# -*- coding: utf-8 -*-
from openerp import models, fields, api, _, exceptions
import openerp.addons.decimal_precision as dp


class MrpWorkcenter(models.Model):

    _inherit = 'mrp.workcenter'

    time_cycle = fields.Float(digits=dp.get_precision('Workcenter Cycles'))
    time_start = fields.Float(digits=dp.get_precision('Workcenter Cycles'))
    time_stop = fields.Float(digits=dp.get_precision('Workcenter Cycles'))