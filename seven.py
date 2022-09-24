a = 5        # Question no :- 7

try:
    print("File opened")
    b = int(input("Enter a number "))
    c = a + b
except ValueError:
    print("This is value error")
except Exception:
    print("something wrong happen")
else:
    print(c)
finally:
    print("File closed")
