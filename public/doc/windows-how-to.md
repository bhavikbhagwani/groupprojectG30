Exercise - Windows how to setup
==========================

This is a quick and dirty setup for the Windows development environment to make it compatible with the repo used in E02.



Install python
--------------------------

Do install python and check that its in your path. You can use any terminal for this, for example the PowerShell.

```
PS C:\WINDOWS\system32> python --version
Python 3.9.1
```



Install make
--------------------------

The repo uses `make` so lets install that for Window. We use the Windows package manager Chocolatey to do this.

If you do not have the Chocolatey, [do install that first](https://chocolatey.org/install).

In Powershell, check the version of `choco`. It might look like this.

```
PS C:\WINDOWS\system32> choco --version
0.10.15
```

Now install GNU make using choco.

```
choco install make
```

Check the version of `make`. It looks somewhat likes this.

```
PS C:\WINDOWS\system32> make --version
GNU Make 4.3
Built for Windows32
```

Excellent work. Lets move on.



Install Git
--------------------------

Lets [install Git](https://git-scm.com/).

Check that you can execute `git` from the PowerShell and check what version you have.

```
PS C:\WINDOWS\system32> git --version
git version 2.16.1.windows.2
```

Perfect. A good start.



Git Bash and Unix
--------------------------

When you install Git you will get a terminal named Git Bash with it (Windows). It is a Unix terminal that makes it possible to write git commands and work with the repo. MacOS and Linux already have a Unix terminal

Here are som commands that are useful in a Unix terminal.

| Command | What
|---------|------
| `ls` | Show all files and directories in the current directory.
| `ls -l` | Show additional details on the files and directories.
| `ls -a` | Show even the hidden files, those starting with a dot `.`.
| `ls -la` | Do it all.
| `mkdir somedir` | Create a new directory named `somedir`.
| `cd somedir` | Change to a sub directory named `somedir`, the directory must exist.
| `cd ..` | Change one directory up in the directory hierarchy.
| `cd` | Change directory to your home directory.
| `pwd` | Show the current working directory.
| `touch file.txt` | Create a new file named `file.txt`
| `cat file.txt` | Show the content of the file.
| `more file.txt` | Show the content of the file and paginate its output.

Here is a larger list on some [basic Unix commands](http://mally.stanford.edu/~sr/computing/basic-unix.html), check it out and roughly review it.

Try to open up Git Bash and play around with the commands above to see how they works.



Git Bash and Git repo
--------------------------

Good, Git Bash is still open?

Go to your users home directory and create a directory named `git` and move into it.

```
cd
mkdir git
cd git
ls
```

This is now a great place to save your git repos. One repo in each directory.

Lets download the exercise repo by using Git.

```
git clone https://gitlab.com/mikael-roos/sustainable-programming-exercise.git exercise
cd exercise
ls
ls -a
ls -la
```

There it is, a git repo, a folder contianing the exercise.

Now open your IDE/Texteditor with this path/directory, so you can see all files in it.

Look around and try to get aquainted with the files in the repo. Do you recognize some of them, perhaps the files ending with `.py`?



Check that python & make is working
--------------------------

We are now in the Git bash terminal so lets check that python and make is still working.

Remember that we actually installer python and make in the Windows operating system using PowerShell. The Git Bash is a Unix-like terminal but it will still be able to execute the `make` and `python` that is installed in Windows. It is real good to have som knowledge about where the stuff actually are installed. It might help troubleshooting.

So, lets check the version and where the `make` and `python` are installed.

```
$ make --version
GNU Make 4.3
Built for Windows32
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

$ which make
/c/ProgramData/chocolatey/bin/make
```

```
$ python --version
Python 3.9.1

$ which python
/c/Users/mos/AppData/Local/Programs/Python/Python39/python
```

Ok, excellent. Now we know it works, what versions we have and where they are installed.



Execute the example programs
--------------------------

There are two example programs in the repo, execute them adn check out their source code.

```
$ cd dice

$ python dice.py
Rolling the dice, it was a 5
Rolling the dice, it was a 5
You have rolled the dice 2 times.
```

Then do the same with the `guess` game.



Update the Makefile
----------------------

In the Makefile there is a part saying the name of the executable for `python`. You need to set that up so it matches the executable on your system.

Open each Makefile in the texteditor (each example program has its own Makefile).

On Windows it it most likely it should look like this (use `python`) but on Mac and Linux it might be more correct to use `python3` since `python` may refer to version 2 and not version 3 on those systems. On some systems you might need to use `py`. The `#` is a comment in the Makefile.

```
# Change this to be your variant of the python command
#PYTHON = python3
PYTHON = python
#PYTHON = py
```

Great, the Makefile is prepared.



Create a virtual environment
--------------------------

The example repo contains a file `requirements.txt` with pip packages that we want to install. We will do this in a Python virtual environment.

We will create and activate the virtual environment using make.

```
$ make venv
[ -d .venv ] || python -m venv .venv
Now activate the Python virtual environment.
On Unix and Mac, do:
. .venv/bin/activate
On Windows, do:
. .venv/Scripts/activate
Type 'deactivate' to deactivate.
```

Now we activate it.

```
$ . .venv/Scripts/activate

(.venv)
$
```

The prompt changed. Now we are using that particular virtual environment.

Ensure that the prompt actually changed. It is important.

**If the prompt does not change**, try enter the following in PowerShell and answer "All". This is [explained in the documents](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then restart your Git Bash terminal and try activating the virtual environment again.

The prompt must change, before we proceed.



Install the dependencies
--------------------------

Now we install the packages from `requirements.txt`, using make.

The contents in the `requirements.txt` looks something like this.

```
# Unittest
coverage

# Code analysis
bandit
flake8
flake8-docstrings
flake8-polyfill
pylint
radon

# Documentation
pdoc3
sphinx
```

Using make you can install them all. But ensure that you are in the virtual environment before installing (the prompt has changed and starts with "(.venv)").

```
make install
```

When its done, check out whats installed by using make.

```
make installed
```

Well, thats more or less all, now we can start working.

Now try to work through the exercise, one step at a time and ask for help when you get stuck.
