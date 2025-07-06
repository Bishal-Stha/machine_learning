from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = (
    "Bishal " * 20 +
    "creative dedicated curious consistent passionate "
    "helpful honest hardworking thoughtful disciplined"
)

wordcloud = WordCloud(background_color='black').generate(text)

plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout()
plt.show()
