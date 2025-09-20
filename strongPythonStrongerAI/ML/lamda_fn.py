squared = lambda x: x**2
print(squared(11))

numbers = [x for x in range(1,11)]
print(numbers)

squared_numbers = list(map(squared,numbers))
print(squared_numbers)

odd_squares = list(filter(lambda x: x%2 != 0, list(squared_numbers)))
print(odd_squares)

##########
# list comprehensions
alphabets = [chr(x+97) for x in range(0,26)]
# alphabets = [chr(x) for x in range(ord('a'), ord('z')+1)]
print(alphabets)

