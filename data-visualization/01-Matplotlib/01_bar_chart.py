import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [26, 32, 41, 21, 35, 48, 52, 45, 38, 42, 50, 65]
}


df = pd.DataFrame(data)
plt.bar(height='Sales', x='Month', data=df, color="#0C527A")
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.title('Monthly sales of mobile phone')
plt.tight_layout()
plt.show()
