import streamlit as st


def app():
    code = """
       def Release_Notes():
           Side_Bar_Nav = 'Implemented at the Top Left ✅'
           Convert_to_MP3 = 'Implemented ✅'
           Convert_to_MP4 = 'Implemented ✅'
           YouTube_Pro_No_ADS = 'Soon 😈'
           Music_Stream = 'Hmm.. 🧐'
           """

    st.code(code, language='python')
