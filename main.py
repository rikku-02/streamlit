from requests import get
import streamlit as st

ip = get('https://api.ipify.org').text
st.write('My public IP address is: {}'.format(ip))