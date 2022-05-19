import streamlit as st
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import datetime
from moviepy.editor import *
import os

# Dev-R
st.set_page_config(
   page_title="YouTube to Mp3 by Devr-R",
   page_icon="https://cdn3.iconfinder.com/data/icons/e-commerce-35/74/money_conversion-512.png",
   layout='centered',
   initial_sidebar_state="collapsed",
   menu_items={
         'Get Help': 'https://fb.me/devric.ui',
         'Report a bug': "https://fb.me/devric.ui",
         'About': "# Created by Dev-R"
     }
)

st.image('https://owo.whats-th.is/8G7k3AX.png')
st.header('YouTube to Mp3 Converter')

filePath = ''

url = st.text_input(label='URL: ')

convert = st.button('Convert')

if convert:
    try:
        yti = YouTube(url)
        st.subheader(yti.title)
        st.image(yti.thumbnail_url, width=200)
        sec = yti.length
        res = datetime.timedelta(seconds=sec)
        st.text(f'Duration: {res} ')

        with st.spinner('Converting...'):
            yt = YouTube(url)

            yt.streams.filter(only_audio=True)
            stream = yt.streams.get_by_itag(140)

            freshDownload = stream.download(filePath)

            basePath, extension = os.path.splitext(freshDownload)

            video = AudioFileClip(os.path.join(basePath + ".mp4"))
            video.write_audiofile(os.path.join(basePath + ".mp3"))

            with open(os.path.join(basePath + ".mp3"), 'rb') as f:
                st.success('Success!')
                st.download_button('Download', f, file_name=yt.title + '.mp3')

    except RegexMatchError:
        st.warning('Please input a valid URL!')