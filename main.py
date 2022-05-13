import streamlit as st
import owo
import pathlib

st.title('Rikku.URL Shortener')
key = st.secrets['API_KEY']

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

btnUp = st.button('Upload')

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.getvalue()
    with open(upload_file.name + '.txt', 'w') as f:
        f.write(bytes_data)
        f.close()
    

    if btnUp:
        ext = pathlib.Path(uploaded_file.name).suffix
        st.write(owo.upload_files(key, upload))
        

    

    
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
     
