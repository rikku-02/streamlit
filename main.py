import streamlit as st
import owo
import pathlib

IMAGE_URL = "https://ahegao.b-cdn.net/wp-content/uploads/2021/04/Ijiranaide-Nagatoro-san-Episode-1-Nagatoro-Wipes-More-Senpai-Tears.jpg"
key = st.secrets['API_KEY']

st.header('Rikku.File Upload and Url Shortener')
st.image(IMAGE_URL)

st.subheader('Rikku.File Upload')
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

btnUp = st.button('Upload')

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    with open(f'{uploaded_file.name}', 'wb') as f: 
        f.write(bytes_data)
    
    if btnUp:        
        st.write(owo.upload_files(key, uploaded_file.name))  

    
#####
st.subheader('Rikku.URL Shortener')
url = st.text_input('ex. https://...', '')
btn = st.button('Shorten')



try:
    if btn:
        st.write(owo.shorten_urls(key, url))

except ValueError:
    st.write('Invalid URL, Please input "https://..."')
    

     
