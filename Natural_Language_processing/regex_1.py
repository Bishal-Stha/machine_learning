import re

# input_text = input()
# pattern = r"\d"
# output_text = re.search(pattern,input_text)
# print(output_text)

text = ''' Elon musk's phone number is 2535215115. you can him if you have any question related to SpaceX you can on this number also. (924)-235-2514'''

pattern2 = r"\d{10} | /(/d{3}/)-d{3}-d{4}"
print(re.search(pattern2,text))