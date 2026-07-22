import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = input("Enter a text: ")
text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))

tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_tokens = []

for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)

stemmer = PorterStemmer()
stemmed_words = []

for word in filtered_tokens:
    stemmed_words.append(stemmer.stem(word))

lemmatizer = WordNetLemmatizer()
lemmatized_words = []

for word in filtered_tokens:
    lemmatized_words.append(lemmatizer.lemmatize(word))

print("Original Tokens:", tokens)
print("Filtered Tokens:", filtered_tokens)
print("Stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)