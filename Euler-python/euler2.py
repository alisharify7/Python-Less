
#This function check is a number even or not
#And return true if a number is even
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


#Defind variables
counter = 0
seccond_number = 2
first_number = 1
next_number = 0
    
while (first_number < 4000000):
    #Update counter step
    
    #Get fib number with collect first number and seccond number
    next_number = first_number + seccond_number
    
    #Assign new number to variable
    first_number = seccond_number
    seccond_number = next_number
    
    #Check if fib number is even or Not!
    if (even(next_number) == True):
        counter += next_number
           
  
#Print final resualt           
print(counter)             
 
