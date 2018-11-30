## -*- coding: utf-8 -*-

from openerp import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
import xlrd
import shutil



class respartnerzonas(models.Model):
	_name = 'zonas.partner'

	name = fields.Char(string='Zona de Residencia', help='Coloca la zona de residencia para especificar la zona de localizacion', requiered=True)



class InheritZona(models.Model):

	_inherit = 'res.partner'

	zone = fields.Many2one('zonas.partner',string='Zona de Entrega', help='Coloca la zona de residencia para especificar la zona de localizacion')




