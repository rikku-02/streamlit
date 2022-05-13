import streamlit as st
import owo

st.title('Rikku.URL Shortener')
key = st.secrets['API_KEY']



url = st.text_input('')
btn = st.button('Shorten')

IMAGE_URL = "https://i.pinimg.com/originals/0e/26/1b/0e261bfd97562baad77e39a7c3dad32d.png"
st.image(IMAGE_URL)

try:
    if btn:
        st.write(owo.shorten_urls(key, url))

except ValueError:
    st.write('Invalid URL, Please input "https://..."')
