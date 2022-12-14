"""
Ragul
CP1404/CP5632 Practical8
UnreliableCar tester
"""

from unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drive {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drive {:2}km".format(bad_car.name, bad_car.drive(i)))
    print(good_car)
    print(bad_car)


main()