import nltk
from nltk.corpus import reuters

nltk.download('reuters')
print(reuters.fileids())

reuters_text = reuters.words('test/14826')
print("First 100 words of reuters document:", reuters_text[0:100])