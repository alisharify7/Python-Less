from random import randint,seed
import time
import sys
from colorama import init, Fore

init()

# Global variable For Keep Tracking Rate of  Players
human = 0
bot_rate = 0

def pick_winner(bot,user):
    global human
    global bot_rate

    # check for tie between user and bot
    if (user == bot):
        print("- Game Tie !")

    elif (user == "rock" and bot != "paper") or (user == "scissors" and bot != "rock") or (user == "paper" and bot != "scissors"):
        print("- You Win!")
        human += 1
    
    else:
        print("- Bot win!")
        bot_rate += 1

seed()

# all option for chose
chance = ["rock","paper","scissors"]
counter_round = 0

while (True):
    print("-"*20)    
    print(f"\nRound {counter_round}")
    time.sleep(1)

    print(f"{Fore.MAGENTA}Chose between options")
    for i in chance:
        print("- ",i)

    print(f"{Fore.GREEN}\nHuman: {human} \nbot: {bot_rate}\n")
    print(f"{Fore.WHITE}What Are You Choosing:",end="")
    user_input = input().lower()

    # if user input not in option so just quit
    if user_input not in chance:
        print("Invalid input :((( ")
        sys.exit(2)

    # create random number between 0 to 2 {0.1.2}
    rand = randint(0,2)

    # select randomly from random numbers
    chosen = chance[rand]
    time.sleep(1)
    
    print(f"{Fore.LIGHTMAGENTA_EX}- Bot Chose The: {chosen.title()}")
    time.sleep(1)
    pick_winner(chosen,user_input)

    # exit mode 
    print('\033[39m',end="")
    xx = input(f"Do you wanna Exit or continue: [-Y- For EXIT, -C- For Continue-]: ").upper()
    
    if (xx.upper() in ["YES","Y","YEP"]):
        sys.exit(0)
    elif (xx in ["C","CONTINUE"]):
        continue
    else:        
        print("Invalid Input \nBut We Going For next Round")
        time.sleep(1)
    
    counter_round +=1

    
    
