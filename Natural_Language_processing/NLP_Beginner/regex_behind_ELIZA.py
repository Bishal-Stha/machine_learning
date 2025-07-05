# User: "do you remember when you ate strawberries in the garden?"
# ELIZA: "How could i forget when I ate strawberries in the garden?"

import re

pattern = r"do you remember (.*)"
message = "do you remember when you ate strawberries in the garden?"
match = re.search(pattern, message)

if match:
    print("string matches!")
    print(match.group(1))
else:
    print("No match found.")

def swap_pronouns(phrase):
    # Replace 'my' with 'your' (case-insensitive)
    phrase = re.sub(r'\bmy\b', 'your', phrase, flags=re.IGNORECASE)
    # Replace 'I' with 'you' (case-insensitive)
    phrase = re.sub(r'\bI\b', 'you', phrase, flags=re.IGNORECASE)
    return phrase

phrase = "my name is bishal shrestha. I was went to Sushma Godawari college."    
print(swap_pronouns(phrase))

