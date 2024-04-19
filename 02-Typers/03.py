import typer

def uppercase(name:str,uppercase:bool=False):
    if uppercase :
        print(name.upper())
    else :
        print(name)


if __name__ == "__main__":
    typer.run(uppercase)
