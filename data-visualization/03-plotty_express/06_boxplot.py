import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'Salary': np.concatenate([
        np.random.normal(50000, 8000, 50),
        np.random.normal(65000, 10000, 50),
        np.random.normal(80000, 12000, 50),
        np.random.normal(55000, 9000, 50)
    ]),
    'Department': ['Sales']*50 + ['Marketing']*50 + ['Engineering']*50 + ['Finance']*50
}
df = pd.DataFrame(data)

fig = px.box(
    df,
    x='Department',
    y='Salary',
    color='Department',
    title='Salary Distribution by Department',
    color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
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