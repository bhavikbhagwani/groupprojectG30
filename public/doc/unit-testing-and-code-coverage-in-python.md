---
revision: 
    2023-02-20: "(B, mos) change base repo to oopython"
    2022-01-04: "(A, mos) first version"
---
Unit testing and code coverage in Python
=============================

This is a walkthrough on how to work with unit testing and code coverage in Python using existing code examples.

In this article/exercise you will learn how to create and run unit tests together with code coverage in Python.

The article does not explicitly show how to create the code nor unittest, it just provide the foundation where you can work and do that on your own. Theefore you need to have the documentation for [Python unittest](https://docs.python.org/3/library/unittest.html) at hand.

[[_TOC_]]



Preconditions
--------------------------

The article is written to be used on one of the following environments.

* Windows where Python is installed in the Windows installation and the terminal used is Git Bash.
* Linux, macOS or Windows with WSL using a bash compatible terminal.

The unittest framework used is [Python unittest](https://docs.python.org/3/library/unittest.html).

To generate and display code coverage the [package coverage](https://coverage.readthedocs.io/) is used.



Prepare
--------------------------

There is a repo to use for the exercise and you will [find it on GitLab](https://gitlab.com/mikael-roos/oopython). Review the repo and its content before downloading it.



### Download the repo

Start by downloading the repo, either as a zip-file (check the web page for download options) or using `git clone`.

This is how you can `git clone` in the terminal.

```
git clone https://gitlab.com/mikael-roos/oopython.git
cd oopython
ls
```



### Create the virtual environment

Create and use the virtual venv.

```
make venv
```

If you use a Python installation on Window, then activate like this.

```
. .venv/Scripts/activate
```

If you use a Python installation on Mac/Linux, then activate like this.

```
. .venv/bin/activate
```

Do not forget to `deactivate` when you are done.



### Install the essentials

You can now install the essential Python packages from the file `requirements.txt`.

```
make install

# Show the installed packages
make installed
```



Exercise 1 - Dice
--------------------------

Execute the program.

```
cd src/dice
python main.py
```

Review its source code to learn about it.

Execute the linters to check how they rate the code.

```
make flake8
make pylint
make lint
```

Execute the unit tests by running them from their main function.

```
python test_dice.py
```

Review the code for the unit tests, it is in the file `test_dice.py`. That is how you can write the unit tests.

You can also execute the testsuite using make.

```
make unittest
```

In the makefile we use another way of executing all the unit tests in the current folder. You can try to execute this command to see all the tests execute again.

```
python3 -m unittest discover
```

If you add a `-v` option you will se more details on each testcase executed.

```
python3 -m unittest discover -v
```

Lets move over to code coverage.

Run the coverage report to see how well the unit tests cover the code. Start by executing the testsuite and recording the basis for the coverage.

This is how to do it all from the Makefile.

```
make coverage
```

This is how to run the actual commands, one by one.

```
coverage run -m unittest discover
```

The execute the coverage report.

```
$ coverage report -m
Name      Stmts   Miss  Cover   Missing
---------------------------------------
dice.py      20      4    80%   64-65, 76, 80
---------------------------------------
TOTAL        20      4    80%
```

Do also execute the coverage report and generate HTML of it. You can then open the report in a web browser.

```
$ coverage html
$ ls htmlcov/
$ firefox htmlcov/index.html
```

In your web browser you can now inspect the parts that is covered and not covered by unit tests.



### NOW - DO THIS

Try to add more unit testcases to reach a code coverage of 100%.

When you are done, execute `make test` that executes `make lint coverage` to get the final results displayed of your effort.

You can remove all the generated files by using the target clean in the Makefile.

```
make clean
```



Exercise 2 - Guess my number
--------------------------

Play a game of "Guess my number", add a feature to it and add unit tests to cover it.

Execute the game.

```
cd src/guess
python main.py
```

Try to understand how the program works and review the details of it. You can start by checking out the files and classes from this list.

| File | Purpose |
|------|---------|
| `main.py`  | The main program, where the execution starts. |
| `shell.py` | Using the cmd module to create a shell for the main program. |
| `game.py`  | Guess the number I am thinking of. |

Execute the test suite to see how well the code is doing. This includes the linters (pylint, flake8) and the unit tests and the code coverage report.

```
make test
```

Consider if all tests are there, is something missing?



### NOW - DO THIS

Add the most of your code into the Game class.

Avoid adding to much code into the class Shell since that is not covered of unit tests. Perhaps it could/should be added though, but let leave that for another day.

1. Add the end of the game, so one knows when the game is over or one has won.
1. Show the number of guesses the player has done.
1. Limit the number of guesses so one has max 5 guesses.
1. Add unit tests to try to make 100% of code coverage in the Game class.
1. Ensure that `make test` pass without errors.



### Extra features

Do this if you have the energy and if you want more practise.

1. Add a command "log" which prints out a log of all the games played, showing the statistics if the computer or the player won, how many guesses it took and what number it was.
1. Save the log/highscore to a file.
1. Add unit tests.
1. Get high coverage.
1. Ensure `make test` pass.



Resources
--------------------------

About the cmd package.

* [cmd — support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)

About code style and being pythonic.

* [The hitchhiker's Guide to Python - Code Style](https://docs.python-guide.org/writing/style/).

About linting.

* Static code analysis with [pylint](https://www.pylint.org/)
    * [pypi pylint](https://pypi.org/project/pylint/)
* Static code analysis with [flake8](https://flake8.pycqa.org/en/latest/)
    * [pypi flake8](https://pypi.org/project/flake8/)
    * [pypi flake8-docstrings](https://pypi.org/project/flake8-docstrings/)

About unit testing and code coverage.

* [Python doctest](https://docs.python.org/3/library/doctest.html)
* [Python unittest](https://docs.python.org/3/library/unittest.html)
* [Python coverage](https://coverage.readthedocs.io/)
