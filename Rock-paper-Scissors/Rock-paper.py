from random import randint,seed
import time
import sys


def pick_winner(bot,user):
    # check for tie between user and bot
    if (user == bot):
        print("Game Tie !")


    elif (user == "rock" and bot != "paper") or (user == "scissors" and bot != "rock") or (user == "paper" and bot != "scissors"):
        print("You win!")
       
    else:
        print("Bot win!")


seed()
# all option for chose
chance = ["rock","paper","scissors"]
counter_round = 0

while (True):    
    print(f"\nRound {counter_round} ! Started")
    time.sleep(1)

    print("Chose between options")
    for house in range(3):
        print(" | " + chance[house] ,end="")
    print("\n")    

    user_input = input("what are you choosing: ").lower()

    # if user input not in option so just quit
    if user_input not in chance:
        print("Invalide input :((( ")
        sys.exit(2)

    # create random number between 0 to 2 
    rand = randint(0,2)
    # select randomly from options
    chosen = chance[rand]
    time.sleep(1)
    
    print(f"Bot Chose the: {chosen}")
    time.sleep(1)
    pick_winner(chosen,user_input)

    # exit mode for exit
    xx = input("Do you wanna Exit or continue: [-Y- For EXIT, -C- For Continue-]: ").upper()
    
    if (xx.upper() in ["YES","Y","YEP"]):
        sys.exit(0)
    elif (xx in ["C","CONTINUE"]):
        print("Ok Lets Go :)\n")
        time.sleep(1)
    else:        
        print("INVALIDE INPUT \nBut We Going For Bext Round")
        time.sleep(1)
    
    counter_round +=1

    
    
