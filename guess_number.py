import random
# importing the pyttsx library 
import pyttsx3 

def speak(string):
    engine = pyttsx3.init() 
    engine.say(string)
    engine.runAndWait()

print("Welcome to this game called Guess the Number")   
speak("Welcome to this game called Guess the Number") 
print ("The number is between 1 and 100 and is an integer.")
speak("The number is between 1 and 100 and is an integer") 

chances = 7
print("You will get total 7 attempts to guess the number")
speak("You will get total 7 attempts to guess the number")

n = random.randint(1, 100)
while chances>0:
    speak("Please Guess a number:") 
    guess = int(input("Please Guess a number: "))
    

    if guess==n:
        print("*****Congrats you won the game!*****")
        speak("Congrats you won the game!") 
        print("Chances left=", chances)
        speak(f"{chances} Chances left")
        quit()
        
    elif guess<0 or guess>100:
        print("Please, Enter the number only between 0 and 100")
        
    elif guess>n:
        print ("**Decrease your number**")
        speak("Decrease your number")
        chances -= 1
        print("Chances left=", chances)
        speak(f"{chances} chances left")

    elif guess<n:
        print("**Increase your number**")
        speak("Increase your number")
        chances -= 1
        print("Chances left=", chances)
        speak(f"{chances} chances left")

    else:
        print("Invalid input!")
        speak("Invalid input!")

    if chances == 0:
        print("The answer was", n)
        speak(f"The answer was {n}")
