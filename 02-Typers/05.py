# Anotation :

import typer
from typing_extensions import Annotated

app = typer.Typer()

# Add empty function because Annotated dont work with one function :
@app.command()
def add():
    pass


@app.command()
def delete(username, confirm:Annotated[bool, typer.Option(prompt="Are you sure ? ")]):
    if confirm:
        print(f"Deleteing User : {username}")
    else: 
        print("Operation Canceled")


if __name__ == "__main__":
    app()