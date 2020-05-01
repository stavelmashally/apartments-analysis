import requests
import time
import config
import random
import os
from bs4 import BeautifulSoup


def to_html_file(html, area, code):
    filename = f'{area}{code}.html'
    with open(os.path.join(config.DATA_PATH, filename), 'w') as file:
        file.write(html)


def generate_headers():
    headers = config.HEADERS
    headers['User-Agent'] = random.choice(config.AGENTS)
    return headers


def extract_info(id_list):
    for item_id in id_list[:1]:
        url = config.ITEM_URL.format(item_id=item_id)
        res = requests.get(url, headers=generate_headers())
        # to_html_file(res.text, 'item', item_id)
        soup = BeautifulSoup(res.text, 'html.parser')
        print(soup.prettify())
        time.sleep(3)


def extract_apartments_ids():
    apt_ids = []
    for file in os.listdir(config.DATA_PATH):
        with open(os.path.join(config.DATA_PATH, file), 'r') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            for apt in soup.findAll(attrs={'class': 'feed_item_table_map'}):
                apt_ids.append(apt['item-id'])
    return apt_ids


def scrape_apartments():
    for area, codes in config.NEIGBORHOODS.items():
        for code in codes:
            url = config.URL.format(area_code=code)
            res = requests.get(url, headers=generate_headers())
            print(res.status_code)
            to_html_file(res.text, area, code)
            time.sleep(3)


if __name__ == "__main__":
    # scrape_apartments()
    apt_ids = extract_apartments_ids()
    extract_info(apt_ids)
