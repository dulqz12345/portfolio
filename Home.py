import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Jacek S")
    content = """
    Lorem ipsum Lorem ipsumLorem ipsumLo
    Lorem ipsumLorem ipsumLorem ipsumLorem ipsum
    Lorem ipsumLorem ipsumLorem ipsumLorem ipsumLorem ipsum
    Lorem ipsumLorem ipsumLorem ipsumLorem i
    """
    st.info(content)

content2 = """
Below you will find my projects. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")
