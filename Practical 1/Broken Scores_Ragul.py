score = float(input("Enter score: "))
while 0 >= score > 100:
    if 0 < score <= 50:
        print("Bad score")
    elif 50 < score <= 90:
        print("Passing score")
    elif 90 < score <= 100:
        print( "Excellent Score")
    score = float(input("Enter score: "))
else:
    print("Invalid Score")



