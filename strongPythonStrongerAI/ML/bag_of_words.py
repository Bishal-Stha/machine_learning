# get the text
texts = input("enter text: ").lower()



# refine text and split into words
words = [word for word in texts.split() if word.isalnum()]
# print(words)

# then assign the word according to its frequency
word_dicts = {}
for word in words:
    if word not in word_dicts.keys():
        word_dicts[word] = 0
    word_dicts[word] += 1

# sort based on frequency in descending order.
sorted_word_dict = dict(sorted(word_dicts.items(),key= lambda x: x[1], reverse=True))

# then finally print it.
print(sorted_word_dict)