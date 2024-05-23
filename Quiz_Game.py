print("Welcome to my Quiz !")

playing = input("Do you want to play game? ")

if playing.upper() != "YES":
    quit()

print("Okay! Lets start quiz")

score = 0

answer = input("What is CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions Correct! ")
print("You got " + str((score / 4) * 100) + "% ")
