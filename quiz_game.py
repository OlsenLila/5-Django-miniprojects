print("Welcome to my Quiz Game")
playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()
print("Ok, let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central proccessing unit":
    print("Correct, this is True")
    score += 1
else:
    print("Wrong answer")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics proccessing unit":
    print("Correct, this is True")
    score += 1
else:
    print("Wrong answer")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct, this is True")
    score += 1
else:
    print("Wrong answer")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct, this is True")
    score += 1
else:
    print("Wrong answer")

print("You got " + str(score) + " questions correct!")
print("You were correct " + str((score /4) * 100) + "%")