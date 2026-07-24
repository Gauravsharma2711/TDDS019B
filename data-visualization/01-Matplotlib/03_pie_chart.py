import matplotlib.pyplot as plt


os_labels = ['Windows', 'macOS', 'Linux', 'ChromeOS', 'Others']
market_share = [62.16, 14.58, 3.09, 1.42, 18.75]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']


plt.figure(figsize=(6, 6))
plt.pie(market_share, labels=os_labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Global Desktop Operating System Market Share')
plt.show()
