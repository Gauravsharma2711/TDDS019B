import nltk
from nltk.corpus import gutenberg

nltk.download("gutenberg")

words = gutenberg.words("austen-emma.txt")
print("Words:", len(words))
print("First 25:", words[:25])