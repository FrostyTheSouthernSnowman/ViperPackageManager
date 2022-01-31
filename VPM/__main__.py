import typer
import halo
from halo import Halo
import os
from src.initialize import initialize_proj


app = typer.Typer()


@app.command()
def install(package: str):
    typer.echo(f"Installing {package}.")
    spinner = halo.Halo(text=f'Upgrading pip.', spinner='dots')
    spinner.start()
    stream = os.popen("python -m pip install --upgrade pip")
    spinner.stop()
    spinner = halo.Halo(
        text=f"Installing {package} with pip.", spinner="bouncingBall")
    spinner.start()
    stream = os.popen(f'pip install {package}')
    output = stream.read()
    stream.close()
    spinner.stop()
    print("\n")
    typer.echo(output)

    typer.echo(f"package {package} installed successfully")


@app.command()
def run(command: str):
    typer.echo(f"Now running {command}.")


@app.command()
def init():
    initialize_proj()


if __name__ == "__main__":  # pragma: no cover
    app()
