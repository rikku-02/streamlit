import streamlit as st
from bs4 import BeautifulSoup
from lxml import etree
import requests


def color_by_hex():
    hex_code = input('Hex Code: ')

    url = f'https://www.color-name.com/hex/{hex_code}'
    color_url = f'https://www.color-name.com/color-image?c={hex_code}&square&tx'
    request_result = requests.get(url)

    soup = BeautifulSoup(request_result.text, "html.parser")

    dom = etree.HTML(str(soup))
    print(dom.xpath('/html/body/section/div[1]/div/div/div[1]/div/h1')[0].text)
    print(dom.xpath('/html/body/section/div[1]/div/div/div[1]/div/h4')[0].text)
    print(dom.xpath('/html/body/section/section[1]/div/h2')[0].text)
    header = soup.findAll("div", {"class": "color-bio"})

    for div in header:
        name = div.find('p').text
        print(name)


def streamlit_code():
    try:
        st.title('Hex Color Indetifier - りく')
        hex_code = st.text_input('Hex Code: ')
        hash_code = '#'

        identify = st.button('Identify')

        if identify:

            if hash_code in hex_code:
                hex_c = hex_code.replace(hash_code, '')

                url = f'https://www.color-name.com/hex/{hex_c}'
                request_result = requests.get(url)
                soup = BeautifulSoup(request_result.text, "html.parser")
                dom = etree.HTML(str(soup))
                header = soup.findAll("div", {"class": "color-bio"})
                color_url = f'https://www.color-name.com/color-image?c={hex_c}&square&tx'

                st.title(dom.xpath('/html/body/section/div[1]/div/div/div[1]/div/h1')[0].text)
                st.subheader(dom.xpath('/html/body/section/div[1]/div/div/div[1]/div/h4')[0].text)
                st.image(color_url, width=80)
                for div in header:
                    description = div.find('p').text
                    st.markdown(description)

            elif hash_code not in hex_code:
                url = f'https://www.color-name.com/hex/{hex_code}'
                request_result = requests.get(url)
                soup = BeautifulSoup(request_result.text, "html.parser")
                dom = etree.HTML(str(soup))
                header = soup.findAll("div", {"class": "color-bio"})
                color_url = f'https://www.color-name.com/color-image?c={hex_code}&square&tx'

                st.title(dom.xpath('/html/body/section/div[1]/div/div/div[1]/div/h1')[0].text)
                st.subheader(dom.xpath('/html/body/section/div[1]/div/div/div[1]/div/h4')[0].text)
                st.image(color_url, width=80)
                for div in header:
                    description = div.find('p').text
                    st.markdown(description)

    except IndexError:
        pass


if __name__ == '__main__':
    # color_by_hex()
    streamlit_code()
