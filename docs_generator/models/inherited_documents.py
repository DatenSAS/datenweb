# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from datetime import date

import logging
_logger = logging.getLogger(__name__)

class documents_document(models.Model):

    _inherit = 'documents.document'

    def generar_documento(self):

        month_labels = {
            '1': 68,
            '2': 69,
            '3': 70,
            '4': 71,
            '5': 72,
            '6': 73,
            '7': 74,
            '8': 75,
            '9': 76,
            '10': 77,
            '11': 78,
            '12': 79,
        }

        year_labels = {
            '2023': 65,
            '2024': 66,
            '2025': 67,
        }

        contactos = self.env['res.partner'].search([('category_id','in',[2,5,3,4,6])])
        month = str(date.today().month)
        year = str(date.today().year)

        for contacto in contactos:
            if contacto.category_id.id == 2:
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids':[year_labels[year], month_labels[month], 83],
                    'name':'DS - ' + contacto.name,
                    'partner_id': contacto.id
                })
            elif contacto.category_id.id == 5:
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids': [year_labels[year], month_labels[month]],
                    'name': 'Extracto Bancario',
                    'partner_id': contacto.id
                })
            elif contacto.category_id.id == 3:
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids': [year_labels[year], month_labels[month], 81],
                    'name': 'FE Cliente - ' + contacto.name,
                    'partner_id': contacto.id
                })
            elif contacto.category_id.id == 4:
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids': [year_labels[year], month_labels[month], 80],
                    'name': 'FE Proveedor - ' + contacto.name,
                    'partner_id': contacto.id
                })
            elif contacto.category_id.id == 6:
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids': [year_labels[year], month_labels[month]],
                    'name': 'DIAN Retefuente',
                    'partner_id': contacto.id
                })
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids': [year_labels[year], month_labels[month]],
                    'name': 'DIAN IVA',
                    'partner_id': contacto.id
                })
                self.env['documents.document'].create({
                    'folder_id': 23,
                    'activity_type_id': 10,
                    'tag_ids': [year_labels[year], month_labels[month]],
                    'name': 'DIAN Declaración Renta',
                    'partner_id': contacto.id
                })