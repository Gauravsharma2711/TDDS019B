import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5, 6, 7]
y = [22, 24, 23, 26, 28, 27, 29]

sns.set_style("white")
with plt.xkcd():
    plt.figure(figsize=(7, 5))
    sns.lineplot(x=x, y=y, linestyle="solid")
    plt.title("Daily Temperature Tracker")
    plt.xlabel("Day of the Week")
    plt.ylabel("Temperature (C)")
    plt.tight_layout()
    plt.show()
