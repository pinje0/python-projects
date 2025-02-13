print("Welcome to my computer quiz!")

playing = input("Do you want to play (Yes/No) ? ").lower()

if playing != "yes":
    quit()

print("Ok let's play :)")

number_of_questions = 4
score = 0

# Question 1
answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 2
answer = input("What does GPU stand for? ").lower()

if answer == "graphic processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 3
answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

# Question 4
answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / number_of_questions) * 100) + "%")
