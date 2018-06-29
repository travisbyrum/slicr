"""
Created June 29, 2018

@author: Travis Byrum
"""

from slicr.cli import main


def test_cli_main_version(runner):
    """Test cli main invokation."""

    result = runner.invoke(main, ['--version'])

    assert result.exit_code == 0


def test_cli_db_create(runner, db):
    """Test cli database creation."""

    db.drop_all()

    result = runner.invoke(main, ['db', 'create'])

    assert result.exit_code == 0


def test_cli_db_delete(runner, db):
    """Test cli database deletion."""

    result = runner.invoke(main, ['db', 'delete'])

    db.create_all()

    assert result.exit_code == 0
