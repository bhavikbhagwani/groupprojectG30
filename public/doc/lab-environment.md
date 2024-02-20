---
revision:
    "2022-01-04": "(A, mos) First version."
---
Lab environment
========================

This is the essential lab environment you need to have before starting to work with the exercises in this repo. Ensure that you have it all installed on your computer.

There are a lot of alternate development environments that likely will work for you. But to make everything as smooth as possible it is expected that you use a development environment that includes the following.

* Git
* Python 3
* Terminal (bash or zsh)
* Make

[[_TOC_]]

<!--
TODO

* The most updated version is in pdf. Perhaps rewrite or update this article to look alike that?

-->



Computer and operating system
------------------------

You need a computer with an operating system like **Windows, MacOS or Linux**. Use the latest version to avoid trouble. Ensure that you are up to date.



Git
------------------------

Install [Git](https://git-scm.com/) and learn how to use it through the terminal.

You can check your current version like this in your terminal.

```
$ git --version
git version 2.20.1
```

If you need assistance there is a video here.

* [Install Git from the installation program on Windows 10 and configure it](https://www.youtube.com/watch?v=02u7ao7uK5k&list=PLEtyhUSKTK3iTFcdLANJq0TkKo246XAlv&index=1)



The terminal
------------------------

Get acquainted with your **terminal** and learn how to use it and navigate through it. The terminal is here a Unix like terminal running bash or zsh.

* Windows - git bash (cygwin and WSL are alternatives)
* MacOS - terminal (bash or zsh)
* Linux - any terminal application (prefer bash but others might work)

If you need assistance there is a video here.

* [Use various bash terminals on Windows (Git Bash, Cygwin, Debian/WSL2)](https://www.youtube.com/watch?v=kialYZs6Oyc&list=PLEtyhUSKTK3gHj087mUjPfXyqMvSy2Rwz&index=2)

**NOTE** You could also set up a development environment using the Windows terminals cmd and powershell (or using GUI tools). However, they have a different syntax than a bash terminal and to make the it easy and straightforward it is expected that you are working with a bash terminal.



Python
------------------------

Check your version of Python or download and install the [latest version of Python](https://www.python.org/downloads/).

You can check your current version like this. The `$` sign is the prompt and is not part of the command to write.

```
$ python3 --version
Python 3.7.3
```

If you need assistance there is a video here.

* [Install python on Windows and run in cmd terminal and in git bash terminal](https://www.youtube.com/watch?v=PeM9UxEGH0o&list=PLEtyhUSKTK3hOCnMrPKGOu3_VjUAkhsgG&index=2)



GitLab or GitHub
------------------------

You may add your projects to a private instance of [GitLab](https://gitlab.com/) or [GitHub](https://github.com/) or equal Git web service.

You should learn to use these services as they or similar will most likely be part of your everyday work environment.

If you do not know which to choose, then get started with GitHub and create an account there.



Make and Makefiles
------------------------

The Make command and the Makefiles are in general used to compile, build and run programs and tasks.

If you have not yet heard about Makefiles, then read the short [introduction to Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html).

Ensure that you have it installed in your terminal.

You can check your current version like this.

```
$ make --version
GNU Make 4.3
```



### Install make on Windows

If you are using Git Bash on Windows, then check out this post about how to [install make on Windows](https://stackoverflow.com/a/32127632). The Windows package manager `chocolatey` is one way to do this. You will then install the make command within Windows and it can then be used from Git Bash.

1. [Install the Windows packet manager Chocolatey](https://chocolatey.org/install).
1. [Install GNU make](https://community.chocolatey.org/packages/make) using `choco install make` using PowerShell (you might need to run the terminal as admin).
1. Open a new window for Git Bash and check that it works be checking what version you have using `make --version`.

If you need assistance there is a video here.

* [Install GNU Make on Windows using Chocolatey package manager](https://www.youtube.com/watch?v=5TavcolACQY&list=PLEtyhUSKTK3hOCnMrPKGOu3_VjUAkhsgG&index=3)



<!--
Node and npm
------------------------

You need to install [node](https://nodejs.org/en/) which provides an environment to run JavaScript from your terminal. This will include the package manager [npm](https://www.npmjs.com/). These will be used as development tools.
-->


<!--
Web browser
------------------------

Get a **web browser**, or three. It is useful to test out your website in different browsers since there are differences among them. Take the browser that is available on your computer and complement with [Google Chrome](https://www.google.com/intl/en/chrome/) and [Firefox](https://www.mozilla.org/en-US/firefox/new/). Try to make your code work in all browsers.
-->



Texteditor/IDE
------------------------

Install a texteditor or IDE of your choice. The texteditors and development environments [Atom](https://atom.io/) and [Visual Studio Code](https://code.visualstudio.com/) are both good choices as a plain texteditor with plugin capabilities.

No matter what editor you choose, ensure you are using the following setup through out the course:

* File format UTF-8 NOBOM
* Unix style line endings LF `\n`
* Soft tabs, length 4



Where to go from here?
------------------------

Here are a few things you could do to learn a bit about your development environment.



### Learn more on Git

If you are new to Git, you might want to work through the document "[Work with Git](work-with-git)" to gain some basic knowledge on how to work with Git and Git repos.

There is a video playlist showing you how to work with the initial steps in Git.

* [Git, GitHub and GitLab - Learn and practice](https://www.youtube.com/playlist?list=PLEtyhUSKTK3iTFcdLANJq0TkKo246XAlv)



### Clone a repo

Clone a repo and see how it looks. You can clone this repo by entering the following into the terminal.

```
git clone https://gitlab.com/mikael-roos/oopython.git
```

You can visit the [same repo online](https://gitlab.com/mikael-roos/oopython).



### Learn some Unix commands

Here are a few useful Unix commands when you try to learn your way around the terminal.

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
| `rm file.txt` | Remove the file.

There is an helpful online resource "[Learning the Shell](http://linuxcommand.org/lc3_learning_the_shell.php)" that can be useful to follow.
