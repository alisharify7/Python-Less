import random

answer = False
print('Guessing game')
print('guess a number betweeb 1 to 100')

# in This list we store all Guess in the game
Guessed = []

end = 100
start = 0

while answer != True:
    # in each iterate Guess number between 1 to 100
    Guess = random.randint(start,end)

    # then check if number is in Guess list
    if Guess in Guessed:
        continue
        # pass this round 
    
    # show to user to type is number is correct or not
    print('Y for yes | G for Greater than | L for less than')
    user = input(f"Your Number is {Guess}? ").upper().strip()
    
    # if Number of user is Less than <Guess>
    if user == 'L':
        # we set <end> to this point to small our range
        end = Guess
        Guessed.append(Guess)

    # if user input is Grader than this point we
    # set <Start> to this point 
    elif user == 'G':
        start = Guess
        continue
        Guessed.append(Guess)
        
    # and finall condition if We gess user input correct print
    # and quit from loop
    elif user == 'Y':
        print("HOOOO HOOO!")
        answer = True