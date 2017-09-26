# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2017 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html.
#
##############################################################################
{
    'name': 'Workcenter Cycle Precision',
    'summary': 'Increaced decimal precision for workcenter cycles',
    'version': '8.0.1.0.0',
    'category': 'MRP',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta OS Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'mrp',
    ],
    'data': [
        'data/decimal_precision.xml',
        'views/mrp_workcenter.xml',
    ],
}
