import streamlit as st
import owo

st.title('Rikku.URL Shortener')
key = st.secrets['API_KEY']



url = st.text_input('')
btn = st.button('Shorten')

IMAGE_URL = "https://i.pinimg.com/564x/91/81/c4/9181c4016c719f4e9daf194db019cf3c.jpg"


try:
    if btn:
        st.write(owo.shorten_urls(key, url))

except ValueError:
    st.write('Invalid URL, Please input "https://..."')
    
st.image(IMAGE_URL)
