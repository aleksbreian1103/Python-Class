count = 1
secret = 18

num = int(input("\nGuess a number between 1 and 20: "))

while True:
    if (num == secret or count == 5):
        break
    elif (num > secret):
        num = int(input("It was too high. Guess again: "))
    elif (num < secret):
        num = int(input("It was too low. Guess again: "))
    count += 1
if (num == secret):
    print("You guessed right with " + str(count) + " guesses!")
elif (count == 5):
    print("You guessed more than five times.")

