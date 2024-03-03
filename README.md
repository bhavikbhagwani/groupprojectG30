#  PIG DICE GAME (NORMAL VARIATION WITH 50 POINTS)
PIG DICE GAME (NORMAL VARIATION WITH 50 POINTS)

Welcome to the Pig Dice Game Normal Variation! You are the player and you play against the computer.
You both have the objective to roll the dice and accumulate points to 
reach 50 points and win the game. Have fun and good luck.

## STARTING OFF

Make sure you have make installed in your machine to make it easy for you
to run certain features such as for testing and generating documentation

## SETTING VENV

First of all you need to set the virtual environment
You can set a virtual environment using 'make venv'.

## CHECK VERSION AND INSTALL FEATURES

After having make installed check your python version using 'make version'
Make sure your python version is below 3.12.0 as 'make pdoc' will only work with versions below 3.12.0
Run 'make installed' to see what is installed in your venv
If its only ... then run 'make install' to install all features for this project

## RULES

Player and computer take turns rolling a die.
If either rolls a 1, they lose their current round's points, and it's the next opponent's turn.
Either can choose to hold, adding their current round's points to their total score.
The first player to reach a score 50 points wins the game.
You can also cheat in the game, but your results or stats won't be stored if you cheat

## INSTALLATION

We set our GitHub Repository to private, meaning nobody is able to clone it.
However, you will have a zip file containing all files. 
Download this zip file, extract the files and open them

## RUN GAME

To run the game, one should go to the 'pig' directory and run

                    python main.py

## HELP IN GAME

You are free to type '?' or 'help' and a command afterwards to get a description of what the command does
You can get the list of commands by typing '?' or 'help'

To start/restart the game you shall type 'start'.
After this you should fill you name in and set the difficulty
You can start/restart, change name and set difficulty anytime you want
The previous 2 steps can be done faster by typint 'default' (play with default settings)

After this you can roll, hold or cheat. If you cheat, your results and stats won't be stored/recorded. 
A useful command is 'show' to show the results of you and the computer in the current game

## UNIT TESTING

To effectively perform unit testing in the pig dice program you can
implement 'make test' and 'make coverage' commands
'make test' will run the linters and provide a rating for the overall code
'make test' will also run 'make coverage' which you can do separately
'make coverage' will inform you about the test coverage throughout the code
proving percentages. A html file will also be created which you can open with your browser
to have a better visualization of the code coverage

## DOCUMENTATION

Documentation is a helpful feature...
To generate documentation for the Pig Dice Game Project, you can
implement...