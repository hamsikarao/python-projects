print("Welcome to the quiz!!")
playing = input("Do you want to play? Yes or No:")

if playing.lower() != "yes":
    quit()

print("ok! Let's play!!")
score =0

answer = input(" 1.What does CPU stand for?:")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect Answer")


answer = input(" 2.What does GPU stand for?:")
if answer.lower() == "graphics processing unit":
     print("Correct!")
     score+=1
else:
     print("Incorrect Answer")

answer = input(" 3.What does RAM stand for?:")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect Answer")

answer = input(" 4.What does PSU stand for?:")
if answer.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect Answer")

print( "your score is " ,score)