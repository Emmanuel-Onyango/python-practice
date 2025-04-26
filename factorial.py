def factorial(n):
    if n==0 or n==1:# base case ,where the answer is known since 0 factorial=1 and 1 factorial=1
        return 1
    else:
        return n * factorial(n-1)# Recursive case
print(factorial(3))# output=6