print("Welcome to the PRO version of Calculator+! This calculator has the ability to add, subtract, multiply,\nand divide. Remember that multiple numbers are not compatible with division. This calculator is only compatible with four numbers. If you have any issue with this calculator")
num1 = float(input("First Number?"))
op = input("Enter operator, ex. +, -, *, /:")
num2 = float(input("Second Number?"))
num3 = float(0)
num4 = float(0)
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



if op == "+":
    print(num2 + num1 + num3 + num4)
elif op == "-":
    print(num1 - num2 + num3 - num4)
elif op == "*":
    print(num2 * num1 * num4 * num3)
elif op == "/":
    print(num1 / num2)
else:
    print("You have entered an incorrect character.")
    print("To restart, you will need to re-run your calculator.")
    exit()

