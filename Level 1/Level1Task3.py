import re

def valid_email(email):
    # Define a regular expression pattern for a valid email address
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")


mail=input("enter the the mail ID :") 
valid_email(mail)
