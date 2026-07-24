import plotly.graph_objects as go
import plotly.express as px

df = px.data.tips()

# Grouping data to create a clear bar chart
df_grouped = df.groupby('total_bill', as_index=False)['tip'].mean()

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_grouped['total_bill'],
    y=df_grouped['tip'],
    marker=dict(
        color='#2B5C8F',
        opacity=0.85,
        line=dict(width=0.5, color='rgba(0, 0, 0, 0.2)')
    ),
    hovertemplate='<b>Total Bill:</b> $%{x:.2f}<br><b>Avg Tip:</b> $%{y:.2f}<extra></extra>',
    name='Average Tip'
))

fig.update_layout(
    title=dict(
        text="<b>Average Tip by Total Bill Range</b>",
        x=0.02,
        y=0.95,
        font=dict(size=18, family="Arial, sans-serif", color="#212529")
    ),
    xaxis=dict(
        title="Total Bill ($)",
        showgrid=True,
        gridcolor="#E9ECEF",
        zeroline=False,
        linecolor="#CCCCCC",
        tickfont=dict(color="#495057"),
        rangeslider=dict(
            visible=True,
            bgcolor="#F8F9FA",
            bordercolor="#CED4DA",
            borderwidth=1,
            thickness=0.12
        )
    ),
    yaxis=dict(
        title="Average Tip Amount ($)",
        showgrid=True,
        gridcolor="#E9ECEF",
        zeroline=False,
        linecolor="#CCCCCC",
        tickfont=dict(color="#495057")
    ),
    template="plotly_white",
    paper_bgcolor='#FFFFFF',
    plot_bgcolor='#FAFAFA',
    margin=dict(t=80, b=60, l=60, r=60)
)

fig.show()