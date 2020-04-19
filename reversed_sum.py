n1 = input("First number:")[::-1] #take first input as a string and reverse it

int1 = int(n1) #convert the first input to an integer

n2 = input("Second number:")[::-1] #take second input as a string and reverse it

int2 = int(n2) #convert the second input to an integer

sum = int1 + int2 #sum up the integers

sum1 = str(sum)[::-1] #convert sum to string and reverse it

sum2 = int(sum1) #convert string to integer

print(sum2) #print out the reversed sum  