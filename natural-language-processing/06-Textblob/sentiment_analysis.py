from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer

sentences  = input("Enter a few sentences : ").split()

for sentence in sentences :
    score = analyzer.polarity_scores(sentence)
    print(sentence)
    print(score)
    print()