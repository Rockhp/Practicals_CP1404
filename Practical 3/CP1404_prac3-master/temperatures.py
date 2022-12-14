'''
Ragul
Cp1404
temperature
'''
MENU = """
C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    menu = input(">>> ").upper()
    choice(menu)


def choice(menu):
    while menu != "Q":
        if menu == "C":
            celsius = float(input("Celsius: "))
            calC(celsius)
        elif menu == "F":
            fahrenheit = float(input("fahrenheit: "))
            calF(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        menu = input(">>> ").upper()
    print("Thank you.")


def calC(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def calF(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()
