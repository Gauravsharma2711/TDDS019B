import matplotlib.pyplot as plt
import seaborn as sns

brands = ["Apple", "Samsung", "Google"]
sales = [150, 125, 85]

sns.set_style("white")
with plt.xkcd():
    plt.figure(figsize=(7, 5))
    sns.barplot(x=brands, y=sales, errorbar=None)
    plt.title("Weekly Smartphone Sales")
    plt.xlabel("Brand Name")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.show()
