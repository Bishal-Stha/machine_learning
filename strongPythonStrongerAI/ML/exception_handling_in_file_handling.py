# try:
#     with open("../helloo.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File doesn't exists.")

# finally:
#     print("Program ends here no matter what happens to the file.")

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Age:", age)

except ValueError as e:
    # If it's not an integer OR age < 0, ValueError occurs
    print(e if str(e) else "Enter integer value only.")
