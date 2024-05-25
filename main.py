import streamlit as st

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