from datetime import date

time = date.today()
cy = time.year
age = 60


class Guitar:  # sort guitar
    def __init__(self, name="", year=0, cost=0):  # set everything on value if not it'll error
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):  # return string
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):  # get guitar age
        return cy - self.year

    def is_vintage(self):  # considered the vintage or not
        return self.get_age() >= age

    def __lt__(self, other):  # for year release
        return self.year < other.year
