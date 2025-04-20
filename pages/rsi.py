import streamlit as st

if "df" in st.session_state:
    df = st.session_state["df"]
else:
    st.warning("No data uploaded yet. Please upload from the raw Data page")




st.button("button 1")
st.checkbox("button 2")
st.toggle("button 3")
st.radio("choose", ["1","2","3"])
st.multiselect("choose", ["1","2","3","4"])