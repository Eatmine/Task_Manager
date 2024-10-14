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

def insert_todo(todo:Todo):
    c.execute("select count(*) FROM todos")
    count = c.fetchonee()[0]
    todo.position = count if count else 0
    data = {"task": todo.task, "category": todo.category, "description" : todo.description,
            "date_assigned": todo.date_assigned, "priority":todo.priority, "date_completed": todo.date_completed,
            "status":todo.status, "position": todo.position}
    with connect:
        c.execute('INSERT INTO todos VALUES (:task, :category, :description, :date_assigned, :date_completed, :status, :position)',data)

def get_all_todos() -> List[Todo]:
    c.execute('select * from todos')
    records = c.fetchall()
    todos = []
    for row in records:
        todos.append(Todo(*row))
    return todos