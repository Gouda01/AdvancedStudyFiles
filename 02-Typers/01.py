import typer

def mysum(x:int,y:int):
    print(x+y)


if __name__ == "__main__":
    typer.run(mysum)
