# Take in ((1, 1), (2, 2), (12, 13), (4, 4))
# Print out the multiplication of each pair.

intup = []
numtup = 1

print("Please input tuples of two numbers.")
print("They will be multiplied.\n")

while True:
    print("Tuple " + str(numtup))
    first = int(input("First number: "))
    second = int(input("Second number: "))
    intup.append((first, second))
    finished = input("Are you finished? (y/n): ")
    if finished.lower()[0] == "y":
        break
    else:
        numtup += 1

for tuple in intup:
    mult = tuple[0] * tuple[1]
    print("{0:<4d} = {1[0]:2d} * {1[1]:2d}".format(mult, tuple))