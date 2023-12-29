import streamlit as st
st.write("<h1>Good morning</h1>",unsafe_allow_html=True)

st.write("<h1 style='color:blue;'>Good morning</h1>",unsafe_allow_html=True)

st.file_uploader("upload file")

st.image("https://img.freepik.com/free-photo/beautiful-rose-nature_23-2150737339.jpg")
st.vedio("https://youtu.be/KGGzd8UxQQ4?si=LzDoaJkhElWEynlc")
img = st.file_uploader("Upload image")
st.image(img)

