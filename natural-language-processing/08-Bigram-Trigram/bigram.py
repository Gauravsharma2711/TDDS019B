import nltk 
from nltk import word_tokenize, bigrams 
from collections import Counter 
nltk.download("punkt_tab")

text =input("enter the setnetce : ")
word_tokens = word_tokenize(text.lower()) 
unigram_counts = Counter(word_tokens)
bigrams_count = Counter(bigrams(word_tokens))

sentence = input("enter the sentence for training senetences : ")
input_words = word_tokenize(sentence.lower())
input_bigrams = list(bigrams(input_words))
probability = 1 

for w1,w2 in input_bigrams:
    if unigram_counts[w1] > 0:
      probability*= bigrams_count[(w1,w2)] / unigram_counts[w1]
    else:
      probability = 0
print("Bigrams:",input_bigrams)
print("Probability:",probability)