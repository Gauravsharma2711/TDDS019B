import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('iris')


setosa = df[df['species'] == 'setosa']
versicolor = df[df['species'] == 'versicolor']
virginica = df[df['species'] == 'virginica']


plt.scatter(setosa['sepal_length'], setosa['sepal_width'], color='red', label='Setosa')
plt.scatter(versicolor['sepal_length'], versicolor['sepal_width'], color='blue', label='Versicolor')
plt.scatter(virginica['sepal_length'], virginica['sepal_width'], color='green', label='Virginica')


plt.title('Iris Dataset Scatter Plot')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
