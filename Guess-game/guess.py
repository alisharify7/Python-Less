import random
import time

answer = False
print('╔                                 ╗')
print('║         Guessing Game           ║')
print('║ Guess a Number betweeb 1 to 100 ║')
print('╚                                 ╝')
for i in range(1,4):
    print('.' * i)
    time.sleep(1)


# in This list we store all Guess in the game
Guessed = []

step_c = 0
end = 100
start = 0

while answer != True:
    # in each iterate  Program Guess Number between 1 to 100
    Guess = random.randint(start,end)

    # then check if number is in <Guess> list
    if Guess in Guessed:
        continue
        # if in the list pass this round 
    
    step_c += 1

    # show to user to type is number is correct or not
    print('Y for yes | G for Greater than | L for less than')
    user = input(f"Your Number is {Guess}? ").upper().strip()
    
    # if Number of user is Less than <Guess>
    if user == 'L':
        # we set <end> to this point to small our range
        end = Guess
        Guessed.append(Guess)
        continue

    # if user input is Grader than this point we
    # set <Start> to this point 
    elif user == 'G':
        start = Guess
        Guessed.append(Guess)
        continue
        
    # and finall condition if We guess user input correct print
    # and quit from loop
    elif user == 'Y':
        print(f"HOOOO HOOO!\nGuess Your Number In {step_c} steps")
        answer = True