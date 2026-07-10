import matplotlib.pyplot as plt
import seaborn as sns

departments = ["HR", "HR", "HR", "IT", "IT", "IT", "Sales", "Sales", "Sales"]
salaries = [3200, 3500, 3100, 5400, 5800, 5200, 4100, 4600, 4300]

sns.set_style("white")
with plt.xkcd():
    plt.figure(figsize=(7, 5))
    sns.boxplot(x=departments, y=salaries)
    plt.title("Employee Salaries by Department")
    plt.xlabel("Department")
    plt.ylabel("Monthly Salary ($)")
    plt.tight_layout()
    plt.show()
