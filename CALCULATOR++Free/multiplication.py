print("""

      Welcome to the FREE version of Calculator++!

      This calculator has the ability to multiply.

      This calculator is only compatible with four numbers.

      If you have any issue with this calculator then go here: \n https://github.com/aramservices198/Unimaginable-Python-Projects/issues/new""")
num1 = float(input("First Number?"))
num2 = float(input("Second Number?"))
num3 = float(1)
num4 = float(1)
neednum1 = ()
neednum = input("Do you need another number? yes or no for our server is case sensitive. :)")
if neednum == "yes":
    num3 = float(input("Third Number?"))
    neednum1 = input("Do you need another number? yes or no for our server is case sensitive. :)")
elif neednum == "no":
    print()

if neednum1 == "yes":
    num4 = float(input("Fourth Number?"))
elif neednum == "no":
    print()

result = float(num1 * num2 * num3 * num4)
print(result)