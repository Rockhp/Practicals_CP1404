"""
Ragul
CP1404/CP5632 Practical 4
Quick pick program
"""

import random

NUMBERS_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    number_quickpicks = int(input("How many quick picks? "))
    while number_quickpicks < 0:
        print("That makes no sense!")
        number_quickpicks = int(input("How many quick picks? "))

    for i in range(number_quickpicks):
        quick_pick = []
        for j in range(NUMBERS_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()