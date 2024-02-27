"""
Lets play the Pig Dice Game Normal Variation.

You will play against the computer. You will roll the dice and the dice value
gets added to your score. But be careful, if you get a one on the dice, you score a fat zero
and add not points. 

To start, first start the game using 'start' then
change your name typing 'name' followed by your name and then
set the difficulty typing 'difficulty' follower by the difficulty (easy, medium, hard)
OR type 'default' to start quick and play with default settings

Play at your own risk. Good Luck!

"""
import shell

def main():

    pig_Shell = shell.Shell()
    pig_Shell.cmdloop()


if __name__ == "__main__":
    main()