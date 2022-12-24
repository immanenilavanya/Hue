#this will be the web app built with streamlit
import streamlit as st
from PIL import Image
import time

st.write("This is the sample text to be displayed")

status_bar = st.progress(0)
latest_iteration = st.empty()
for i in range(100):
	latest_iteration.text(f'Progress bar {i}')
	bar.progress(i+1)
	timesleep(0.1)

st.write(Image.open("palette.png"))
