import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
x = np.linspace(0, 10, 50)
df = pd.DataFrame({
    'X': np.tile(x, 3),
    'Y': np.concatenate([
        np.sin(x) + np.random.normal(0, 0.1, 50),
        np.cos(x) + np.random.normal(0, 0.1, 50),
        np.sin(x) * np.exp(-x/5) + np.random.normal(0, 0.05, 50)
    ]),
    'Category': ['Sine Wave']*50 + ['Cosine Wave']*50 + ['Damped Sine']*50
})


fig = px.line(
    df,
    x='X',
    y='Y',
    color='Category',
    line_dash='Category',
    markers=True,
    title='Line Plot',
    color_discrete_sequence=px.colors.qualitative.Set2,
    template='plotly_white'
)


fig.update_layout(
    title_font=dict(size=24, family='Arial Black'),
    hovermode='x unified',
    legend=dict(
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='gray',
        borderwidth=1
    )
)


fig.update_traces(
    marker=dict(size=10, line=dict(width=1, color='white')),
    line=dict(width=3)
)

fig.show()