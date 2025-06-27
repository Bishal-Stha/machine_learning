import re

pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input = input("Enter email: ")
if(re.search(pattern,user_input)):
    print("Valid email.")
else:
    print("Invalid email.")