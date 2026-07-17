import plotly.graph_objects as go
import numpy as np

np.random.seed(42)
satisfaction = np.random.choice([1, 2, 3, 4, 5], 200, p=[0.05, 0.1, 0.2, 0.35, 0.3])

fig = go.Figure(data=[
    go.Histogram(
        x=satisfaction,
        nbinsx=5,
        marker_color=['#FF6B6B', '#FECA57', '#FF9F43', '#54A0FF', '#5F27CD'],
        marker_line_color='white',
        marker_line_width=2,
        texttemplate='%{y}',
        textposition='outside'
    )
])

fig.update_layout(
    title='Customer Satisfaction Ratings',
    xaxis_title='Rating (1-5)',
    yaxis_title='Number of Customers',
    template='plotly_white',
    width=700,
    height=500,
    showlegend=False,
    xaxis=dict(
        tickmode='array',
        tickvals=[1, 2, 3, 4, 5],
        ticktext=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐']
    )
)

fig.show()