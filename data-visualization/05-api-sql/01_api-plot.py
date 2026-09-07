import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

DEFAULT_KEY = "CG-z8rTVe2GEE9G71uKbL1SXFbx"

BASE = "https://api.coingecko.com/api/v3"
NUM_COINS = 15

GREEN = "#26a69a"
RED = "#ef5350"

st.set_page_config(
    page_title="Live Crypto Dashboard",
    page_icon="🪙",
    layout="wide",
)


with st.sidebar:
    st.header("Controls")
    api_key = st.text_input(
        "CoinGecko API key",
        value=DEFAULT_KEY,
        type="password",
    )
    refresh = st.slider(
        "Auto-refresh (seconds)",
        30, 300, 60,
        step=30,
    )
    st.markdown("[Get a free key](https://www.coingecko.com/en/api)")
    st.caption("Free plan: 30 calls/min")

st_autorefresh(interval=refresh * 1000, key="refresh")

st.title("Live Crypto Market Dashboard")
st.caption(
    f"Last updated: {datetime.now().strftime('%H:%M:%S')}"
    f" | refresh every {refresh}s"
)

HEADERS = {}
if api_key and "PASTE" not in api_key:
    HEADERS = {"x-cg-demo-api-key": api_key}

def _get(url, params=None):
    r = requests.get(url, params=params, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        try:
            reason = r.json()["status"]["error_message"]
        except Exception:
            reason = r.text[:120]
        msg = f"HTTP {r.status_code} - {reason}"
        raise RuntimeError(msg)
    return r.json()


@st.cache_data(ttl=30, show_spinner=False)
def fetch_global(_key):
    return _get(f"{BASE}/global")["data"]


@st.cache_data(ttl=30, show_spinner=False)
def fetch_markets(_key):
    data = _get(f"{BASE}/coins/markets", params={
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": NUM_COINS,
        "page": 1,
        "sparkline": "true",
        "price_change_percentage": "1h,24h,7d",
    })
    return pd.DataFrame(data)


def fmt_usd(n):
    if n >= 1e12:
        return f"${n/1e12:.2f}T"
    if n >= 1e9:
        return f"${n/1e9:.2f}B"
    if n >= 1e6:
        return f"${n/1e6:.2f}M"
    return f"${n:,.0f}"


def safe(v):
    return 0 if pd.isna(v) else v

try:
    g = fetch_global(api_key)
    df = fetch_markets(api_key)
except Exception as e:
    st.error(f"API error: {e}")
    if "401" in str(e):
        st.info("Invalid key. Paste your CoinGecko key in sidebar.")
    if "429" in str(e):
        st.info("Rate limited. Increase the refresh interval.")
    st.stop()

if "PASTE" in api_key:
    st.warning(
        "No API key set. Get one free: "
        "https://www.coingecko.com/en/api"
    )

mc = g["total_market_cap"]["usd"]
mcc = g["market_cap_change_percentage_24h_usd"]
vol = g["total_volume"]["usd"]
btc = g["market_cap_percentage"]["btc"]
coins = g["active_cryptocurrencies"]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Market Cap", fmt_usd(mc), f"{mcc:+.2f}% (24h)")
c2.metric("24h Volume", fmt_usd(vol))
c3.metric("BTC Dominance", f"{btc:.1f}%")
c4.metric("Active Coins", f"{coins:,}")

st.subheader("Top Coins")
cols = st.columns(4)
for col, (_, row) in zip(cols, df.head(4).iterrows()):
    chg = safe(row["price_change_percentage_24h_in_currency"])
    col.metric(
        label=row["symbol"].upper(),
        value=f"${row['current_price']:,.2f}",
        delta=f"{chg:+.2f}% (24h)",
    )

st.subheader("7-Day Price Chart")
coin = st.selectbox("Coin", df["name"])
row = df[df["name"] == coin].iloc[0]
prices = row["sparkline_in_7d"]["price"]
chg7 = safe(row["price_change_percentage_7d_in_currency"])
times = pd.date_range(
    end=datetime.now(),
    periods=len(prices),
    freq="60min",
)

if chg7 >= 0:
    line_color = GREEN
    fill_rgb = "38,166,154"
else:
    line_color = RED
    fill_rgb = "239,83,80"
fill_rgba = f"rgba({fill_rgb},0.12)"

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=times,
    y=prices,
    mode="lines",
    line=dict(color=line_color, width=3),
    fill="tozeroy",
    fillcolor=fill_rgba,
))
fig.update_layout(height=320, margin=dict(l=10, r=10, t=20, b=10))
fig.update_yaxes(title="USD")
fig.update_xaxes(tickformat="%b %d")
st.plotly_chart(fig, use_container_width=True)

st.caption(
    f"7d change: {chg7:+.2f}% | "
    f"High ${max(prices):,.2f} | Low ${min(prices):,.2f}"
)

st.subheader("Market Cap - Top 10")
top = df.head(10)
chg24 = top["price_change_percentage_24h_in_currency"].apply(safe)
colors = []
for v in chg24:
    colors.append(GREEN if v >= 0 else RED)
labels = [fmt_usd(v) for v in top["market_cap"]]

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=top["name"],
    y=top["market_cap"],
    marker_color=colors,
    text=labels,
    textposition="outside",
))
fig2.update_layout(height=380, margin=dict(l=10, r=10, t=20, b=10))
fig2.update_yaxes(type="log", title="Market Cap (log)")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Full Market Data")
show = df[[
    "name",
    "symbol",
    "current_price",
    "price_change_percentage_1h_in_currency",
    "price_change_percentage_24h_in_currency",
    "price_change_percentage_7d_in_currency",
    "market_cap",
    "total_volume",
]].copy()
show.columns = [
    "Coin", "Symbol", "Price",
    "1h %", "24h %", "7d %",
    "Market Cap", "Volume 24h",
]
for c in ["1h %", "24h %", "7d %"]:
    show[c] = show[c].apply(safe)

st.dataframe(
    show,
    column_config={
        "Price": st.column_config.NumberColumn(format="$%.2f"),
        "1h %": st.column_config.NumberColumn(format="%+.2f%%"),
        "24h %": st.column_config.NumberColumn(format="%+.2f%%"),
        "7d %": st.column_config.NumberColumn(format="%+.2f%%"),
        "Market Cap": st.column_config.NumberColumn(format="$%.0f"),
        "Volume 24h": st.column_config.NumberColumn(format="$%.0f"),
    },
    hide_index=True,
    use_container_width=True,
)