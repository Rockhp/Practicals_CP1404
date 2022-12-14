try:
    numerator = int(input("Enter the Numerator: "))
    denominator = int(input("Enter the Denominator: "))
    fraction = numerator/denominator
    print(fraction)

except ValueError and ZeroDivisionError:
    print("Numerator and denominator must be valid numbers!")
