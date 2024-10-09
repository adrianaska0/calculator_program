import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    '''Test exit command'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_uknown_command(capfd, monkeypatch):
    '''Test unknown command handling'''
    inputs = iter(['unknown_command 3 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()
    res = capfd.readouterr()
    assert "No such command: unknown_command" in res.out