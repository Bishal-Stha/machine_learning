import nltk
from nltk import word_tokenize, pos_tag

# Download the correct POS tagger
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger_eng')

sentence = """In New York, I like to ride the Metro to visit MOMA and some restaurants rated well by Ruth Reichl."""
tokenized_sent = word_tokenize(sentence)
tagged_sent = pos_tag(tokenized_sent, lang='eng')  # Specify lang='eng' to use the new model

print(tagged_sent[:3])
print(nltk.ne_chunk(tagged_sent))