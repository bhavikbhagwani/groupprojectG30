---
revision:
    "2023-01-04": "(B, mos) Added codestyle with black."
    "2022-01-04": "(A, mos) First version."
---
Work with an example Python development repo
=========================

This example shows how you can get going with a Python project using Git, Make, Python venv and examples of object oriented python code.

[[_TOC_]]



Video
---------------------------

The following video show when I work through parts of this article.

[![](http://img.youtube.com/vi/nWsm0COnWew/0.jpg)](http://www.youtube.com/watch?v=nWsm0COnWew "YouTube: Work with an example Python development repository with code analysis and test tools")



Preconditions
-------------------------

The article is written to be used on one of the following environments.

* Windows where Python is installed in the Windows installation and the terminal used is Git Bash.
* Linux, macOS or Windows with WSL.

You have an development environment that fulfills the needs as specified in [Lab environment](lab-environment).

You can work using a [Python virtual environment](python-venv).

You can [work with Git](work-with-git).



Clone the repo
-------------------------

You can visit the example repo at [GitLab oopython](https://gitlab.com/mikael-roos/oopython).

Start by cloning it.

```
git clone https://gitlab.com/mikael-roos/oopython.git
cd oopython
ls -la
```

Do investigate the files that comes with the repo. You can find the Python code in the directory `dice/`.



The Makefile
-------------------------

There is a Makefile included with the project that can help us work with the code and the test utilities included.

The Makefile has a setting that points to the Python executable to use. You need to verify that it is correct.

This will check what Python executable you are currently using with the Makefile.

```
make version
```

You can change the executable used by defining it of the command line or as a environment variable.

This is how to change on the command line.

```
PYTHON=python3 make version
```

This is how to do it using an environment variable.

```
export PYTHON=python3
make version
```

You could also go into the Makefile and update it. But that would be bad if your teammates have another setting for it so go ahead by using the environment variable like above.



Create the venv and install from requirements
-------------------------

The Makefile contains the commands to create the virtual environment.

```
make venv
```

Now we activate the venv.

```
# With Python installed in Windows
. .venv/Scripts/activate

# With Python installed in Mac/Linux
. .venv/bin/activate
```

Remember that you can deactivate the venv by just entering the command `deactivate`.

Lets stay in the venv and install the needed packages from the file `requirements.txt`. The makefile includes a target that does that.

```
make install
```

You can now check what packages that are installed. The Makefile contains a target to do this.

```
make installed
```

You can think of the Makefile as a container where you can store the commands and easily access them later on.



Run the programs
-------------------------

There are a set of example programs in this repo. You will find them below the `src/` directory. Lets try a few of them and do review the code within them.



### The dice example program

This program has a main program which uses a Dice class to roll a dice.

Run the program like this.

```
cd src/dice
python main.py
python main.py 7
```



### The linters

You can run the linters that verify the code using static code analysis.

```
make flake8
make pylint
make lint
```

Try to solve all issues you get warnings for. That helps you write good and clean code.



### Enforce codestyle

You can run the tool that enforces the codestyle.

```
make black
make codestyle
```

Your code might be updated to obey the codestyle "black". Having a unified codestyle is essential when working in teams.



### The unit test and code coverage

There are unit tests and reports of code coverage that you can run like this.

```
make unittest
make coverage
```

You can run both the linters and the unit tests with code coverage report like this.

```
make test
```



### The guess example program

This program has a main program which uses menu driven application to play a game of "Guess what number I think of".

Start by running the tests.

```
cd src/guess
make test
```

Now run the program like this.

```
python main.py
```

You can run the linters, codestyle and tests like you did with the other example program.



Summary
-------------------------

Now you have seen how you can package a development repository and get going with it and its development utilities.



References
-------------------------

* [GNU Make](https://www.gnu.org/software/make/manual/make.html)
* [Flake8](https://flake8.pycqa.org/)
* [pylint](https://pylint.org/)
* [Black](https://black.readthedocs.io/en/stable/)
* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/en/6.3.1/)
