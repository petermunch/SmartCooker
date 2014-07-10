#!/usr/bin/env python
__author__ = 'munchp'

import sqlite3 as lite
from datetime import datetime

con = lite.connect('database/dbs/temperatures.db', check_same_thread=False)

time = datetime.now().time()
t = time.strftime('%H:%M:%S')  #TODO: Kontrollere nyt format


def db_insert_pit(temperature):

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Pit(Time, Celcius) VALUES(?,?)", (t, temperature))
        print "Temperature added to db"


def db_insert_grill(temperature):

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Grill(Time, Celcius) VALUES(?,?)", (t, temperature))
        print "Temperature added to db"


def db_insert_food(temperature):

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Food(Time, Celcius) VALUES(?,?)", (t, temperature))
        print "Temperature added to db"


def db_fetch_pit():

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Pit")

    rows = cur.fetchall()
    print "Data From Pit"
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Time"], row["Celcius"])


def db_fetch_grill():

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Grill")

    rows = cur.fetchall()
    print "Data From Grill"
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Time"], row["Celcius"])


def db_fetch_food():

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Food")

    rows = cur.fetchall()
    print "Data From Food"
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Time"], row["Celcius"])