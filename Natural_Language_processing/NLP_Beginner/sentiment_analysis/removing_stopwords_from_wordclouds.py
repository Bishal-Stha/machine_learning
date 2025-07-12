# Import Libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
movie = pd.read_csv("../../NLP_Projects/IMDB Dataset.csv")

# Combine all reviews into one string
text = " ".join(review for review in movie['review'])



# print(STOPWORDS)
# print(len(STOPWORDS))

my_stopwords = set(STOPWORDS)
my_stopwords.update(["film","br","movie","movies","films","watch"])
# print(my_stopwords)
# print(len(my_stopwords))

# Generate word cloud
wcloud = WordCloud(stopwords=my_stopwords, background_color='white').generate(text)

# Display word cloud
plt.imshow(wcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
