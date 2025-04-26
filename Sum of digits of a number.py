

def sum_Digits(digit):
    sum = 0  # initialized the sum variable to zero and store the sum of the digits
    for x in str(digit):#for loop to iterate each digit type casted to a string for the loop
      sum += int(x)# addition of one digit after the other following each iteration and stored
                               # in the sum variable as an integer
    return sum

print(sum_Digits(211)) #output=4

