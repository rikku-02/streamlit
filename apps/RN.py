import streamlit as st


def app():
    code = """
       def Release_Notes():
           Side_Bar_Nav = 'Implemented at the Top Left ✅'
           Convert_to_MP3 = 'Implemented ✅'
           YouTube_Pro_No_ADS = 'Soon 😈'
           YouTube_to_MP4 = "We're working on that.. ☕"
           Music_Stream = 'Hmm.. 🧐'
           """

    st.code(code, language='python')
