from textblob import TextBlob


n = int(input("How many sentences do you want to enter: "))

sentences = []
for i in range(n):
    text = input(f"Enter Sentence {i+1}: ")
    sentences.append(text)

print("\n--- Sentiment Results ---")


for sentence in sentences:
    blob = TextBlob(sentence)
    print(f"Sentence: {sentence}")
    print(f"Sentiment Score: {blob.sentiment.polarity}\n")
