import typer 
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

# defined add func, and created task, category, and description variables.
@app.command(short_help='adds an item')
def add(task: str, category:str, description:str):
    typer.echo(f"adding {task}, {category}, {description}")

@app.command()
def delete(position:int):
    typer.echo(f"deleting {position}")


@app.command()
def update(position:int, task:str = None, category:str = None, description:str=None):
    typer.echo(f"updating {position}")






if __name__ == "__main__":
    app()