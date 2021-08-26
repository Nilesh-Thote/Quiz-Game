
print("Let's play Quiz_Game")
answer=input("Do you want to play the game Press Yes/No : ")
try:
    if answer.isalpha():
        answer=answer.lower()
        if answer=="yes":
            print("Cool, let's get started")
except:
    print("Quitting")
    quit()

score=0
answer=input("What is a correct syntax to output \"Hello World\" in Python?")
if answer=="print(\"Hello World\")":
    score+=1
    print("Correct Answer")
else:
    print("Incorrect Answer")
answer=input("How do you insert COMMENTS in Python code?")
if answer=="//":
    score+=1
    print("Correct Answer")
else:
    print("Incorrect Answer")
answer=input("What is the correct file extension for Python files?")
if answer==".py":
    score+=1
    print("Correct Answer")
else:
    print("Incorrect Answer")
answer=input("In Python, 'Hello', is the same as \"Hello\" True or False").lower()
if answer=="true":
    score+=1
    print("Correct Answer")
else:
    print("Incorrect Answer")
answer=input("Which method can be used to remove any whitespace from both the beginning and the end of a string?")
if answer=="strip()":
    score+=1
    print("Correct Answer")
else:
    print("Incorrect Answer")
print("You gave "+str(score)+" correct answer")
print("Your Total score is "+str((score/5)*100)+"%.")
