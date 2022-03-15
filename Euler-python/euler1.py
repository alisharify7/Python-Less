#the resualt variable
counter = 0

for i in range(1000):
    #check for number multiples to 3 or 5 whit % oprator
    if (i % 3 == 0 or i % 5 == 0):
        #if we found that number so we added to counter variable
        counter += i
 
#print resualt    
print(counter)    
