
str = "szymon"
len = len(str) - 2
stars = len * "*"

if len >= 3:
    print(str[0] + stars + str[-1])

if len < 2 and str !="":
    print("haslo jest za krotkie")

if str == "":
    print("nie podano hasla")
