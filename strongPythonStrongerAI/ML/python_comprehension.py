values = []
for x in range(10):
    values.append(x)

# List comprehension
values2 = [x for x in range(10)]

evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)

evens2 = [num for num in range(50) if num %2 == 0]
# evenss = [num for num in range(50) if num % 2 == 0]
# both works
print(evens2)

options = ["any","apple","albany","world","hello",""]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue

    if string[0] != "a":
        continue

    if string[-1] != "y":
        continue

    valid_strings.append(string)

# print(valid_strings)

valid = [string for string in options if ((len(string) >=2) and (string[0]=="a") and string[-1]=="y")]
print(valid)

# Flattening a matrix (list of lists)
matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
flatten = []

for row in matrix:
    for num in row:
        flatten.append(num)

flat = [num for row in matrix for num in row]
print(flat)

# even or old
category = []
category = ["Even" if num%2==0 else "Odd" for num in range(50)]
print(category)

def squared(x):
    return x**2

squared_number = [squared(x+1) for x in range(10)]
print(squared_number)

# Creating a dictionary
pairs = [("a",1),("b",2),("c",3)]
my_dict = {k:v for k,v in pairs}
print(my_dict)

# Creating set comprehension
nums = [1,2,2,2,3,3,3,3,4,5,6,6,7]
unique_squares = {x**2 for x in nums}
print(unique_squares)

sum_of_squares1M = sum(x**2 for x in range(1000_000))
print(sum_of_squares1M)