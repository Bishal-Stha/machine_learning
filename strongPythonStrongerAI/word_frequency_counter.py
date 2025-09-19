with open("email.txt","r") as file:
    texts = file.read()

# print(texts)
# preprocessing
texts = texts.lower().replace(".","")


texts = texts.split()
# print(texts)

word_dict:dict = {}
for word in texts:
    if word not in word_dict.keys():
        word_dict[word] = 0
    word_dict[word] += 1

# sort by values (frequency), highest first
sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for word, freq in sorted_words:
    print(f"{word}: {freq}")
