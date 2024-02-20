---
revision:
    "2022-01-04": "(A, mos) First version."
---
Work with Git
======================

Here is a basic work flow when you work with Git and a master on GitHub or GitLab.

[[_TOC_]]



Quick reference
--------------------------

Lets start with an overview of some basic commands.

| Command | What
|---------|------
| `git status` | Do a healthcheck and see how you local changes reflect to the current repo and its master.
| `git add <filename>` | Add a specific file to the repo.
| `git add .` | Add all files in the current directory.
| `git commit -a -m "Message"` | Commit all `-a` changes to the repo and attach a commit message `-m "Message"`.
| `git push` | Push all committed changes to your master.
| `git pull` | Update your local repo with and files changed on the master. Useful then updating the repo from several places.
| `git tag -a v1.0.0 -m "Message"` | Add a tag to your repo and attach a tag message.
| `git push --tags` | Push the tags to your master.

The commands are further explained below.



Basics
--------------------------

[Git](https://git-scm.com/) is the code versioning tool, it is used to provide version management to software code and equal documents.

GitHub and GitLab are two examples on websites that hosts git repos and provide additional services to work with the repo.



Precondition
--------------------------

You have installed Git and you have a existing repo available to play around with.



Video playlist on Git and GitHub
--------------------------

You might also want to try out some of the videos in the following playlist as a complement to this article.

* [Git, GitHub and GitLab - Learn and practice](https://www.youtube.com/playlist?list=PLEtyhUSKTK3iTFcdLANJq0TkKo246XAlv)



Git Bash
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
| `rm file.txt` | Remove the file.

Try to open up Git Bash (or Terminal in MacOS or any Linux terminal) and play around with the commands above to see how they works.



Check the status of the repo
--------------------------

Go to your repo (change directory to your repo).

You can check a status of a repo.

```
git status
```

It is sort of a health check on the repo and it compares your local version (your local branch master) with the remote version (your origin/master).



Add a file to the repo
--------------------------

Go to your repo and create a new file `test.html`.

```
# Go to your repo
touch test.html
ls -l
```

You can open the file in your texteditor and add some sample text into it, just for the fun of it.

Use `git status` to see how it looks.

We shall now add the file to the repo.

```
git add test.html
```

The file is added to the repo.

An alternative is `git add .` which add all files to the repo.

You can now do another `git status`.



Commit all changes
--------------------------

When you are done with all your additions, and changes, then you shall commit them. It is like permanent writing your updates into the repo.

```
git commit -a -m "First commit"
```

The switches `-a` means all files that are changed and `-m "First commit"` is a commit-message attached to this commit, explaining what the commit was about.

You can also commit only one file at the time.

```
git commit test.html -m "First commit"
```

You can the check with `git status`.



Push changes to your master
--------------------------

When you are done with all commits you should push them all to your master.

```
git push
```

The changes are now uploaded and you can reload your repo page on your website to check that all changes were uploaded.

Check your `git status`.

You are now up to date with your master.



Get updates from the master
--------------------------

If there are changes to the master that you have not yet downloaded locally, then do like this.

```
git pull
```

Your local repo is then updated to mirror the master.



Create a tag and push it
--------------------------

When you have a certain baseline in your project, you may want to tag it with a version number. This makes it easier to know the status of the repo and make it visible what part of it that might be thought of as more stable.

```
git tag -a v1.0.0
git push --tags
```

You can add a new tag at any stage.

You need to push the tags separately, by adding `--tags`.

You can list all tags like this.

```
git tag
```



Review the Git history
--------------------------

Check out the tags and the commit history for the repo.

The command `git log` shows a complete history on each commit made to the repo. Each commit has a commit reference to make it unique.

```
git log
```

You can get a more pretty online output with the following command.

```
git log --pretty=oneline
```

You can also format the output for enhanced clarity.

```
git log --pretty=format:"%h - %an, %ar : %s"
```

You can make an alias of the above command. That is quite useful when using it a lot to review the commit history.

Here is how to create an alias named 'hist'.

```
git config --global alias.hist 'log --pretty=format:"%h - %an, %ar : %s"'
```

Now you can use the alias as an ordinary git command.

```
git hist
```

When using services like GitHub and GitLab they usually have a really good way of displaying the commit history and visually showing all the details on each file and changes involved in a certain commit.



Learn more Git basics
--------------------------

The [documentation for git is available online](https://git-scm.com/doc).

There are a few [short videos that provide the essentials about Git](https://git-scm.com/videos).
