# lab.python

Adventures on Python

## Requirements

See `requirements.txt`

## Setting the .venv environment

### From VSCode

[Creating environments](https://code.visualstudio.com/docs/python/environments#_creating-environments)

> Using the Create Environment command
From within VS Code, you can create local environments, using virtual environments or Anaconda, by opening the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment command to search, and then select the command.

### From the Shell

``` shell
# you may need to upgrade pip first
python -m pip install --upgrade pip

python -m venv .venv
./.venv/scripts/activate # bash -> source .venv/bin/activate
python -m pip install -U -r requirements.txt
```
