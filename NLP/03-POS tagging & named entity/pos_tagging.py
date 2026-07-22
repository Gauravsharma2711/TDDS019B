import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

text = input("Enter text: ")
tokens = word_tokenize(text)

pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)

ner_tree = ne_chunk(pos_tags)
print("Named Entities:\n", ner_tree)