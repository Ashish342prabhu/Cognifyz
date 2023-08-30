mystr=input("Enter the string: ") 
revstr=reversed(mystr) 
if list(mystr)==list(revstr): 
    print("The given string is palindrome") 
else: 
    print("The given string is not palindrome")