import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crypto Intelligence", layout="wide")

st.title("Crypto Intelligence Dashboard")

uploaded_file = st.file_uploader("Upload your crypto CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Columns detected:", df.columns.tolist())
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