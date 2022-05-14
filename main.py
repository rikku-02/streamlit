import streamlit as st
import owo
import random

def main():
  # File Uploader
  key = st.secrets['API_KEY']

  st.header('Rikku.File Upload and Url Shortener')
  link1 = 'https://owo.whats-th.is/ACLxPmx.png'
  link2 = 'https://owo.whats-th.is/q467i7A.jpg'
  link3 = 'https://owo.whats-th.is/5FwveEs.jpg'
  link4 = 'https://owo.whats-th.is/5NvMyWE.png'
  IMAGE_URL = random.choice([link1, link2, link3, link4])
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
