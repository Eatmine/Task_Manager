import typer 
from rich.console import Console
from rich.table import Table
from typing import Optional
import datetime
from model import Todo
from db import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo


console = Console()
app = typer.Typer()

# defined add func, and created task, category, and description variables.
@app.command(short_help='adds an item, enter Oct dd-yyyy HH:mmAM/PM ')
def add(task: str, category:str, description:str, date_assigned:str, priority:str):
    format = '%b %d %Y %I:%M%p'
    date_assigned = datetime.datetime.strptime(date_assigned, format)
    typer.echo(f"adding {task}, {category}, {description} , {date_assigned}, {priority}")
    todo = Todo(task,category,description,date_assigned,priority)
    insert_todo(todo)
    show()

@app.command()
def delete(position:int):
    typer.echo(f"deleting {position}")
    delete_todo(position)
    show()

@app.command()
def update(position:int, task: Optional[str] = None, category: Optional[str] = None, description: Optional[str] = None, 
date_assigned: Optional[str] = None, priority: Optional[str] = None):
    typer.echo(f"updating {position}")
    update_todo(position = position,task=task,category=category,description=description,priority=priority,date_assigned=date_assigned)
    show()

@app.command()
def complete(position:int):
    typer.echo(f"complete {position}")
    complete_todo(position)
    show()

@app.command()
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]Todos!", "💻")

    table = Table(show_header=True, header_style="blue1")
    table.add_column("#", style="dim", width=6)
    table.add_column("Task", width=13, justify="center")
    table.add_column("Category", width=13, justify="center")
    table.add_column("Description", width=13, justify="center")
    table.add_column("Date Assigned", width=13, justify="center")
    table.add_column("Priority", width=13, justify="center")
    table.add_column("Complete", width=13, justify="center")

    def get_priority_color(priority):
        COLORS = {"HIGH": "red", "MEDIUM": "dark_orange", "LOW": "cyan"}
        if priority in COLORS:
            return COLORS[priority]
        else:
            return "white"

    for idx, task in enumerate(tasks,start=0):
        c = get_priority_color(task.priority)
        is_done_str = "✅" if task.status == 2 else "❌"
        table.add_row(str(idx), task.task, task.category, task.description, task.date_assigned, f'[{c}]{task.priority}[/{c}]', is_done_str)
    
    console.print(table)



if __name__ == "__main__":
    app()