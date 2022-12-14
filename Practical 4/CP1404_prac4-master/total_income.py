"""
Ragul
CP1404/CP5632 Practical 4
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for MONTH in range(1, months + 1):
        income = float(input("Enter income for month {x} : ".format(x=MONTH)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for MONTH in range(1, months + 1):
        income = incomes[MONTH - 1]
        total += income
        print("month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(MONTH, income, total))


main()