print("Enter 1 -> for Addition")       # Question no :- 6  
print("Enter 2-> for subtraction")
print("Enter 3-> for multiplication")
print("Enter 4-> for division")

option = int(input("Enter a option do you want perform "))

match option:
    case 1:      
        try:
            a = int(input("Enter first number "))
            b = int(input("Enter second number "))
            c = a+b
        except Exception:
            print("any error occur")
        else:
            print("Addition of",a,"and",b,"is",c)
    case 2:
        try:
            a = int(input("Enter first number "))
            b = int(input("Enter second number "))
            c = a - b
        except Exception:
            print("you not take a and b value valid")
        else:
            print("subtraction of",a,"and",b,"is",c)
    case 3:
        try:
            a = int(input("Enter first number "))
            b = int(input("Enter second number "))
            c = a*b
        except Exception:
            print("you should take a and b valid")
        else:
            print("multiplication of",a,"and",b,"is",c)
    case 4:
        try:
            a = int(input("Enter first number "))
            b = int(input("Enter second number "))
            c = a / b
        except ArithmeticError:
            print("Division by zero")
        except ValueError:
            print("maybe you take either A or B as a word or special character you should take A and B as a integer")
        except Exception:
            print("error occur")
        else:
            print("division of",a,"and",b,"is",c)
    case _:
        print("you enter wrong option")