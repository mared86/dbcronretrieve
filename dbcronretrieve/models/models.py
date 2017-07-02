# -*- coding: utf-8 -*-

from odoo import models, fields, api


class e3tmad_field(models.Model):
    _name = 'e3tmad.field'
    _rec_name = 'name'
    name = fields.Char('Field Name', requiered=True)
    table_id = fields.Integer('Table')


class e3tmad_databases(models.Model):
    _name = 'e3tmad.database'

    name = fields.Char('Drivername')
    driver = fields.Selection([('mys', 'MySql'), ('pg', 'Postgres')])
    host = fields.Char('Host')
    user = fields.Char('Server User')
    password = fields.Char('Server Password')
    dbname = fields.Char('Database')

    @api.one
    @api.depends('driver', 'user', 'password', 'dbname')
    def _calconstr(self):

        if (self.driver == 'pg'):
            conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
                self.host, self.dbname, self.user, self.password)
            self.constring = conn_string

        if (self.driver == 'mys'):
            conn_string = 'co = host = "%s", db = "%s", user = "%s", passwd = "%s"' % (
                self.host, self.dbname, self.user, self.password)
            conn_dic = '{ "host" : "%s", "db" : "%s", "user" : "%s", "passwd" : "%s"}' % (
                self.host, self.dbname, self.user, self.password)

            self.constring = conn_string

    constring = fields.Char('Connnection String', store=True, compute='_calconstr')


class e3tmad_table(models.Model):
    _name = 'e3tmad.table'

    name = fields.Char('Query Name')
    db_id = fields.Many2one('e3tmad.database', 'DataBase')
    table = fields.Char('Table')
    is_ret = fields.Boolean('is Retievable', default=True)
    where = fields.Many2one('e3tmad.wherefield', string='Where Condition')
    tb_fields = fields.One2many('e3tmad.field', 'table_id', string='Select Fields')

    @api.one
    @api.depends('table', 'tb_fields', 'where')
    def _calqystr(self):
        qu_fields = ''
        if len(self.tb_fields) > 0:
            for field in self.tb_fields:
                if field.name != False:
                    if (qu_fields == ''):
                        qu_fields = qu_fields + ' ' + field.name
                    else:
                        qu_fields = qu_fields + ' , ' + field.name
        qs = 'SELECT %s  FROM %s  WHERE %s BETWEEN %s AND %s' % (
            qu_fields, self.table, self.where.field.name, self.where.from_value, self.where.to_value)
        self.qustring = qs

    qustring = fields.Char('Quary String', store=True, compute='_calqystr')


class e3tmad_where_field(models.Model):
    _name = 'e3tmad.wherefield'

    field = fields.Many2one('e3tmad.field', string='Field', requiered=True)
    from_value = fields.Char(string='From', requiered=True)
    to_value = fields.Char(string='To', requiered=True)

    def name_get(self):
        result = []
        for record in self:
            if record.id==False:
                return result
            result.append(
                (record.id,
                 u'%s from %s to %s' % (record.field.name, record.from_value, record.to_value)
                 ))
            return result
