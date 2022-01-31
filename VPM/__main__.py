import typer
import halo
from halo import Halo
import os
from subprocess import PIPE, Popen


app = typer.Typer()


@app.command()
def install(package: str):
    typer.echo(f"Installing {package}.")
    spinner = halo.Halo(text=f'Upgrading pip.', spinner='dots')
    spinner.start()
    pipe = Popen("python -m pip install --upgrade pip",
                 shell=True, stdout=PIPE, stderr=PIPE)
    stream, stream_err = pipe.communicate()
    spinner.stop()
    spinner = halo.Halo(
        text=f"Installing {package} with pip.", spinner="bouncingBall")
    spinner.start()
    stream = os.popen(f'pip install {package}')
    output = stream.read()
    stream.close()
    spinner.stop()
    typer.echo("\n")
    typer.echo(output)

    typer.echo(f"package {package} installed successfully")


@app.command()
def run(command: str):
    typer.echo(f"Now running {command}.")


if __name__ == "__main__":  # pragma: no cover
    from src.initialize import initialize_proj

    @app.command()
    def init():
        initialize_proj()

    app()
