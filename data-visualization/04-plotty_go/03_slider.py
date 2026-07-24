import plotly.graph_objects as go
import plotly.express as px

df = px.data.tips()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['total_bill'],
    y=df['tip'],
    mode='markers',
    marker=dict(
        size=8,
        color='#2B5C8F',
        opacity=0.8,
        line=dict(width=0.5, color='rgba(0, 0, 0, 0.2)')
    ),
    text=df.apply(lambda r: f"Day: {r['day']}<br>Size: {r['size']}", axis=1),
    hovertemplate='<b>Total Bill:</b> $%{x:.2f}<br><b>Tip:</b> $%{y:.2f}<br>%{text}<extra></extra>',
    name='Tips'
))

fig.update_layout(
    title=dict(
        text="<b>Tip Amount vs. Total Bill</b>",
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
            thickness=0.1
        ),
        rangeselector=dict(
            buttons=list([
                dict(count=10, label="$10", step="all", stepmode="backward"),
                dict(count=20, label="$20", step="all", stepmode="backward"),
                dict(count=30, label="$30", step="all", stepmode="backward"),
                dict(step="all", label="All")
            ]),
            bgcolor="#FFFFFF",
            activecolor="#E2E8F0",
            bordercolor="#CED4DA",
            borderwidth=1,
            font=dict(size=11, color="#333333"),
            x=0.02,
            y=1.08
        )
    ),
    yaxis=dict(
        title="Tip Amount ($)",
        showgrid=True,
        gridcolor="#E9ECEF",
        zeroline=False,
        linecolor="#CCCCCC",
        tickfont=dict(color="#495057")
    ),
    template="plotly_white",
    paper_bgcolor='#FFFFFF',
    plot_bgcolor='#FAFAFA',
    hovermode="closest",
    margin=dict(t=90, b=60, l=60, r=60)
)

fig.show()