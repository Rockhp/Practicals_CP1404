"""Ragul practical3"""
'''password check'''


def main():
    """Start Program."""
    password = input("Please enter a password: ")

    if get_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def get_password(password):
    return password == "1234"


main()
