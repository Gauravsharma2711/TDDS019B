import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "I love this movie",
    "This was awesome",
    "Great film",
    "I hated this",
    "This was terrible",
    "Bad movie"
]
labels = np.array([1, 1, 1, 0, 0, 0]) 

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)
print("1. Sentences converted to numbers:")
for i in range(len(sentences)):
    print(f"   '{sentences[i]}' -> {sequences[i]}")

max_length = 5
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')
print("\n2. Padded sequences (all made to length 5):")
print(padded_sequences)

model = Sequential()
vocab_size = len(tokenizer.word_index) + 1
model.add(Embedding(input_dim=vocab_size, output_dim=8, input_length=max_length))
model.add(SimpleRNN(16))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("\n3. Starting Training...")
model.fit(padded_sequences, labels, epochs=15, verbose=1)

new_review = ["I really love this"]
test_seq = tokenizer.texts_to_sequences(new_review)
test_padded = pad_sequences(test_seq, maxlen=max_length, padding='post')
prediction = model.predict(test_padded)[0][0]

print(f"\n4. Prediction for '{new_review[0]}':")
print(f"   Probability Score: {prediction:.4f}")

if prediction >= 0.5:
    print("   Result: POSITIVE!")
else:
    print("   Result: NEGATIVE!")