
def string_Reversal():#function name
    name=input("Name:")#I allow a user to input a string
    if name=="":# The if statement is  for file handling incase a user enters nothing and hits enter
        print("Error,You require to put sth")
        return #terminates the function and ends the program
    else:
      store="" #variable to store the reversed string
      for x in range(len(name)-1,-1,-1):#for loop iterates the reversal of the letters based on string name and length
        store+=name[x]#Letters are added and stored based on the index
      return store
print(string_Reversal())

