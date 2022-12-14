"""
Ragul
CP1404 Practical8
Taxi simulator
"""
from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)choose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100, 1.23), SilverServiceTaxi("Limo", 100, 2, 2.46), SilverServiceTaxi("Hummer", 200, 4, 4.92)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("How far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             trip_cost))
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are arrive now:")
    display_taxis(taxis)


def display_taxis(taxis):  # display list
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()