Exercise - Test driven development
==========================

In this exercise you shall practise how to work according to the test-driven development process where you write your tests first and then write code to pass the test.

[[_TOC_]]



Preconditions
--------------------------

You should have learnt the concept on test-driven development (TDD).



Prepare
--------------------------

You already have the exercise repo with the "dice" and the "guessing game".

Otherwise you might [find the repo oopython on GitLab](https://gitlab.com/mikael-roos/oopython).



TDD mantra
--------------------------

Do remember the TDD mantra, "red/green/refactor", repeating the steps of adding test cases that fail, passing them, and refactoring.

1. Decide on a feature you want to develop
1. Add a test case for the feature
1. Execute the test case and watch it fail
1. Implement the feature
1. Execute the test case and watch it pass



TDD with DiceHand
--------------------------

Work as a TDD would do.

The code is in the directory `src/dice/`.

Prepare to add the feature:

> "A dicehand that can hold a set of dices and throw them all at once."

Think it over.

Start by adding a testcase that fails. Perhaps something about creating an object for the DiceHand.

Watch the testcase fail.

Implement the minimal amount of code to pass the testcase.

Watch the testcase pass.

Repeat until the feature is fully implemented and tested.

Finish up by checking that the `make test` passes and check that you have enough code coverage of your tests.


<!--
Exercise 2 - Guess my number
--------------------------

The code is in the directory `src/guess/`.

Add a timer so you can time how long it takes for the player to guess the right number. Save the data to the log/highscore file as game statistics.

Make an option where the computer tries to guess the number by itself. The computer should be the one who guesses the number.

You can allow the computer to have as many guesses as it wants.

You can add two or more strategies that the computer can use, for exampe an optimal strategy that you implement or a random guessing strategy.

Work as a TDD would do. If it feels hard to work as TTD, reflect on why that is and do put in some extra effort to actually do it the TDD way.

Finish up by checking that the `make test` passes and check that you have enough code coverage of your tests.
-->
