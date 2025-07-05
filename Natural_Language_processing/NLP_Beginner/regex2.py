import re

match_digit_and_words = ('(\d+|\w+)') # type: ignore
output = re.findall(match_digit_and_words, "I am 18 years old.")
print(output)