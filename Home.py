import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile pic.jpg", width = 450)


with col2:
    st.title("Ryan A. Kaufman")
    content = """
    Hello, I am Ryan! I am a developer and Latin teacher -- quite the combination, I am aware! I suppose it was bound to
    be this way, operating in polar extremes; I also love classical music...as well as heavy metal; I love poetry and 
    literature, but at the same time, am a fan of mixed martial arts. You get the idea. I have a B.A. in Biblical 
    Studies from Geneva College, and a Master of Divinity from Reformed Theological Seminary.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I've built. Feel free to contact me by clicking on 'contact me' on the left side of this page!
"""
st.write(content2)

col3, spacer_col, col4 = st.columns([1.5, 0.5, 1.5]) # list of ratio dimensions for the argument

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image ("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")