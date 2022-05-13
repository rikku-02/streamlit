import streamlit as st
import owo
import pathlib

st.title('Rikku.URL Shortener')
key = st.secrets['API_KEY']

uploaded_file = st.file_uploader("Choose a file")

btnUp = st.button('Upload')


if uploaded_file is not None:
     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     string_data = stringio.read()
     st.write(string_data)
    
        

    

    
#####
url = st.text_input('')
btn = st.button('Shorten')

IMAGE_URL = "https://ahegao.b-cdn.net/wp-content/uploads/2021/04/Ijiranaide-Nagatoro-san-Episode-1-Nagatoro-Wipes-More-Senpai-Tears.jpg"


try:
    if btn:
        st.write(owo.shorten_urls(key, url))

except ValueError:
    st.write('Invalid URL, Please input "https://..."')
    
st.image(IMAGE_URL)
     
