import plotly.express as px
import pandas as pd

# Monthly Revenue Data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [25000, 28000, 32000, 29000, 35000, 38000]
}

df = pd.DataFrame(data)

# Simple bar chart
fig = px.bar(
    df,
    x='Month',
    y='Revenue',
    title='💰 Monthly Revenue 2025',
    text='Revenue',  # Show values on bars
    color='Revenue',  # Color based on value
    color_continuous_scale='Viridis'  # Attractive color gradient
)

# Simple styling
fig.update_layout(
    template='plotly_white',
    width=800,
    height=500,
    showlegend=False
)

fig.update_traces(
    texttemplate='$%{text:,}',
    textposition='outside',
    marker=dict(line=dict(color='white', width=2))
)

fig.update_yaxes(tickprefix='$', tickformat=',d')

fig.show()