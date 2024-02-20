---
revision:
    "2023-01-03": "(A, mos) First release."
---
Weekly log
=====================

This is the teacher's notes on what might be important to do to get a nice journey through these parts of the course.

[[_TOC_]]

<!--
TODO

* Slide on clean code for part 3 summary
    * Check if sonarcloud is an option to work with
    https://sonarcloud.io/project/overview?id=mosbth_python-template
* oopython is not included as slides nor exercise?
* Add video on Python OO, coding a dice/card game? 
    * https://www.youtube.com/playlist?list=PLEtyhUSKTK3hOCnMrPKGOu3_VjUAkhsgG

* Work through all exercises and improve them.
* Also make them go hand in hand with the python template.
* Is Sonarcloud a way to go?
* Wrap it all up by adding a devops flow?
* Improve the metrics part och show example on how to compare code by metrics

FIX

* cohesion not working with flake8

IMPROVE

*
-->

Precondition
---------------------

You should know Git and GitHub and you should have Git with GitBash installed on your environment.

You should know how to write an object-oriented program with Python using classes.



Overview of parts 2 & 3
---------------------

"Part 2: Testing" is about testing and documentation of the code.

* Work in teams of two and two and develop an application using object-oriented Python.
    * Apply linters to enhance the code.
    * Use unit testing.
* Oppose other projects by reviewing them.

"Part 3: Clean Code" is about the concept of what makes clean and good code.

* Write a report and summarize your view of the topic and your learnings from the project work and the opposition.



Prepare
---------------------

Prepare yourself through the following.

1. [Work with Git](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/doc/work-with-git.md). Review this article that provides an overview of Git commands and practice the commands on the terminal Git Bash. The article includes a [video playlist](https://www.youtube.com/playlist?list=PLEtyhUSKTK3iTFcdLANJq0TkKo246XAlv) that shows the basics.

Using Git is optional in the assignment, but it is also highly recommended as an important learning experience.



Week 05 - Part 2 Testing
---------------------

Start with an overall introduction and get going with the lab environment and the assignment.

**Teacher activities**

* Slides on "[Introduction to testing and clean code](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/lecture/intro-testing-clean-code/README.md)" as an overall introduction to the concepts.

<!--
*_About _object-oriented_ programming with_ Python. Hmmm, is this already fixed? Perhaps an OO example using slides?_
-->

**Lab environment & Exercises**

* Work through the Canvas article "[Lab environment and tools](https://hkr.instructure.com/courses/5722/pages/lab-environment-and-tools?module_item_id=290310)" that helps you set up the lab environment.

<!-- 

* Add small exercise on how to create class in Python and use it.
    * Without the need of a development environment, only build in modules
    * Perhaps Calculator (use in unittests)
    * Dice & Graphical dice
        * Dice game?
    * How to create the Guessing game?

* Using Canvas article instead of these 

    * Ensure that you have [all tools in your lab environment](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/doc/lab-environment.md).
    * Learn how to "[Work in a Python virtual environment](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/doc/python-venv.md)".
    * When you have installed all parts of the development environment, then you can try all tools out in the article/exercise "[Work with an example Python development repo](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/doc/work-with-a-example-python-development-repo.md)".
-->

**Assignment**

* Start of [A02](A2.md) and a walkthrough of the requirements.
    * There is a [template you can use for the project](https://gitlab.com/mikael-roos/python-template).

**Work**

* Establish the project team and start working by reading through the guidelines in "[Hints for a healthy team](../../public/doc/hints-for-a-healthy-team.md)".



Week 06 - Unit testing
---------------------

How to add unit tests to your project.

**Teacher activities**

* Slides on "[Python Unit tests and code coverage](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/lecture/unittesting-in-python/README.md)" as an overall introduction to the concepts.

* A walkthrough of the exercise "[Unit testing and code coverage in [Python](https://gitlab.com/mikael-roos/oopython/-/blob/main/public/doc/unit-testing-and-code-coverage-in-python.md)" will learn you the basics of unit testing and code coverage in Python.

* A discussion on [how to become a healthy team (part 2)](../../public/doc/hints-for-a-healthy-team-part-2.md).

<!--
IMPROVE

* Work with unittests on the previous classes, create exercise and video.
    * Calculator
    * Dice, DiceGraphic, DiceGame
    * GuessingGame
* Make slides based on above
* Improve slides once more, to many slides...

-->

**Lectures**

During this week you shall review the pre-recorded lectures that also have reading instructions.

* Lecture 6 - Introduction to Software Testing
* Lecture 7 - Software Unit Testing

**Work**

* Add unit testing to A02 (amongst other things).



Week 07 - TDD and Documentation
---------------------

Discuss TDD and generate documentation and prepare to submit A2 next week.

**Teacher activities**

The session in class will focus on discussing and solving the following exercises:

* [Test Driven Development](../../public/doc/test-driven-development.md)
* [Software Documentation](../../public/doc/generate-python-documentation.md)

**Lectures**

During this week you shall review the pre-recorded lectures that also have reading instructions.

* Lecture 8 - Test-driven development
* Lecture 9 - Software Documentation

**Work**

* Generate documentation for your A02.
* Prepare to submit A02 next week.



Week 08 - Part 3 Clean code
---------------------

Let's review the concept of good and clean code.

**Teacher activities**

* The lecture "[Clean code, metrics and philosophies with Python](../../public/lecture/clean-code-metrics/README.md)" is an introduction to this part of the course.
* Assignment 3 "Sustainable programming through good and clean code" will be presented together with guidelines on how to structure the report.

The session in class will focus on the following exercises:

* [Static code analysis and metrics](../../public/doc/static-code-analysis-and-metrics.md)

**Lectures**

During this week you shall review the pre recorded lectures that also have reading instructions.

* Lecture 11 - Static code analyzing and metrics

**Work**

* Run metrics on your A02 code, anything to fix before submission?
* Deadline to submit A02.
* Start working on the report for A03.



Week 09 - Opposion and Report week
---------------------

Work with the report and the opposition.

**Teacher activities**

* Start the opposition part of A02.
* Classroom session with analysing metrics.
* Helpsession with the writing of the report.

<!--
1. Start with the opposition, how it shall work
1. Talk about the opposition report
---
1. Show the updated report template
    * https://docs.google.com/document/d/1oP6-lM7wNdevtKZ4a0DfNJfgOTJJobEYFkXDbKlNu2E/edit?usp=sharing
1. Talk about vital learnings during the project
    1. Hint on title & research questions on the report
---
1. Quickly review the slides for metrics?
1. Quickly review the exercise for metrics
1. Talk on how to make a metrics part of the report

-->

**Lectures**

During this week you shall review the prerecored lectures that also have reading instructions.

* Lecture 12 - What about good and clean code?
* Lecture 13 - Software development philosophies

**Work**

* Begin the opposition part of A02.
* Write on your report A03.



Week 10 - Submission week
---------------------

**Teacher activities**

* Supervision and helpsession with the writing of the report.

**Submit your work**

* Submit the opposition report on A02.
* Submit the report on A03.
