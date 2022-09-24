a = 36                # Questio no :- 10
try:
    b = int(input("Enter a number "))
    c = a / b
except ValueError:
    try:
        d = int(input("Enter a number "))
        e = a / d
    except ZeroDivisionError:
        print("In outer block value error and in inner block zero division error")
    except ValueError:
        print("both outer and inner block value error occur")
    else:
        print("In outer block value error")

except ZeroDivisionError:
    try:
        d = int(input("Enter a number "))
        e = a / d
    except ValueError:
        print("In outer block zero division error and in inner block value error")
    except ZeroDivisionError:
        print("both outer and inner block zero division error occur")
    else:
        print("In outer block zero division  error")
else:
    print("no error")    