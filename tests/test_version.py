import pathlib

import tomllib

import pagemeta


def test_version():
    path = pathlib.Path("pyproject.toml")
    data = tomllib.loads(path.read_text())
    version = data["tool"]["poetry"]["version"]
    assert version == pagemeta.__version__
