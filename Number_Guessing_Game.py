import random

top_of_range = input("Type a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()
else:
    print("Please a number next time")
    quit()


random_number = random.randrange(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please a number next time")
        continue

    if user_guess == random_number:
        print("You got it! ")
        break
    else:
        if user_guess > random_number:
            print("You were above the number")
        else:
            print("You were below the number")

print(f"You got it in {guess} guesses")