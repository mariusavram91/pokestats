# PokeStats

Command line tool that takes a pokemon name as a parameter and displays its statistics using PokeAPI (https://pokeapi.co).

## Environment

If you don't have Python you can follow the instructions from https://www.python.org/downloads/.

Make sure to install Python 3.x

First, create an environment.
```
$ virtualenv env
```
If you have both python 2.x and 3.x versions, use the below command.
```
$ virtualenv --python=/usr/bin/python3 env
```
You can activate it.
```
$ source ./env/bin/activate
```
Verify the version of python with the below command.
```
$ python
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
When not using you can deactivate it.
```
$ deactivate
```
## Dependencies

```
$ pip install -r requirements.txt
```

## Run the script

Python 3 is a requirement.

```
$ python pokestats.py bulbasaur
```

### Output example

```
******************************************************************
Stats for bulbasaur
******************************************************************
speed
        base: 45
        effort: 0
special-defense
        base: 65
        effort: 0
special-attack
        base: 65
        effort: 1
defense
        base: 49
        effort: 0
attack
        base: 49
        effort: 0
hp
        base: 45
        effort: 0
```

### Executable (Linux)

```
$ sudo make install
$ pokestats pikachu
```
