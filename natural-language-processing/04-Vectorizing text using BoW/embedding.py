from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

S = [["rahul", "goes", "to", "college"], ["neha", "studies", "data", "science"]]

model = Word2Vec(
    sentences=S,
    vector_size=50,  
    window=2,  
    min_count=1,  
    sg=1,  
)


w = list(model.wv.index_to_key)  
print("words in vocabulary: \n")
print(w)


v = []
for i in w:
    x = model.wv[i]
    v.append(x)
print("Vector: ", v)

pca = PCA(n_components=2)
result=pca.fit_transform(v)
plt.figure(figsize=(8,6))
plt.scatter(result[:,0] , result[:,1])
i = 0
for x in w :
    plt.annotate(x,(result[i][0],result[i][1]))
    i = i + 1
plt.title("Skip Gram word embedding")
plt.grid()
plt.show()