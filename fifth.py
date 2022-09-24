a = 25      # Question no :- 5
try:
    b = int(input("Enter a number "))
    if a == b:
        raise ArithmeticError()
    c = a / b

except ValueError:
    print("This is value error ")
except ZeroDivisionError:
    print("Division by zero ")
except ArithmeticError:
    print("This is arithmetic error ")
except Exception:
    print("Any kind of error occur ")
else:
    print(c)