


def sum_func(number_list):
    total = 0 #initialized the total variable to 0 to store the sum of elements in the list
    for x in number_list:#for loop to iterate through the list
        total+=x # total stores the sum of the elements after each iteration
    return total

print(sum_func([1,2,8])) #output=11