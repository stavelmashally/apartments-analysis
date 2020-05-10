import requests
import time
import config
import random
import os
from bs4 import BeautifulSoup


def to_html_file(html, filename, path):
    filename = f'{filename}.html'
    path = os.path.join(path, filename)
    with open(path, 'w', encoding="utf8") as file:
        file.write(html)


def generate_headers():
    headers = config.HEADERS
    headers['User-Agent'] = random.choice(config.AGENTS)
    return headers


# Last call was: [0:0]
def extract_info(id_list):
    for item_id in id_list[0:0]:
        url = config.ITEM_URL.format(item_id=item_id)
        res = requests.get(url, headers=generate_headers())
        to_html_file(res.text, item_id, config.ITEMS_PATH)
        soup = BeautifulSoup(res.text, 'html.parser')
        print(soup.prettify())
        time.sleep(3)


def extract_apartments_ids():
    apt_ids = []
    for file_name in os.listdir(config.SEARCH_RESULTS_PATH):
        with open(os.path.join(config.SEARCH_RESULTS_PATH, file_name), 'r', encoding="utf8") as file:
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
            filename = f'{area}{code}'
            to_html_file(res.text, filename, config.SEARCH_RESULTS_PATH)
            time.sleep(3)


if __name__ == "__main__":
    # scrape_apartments()
    apt_ids = extract_apartments_ids()
    extract_info(apt_ids)
