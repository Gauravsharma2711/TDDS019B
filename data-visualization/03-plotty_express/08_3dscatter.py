import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
n_customers = 300
data = {
    'Age': np.random.normal(40, 15, n_customers),
    'Income': np.random.normal(65000, 25000, n_customers),
    'Spending': np.random.normal(5000, 2000, n_customers),
    'Segment': np.random.choice(['Premium', 'Standard', 'Budget'], n_customers, p=[0.3, 0.45, 0.25])
}
df = pd.DataFrame(data)
df['Age'] = np.clip(df['Age'], 18, 80)
df['Income'] = np.clip(df['Income'], 20000, 150000)
df['Spending'] = np.clip(df['Spending'], 1000, 10000)

fig = px.scatter_3d(
    df,
    x='Age',
    y='Income',
    z='Spending',
    color='Segment',
    title='Customer Segmentation Analysis',
    color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1'],
    opacity=0.7,
    size_max=10
)

fig.update_traces(marker=dict(size=6))

fig.update_layout(
    scene=dict(
        xaxis_title='Age',
        yaxis_title='Annual Income ($)',
        zaxis_title='Annual Spending ($)',
        xaxis=dict(backgroundcolor='rgb(240, 240, 245)'),
        yaxis=dict(backgroundcolor='rgb(240, 240, 245)'),
        zaxis=dict(backgroundcolor='rgb(240, 240, 245)')
    ),
    template='plotly_white',
    width=900,
    height=700
)

fig.show()