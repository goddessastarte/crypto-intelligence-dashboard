import streamlit as st

if "df" in st.session_state:
    df = st.session_state["df"]
else:
    st.warning("No data uploaded yet. Please upload from the raw Data page")

st.button("button 1")
st.button("button 2")