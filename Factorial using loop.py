
def loop_Factorial(n):
    store=1 #initialized as 1 to handle the (number-1)factorial part
    for x in range((n), 0, -1):# The range in combination with the store variable ensures that
                               #the 0 instance is well handled since x can never be zero, the last possible output is 1,
                               # because 0 factorial is 1
                               #The logic of the range starts from the number whose factorial is to be found
        store *=x          # product is stored after each iteration
    return store
print(loop_Factorial(0)) # outputs 1