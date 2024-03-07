#Create a class Dice and there should be a method roll()
# Whenever roll function is called it should create dice value like (2, 6) in a random format
# Value of the dice can't be changed
# We should print the value in the format: (x, y)

import random

class Dice:
    def roll(self):
        dice = (random.randint(1, 6), random.randint(1,6))
        print(dice)

dice_obj = Dice()
dice_obj.roll()