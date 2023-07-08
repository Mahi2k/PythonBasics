prt=print

def calculate(numberOne, numberTwo, userChoice = '+'):
    if (userChoice == '+'):
        prt("Addition: ",numberOne+numberTwo)

    elif (userChoice == '/'):
        prt("Division: ",numberOne/numberTwo)

    elif (userChoice == '-'):
        prt("Substraction: ",numberOne-numberTwo)
        
    elif (userChoice == '*'):
        prt("Multiplication: ",numberOne*numberTwo)
        
    elif (userChoice == '&'):
        prt("And: ",numberOne and numberTwo)

    elif (userChoice == '|'):
        prt("Or: ",numberOne or numberTwo)

    elif (userChoice == '>'):
        prt("Greater than: ",numberOne>numberTwo)

    elif (userChoice == '<'):
        prt("Lesser than: ",numberOne<numberTwo)

    elif (userChoice == "="):
        prt("Equality", numberOne==numberTwo)

    elif (userChoice == "%"):
        prt("Modulus", numberOne%numberTwo)
        
    else:
        prt("Wrong Choice!! Please try again.")


numberOne = float(input('Enter first operand: '))
numberTwo = float(input('Enter second operand: '))
userChoice = input("Enter operations (+, -, *, /, &, |, >, <, %): ")

calculate(numberOne, numberTwo)