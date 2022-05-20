import streamlit as st
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import datetime
from moviepy.editor import *
import os

# Dev-R

st.subheader('MP3 Convert')
def app():
    filePath = ''

    url = st.text_input(label='URL: ')
    convert = st.button('Convert')
    code = """
    def Release_Notes():
        YouTube_to_MP4 = 'Hmm..'"""

    st.code(code, language='python')
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
                    stream = yt.streams.get_by_itag(140)

                    freshDownload = stream.download(filePath)

                    basePath, extension = os.path.splitext(freshDownload)

                    video = AudioFileClip(os.path.join(basePath + ".mp4"))
                    video.write_audiofile(os.path.join(basePath + ".mp3"))

                    with open(os.path.join(basePath + ".mp3"), 'rb') as f:
                        st.success('Successful! Download Now ⬇')
                        st.download_button('Download Mp3', f, file_name=yt.title + '.mp3')

        except RegexMatchError:
            st.warning('Please input a valid URL!')

