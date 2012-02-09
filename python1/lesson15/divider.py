while True:
    integer = input("Provide and integer: ")
    if integer == "":
        break
    try:
        result = 10/int(integer)
        print(result)
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero (0)")