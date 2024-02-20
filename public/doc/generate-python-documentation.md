Exercise - Generate Python documentation
==========================

In this exercise you will practise how to document your Python software from various aspects by automatically generate the documentation from your code.

[[_TOC_]]



Preconditions
--------------------------

The article is written to be used on one of the following environments.

* Windows where Python is installed in the Windows installation and the terminal used is Git Bash.
* Linux, macOS or Windows with WSL using a bash compatible terminal.



Prepare
--------------------------

You already have [the exercise repo](https://gitlab.com/mikael-roos/oopython) with the "dice" and the "guessing game".

You should work in your virtual environment where you previously did a `make install`. Do not forget to activate your virtual environment.



Install the dot command
--------------------------

We need to install the `dot` command to help generating the UML pictures from the sourc code structure when we are using `pyreverse`. The `dot` command is part of the package called graphviz and you can install it using your package manager. You may wanna read about the [Graphviz project](https://graphviz.org/).

Windows, through the "[Chocolatey](https://chocolatey.org/)" package manager using for example PowerShell as an Administrator.

```
choco install graphviz
```

Mac OS, through the "[brew](https://brew.sh/)" package manager.

```
brew install graphviz
```

Debian (and other Linux), through your package manager.

```
apt install graphviz
```

After the installation is done you can check what version you got.

```
$ dot -V
dot - graphviz version 2.40.1 (20161225.0304)
```



Exercise 1 - Generate documentation using pydoc & pdoc
--------------------------

The code is in the directory `src/dice/`.


### pydoc

Use [`pydoc`](https://docs.python.org/3/library/pydoc.html) to generate documentation for the Dice class. You will get a quick and readable documentation generated from your source code.

```
cd src/dice
python -m pydoc dice
```

You can also generate a html page for the documentation.

```
python -m pydoc -w dice
```

Open the generated html documentation in your web browser.



### pdoc

Now try out the command [`pdoc`](https://pdoc.dev/) to generate documentation as HTML.

```
pdoc --html --output-dir doc/pdoc *.py
```

Open up the documentation in your web browser and review it.

It is real easy to generate the documentation once you have documented your code accordingly.



### make pdoc

The Makefile supports pdoc through the following target.

```
make pdoc
```

Verify that the target work.

Inspect the Makefile to see what commands are implemented behind the target.

Check in the `doc/` directory what was generated.



### Questions to think about

1. Should the `doc/` be included in the repo or should it always be generated?

1. Should the test files be included in the generated documentation?

1. Quickly read though the documentation of pydoc and pdoc. Which do you prefer to use or both?



Exercise 2 - Learn from documentation
--------------------------

The code is in the following directories:

* `src/dice_graphic/`
* `src/guess/`



### make pdoc

Go into the two directories and build the documentation pdoc.

Study the documentation for each project and consider if you are getting a good picture of the code by reviewing the documentation.

These projects contain more classes and object oriented structure like inheritance and composition.

PS. The generated documentation structure differ between dice_graphic and guess, you can review the Makefiles to see what differs.



### Questions to think about

1. Can you get a good picture on the code in the modules from viewing the generated documentation?



Exercise 3 - Generate documentation as UML diagrams
--------------------------

The code is in the directory `dice/`.

Use `pyreverse` to generate UML documentation for the Dice class.

```
cd dice
pyreverse dice.py
dot -Tpng classes.dot -o classes.png
```

Open up the file `classes.png` in your web browser and review it.



### make pyreverse

You can now try to use its make target to generate the UML docs for all classes in the module.

```
make pyreverse
```

Review the Makefile to see what commands are executed.

Locate the generated images and open up them in your web browser.



### Questions to think about

1. Can you get a good picture on the code in the modules from viewing the generated documentation?

1. Should the test classes be included in the generated documentation?



Exercise 4 - Learn from UML diagrams
--------------------------

The code is in the following directories:

* `src/dice_graphic/`
* `src/guess/`



### make clean-doc doc

Go into the two directories and rebuild the complete documentation.

First remove the old documentation.

```
make clean-doc
```

Now generate the complete documentation again.

```
make doc
```

You can also run the two targets directly.

```
make clean-doc doc
```

Study the UML diagrams for each project and consider if you are getting a good picture of the code by reviewing the documentation.

PS. The generated UML diagram differ between dice_graphic and guess, you can review the Makefiles to see what differs.



### Questions to think about

1. Can you get a good picture on the code in the modules from viewing the generated documentation?

1. Should the test classes be included in the generated UML documentation?

1. How many ancestor classes should be available in the generated UML documentation?



Resources
--------------------------

There is a lot of different settings you can use when generating your documentation. Review each tool to see what can be done.

For generating html documentation from comments in code.

* [pydoc](https://docs.python.org/3/library/pydoc.html)
* [pdoc](https://pdoc3.github.io/pdoc/)

About generating UML diagrams.

* [pyreverse](https://pypi.org/project/pyreverse/)
    * [Using pyreverse to generate UML class diagrams](https://www.redshiftzero.com/pyreverse-uml/)
[Graphviz project](https://graphviz.org/)



### More tools that generate documentation

You might also want to review the following more advanced tools for generating documentation. They need more configuration but can deal with a more flexible structure for generating the documentation.

* [Sphinx](https://www.sphinx-doc.org/en/master/)
* [doxygen](https://www.doxygen.nl/)

Here are more tools that can generate UML diagrams from the source code.

* [Pynsource](https://www.pynsource.com/)
* [Lumpy](http://www.greenteapress.com/thinkpython/swampy/lumpy.html)
