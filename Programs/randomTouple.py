import random

# PRINT RANDOM values
class Dice:

    def roll(self):
        dice_Values=(
            (1,0),
            (3,3),
            (9,1)
        )
        print(random.choice(dice_Values))

    def roll2(self):
        first=random.randint(1,10)
        second=random.randint(1,10)
        print(f"({first}, {second})")


obj=Dice()
obj.roll()
obj.roll2()

