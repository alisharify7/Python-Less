import sys

# get input from user
tmp = input("Enter character: ")

# get ascii value of character
tmp = ord(tmp)

# if tmp between 48 to 57 so user input is number
if (tmp >= 48 and tmp <= 57):
    print("number")

# if tmp between 65 to 90 so user input is number
elif(tmp >= 65 and tmp <= 90):
    print("upper case alphbet")

# if tmp between 97 to 122 so user input is number
elif(tmp >= 97 and tmp <= 122):
    print("Lower case alphabet")        


    # ascii table 
# https://www.asciitable.com/asciifull.gif 
