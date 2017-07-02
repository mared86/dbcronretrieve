import datetime

import mysql.connector
import psycopg2
from odoo import models


class e3tmad_cron_retrieve(models.TransientModel):
    _name = 'e3tmad.cron.retrieve'

    def retrieve(self):

        tables = self.env['e3tmad.table'].search([('is_ret', '=', True)])
        for table in tables:
            if (table.db_id.driver == 'mys'):
                con = mysql.connector.connect(host=table.db_id.host, user=table.db_id.user,
                                              password=table.db_id.password, database=table.db_id.dbname)

                cursor = con.cursor()

                cursor.execute(table.qustring)
                data = cursor.fetchall()
                self.store_date(data=data, table=table)

                con.close()
            if (table.db_id.driver == 'pg'):
                conn = psycopg2.connect(table.db_id.constring)
                cursor = conn.cursor()
                cursor.execute(table.qustring)
                data = cursor.fetchall()
                self.store_date(data=data, table=table)

    def store_date(self, data, table):
        self.env['e3tmad.result'].sudo().create(
            {'name': table.name + ' ' + str(datetime.datetime.now()), 'table': table.name,
             'query': table.qustring,
             'result': str(data)})
