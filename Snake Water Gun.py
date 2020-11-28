#snake water gun game
import random
def snake_water_gun():
    

    def getdate():
        import datetime
        return str(datetime.datetime.now())
    date = getdate()

    items = ["Snake", "Water", "Gun"]

    score_user = 0
    score_comp = 0

    print ("Welcome to the snake water gun game!\nTen chances would be given and at last score would be announced.")

    name = input("What's your name? ")
    print ("You'll have to press S for snake, W for water and G for gun.")

    print ("Let's begin now!!")
    ties = 0
    chances = 10

    try:
        while chances>0:
            item_choice = random.choice(items)

            a = input("What's your choice? ")

            if a in ["s", "S"] and item_choice == "Snake":
                print ("Tie")
                ties = ties+1
                chances = chances - 1
            elif a in ["s", "S"] and item_choice == "Gun":
                print ("You lost this time")
                score_comp = score_comp +1
                chances = chances - 1
            elif a in ["s", "S"] and item_choice == "Water":
                print ("You won this time")
                score_user = score_user+1
                chances = chances - 1

            elif a in ["w", "W"] and item_choice == "Snake":
                print ("You lost this time")
                score_comp += 1
                chances = chances - 1
            elif a in ["w", "W"] and item_choice == "Gun":
                print ("You won this time")
                score_user += 1
                chances = chances - 1
            elif a in ["w", "W"] and item_choice == "Water":
                print ("Tie")
   
                ties = ties+1
                chances = chances - 1

            elif a in ["g", "G"] and item_choice == "Snake":
                print ("You won this time")
                score_user += 1
                chances = chances - 1
            elif a in ["g", "G"] and item_choice == "Gun":
                print ("Tie")
                ties = ties+1
                chances = chances - 1
            elif a in ["g", "G"] and item_choice == "Water":
                print ("You lost this time")
                score_comp = score_comp+1
                chances = chances - 1

            else:
                print ("Invalid input!")
                continue

            if chances == 0:

                print ("Game over! Let's take look at the scores:")

                print ("Your score=", score_user)

                print ("Computer's score=", score_comp)

                print ("Ties=", ties)


                if score_user>score_comp:
                    print ("You won this game", name.capitalize()+"!!!")
                    f = open("SWG game history.txt", 'a')
                    txt_update = f"On {date}, {name.capitalize()} won the game with score= {score_user}, beating computer who had score= {score_comp} with {ties} ties.\n"
                    f.write(txt_update)
                    f.close

                elif score_user<score_comp:
                    print ("You lost this game", name.capitalize()+"!")
                    f = open("SWG game history.txt", 'a')
                    txt_update = f"On {date}, {name.capitalize()} lost the game with score= {score_user}, beaten by computer who had score= {score_comp} with {ties} ties.\n"
                    f.write(txt_update)
                    f.close

                else:
                    print (f"{name.capitalize()}, you have a tie with computer!")
                    f = open("SWG game history.txt", 'a')
                    txt_update = f"On {date}, {name.capitalize()} had a tie with computer, total number of ties counting to {ties} and respective score being {score_user} and {score_comp}.\n"
                    f.write(txt_update)
                    f.close

    except Exception as e:
        print (e)
        quit()

if __name__ == "__main__":
    snake_water_gun()
