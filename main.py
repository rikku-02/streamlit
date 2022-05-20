import streamlit as st
from pytube import YouTube
url = st.text_input(label='URL: ')
convert = st.button('Convert')


if convert:
  yt = YouTube(url)
  stream = yt.streams.get_by_itag(22)
  streams.download()