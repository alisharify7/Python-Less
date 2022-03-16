#implementation of Mario problem set in python
print("Height Must between 1 to 8")

#check if user input is not a number
try:
    #Get input From user
    x = int(input("Enter Height: "))
except ValueError:
    print(f"-{x}- is Not a Number!")
    exit()

#Safety check for get correct Number
if (x <= 0 or x > 8):
    print(f"-{x}- is Out of Range!")
    exit()

#With this for loop we Iterate each line code
for i in range(1 ,(x + 1)):
        # we in each Iterate -1 from X For space
        # if we get 5 in first Line we should print 4 space and one hash
        x -= 1
        #This for loop for print space
        print(" " * x, end ="")
        #this for loop for print hash
        print("#" * i, end ="")
        #for print space between mario block
        print(" ", end="")
        #And this for loop for print right block
        print("#" * i)
