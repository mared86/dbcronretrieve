from odoo import models, fields

class e3tmad_result(models.Model):
    _name = 'e3tmad.result'

    name=fields.Char('Name')
    table=fields.Char('table')
    query=fields.Char('Sql Query')
    result=fields.Text('Result')