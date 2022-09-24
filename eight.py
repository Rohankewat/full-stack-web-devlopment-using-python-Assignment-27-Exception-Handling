a = 5             # Question no :- 8
try:
    b = int(input("Enter a number "))
    c = a / b
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("This is value error")
except Exception:
    print("Kuch to gadbad hi")
else:
    print(c)