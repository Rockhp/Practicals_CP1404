"""
CP1404
Ragul
Practical5
"""
cc = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
      "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
      "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
      "Chocolate3": "#cd661d", "azure1": "#f0ffff",
      "azure2": "#e0eeee", "Claret": "#7f1734",
      "beige": "#f5f5dc", "bisque1": "#ffe4c4",
      "DarkSalmon": "#e9967a", "Cardinal": "#c41e3a"}

c_name = input("Enter a colour name: ")
while c_name != "":
    print("The code for \"{}\" is {}".format(c_name,
                                             cc.get(c_name)))
    colour_name = input("Enter a colour name: ")
