import streamlit as st
import pandas as pd
import numpy as np
import ta

st.set_page_config(page_title="Millimade AI Trader", layout="centered")
st.markdown("<h1 style='text-align: center; color: #00ffd0;'>Millimade AI Trader 💼📈</h1>", unsafe_allow_html=True)

license_input = st.text_input("🔐 Enter License Key", type="password")
if license_input != "MILLI-123-KEY":
    st.warning("Enter a valid license key to unlock the bot.")
    st.stop()

st.success("✅ License verified. Welcome to the Millimade AI trading bot!")

stock = st.text_input("📊 Stock Symbol (e.g., AAPL)", "AAPL")
crypto = st.text_input("💹 Crypto Symbol (e.g., BTCUSDT)", "BTCUSDT")
auto_trade = st.checkbox("⚙️ Enable Auto Trade Logic (Simulated)")

data = pd.DataFrame({
    'close': np.random.normal(100, 1, 100)
})

data['ema_20'] = ta.trend.ema_indicator(data['close'], window=20)
data['ema_50'] = ta.trend.ema_indicator(data['close'], window=50)
data['rsi'] = ta.momentum.RSIIndicator(data['close']).rsi()

last = data.iloc[-1]
signal = "HOLD"
if last['ema_20'] > last['ema_50'] and last['rsi'] < 70:
    signal = "BUY"
elif last['ema_20'] < last['ema_50'] and last['rsi'] > 30:
    signal = "SELL"

st.markdown(f"## 📈 AI Signal: **{signal}**")
if auto_trade and signal in ["BUY", "SELL"]:
    st.info(f"Auto-trade simulated: {signal} {stock} / {crypto}")

st.caption("🧠 Powered by Millimade AI • Web Edition")
