print("welcome to my Computer Quiz!")

playing=input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score=0

answer = input("What does the CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does the RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does the PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct! ")
print("You scored " + str((score/4) * 100) + "%")