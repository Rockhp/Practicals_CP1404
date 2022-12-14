from programming_language import PL


def main():
    ruby = PL("Ruby", "Dynamic", True, 1995)
    python = PL("Python", "Dynamic", True, 1991)
    visual_basic = PL("Visual Basic", "Static", False, 1991)

    lang = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for x in lang:
        if x.is_dynamic():
            print(x.name)
    print("\nthe statically typed language are:")
    for y in lang:
        if y.is_static():
            print(y.name, y.typing, )



main()