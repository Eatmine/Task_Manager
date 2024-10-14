import sqlite3
from typing import List 
import datetime
from model import Todo

connect = sqlite3.connect("todos.db")
c = connect.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos(
    task text,
    category text,
    description text,
    date_assigned text,
    priority text,
    date_completed
    status integer,
    position integer,
    )""")

create_table()

