# Anti-Duplicator

The script searches for duplicates in the indicated folder. Two files are duplicates if their sizes and hash functions coincide.
For a better readability of the output install the module `termcolor` with the command
```#!bash
$ pip install -r requirements.txt
```
# Usage

```#!bash
$ python duplicates.py /Users/anyya/bot
Following duplicates were found:


Duplicates of many-body theory.pdf:
/Users/anyya/bot/physics/condensed matter/many-body theory.pdf
/Users/anyya/bot/physics/condensed matter/bosonization/lectures-2.pdf
/Users/anyya/bot/work/articles/bosonization/lectures-2.pdf

Duplicates of Solid State Theory.pdf:
/Users/anyya/bot/physics/condensed matter/Solid State Theory.pdf
/Users/anyya/bot/physics/solid state/Solid State Theory.pdf

...
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
