# Game of life

An alternative implementation of the game of life using [pyxel](https://github.com/kitao/pyxel).

## Requirements

- [Poetry](https://python-poetry.org/)
- [Pyenv](https://github.com/pyenv/pyenv)

## Setup

1. `pyenv install 3.11.1`
1. `poetry install`
2. `poetry env use ~/.pyenv/versions/3.11.1/bin/python`
2. `poetry shell`
2. `python application.py`

## Pyxel related commands

The following commands are executed from the root of the project

### Create package

`pyxel package . ./application.py`

The package can be tested by running

`pyxel play game-of-life.pyxapp`

### Create html version

`pyxel app2html game-of-life`

Just copy the `game-of-life.html` path and try it out in a web browser.

## Additional notes

- background copied from https://github.com/k-o-matic/fictionx 
