import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter text: ")

tokens = word_tokenize(text)

print(tokens)