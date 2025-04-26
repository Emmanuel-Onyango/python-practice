# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def sum_func(string_list):  # function that has the string whose elements are to be calculated as parameter
    num = 0  # num variable stores the number of elements of the list, initially with 0 elements
    for x in string_list:  # loop through the list and count the elements
        num += 1  # stored number of elements
    return num


print(sum_func([1, 2, "b", 55.6, 99, "manu"]))  # output=6