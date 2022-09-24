a = 10          #  Question no :- 4     

try:
    b = int(input("Enter a number "))
    c = a / b
except ValueError:
    print("this is value error ")
except Exception:
    print("you do something mistake ")
else:
    print(c)