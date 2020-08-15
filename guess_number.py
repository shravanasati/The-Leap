import random
print ("This is the guess the number game!!")

chances = 7
print ("The number is between 1 and 100 and is an integer.")

n = random.randint(1, 100)
while chances>0:
    guess = int(input("Guess the number: "))

    if guess==n:
        print("*****Congrats you won the game!*****")
        print("Chances left=", chances)
        quit()

    elif guess>n:
        print ("**Decrease your number**")
        chances -= 1
        print("Chances left=", chances)

    elif guess<n:
        print("**Increase your number**")
        chances -= 1
        print("Chances left=", chances)

    else:
        print("Invalid input!")

    if chances == 0:
        print("The answer was", n)