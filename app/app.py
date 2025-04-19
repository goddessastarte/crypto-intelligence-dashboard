import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crypto Intelligence", layout="wide")

st.title("Crypto Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload your crypto CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.dataframe(df.head())

    if 'snapped_at' in df.columns:
        df['date'] = pd.to_datetime(df['snapped_at'].str.replace(" UTC", ""))
        df = df[["date", "price"]]
        df = df.sort_values('date')

        st.line_chart(df.set_index("date")["price"])

    else:
        st.warning("This CSV has no 'snapped_at' columns.")
else:
    st.info("Please upload a CSV file to get started")

df['sma_20'] = df['pric'].rolling(window=20).mean()
df['sma_100'] = df['price'].rolling(window=100).mean()

st.subheader("📈 Price with Moving Averages")

plt.figure(figsize=(10, 4))
plt.plot(df['date'], df['price'], label="Close Price")
plt.plot(df['date'], df['sma_20'], label="SMA 20", linestyle='--')
plt.plot(df['date'], df['sma_100'], label="SMA 100", linestyle=':')
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.title("Price + Moving Averages")
st.pyplot(plt)

