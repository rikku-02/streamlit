import streamlit as st
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json


def search():
    st.title('Pre-Activated Applications [Scraper]')
    text = st.text_input('Search:')
    page = st.number_input('Page: ', value=1)
    dl_link = st.text_input('Download Link: ')

    try:
        with st.spinner('Loading'):
            # BeautifulSoup

            url = f'https://filecr.com/?page={page}&s=' + text + '&subcat_filter=&category-type=2'
            request_result = requests.get(url)
            soup = BeautifulSoup(request_result.text,
                                 "html.parser")

            header = soup.findAll("div", {"class": "product"}, {'class': 'product-icon'})

            col1, mid, col2 = st.columns([20, 1, 10])

            with col1:
                for div in header:
                    icon = div.find('img')['src']
                    title = div.find('img')['alt']
                    desc = div.find('p', {'class': 'product-desc'})
                    link = div.find('a')['href']
                    # size = dom.xpath('/html/body/div[2]/div[2]/main/section/div[2]/div[10]/div[4]')[0].text




                    # API
                    st.image(icon, width=80)
                    st.subheader(title)

                    dl = st.button(f'Scrape [{title}]')

                    if dl:
                        request_size = requests.get(link)
                        soup_size = BeautifulSoup(request_size.text,
                                                  "html.parser")

                        dom_size = etree.HTML(str(soup_size))

                        size = dom_size.xpath('/html/body/div[2]/div[2]/aside/div[2]/div[1]/text()')[0]
                        byte_i = dom_size.xpath('/html/body/div[2]/div[2]/aside/div[2]/div[1]/span')[0].text
                        data = {'Product': []}
                        data['Product'].append({
                            'Title': title,
                            'Icon': icon,
                            'Download-Link': str(dl_link),
                            'Description': desc.getText(),
                            'File-Size': f'{size} {byte_i}'
                        })

                        with open('data.json', 'w+') as outfile:
                            json.dump(data, outfile, indent=4)
                            st.success('Done!')

                        with open('data.json', 'rb') as jf:
                            json_file = jf.read()
                            st.download_button(
                                label="Download Data",
                                data=json_file,
                                file_name='data.json',
                                mime='application/JSON',
                            )

    except SystemError:
        pass

    else:
        if text == '':
            pass


if __name__ == '__main__':
    search()
