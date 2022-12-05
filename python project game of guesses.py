import random

print("lets play the game")
print("you will be given 3 chances to play the game")
i = 1
score = 0

while (i <= 3):
    c = random.randint(1, 10)

    d = int(input("enter your choice: "))
    if (d == c):
        score += 1
        print("congrats it was the correct guess")
        print(f"you have {3 - i} chances left +1")
    elif (d > c):
        print(" oops !!your choice was too high")
        print(f"you have {3 - i} chances left,better luck next time")
    elif (d < c):
        print(" oops !!your choice was too low")
        print(f"you have {3 - i} chances left,better luck next time")
    i += 1

print(f"your score is {score}")