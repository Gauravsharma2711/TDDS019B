import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = px.data.tips()

plot = go.Figure()

plot.add_trace(go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',
    marker=dict(
        size=10,
        color=df['size'],
        colorscale='Viridis',
        showscale=True,
        opacity=0.85,
        colorbar=dict(
            title=dict(
                text="Party Size",
                side="top"
            ),
            thickness=14,
            len=0.85
        ),
        line=dict(width=0.5, color='rgba(0,0,0,0.3)')
    ),
    text=df.apply(lambda r: f"Sex: {r['sex']}<br>Smoker: {r['smoker']}<br>Time: {r['time']}", axis=1),
    hovertemplate='<b>%{x}</b><br>Tip: $%{y:.2f}<br>%{text}<extra></extra>',
    name='Tips'
))

plot.update_layout(
    title=dict(
        text="<b>Restaurant Tips Analysis by Day & Party Size</b>",
        x=0.02,
        y=0.95,
        font=dict(size=18, family="Arial, sans-serif", color="#212529")
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
    paper_bgcolor='#FFFFFF',
    plot_bgcolor='#FAFAFA',
    hovermode="closest",
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            x=0.98,
            xanchor="right",
            y=1.18,
            yanchor="top",
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
                    args=[{"type": "violin", "textposition": "none"}],
                    label="Violin",
                    method="restyle"
                )
            ]),
            bgcolor='#FFFFFF',
            bordercolor='#CED4DA',
            borderwidth=1,
            font=dict(size=12, color='#333333'),
            active=0
        )
    ],
    margin=dict(t=100, b=60, l=60, r=60)
)

plot.show()