import streamlit as st
from multiapp import MultiApp
from apps import ytmp3

app = MultiApp()
# Dev-R
st.set_page_config(
   page_title="YouTube to Mp3 by Devr-R",
   page_icon="https://cdn3.iconfinder.com/data/icons/e-commerce-35/74/money_conversion-512.png",
   layout='centered',
   initial_sidebar_state="collapsed",
   menu_items={
         'Get Help': 'https://fb.me/devric.ui',
         'Report a bug': "https://fb.me/devric.ui",
         'About': "# Created by Dev-R"
     }
)

st.image('https://owo.whats-th.is/8G7k3AX.png')
st.header('YouTube to Mp3/Mp4 Converter')

app.add_app("YT_Convert to Mp3", ytmp3.apps)

app.run()