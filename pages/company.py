import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(layout="wide")

# Page title
st.title("The Best Company")

# Content section
content = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
"""
st.write(content)

# Team section title
st.title("Our Team")

# Load the data
df = pd.read_csv("data2.csv")

# Create columns
col1, col2, col3 = st.columns(3)

# Display team members in columns
with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.write(row["role"])
        st.image("./images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.write(row["role"])
        st.image("./images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.write(row["role"])
        st.image("./images/" + row["image"])
