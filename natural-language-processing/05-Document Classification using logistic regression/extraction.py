from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
documents = [
    "exam timetable is announced" , 
    "project subbmission deadline" , 
    "college annual function",
    "sports day celebration",
    "results will be declared soon",
    "cultural fest invitation"
]

labels = [0,0,1,1,0,1]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(documents)
model = LogisticRegression()
model.fit(X , labels)