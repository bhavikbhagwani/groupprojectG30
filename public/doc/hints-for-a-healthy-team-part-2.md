---
revision:
    "2023-01-04": "(A, mos) First version."
---
Hints for a healthy team (Part 2)
========================

This is a collection of hints that may make your teamwork go smoother.

[[_TOC_]]



Precondition
------------------------

This text relies on that you read the first part of the "[Hints for a healthy team](./hints-for-a-healthy-team.md)".




Get a good start
------------------------

How to get going with the team work

* Read through spec and agree on your focus
* Sketch an UML diagram
* Agree on classes and larger modules (with several classes)
* Work using public interfaces and create empty classes/methods
* Divide work in team - some do more, some do less - its fine



Create the project strucutre
------------------------

WORK ONGOING

* Create empty files, but name them so everybody sees the whole picture
    * Create usable but empty classes & methods for the public interfaces

* Do not change the public interface without having a discussion on it, perhaps GitHub issues would be a great idea
* Integrate early, at least once a week or when needed
* Do not integrate before each has a passing testsuite
* Integrate by:
    * Copying files
    * Fork and pull requests
    * All write to the same repo and work in
        * main
        * branches



About working with Git
------------------------

* Git master & integration manager
    * Setup a git repo for the project
        * Perhaps use the available python template to get a quick start
    * Create empty files, but name them so everybody sees the whole picture
        * Create usable but empty classes & methods for the public interfaces
    * Integrate for the first time and see that it works
        * Make someone responsible for Main/Shell class that tie it all together into an application?
    * Add the testsuite
        * Add empty test files
        * Add testclasses for each testobject
        * Add a empty/assertTrue testcase for each class
        * Run the testsuite and see it work and pass

