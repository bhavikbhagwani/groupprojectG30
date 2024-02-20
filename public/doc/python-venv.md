---
revision:
    "2023-01-04": "(B, mos) Added more details on requirements.txt."
    "2022-01-04": "(A, mos) First version."
---
Work in a Python virtual environment
===========================

A virtual environment in Python means you can install the tools and libraries needed within the projects files.

The benefit is that you do not need to install these globally in your operating system, you can install them specifically for each project without polluting your server with various installations.

This article shows the basic approach when creating and working with a virtual environment and it assumes that you are working on a bash-terminal.

The article is written to be used on one of the following environments.

* Windows where Python is installed in the Windows installation and the terminal used is Git Bash.
* Linux, macOS or Windows with WSL using a bash compatible terminal.

[[_TOC_]]



Video
---------------------------

The following video show when I work through parts of this article.

[![](http://img.youtube.com/vi/UsmNyNxndv4/0.jpg)](http://www.youtube.com/watch?v=UsmNyNxndv4 "YouTube: Get going with Python venv and virtual environments")



Create and use a virtual environment
---------------------------

Lets walk through the basic setup on how the Python virtual environment is working and how we use it.

Your python is most likely installed as `python` or `python3`. I will use only `python` in my examples below.



### Create project directory

We start by creating a directory where we intend to have our project development.

```
mkdir proj
cd proj
```



### Create the venv environment

Continue by creating the basis for the virtual environment.

```
python -m venv .venv
ls -l .venv
```

This creates the directory `.venv` which will contain all the stuff installed into your local environment.

You can see that the `.venv` directory contains some files and libraries. The content of the library looks slightly different depending on if you installed Python into Windows or if you did it into Mac/Linux. However, it still works the same.



### Activate the venv environment

You now need to activate the particular environment. You can have several virtual environments in their own directories, but you can only have one active at the time.

When you activate it, all Python commands will take the `.venv` directory into account.

If you use a Python installation on Window, then activate like this. Remember that we are doing this on a bash terminal like Git Bash. It looks different when doing this on a Window terminal (cmd, powershell).

```
. .venv/Scripts/activate
```

If you use a Python installation on Mac/Linux, then activate like this.

```
. .venv/bin/activate
```

Your terminal promt is now changed to display the name of the virtual venv directory `.venv`. This is a reminder on that you currently have an active venv.



### Install packages into the venv

Now, when you install packages using pip, they will be installed locally in the `.venv` directory and they will not pollute your system with various versions of python packages.

You can install packages from `requirements.txt`, or from pip directly.

This is how to install from pip directly.

```
python -m pip install numpy
python -m pip list
```

This is how to install from the requirements file. The file `requirements.txt` can contain a long list of packages.

```
python -m pip install -r requirements.txt
python -m pip list
```

The file `requirements.txt` is a textfile and it can look like this where `#` is a comment.

```text
# Code analysis
flake8
pylint

# Code style
black

# Unit test and coverage
coverage
```

It is preferable to use a `requirements.txt` for the needed packages and tools. This file is a text files with the packages to install and one can set explicitly the version to be installed.



### Deactivate the venv

When you are done you can deactivate the virtual environment and stop using it.

```
deactivate
```

Note that the terminal prompt changed itself again and removed the directory of the venv.



Final thoughts
--------------------------

If you do something wrong, or you want to restart your venv, then you can just remove the venv directory and create it again and install the packages you need.

This is really useful when you work on a project with your team. You can assure that all your team members have exactly the same setup and version of the pip packages by defining this in the requirements file.

There is also much less hassle and trouble to install packages into a virtual environment than installing into your host operating systems filesystem where different versions may clash with all your different projects and their different requirements.



Using different versions of Python
--------------------------

This is out of the scope for this article but I will explain them shortly.

If you have a need to control what version of Python is used in your project, then there is another package that can do that. It is called [virtualenv](https://pypi.org/project/virtualenv/).

Another approach to use various and defined versions of python in your project would be to use docker and/or docker-compose.



References
--------------------------

* [12. Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
* [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
* [Pip documentation](https://pip.pypa.io/en/stable/user_guide/)
* [Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
