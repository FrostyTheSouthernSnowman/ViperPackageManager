from typer.testing import CliRunner

from VPM.__main__ import app

runner = CliRunner()


def test_initialize():
    result = runner.invoke(app, ["init"])
    print(result.stdout)
    assert result.exit_code == 0
    assert "Initialized viper project in current directory." in result.stdout
