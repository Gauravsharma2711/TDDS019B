def calculate(given_text):
    import string
    text = ""
    for ch in given_text:
        if ch not in string.punctuation:
            text += ch
    words = text.split()
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else :
            word_frequency[word] = 1
    return word_frequency

text = input("Enter a Sentence with repeated words : ")
wfreq=calculate(text)
for word , frequency in wfreq.items():
    print(word, ":",frequency)
