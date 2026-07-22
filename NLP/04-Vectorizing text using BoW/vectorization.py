from sklearn.feature_extraction.text import TfidfVectorizer
def get_docs_and_terms():
    d1=input("Enter D1 : ")
    d2=input("Enter D2 : ")
    d3=input("Enter D3 : ")

    t1=input("Enter T1 : ").strip()
    t2=input("Enter T2 : ").strip()
    t3=input("Enter T3 : ").strip()

    return [d1 ,d2 , d3] , [t1 , t2 , t3]


documents , terms = get_docs_and_terms()


tfidf=TfidfVectorizer(vocabulary=terms)
result=tfidf.fit_transform(documents)
print("Vocabulary (TF-IDF) :", tfidf.get_feature_names_out())
print("\nTF-IDF Matrix (Array Format):\n",round(result).toarray().astype(int))