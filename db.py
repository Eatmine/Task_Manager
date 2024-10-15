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
        c.execute("INSERT INTO todos VALUES (:task, :category, :description, :date_assigned, :date_completed, :status, :position)",data)

def get_all_todos() -> List[Todo]:
    c.execute("select * from todos")
    records = c.fetchall()
    todos = []
    for row in records:
        todos.append(Todo(*row))
    return todos

def delete_todo(position):
    c.execute("select count(*) from todos")
    count = c.fetchone()[0]

    with connect:
        c.execute("DELETE from todos WHERE position=:position", {"position":position})
        for pos in range(count):
            if position == pos:
                return position
        

def update_todo(position: int, task:str, category:str, description:str, date_assigned:str,priority:str ):
    with connect:
        if task is not None and category is not None and description is not None and priority is not None and date_assigned is not None:
            c.execute("UPDATE todos SET task =:task, category =:category, description =:description, date_assigned=:date_assigned, priority=:priority WHERE position =:position",
                        {"position": position, "task":task, "category": category, "description":description, "priority":priority,"date_assigned":date_assigned })

        elif task is not None:
            c.execute("UPDATE todos SET task =:task WHERE position =:position",
                        {"position":position, "task":task})
            
        elif category is not None:
            c.execute("UPDATE todos SET category =:category WHERE position =:position",
                        {"position":position, "category":category})
        
        elif description is not None:
            c.execute("UPDATE todos SET description =:description WHERE position =:position",
                        {"position":position, "description":description})
        
        elif date_assigned is not None:
            c.execute("UPDATE todos SET date_assigned =:date_assigned WHERE position =:position",
                        {"position":position, "date_assigned":date_assigned})
            
        elif priority is not None:
            c.execute("UPDATE todos SET priority =:priority WHERE position =:position",
                        {"position":position, "priority":priority})
            

def complete_todo(position):
    with connect:
        c.execute("UPDATE todos SET status = 2 , date_completed = :date_completed WHERE position = :position",
                  {"position":position, "date_completed":datetime.datetime.now().isoformat()})
