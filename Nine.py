a = 36             # Question no :- 9
try:
    b = int(input("Enter a number "))
    if b == ValueError:
        raise ValueError()
    c = a / b
except ValueError:
    print("This is value error")
except Exception:
    print("any error occur")
else:
    print(c)