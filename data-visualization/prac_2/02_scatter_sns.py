import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [45, 50, 58, 65, 68, 75, 82, 85, 93, 98]

sns.set_style("white")
with plt.xkcd():
    plt.figure(figsize=(7, 5))
    sns.scatterplot(x=x, y=y)
    plt.title("Study Hours vs Test Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score (%)")
    plt.tight_layout()
    plt.show()
