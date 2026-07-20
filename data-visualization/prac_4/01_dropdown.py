import plotly.graph_objects as go
import plotly.express as px

df = px.data.tips()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',
    marker=dict(
        size=9,
        color=df['total_bill'],
        colorscale='Viridis',
        showscale=True,
        opacity=0.85,
        line=dict(width=0.5, color='rgba(0, 0, 0, 0.3)'),
        colorbar=dict(
            title=dict(
                text="Total Bill ($)",
                side="top"
            ),
            thickness=14,
            len=0.85
        )
    ),
    text=df['time'],
    hovertemplate='<b>Day:</b> %{x}<br><b>Tip:</b> $%{y:.2f}<br><b>Time:</b> %{text}<extra></extra>',
    name='Tips'
))

fig.update_layout(
    title=dict(
        text="<b>Tips Analysis by Day & Total Bill</b>",
        font=dict(size=18, family="Arial, sans-serif", color="#212529"),
        x=0.02,
        y=0.95
    ),
    xaxis=dict(
        title="Day of the Week",
        showgrid=False,
        zeroline=False,
        linecolor="#CCCCCC",
        tickfont=dict(color="#495057")
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
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FAFAFA",
    hovermode="closest",
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{"type": "scatter", "mode": "markers", "textposition": "none"}],
                    label="Scatter",
                    method="restyle"
                ),
                dict(
                    args=[{"type": "bar", "textposition": "none"}],
                    label="Bar",
                    method="restyle"
                ),
                dict(
                    args=[{"type": "box", "textposition": "none"}],
                    label="Box",
                    method="restyle"
                )
            ]),
            direction="down",
            showactive=True,
            x=0.98,
            xanchor="right",
            y=1.18,
            yanchor="top",
            bgcolor="#FFFFFF",
            bordercolor="#CED4DA",
            borderwidth=1,
            font=dict(color="#333333", size=12)
        )
    ],
    margin=dict(t=100, b=60, l=60, r=60)
)

fig.show()