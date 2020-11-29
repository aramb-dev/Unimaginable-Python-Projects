print("Welcome to the FREE version of Calculator++! This calculator has the ability to multiply. This calculator is only compatible with six numbers. If you have any issue with this calculator then go to this link:\n https://github.com/aramservices198/Unimaginable-Python-Projects/issues/new")
num1 = float(input("First Number?"))
num2 = float(input("Second Number?"))
num3 = float(0)
num4 = float(0)
num5 = float(0)
num6 = float(0)
neednum1 = ()
neednum2 = ()
neednum3 = ()
neednum = input("Do you need another number? yes or no for our server is case sensitive. :)")
if neednum == "yes":
    num3 = float(input("Third Number?"))
    neednum1 = input("Do you need another number? yes or no for our server is case sensitive. :)")
    neednum2 = input("Do you need another number? yes or no for our server is case sensitive. :)")
    neednum3 = input("Do you need another number? yes or no for our server is case sensitive. :)")
elif neednum == "no":
    print()

if neednum1 == "yes":
    num4 = float(input("Fourth Number?"))
elif neednum == "no":
    print()
else:
    print("You have entered incorrect syntax.")
    print("Restart the program to try again.")
    exit()
if neednum2 == "yes":
    num5 = float(input("Fifth Number?"))
elif neednum2 == "no":
    print()
else:
    print("You have entered incorrect syntax.")
    print("Restart the program to try again.")
    exit()
if neednum3 == "yes":
    num6 = float(input("Sixth Number?"))
elif neednum3 == "no":
    print()
else:
    print("You have entered incorrect syntax.")
    print("Restart the program to try again.")
    exit()

result = (num1 * num2 * num3 * num4 * num5)
print(result)
