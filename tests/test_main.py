from typer.testing import CliRunner

from VPM.main import app

runner = CliRunner()


def test_run():
    result = runner.invoke(app, ["run", "my-script"])
    assert result.exit_code == 0
    assert "Now running my-script." in result.stdout


def test_install():
    result = runner.invoke(app, ["install", "my-dep"])
    assert result.exit_code == 0
    assert "Installing my-dep." in result.stdout
