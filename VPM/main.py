import typer


app = typer.Typer()


@app.command()
def install(package: str):
    typer.echo(f"Installing {package}.")


@app.command()
def run(command: str):
    typer.echo(f"Now running {command}.")


if __name__ == "__main__":  # pragma: no cover
    app()
