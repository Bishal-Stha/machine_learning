# %pip install textblob

from textblob import TextBlob

text = "Today was a good day."
my_valence = TextBlob(text)
print(my_valence.sentiment)

print("\n",my_valence.pos_tags)