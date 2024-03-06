#  PIG DICE GAME (NORMAL VARIATION WITH 50 POINTS)
PIG DICE GAME (NORMAL VARIATION WITH 50 POINTS)

Welcome to the Pig Dice Game - Normal Variation! You are the player and you play against the computer.
You both have the objective to roll the dice and accumulate points to 
reach 50 points and win the game. Have fun and good luck.

## PYTHON

Check that you have the latest version of Python 3 installed

## INSTALLATION OF PROJECT

We set our GitHub Repository to private, meaning nobody is able to clone it without SSH keys.
However, you will have a zip file containing all files. 
Download this zip file and extract the files. Move this 'game' folder into a familiar location in your computer

## TERMINAL

This game will be played in the terminal. Open Git Bash and navigate to the files
You can use 'cd' to direct you to your destination:

                cd game

DON'T go into the 'pig' directory using 'cd pig' YET.
## MAKE AND MAKEFILE

We recommend working with the MakeFile so make sure you have 'make' installed in your machine to make it easy for you
to compile, build and have certain features such as for testing and generating documentation
If not installed see video on how to install:

https://www.youtube.com/watch?v=5TavcolACQY&list=PLEtyhUSKTK3hOCnMrPKGOu3_VjUAkhsgG&index=3

by Mikael Roos

The Makefile contains a target to execute or run several commands. This will make it easy
to compile, build, test and generate documentation

## SETTING VENV

Once having 'make' installed, first of all you need to set the virtual environment and activate it. 
(Make sure you are in the game directory)
You can set a virtual environment using 

            make venv

Then, you can activate the virtual environment using

            . .venv/Scripts/activate

You should see a (.venv) in your terminal
This will allow all features to be found and run
You can later deactivate the virtual environment by using

            deactivate

## WHAT NEXT   

After having make installed and your venv set up, check your python version using 

                make version

Make sure your python version is below 3.12.0 like 3.11.5 as 'make pdoc' will only work with versions 
below 3.12.0 due to an error encountered where "No module named 'distutils'" occured.
You can do all other things apart from make pdoc if you have version 3.12.0 or above.

Now, install all needed packages from the file requirements.txt using

        make install

You can now check what packages that are installed using

        make installed

## RULES OF GAME

Player and computer take turns rolling a die.
If either rolls a 1, they lose their current round's points, and it's the next opponent's turn.
Either can choose to hold, adding their current round's points to their total score.
The first player to reach a score 50 points wins the game.
You can also cheat in the game, but your results or stats won't be stored if you cheat

## RUN GAME
NOW, you can go to the 'pig' directory.

To run the game, one should go to the 'pig' directory using

                cd pig

and run

                python main.py

## HELP IN GAME, HOW TO PLAY AND OTHER COMMANDS

You are free to type '?' or 'help' and a command afterwards to get a description of what the command does

You can get the list of commands just by typing '?' or 'help'

To start/restart the game you shall type 'start'.

After this you should fill you name in and set the difficulty
This difficulty manages the intelligence of the computer

You can start/restart, change name and set difficulty anytime you want

The previous 2 steps can be done faster by typing 'default' (play with default settings)

After this you can roll, hold or cheat using 'roll', 'hold', or 'cheat'
If you cheat, your results and stats won't be stored/recorded. 
A useful command is 'show' to show the results of you and the computer in the current game

Other commands:

rules - to see the rules and instructions of the game

scores - to see the highscore list from the played games so far (non-cheated only)

exit - exit or quits the game

histogram - to see histogram  of dice values of players (non-cheated only)

## UNIT TESTING

To effectively perform unit testing in the pig dice program you can
implement

            make test 

'make test' will run the linters, provide a code rating and provide you with test coverage

You can also see just the test coverage separetaly by typing

                make coverage

This will inform you about the test coverage throughout the code
providing percentages of how much code was covered using unit tests.

You can also just run linters using

        make lint

or separetaly using

        make flake8         make pylint

After running 'make test' or 'make coverage', a htmlcov/ folder will be 
created with html files that you can open with your browser to have a 
better visualization of the code coverage

## DOCUMENTATION

Documentation is a helpful feature to help understand the code for other developers
First of all install the 'dot' command  to help generate the UML diagrams from the source code
For windows, you can do it through chocolatey in Poweshell as administrator:

        choco install graphviz

For mac OS, through the 'brew' package manager.

        brew install graphviz

Debian (and other Linux), through your package manager.

        apt install graphviz

After the installation is done you can check what version you got.

        $ dot -V

pydoc

Use pydoc to generate documentation for any class.
You will get a quick and readable documentation generated from your source code into your terminal.
For example with Dice class

        cd pig/dice
        python -m pydoc dice

You can also generate a html page for the documentation for any class

        python -m pydoc -w dice

This will create HTML documents inside doc/pydoc
You can open the generated html documentation in your web browser.

To generate UML diagrams you can just type

        make pyreverse

This will generate UML diagrams inside doc/pyreverse

To run both pydoc for all classes/files in directory and pyreverse for UML diagrams, 
there is a target for both these things in the Makefile by typing

        make pdoc

This will create a doc/ folder in the 'pig' directory with with folders:

    pydoc
    pyreverse

The pydoc folder will have HTML documentation for all classes found and
the pyreverse folder will have UML diagrams for all classes found

## CONCLUSIONS

We hope you enjoy your adventure in our project and game.


