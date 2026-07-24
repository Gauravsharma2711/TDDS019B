import matplotlib.pyplot as plt
import seaborn as sns

apps = ["App A", "App A", "App A", "App A", "App B", "App B", "App B", "App B"]
times = [25, 30, 28, 35, 15, 22, 18, 20]

sns.set_style("white")
with plt.xkcd():
    plt.figure(figsize=(7, 5))
    sns.violinplot(x=apps, y=times)
    plt.title("Delivery App Speed Distribution")
    plt.xlabel("Service Provider")
    plt.ylabel("Minutes to Deliver")
    plt.tight_layout()
    plt.show()
