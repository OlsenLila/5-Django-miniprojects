import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please enter a number larger than 0 next time")
        quit()

else:
    print("please enter a number ")
    quit()

random_number = random.randint(0,top_of_range) #randint includes the last number
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time ")
        continue

    if user_guess == random_number:
        print("Congrats, you found the number")
        break

    elif user_guess > random_number:
         print("The number is higher than the value inserted")

    else:
        print("The number is lower than the value inserted")

print("You got it right in: " , guesses , "times")