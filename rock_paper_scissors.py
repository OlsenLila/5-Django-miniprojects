import random

option = ["rock","paper","scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        print("Please insert one of the above options")
        continue
    
    random_number = random.randint(0,2)
    # rock: 0 , paper: 1 , scissors: 2
    computer_pick = option[random_number]
    print("Compiuter picked " + computer_pick + ".")
    if user_input == "rock" and computer_pick == "sissors":
        print("You Won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins += 1

    elif user_input == "sissors" and computer_pick == "paper":
        print("You Won")
        user_wins += 1

    else:
        print("Compiuter Won")
        computer_wins += 1

print("You won ", user_wins, " times.")
print("Compiuter won", computer_wins, " times.")
print("Goodbye")