import plotly.graph_objects as go

labels = ['Product A', 'Product B', 'Product C', 'Product D']
q1 = [1200, 900, 750, 600]
q2 = [1400, 950, 800, 700]
q3 = [1600, 1000, 850, 750]
q4 = [1800, 1100, 900, 800]

fig = go.Figure()

fig.add_trace(go.Pie(
    labels=labels,
    values=q1,
    name='Q1',
    domain={'row': 0, 'column': 0}
))

fig.add_trace(go.Pie(
    labels=labels,
    values=q2,
    name='Q2',
    domain={'row': 0, 'column': 1}
))

fig.add_trace(go.Pie(
    labels=labels,
    values=q3,
    name='Q3',
    domain={'row': 1, 'column': 0}
))

fig.add_trace(go.Pie(
    labels=labels,
    values=q4,
    name='Q4',
    domain={'row': 1, 'column': 1}
))

fig.update_layout(
    title='Quarterly Sales by Product',
    template='plotly_white',
    width=900,
    height=700,
    grid={'rows': 2, 'columns': 2}
)

fig.update_traces(
    textinfo='label+percent',
    textfont_size=12,
    marker_colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
)

fig.show()