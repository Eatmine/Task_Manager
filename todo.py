import typer 
from rich.console import Console
from rich.table import Table
from typing import Optional
import datetime


console = Console()
app = typer.Typer()

# defined add func, and created task, category, and description variables.
@app.command(short_help='adds an item, enter Oct dd-yyyy HH:mmAM/PM ')
def add(task: str, category:str, description:str, date_assigned:str, priority:str):
    format = '%b %d %Y %I:%M%p'
    date_assigned = datetime.datetime.strptime(date_assigned, format)
    print(f"adding {task}, {category}, {description} , {date_assigned}, {priority}")

@app.command()
def delete(position:int):
    print(f"deleting {position}")

@app.command()
def update(position:int, task: Optional[str] = None, category: Optional[str] = None, description: Optional[str] = None, 
date_assigned: Optional[str] = None, priority: Optional[str] = None       ):
    print(f"updating {position}")

@app.command()
def complete(position:int):
    print(f"complete {position}")

@app.command()
def show():
    tasks = [("Apply to Apprenticeship", "LinkedIn", "Fill Out The Application by 10/15", "Oct 09 2024 9:00AM", "HIGH")]
    console.print("[bold magenta]Todos!", "💻")

    table = Table(show_header=True, header_style="bold_blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Task", width=6, justify="center")
    table.add_column("Category", width=6, justify="center")
    table.add_column("Description", width=6, justify="center")
    table.add_column("Date Assigned", width=6, justify="center")
    table.add_column("Priority", width=6, justify="center")
    table.add_column("Complete", width=6, justify="center")

    def get_priority_color(priority):
        COLORS = {"HIGH": "red", "MEDIUM": "dark_orange", "LOW": "yellow1"}
        if priority in COLORS:
            return COLORS[priority]
        else:
            return "white"

    for idx, task in enumerate(tasks,start=0):
        c = get_priority_color(task[-1])
        is_done_str = "✅" if True ==2 else "❌"
        table.add_row(str(idx), task[0], task[1], task[2], task[3], f'[{c}]{task[4]}[/{c}]', is_done_str)
    
    console.print(table)
















if __name__ == "__main__":
    app()