import random
import time

outcomes = ["Snake", "Water", "Gun"]

score_comp = 0
score_user = 0
ties = 0
chances = 10

name = input("What's your name? ")

try:
    print("WELCOME TO THE SNAKE WATER GUN GAME!!")
    while chances>0:
        guess = input("Enter your choice(S/W/G): ")
        outcomes_choice = random.choice(outcomes)
        if outcomes_choice == "Snake" and guess in ["g", "G"]:
            print ("You won this time!")
            chances = chances - 1
            print ("Chances left =", chances)
            score_user += 1
            time.sleep(1)
        elif outcomes_choice == "Snake" and guess in ["w", "W"]:
            print ("You lost this time!")
            chances = chances - 1
            print ("Chances left =", chances)
            score_comp += 1
            time.sleep(1)
        elif outcomes_choice == "Snake" and guess in ["s", "S"]:
            print ("Tie!")
            print ("Chances left =", chances)
            chances = chances - 1
            ties += 1
            time.sleep(1)

        elif outcomes_choice == "Water" and guess in ["s", "S"]:
            print ("You won this time!")
            chances = chances - 1
            print ("Chances left =", chances)        
            score_user += 1
            time.sleep(1)
        elif outcomes_choice == "Water" and guess in ["g", "G"]:
            print ("You lost this time!")
            chances = chances - 1
            print ("Chances left =", chances)       
            score_comp += 1
            time.sleep(1)
        elif outcomes_choice == "Water" and guess in ["w", "W"]:
            print ("Tie!")
            chances = chances - 1
            print ("Chances left =", chances)
            ties += 1
            time.sleep(1)

        elif outcomes_choice == "Gun" and guess in ["w", "W"]:
            print ("You won this time!")
            chances = chances - 1
            print ("Chances left =", chances)
            score_user += 1
            time.sleep(1)
        elif outcomes_choice == "Gun" and guess in ["s", "S"]:
            print ("You lost this time!")
            chances = chances - 1
            print ("Chances left =", chances)
            score_comp += 1
            time.sleep(1)
        elif outcomes_choice == "Gun" and guess in ["g", "G"]:
            print ("Tie!")
            chances = chances - 1
            print ("Chances left =", chances)
            ties += 1
            time.sleep(1)
        else:
            print ("Invalid input")
            continue

    print ("\t\t\t\t\t*****GAME SUMMARY*****")
    if score_comp>score_user:
        print ("\t\t\t\t\tYou lost this game!")
        print ("\t\t\t\t\tYour score =", score_user)
        print ("\t\t\t\t\tComputer's score =", score_comp)
        print ("\t\t\t\t\tTies =", ties)
        f = open("SWG Game History.txt", 'a')
        txt_update = (f"{name} lost the game with his score being {score_user} and computer's score being {score_comp} and ties counting to {ties}.\n")
        f.write(txt_update)
        f.close()

    elif score_user>score_comp:
        print ("\t\t\t\t\tYou won this game!")   
        print ("\t\t\t\t\tYour score =", score_user)
        print ("\t\t\t\t\tComputer's score =", score_comp)
        print ("\t\t\t\t\tTies =", ties)
        f = open("SWG Game History.txt", 'a')
        txt_update = (f"{name} won the game with his score being {score_user} and computer's score being {score_comp} and ties counting to {ties}.\n")
        f.write(txt_update)
        f.close()

    else:
        print ("\t\t\t\t\tTie!")
        print ("\t\t\t\t\tYour score =", score_user)
        print ("\t\t\t\t\tComputer's score =", score_comp)
        print ("\t\t\t\t\tTies =", ties)
        f = open("SWG Game History.txt", 'a')
        txt_update = (f"{name} had a tie with computer, scores counting {score_user}each and ties being{ties}.\n")
        f.write(txt_update)
        f.close()

except Exception as e:
    print (e)
    quit()