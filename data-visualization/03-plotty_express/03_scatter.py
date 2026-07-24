import plotly.express as px
import pandas as pd


data = {
    'Age': [22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58],
    'Income': [30000, 35000, 40000, 45000, 48000, 52000, 58000, 62000, 
               65000, 70000, 72000, 75000, 78000, 80000, 85000]
}

df = pd.DataFrame(data)


fig = px.scatter(
    df,
    x='Age',
    y='Income',
    title='💰 Age vs Income with Trend',
    trendline='ols',  
    color_discrete_sequence=['#FF6B6B']
)

fig.update_traces(marker=dict(size=12, line=dict(color='white', width=2)))

fig.update_layout(
    template='plotly_white',
    width=800,
    height=500,
    yaxis=dict(tickprefix='$', tickformat=',d')
)

fig.show()