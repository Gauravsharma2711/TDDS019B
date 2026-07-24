import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'Salary': np.concatenate([
        np.random.normal(50000, 8000, 150),
        np.random.normal(65000, 10000, 150),
        np.random.normal(80000, 12000, 150),
        np.random.normal(55000, 9000, 150)
    ]),
    'Department': ['Sales']*150 + ['Marketing']*150 + ['Engineering']*150 + ['Finance']*150
}
df = pd.DataFrame(data)

fig = px.violin(
    df,
    x='Department',
    y='Salary',
    color='Department',
    title='Salary Distribution by Department',
    color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
    box=True,
    points='outliers'
)

fig.update_layout(
    template='plotly_white',
    width=800,
    height=500,
    showlegend=False,
    yaxis=dict(tickprefix='$', tickformat=',d')
)

fig.show()