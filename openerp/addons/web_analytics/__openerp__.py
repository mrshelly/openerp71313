# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2012 OpenERP s.a. (<http://openerp.com>).
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
    'name': 'Google Analytics',
    'version': '1.0',
    'category': 'Tools',
    'complexity': "easy",
    'description': """
Google Analytics.
=================

Collects web application usage with Google Analytics.
    """,
    'author': 'OpenERP SA',
    'website': 'http://openerp.com',
    'depends': ['web', 'auth_signup'],
    'data': [],
    'installable': True,
    'active': False,
    'js': ['static/src/js/web_analytics.js'],
}

