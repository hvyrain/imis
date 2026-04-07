import streamlit as st
import seaborn as sns
pg = sns.load_dataset("penguins")

st.title("streamlit 연습장")
st.header("연습용입니다")
st.write(sns.pairplot(pg))