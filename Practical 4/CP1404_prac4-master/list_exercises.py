"""
Ragul
CP1404/CP5632 Practical 4
List Exercises
"""
def main():
    INPUTf()
    # 2. Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter username:")
    if username in usernames:
        print("granted")
    else:
        print("denied")


def INPUTf():
    amounts = []
    storage = int(input("How many of amount want to store: "))
    for storage in range(1, storage + 1):
        amount = int(input(f"enter number for position {storage}: "))
        amounts.append(amount)
    print("------print report------")
    report(amounts)


def report(amounts):
    print(f"the number that storage = {len(amounts)}")
    print(f"the first of the storage is = {amounts[0]}")
    print(f"the last number of storage is = {amounts[-1]}")
    print(f"the smallest number is = {min(amounts)}")
    print(f"the largest number is = {max(amounts)}")
    avg = sum(amounts) / len(amounts)
    print(f"the average of the numbers is = {avg:.2f}")


main()
