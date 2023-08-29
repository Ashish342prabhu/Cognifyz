mystr=input("Enter the string: ") 
def reverse_string(mystr):
    # This function uses slicing to reverse the string. 
    # The `[::-1]` syntax means to start at the end of the string and move backwards with a step of -1, 
    # effectively reversing the string.
    return mystr[::-1]
revstr=reverse_string(mystr)
print("string after reversing: ")
print(revstr) 

