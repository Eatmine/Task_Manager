import typer 
from rich.console import Console
from rich.table import Table
from typing import Optional
import datetime


console = Console()
app = typer.Typer()

# defined add func, and created task, category, and description variables.
@app.command(short_help='adds an item, enter Oct dd-yyyy HH:mmAM/PM ')
def add(task: str, category:str, description:str, date_assigned:str):
    format = '%b %d %Y %I:%M%p'
    date_assigned = datetime.datetime.strptime(date_assigned, format)
    print(f"adding {task}, {category}, {description} , {date_assigned}")

@app.command()
def delete(position:int):
    print(f"deleting {position}")

@app.command()
def update(position:int, task: Optional[str] = None, category: Optional[str] = None, description: Optional[str] = None):
    print(f"updating {position}")

@app.command()
def complete(position:int):
    print(f"complete {position}")













if __name__ == "__main__":
    app()