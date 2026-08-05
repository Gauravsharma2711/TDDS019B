from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = [
    "students attend lectures and practicals",
    "college has library and reading room",
    "students participate in cultural activities",
    "exams and assignments are important",
    "sports and events improve teamwork"
]

vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=2)
lda.fit(X)

words = vectorizer.get_feature_names_out()

topic_number = 1

for topic in lda.components_:
    print("Topic", topic_number)

    top_words = topic.argsort()[-5:]

    for index in top_words:
        print(words[index])

    topic_number += 1
    print()