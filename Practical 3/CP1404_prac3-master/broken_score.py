"""
Ragul
brokenscore
prac3
"""


def main():
    print("please print in the number of your score")
    while True:
        score = float(input("input score here: "))
        print(calscore(score))


def calscore(score):
    if score >= 90:
        Answer = "Excellent"
    elif score >= 50:
        Answer = "Pass"
    elif 0 < score > 100:
        Answer = "the score must in range 0-100"
    else:
        Answer = "BAD!"
    return Answer


main()
