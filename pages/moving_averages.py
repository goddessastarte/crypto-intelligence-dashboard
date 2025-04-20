import streamlit as st
import pandas as pd 
import plotly.express as px

if "df" in st.session_state:
    df = st.session_state["df"]

    sma_20_checked = st.checkbox("SMA 20")
    sma_30_checked = st.checkbox("SMA 30")
    sma_50_checked = st.checkbox("SMA 50")
    sma_100_checked = st.checkbox("SMA 100")

    # Calculate SMAs
    df['sma_20'] = df['price'].rolling(window=20).mean()
    df['sma_30'] = df['price'].rolling(window=30).mean()
    df['sma_50'] = df['price'].rolling(window=50).mean()
    df['sma_100'] = df['price'].rolling(window=100).mean()

    # Determine which columns to show
    columns_to_plot = ['price']
    if sma_20_checked:
        columns_to_plot.append('sma_20')
    if sma_30_checked:
        columns_to_plot.append('sma_30')
    if sma_50_checked:
        columns_to_plot.append('sma_50')
    if sma_100_checked:
        columns_to_plot.append('sma_100')

    # Plot!
    fig = px.line(df, x='date', y=columns_to_plot,
                labels={'value': 'Price', 'date': 'Date'},
                title='Price with Moving Averages')
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No data uploaded yet. Please upload from the raw Data page")