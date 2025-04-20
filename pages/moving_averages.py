import streamlit as st
import pandas as pd 
import plotly.express as px

if "df" in st.session_state:
    df = st.session_state["df"]
    df['sma_20'] = df['price'].rolling(window=20).mean()
    df['sma_100'] = df['price'].rolling(window=100).mean()

    fig = px.line(df, x='date', y=['price', 'sma_20', 'sma_100'],
            labels={'value': 'Price', 'date': 'Date'},
            title='Price with Moving Averages')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data uploaded yet. Please upload from the raw Data page")