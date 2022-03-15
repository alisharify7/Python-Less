
#this function check is a number even or not
#and return true if a number is even
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False


#defind variables
counter = 0
seccond_number = 2
first_number = 1
next_number = 0
i = 0
    
while (first_number <= 4000000):
    #update counter step
    i+=1
    
    #get fib number with collect first number and seccond number
    next_number = first_number + seccond_number
    
    #assign new number to variable
    first_number = seccond_number
    seccond_number = next_number
    
    #check if fib number is even or Not!
    if (zoje(next_number) == True):
        counter += next_number
           
  
#print final resualt           
print(counter)             
 

