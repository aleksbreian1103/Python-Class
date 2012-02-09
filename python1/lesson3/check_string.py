s = input("Please input a string: ")
if not s.isupper() and not s.endswith("."):
    print("String has a lower case character \nand does not end with a period.")
elif not s.isupper():
    print("String has a lowercase character.")
elif not s.endswith("."):
    print("String does not end with a period.")
else:
    print("String is acceptable.")