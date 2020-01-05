# mQuest: Python Mathematics Question Generator
Generates multiplication and division questions in a variety of formats, e.g.
- Multiplication questions (in order) *e.g. 7 times tables* 
- Multiplication questions (in mixed order) *e.g. 9 times tables questions in random order*
- Mixed multiplication questions *i.e. testing more than one times table at a time*
- Division questions (in mixed order) *e.g. divide by 8 questions*

As a bonus, to aid study it can generate a different set of questions for each day of the week.


## Table of contents
  * [Background](#background)
  * [Example outputs](#example-outputs)
  * [Installation](#installation)
  * [Usage](#usage)
    + [With CLI](#with-cli)
      - [Command line options](#command-line-options)
      - [Command line examples](#command-line-examples)
    + [As a module](#as-a-module)
  * [Contributions](#contributions)
  * [License](#license)


## Background
This originally started off as a script I wrote to generate mathematical questions focused around multiplications and divisions, for my daughter to learn and practice her times tables (using pen and paper).  

I decided it may be of use to others, and so, after some over-engineering, here we are!


## Example outputs
```txt
11 x table questions:
---------------------
 1 x 11 = 
 2 x 11 = 
 3 x 11 = 
 ...
12 x 11 = 
```

```txt
8 x table questions (shuffled):
-------------------------------
 6 x 8 = 
 1 x 8 = 
12 x 8 = 
...
 5 x 8 = 
```

```txt
÷ (divide by) 4 questions:
--------------------------
 44 ÷ 4 = 
 36 ÷ 4 = 
  8 ÷ 4 = 
...
 32 ÷ 4 = 
```

```txt
Mixed multiplication questions:
-------------------------------
 7 x 6 = 
 9 x 10 = 
12 x 8 = 
...
 6 x 3 = 


```


## Installation
mQuest is designed to run on Python 3.7 or later, and has no dependencies (other than those in the Python standard library).  To install, run the following at the command prompt:

    git clone https://github.com/JonathanWillitts/mquest.git


## Usage
mQuest can generate questions either by being run with its CLI from a command prompt, or by importing it as a python module and using it directly within your own script/program. 

### With CLI
#### Command line options:
You can list mQuest's options by running `python mquest/mquest.py --help` from the installation directory:
```cmd
usage: mquest.py [-h] -m {m,mm,d} -o OPERANDS [OPERANDS ...] [-s]
                 [-d {0,1,2,3,4,5,6}] [-f FILE]

mQuest: Python Mathematics Question Generator.

optional arguments:
  -h, --help            show this help message and exit
  -m {m,mm,d}, --mode {m,mm,d}
                        Mode, either: 'm' (multiplication), 'mm' (mixed
                        multiplication) or 'd' (division).
  -o OPERANDS [OPERANDS ...], --operands OPERANDS [OPERANDS ...]
                        The operand(s) to apply to the specified mode (used to
                        multiply or divide by). For mixed multiplications
                        specify multiple operands.
  -s, --shuffle         Shuffle order of generated questions (applies to
                        multiplication mode only).
  -d {0,1,2,3,4,5,6}, --start-day {0,1,2,3,4,5,6}
                        Start day, (0 for Monday, 1 for Tuesday, ..., 6 for
                        Sunday).
  -f FILE, --file FILE  If specified write to output file instead of printing
                        to stdout.

```

#### Command line examples:

Generate 7 times table questions:
```cmd
> python mquest/mquest.py --mode m --operands 7
Questions:
----------
 1 x 7 =
 2 x 7 =
 3 x 7 =
...
```

Generate 8 times table questions, and mix order:
```cmd
> python mquest/mquest.py --mode m --operands 8 --shuffle
Questions:
----------
 8 x 8 =
 3 x 8 =
 2 x 8 =
...
```

Generate divide by 9 questions:
```cmd
> python mquest/mquest.py --mode d --operands 9
Questions:
----------
 63 ÷ 9 =
108 ÷ 9 =
 72 ÷ 9 =
...
```

Generate mixed multiplication questions (from 2, 3 and 5 times tables):
```cmd
> python mquest/mquest.py --mode mm --operands 2 3 5
Questions:
----------
10 x 5 =
 5 x 3 =
 9 x 3 =
 1 x 2 =
...
```

Generate 12 times tables, for every day of the week starting Monday, and send output to file:
```cmd
> python mquest/mquest.py --mode m --operands 12 --start-day 0 --file times_12_questions.txt
> cat times_12_questions.txt
Monday:
-------
 1 x 12 = 
...

Tuesday:
--------
 1 x 12 = 
...

Wednesday:
----------
 1 x 12 = 
...

...
...

Sunday:
-------
...
```

### As a module
To run the examples file as as script, use:
```cmd
> python -m examples.examples
```

Note: all the examples below can be found in the [examples.py](examples/examples.py) file.  

```python
from mquest import mquest

# Generate a raw list of ordered 11 times table questions
times_11_questions = mquest.generate_multiplications(multiplier=11)

# Format and print them, with a heading
print(mquest.format_questions(heading="11 x table questions",
                              questions=times_11_questions))

# Generate a single set of 8 times tables questions, shuffle the order,
# format, and print
print(mquest.format_questions(
    heading="8 x table questions (shuffled)",
    questions=mquest.generate_multiplications(multiplier=8,
                                              shuffle_order=True),
))

# Generate a single set of division by 4 questions in shuffled order,
# format, and print
print(mquest.format_questions(
    heading="÷ (divide by) 4 questions",
    questions=mquest.generate_divisions(divisor=4)
))
```

to generate a set of questions for each day of the week:
```python
import calendar

from mquest import mquest # if not already imported

# Define list of study days (i.e. days to generate questions for),
# for each day of the week, starting on Friday
study_days = mquest.get_days_of_week(first_day=calendar.FRIDAY)

# Generate daily 3 times tables questions, in order, format, and print
# (for each day of the week)
for day in study_days:
    print(mquest.format_questions(
        heading=day,
        questions=mquest.generate_multiplications(multiplier=3),
    ))

# Generate daily, mixed, shuffled questions for 2, 3, 4, 5, 6, 8 & 10
# times tables, format, and print (for each day of the week)
for day in study_days:
    print(mquest.format_questions(
        heading=day,
        questions=mquest.generate_mixed_multiplications(
        multipliers=[2, 3, 4, 5, 6, 8, 10]),
    ))
```


## Contributions
Contributions to improve mQuest are welcomed, in the form of suggestions, bug fixes, new features, or anything else you see fit. Please submit a [pull request](https://github.com/JonathanWillitts/mquest/pulls).

## License
mQuest is licensed under the [MIT License](LICENSE)
