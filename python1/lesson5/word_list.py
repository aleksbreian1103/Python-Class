str_in = raw_input("Enter a string: ")
lines = str_in.strip().split("\n")

upper = []
lower = []

for line in lines:
    words = line.strip().split()

    for word in words:
        if word.islower():
            lower.append(word)
        else:
            upper.append(word)

for word in (upper + lower):
    print(word)
