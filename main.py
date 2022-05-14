import streamlit as st
import owo

def auth():
    k = st.empty()
    priv_key = k.text_input('Private Key:', type="password")
    key = st.secrets['USAGE_KEY']

    if priv_key == key:
        k.empty()
        st.success('Success.')
        main()  

def main():
    # File Uploader
    try:
        key = st.secrets['API_KEY']

        st.header('Rikku.File Upload and Url Shortener')
        
        IMAGE_URL = "https://ahegao.b-cdn.net/wp-content/uploads/2021/04/Ijiranaide-Nagatoro-san-Episode-1-Nagatoro-Wipes-More-Senpai-Tears.jpg"
        st.image(IMAGE_URL)


        st.subheader('Rikku.File Upload')
        uploaded_files = st.file_uploader("Upload File:", accept_multiple_files=True)

        btnUp = st.button('Upload')

        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            with open(f'{uploaded_file.name}', 'wb') as f: 
                f.write(bytes_data)
    
        if btnUp: 
          with st.spinner('Uploading...'):
                st.write(owo.upload_files(key, uploaded_file.name))
                st.success('File Uploaded.')
            
                
   
    except UnboundLocalError:
        st.warning('Please select a file.')
            
    
# URL Shortener
    st.subheader('Rikku.URL Shortener')
    url = st.text_input('ex. https://...', '')
    btn = st.button('Shorten')
    req = 'https://'



    try:
        if len(url) > 12:
            if btn:
                st.write(owo.shorten_urls(key, req + url))
                
        if len(url) <= 8:
            if btn:
                st.warning('Please input a URL.')
            

    except ValueError:               
        pass
    

if __name__ == '__main__':
    main()
