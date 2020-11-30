resultadd = float(0)
resultmult = float(0)
resultsub = float(0)
resultdiv = float(0)
numadd = float(0)
numadd1 = float(0)
numadd2 = float(0)
numsub = float(0)
numsub1 = float(0)
numsub2 = float(0)
nummult = float(0)
nummult1 = float(0)
nummult2 = float(0)
numdiv = float(0)
numdiv1 = float(0)
neednotheradd = ()
neednothersub = ()
neednothermult = ()
print("Welcome to the PRO version of Calculator++! This calculator\nhas the ability to add, subtract, multiply,\ndivide. Your shortcuts are\nadd\nsubtract\nmultiply\ndivide.")
typeofcalc = input("What mode do you want?\nNote: Use the shortcuts above.")
print("You want " + typeofcalc + ".  Restart the program to pick another shortcut.")
if typeofcalc == "add":
    numadd = float(input("Enter your number: "))
    numadd1 = float(input("Enter your second addend: "))
    neednotheradd = input("Do you need another number? Pick yes or no:")
    if neednotheradd == "yes":
        numadd2 = float(input("Enter your third addend:"))
    elif neednotheradd == "no":
        print()
    else:
        print("You have entered the wrong syntax.")
        print("Restart the program to try again.")
    resultadd = numadd + numadd1 + numadd2
    print(resultadd)
elif typeofcalc == "subtract":
    numsub = float(input("Enter your number: "))
    numsub1 = float(input("Enter your second number: "))
    neednothersub = input("Do you need another number? Pick yes or no:")
    if neednothersub == "yes":
        numsub2 = float(input("Enter your third number:"))
    elif neednothersub == "no":
        print()
    else:
        print("You have entered the wrong syntax.")
        print("Restart the program to try again.")
    resultsub = numsub - numsub1 - numsub2
    print(resultsub)
elif typeofcalc == "multiply":
    nummult = float(input("Enter your number: "))
    nummult1 = float(input("Enter your second number: "))
    neednothermult = input("Do you need another number? Pick yes or no:")
    if neednothermult == "yes":
        nummult2 = float(input("Enter your third number:"))
    elif neednothermult == "no":
        print()
    else:
        print("You have entered the wrong syntax.")
        print("Restart the program to try again.")
    resultmult = nummult * nummult1 * nummult2
    print(resultmult)
elif typeofcalc == "divide":
    print("Remember dividing does not support more than two numbers in this calculator.")
    numdiv = float(input("Enter your number: "))
    numdiv1 = float(input("Enter your second number: "))
    resultdiv = numdiv / numdiv1
    print(resultdiv)
else:
    print("You have entered the wrong syntax.")
    print("Restart the program to try again.")
    exit()
