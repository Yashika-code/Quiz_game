print("Welcome!! to my computer quiz ")
name=input("Enter your name : ")
playing=input("Do you want to play game ? (yes/no) : ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play : ")
score=0

answer=input("What does CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("What does GUI stands for ? ")
if answer.lower() == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("What does GPU stands for ? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("What does RAM stands for ? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer=input("What does ROM stands for ? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"{name} your score is : {score}")
print(f"Welldone {name} !!")
print(f"Thank You!! or attending the quiz ")