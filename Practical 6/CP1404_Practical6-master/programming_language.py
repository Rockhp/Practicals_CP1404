class PL:
    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):  # return string
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def is_static(self):
        return self.typing == "static"


def test():
    """Run simple tests PL class."""
    ruby = PL("Ruby", "Dynamic", True, 1995)
    python = PL("Python", "Dynamic", True, 1991)
    visual_basic = PL("Visual Basic", "Static", False, 1991)

    lang = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for x in lang:
        if x.is_dynamic():
            print(x.name)


if __name__ == "__main__":
    test()