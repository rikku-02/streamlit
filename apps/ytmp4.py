import streamlit as st
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from moviepy.editor import *
import datetime
import os


def app():
    st.header('Convert to MP4 📹')

    filePath = ''

    url = st.text_input(label='URL: ')
    convert = st.button('Convert')

    if url == '':
        pass

    else:
        try:
            yti = YouTube(url)
            st.subheader(yti.title)
            st.image(yti.thumbnail_url, width=200)
            sec = yti.length
            res = datetime.timedelta(seconds=sec)
            st.text(f'Duration: {res} ')
            # convert = st.button('Convert')

            if convert:
                with st.spinner('Converting...'):
                    yt = YouTube(url)

                    yt.streams.filter(only_audio=True)
                    stream = yt.streams.get_by_itag(22)

                    freshDownload = stream.download(filePath)

                    basePath, extension = os.path.splitext(freshDownload)

                    video = AudioFileClip(os.path.join(basePath + ".mp4"))
                    video.close()

                    with open(os.path.join(basePath + ".mp4"), 'rb') as f:
                        st.success('Successful! Download Now ⬇')
                        st.download_button('Download Mp4', f, file_name=yt.title + '.mp4')

        except RegexMatchError:
            st.warning('Please input a valid URL!')
