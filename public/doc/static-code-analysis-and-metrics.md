Static code analysis and software metrics
=========================

We will practice how to perform various static code analysis and collect software metrics that can aid in visualizing the software quality and provide a startpoint to work to enhance the software quality.

We will use two tools called `radon` and `bandit`. Both perform static code analysis and presents reports that can be used to analyse and improve your codebase.

The tool `radon` is for collecting various software metrics.

The tool `flake8` uses a module `cohesion` that reports metrics on cohesion.

The tool `bandit` is designed to find common security issues in Python code.

The intention of this exercise is for you to learn to use the tools and to produce some reports using them.



Preconditions
--------------------------

The article is written to be used on one of the following environments.

* Windows where Python is installed in the Windows installation and the terminal used is Git Bash.
* Linux, macOS or Windows with WSL using a bash compatible terminal.



Prepare
--------------------------

You already have [the exercise repo](https://gitlab.com/mikael-roos/oopython) with the "dice" and the "guessing game".

You should work in your virtual environment where you previously did a `make install`. Do not forget to activate your virtual environment.



Read the docs
--------------------------

Before you start you should ger familiar with the documentation for the two tools we are going to use.

* [Radon documentation](https://radon.readthedocs.io/en/latest/)
* [Cohesion documentation](https://github.com/mschwager/cohesion)
* [Bandit documentation](https://bandit.readthedocs.io/en/latest/)

Do note that the documentation for Radon and Bandit tools are generated using [Sphinx](https://www.sphinx-doc.org/en/master/). That is a common way to write and generate documentation for Python projects.



Video with slide lecture
---------------------------

There is a slide lecture on the topic "Static code analysis" you can review before or after working through this exercise. It will give you some background on the metrics collected and how they relate to good code practices.

English version.

[![](http://img.youtube.com/vi/SLot2a9m5gE/0.jpg)](http://www.youtube.com/watch?v=SLot2a9m5gE "YouTube: Software quality metrics and static code analysis (English)")

Swedish version.

[![](http://img.youtube.com/vi/AEpbjtpO1T0/0.jpg)](http://www.youtube.com/watch?v=AEpbjtpO1T0 "YouTube: Software quality metrics and static code analysis (Swedish)")



Exercise 1 - Radon
--------------------------

Lets start to see what version we have available of the program.

```
# Check the version
radon --version

# Check where it is installed
which radon
```

It can look like this (your version and output may vary).

```
$ radon --version
5.1.0
```

Good, now we now it works.



### Raw metrics

Radon can produce raw metrics for the code. It can look like this.

```
$ radon raw .
dice_test.py
    LOC: 32
    LLOC: 20
    SLOC: 16
    Comments: 2
    Single comments: 6
    Multi: 0
    Blank: 10
    - Comment Stats
        (C % L): 6%
        (C % S): 12%
        (C + M % L): 6%
dice.py
    LOC: 39
    LLOC: 24
    SLOC: 19
    Comments: 2
    Single comments: 7
    Multi: 0
    Blank: 13
    - Comment Stats
        (C % L): 5%
        (C % S): 11%
        (C + M % L): 5%
```

Read the following about what the `raw` command generates for type of metrics.

* [Raw Metrics](https://radon.readthedocs.io/en/latest/intro.html#raw-metrics)
* [The raw command](https://radon.readthedocs.io/en/latest/commandline.html#the-raw-command)

Ensure you can execute the command in the exercise repo `dice/`, `dice_graphic/` and `guess/` and try to relate to the data.

A good idea is to save the output in a file and compare the output on the three directories.



### Cyclomatic complexity (McCabe)

Radon can produce metrics about the cyclomatic complexity according to McCabe. It can look like this.

```
$ radon cc --show-complexity --average .
main.py
    F 30:0 main - A (3)
test_dice.py
    C 10:0 TestDiceClass - A (2)
    M 13:4 TestDiceClass.test_init_default_object - A (1)
    M 22:4 TestDiceClass.test_roll_a_dice - A (1)
dice.py
    C 49:0 Dice - A (2)
    M 55:4 Dice.__init__ - A (1)  
    M 62:4 Dice.set_faces - A (1)
    M 67:4 Dice.roll - A (1)
    M 74:4 Dice.get_rolls_made - A (1)
    M 78:4 Dice.get_sum_rolls - A (1)

10 blocks (classes, functions, methods) analyzed.
Average complexity: A (1.4)
```

Read the following about what the `cc` command generates for type of metrics.

* [Cyclomatic Complexity](https://radon.readthedocs.io/en/latest/intro.html#cyclomatic-complexity)
* [The cc command](https://radon.readthedocs.io/en/latest/commandline.html#the-cc-command)

Ensure you can execute the command in the exercise repo `dice/`, `dice_graphic/` and `guess/` and try to relate to the data.

A good idea is to save the output in a file and compare the output on the three directories.



### Halstead metrics

Radon can produce Halstead metrics. It can look like this.

```
$ radon hal .
dice_test.py:
    h1: 2
    h2: 5
    N1: 3
    N2: 5
    vocabulary: 7
    length: 8
    calculated_length: 13.60964047443681
    volume: 22.458839376460833
    difficulty: 1.0
    effort: 22.458839376460833
    time: 1.2477132986922685
    bugs: 0.007486279792153611
dice.py:
    h1: 2
    h2: 4
    N1: 2
    N2: 4
    vocabulary: 6
    length: 6
    calculated_length: 10.0
    volume: 15.509775004326936
    difficulty: 1.0
    effort: 15.509775004326936
    time: 0.861654166907052
    bugs: 0.005169925001442312
```

Read the following about what the `hal` command generates for type of metrics.

* [Halstead Metrics](https://radon.readthedocs.io/en/latest/intro.html#halstead-metrics)
* [The hal command](https://radon.readthedocs.io/en/latest/commandline.html#the-hal-command)

Ensure you can execute the command in the exercise repo `dice/`, `dice_graphic/` and `guess/` and try to relate to the data.

A good idea is to save the output in a file and compare the output on the three directories.



### Maintainability index (Visual Studio version)

Radon can produce metrics as the Maintainability index. It can look like this.

```
$ radon mi --show .
dice_test.py - A (81.17)
dice.py - A (79.09)
```

Read the following about what the `mi` command generates for type of metrics.

* [Maintainability Index](https://radon.readthedocs.io/en/latest/intro.html#maintainability-index)
* [The mi command](https://radon.readthedocs.io/en/latest/commandline.html#the-mi-command)

Ensure you can execute the command in the exercise repo `dice/`, `dice_graphic/` and `guess/` and try to relate to the data.

A good idea is to save the output in a file and compare the output on the three directories.



Exercise 2 - Cohesion
--------------------------

Lets start to see that the program is installed.

```
# Get help for the command
cohesion -h
```

You should see the help text for the command.



### Cohesion

Cohesion can produce metrics related to cohesion for the code.

When cohesion is high, it means that the methods and variables of the class are co-dependent and hang together as a logical whole.

```
$ cohesion --directory .
File: ./main.py
File: ./test_dice.py
  Class: TestDiceClass (10:0)
    Function: test_init_default_object 0/0 0.00%
    Function: test_roll_a_dice 0/0 0.00%
    Total: 0.0%
File: ./dice.py
  Class: Dice (49:0)
    Function: __init__ 2/3 66.67%
    Function: set_faces 1/3 33.33%
    Function: roll 3/3 100.00%
    Function: get_rolls_made 1/3 33.33%
    Function: get_sum_rolls 1/3 33.33%
    Total: 53.33%
```

When you have flake8 installed together with cohesion, then the flake8 command will also validate code with respect to cohesion.

Read the following about what the command generates for type of metrics.

* [Intro on the Cohesion command](https://github.com/mschwager/cohesion#cohesion)

Ensure you can execute the command in the exercise repo `dice/`, `dice_graphic/` and `guess/` and try to relate to the data.

A good idea is to save the output in a file and compare the output on the three directories.



Exercise 3 - Bandit
--------------------------

This tool will analyse your code from a security perspective and provide you with a report on potential security flaws in your code.

Lets start to see what version we have available of the program.

```
# Check the version
bandit --version
```

It can look like this (your version and output may vary).

```
$ bandit --version                                                   
bandit 1.7.2                                                         
  python version = 3.7.3 (default, Jan 22 2021, 20:04:44) [GCC 8.3.0]
```

Good, now we now it works.



### Try out the report

Lets run the command and check what type of data it can generate.

```
$ bandit --recursive .
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.7.3
Run started:2021-03-16 12:57:04.864321

Test results:
>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   Location: ./dice.py:22
   More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b311-random
21              self.rolls_made += 1
22              return random.randint(1, self.faces)
23

--------------------------------------------------

Code scanned:
        Total lines of code: 44
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0.0
                Low: 1.0
                Medium: 0.0
                High: 0.0
        Total issues (by confidence):
                Undefined: 0.0
                Low: 0.0
                Medium: 0.0
                High: 1.0
Files skipped (0):
```

Read the following about what the command generates for type of result.

* [Bandit Report Formatters](https://bandit.readthedocs.io/en/latest/formatters/index.html)

Ensure you can execute the command in the exercise repo `dice/`, `dice_graphic/` and `guess/` and try to relate to the data.

A good idea is to save the output in a file and compare the output on the three directories.



Makefile
--------------------------

The makefile supports the following targets.

```
# All metrics including:
# radon-cc radon-mi radon-raw radon-hal cohesion
make metrics

# Security issues
make bandit
```



References
--------------------------

Radon.

* [Download and install](https://pypi.org/project/radon/)
* [Documentation](https://radon.readthedocs.io/en/latest/)

Cohesion.

* [Repo on GitHub](https://github.com/mschwager/cohesion)

Bandit.

* [Download and install](https://pypi.org/project/bandit/)
* [Documentation](https://bandit.readthedocs.io/en/latest/)
