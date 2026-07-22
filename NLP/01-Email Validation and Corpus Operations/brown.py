import nltk
nltk.download('brown')

from nltk.corpus import brown

print("words:", len(brown.words()))