#!/usr/bin/env python
__author__ = 'munchp'

import os.path
import sqlite3 as lite
from datetime import datetime
from sensors import sensors

import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# Get the connection from database/dbs/ directory
con = lite.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'database/dbs/settings.db')), check_same_thread=False)
#(":memory:", check_same_thread=False)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={'status': StatusModule},
            debug=True,
            autoescape=None
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM recipes")
        row = cur.fetchone()
        self.render(
            "index.html",
            page_title = "SmartCooker | Home",
            header_text = "Velkommen til SmartCooker",
            sub_header = "Dit smarte mad valg",
            footer_text = "Her kunne man evt. have noget footer tekst",
            recipe_name = row["Name"],
            setpoint_grill = row["Grill Target"],
            setpoint_food = row["Food Target"],
            cooking_time = row["Cooking Time"],
            email_alert = "ON",
            simulation = "ON",
            grill_temp = sensors.grill_temperature(),
            pit_temp = sensors.pit_temperature(),
            elapsed_time = 35,
            remaining_time = 355
        )

    def post(self):
        start_cooker = self.get_argument('btn_start','')


class StatusModule(tornado.web.UIModule):
    def render(self, status):
        return self.render_string("modules/status.html", status = status)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()