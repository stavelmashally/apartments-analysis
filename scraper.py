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


def extract_items():
    items = []
    for file in os.listdir(config.DATA_PATH):
        items.append(file)


def extract_info(item_list):
    pass


def scrape_apartments():
    for area, codes in config.NEIGBORHOODS.items():
        for code in codes:
            headers = config.HEADERS
            headers['User-Agent'] = random.choice(config.AGENTS)
            res = requests.get(config.URL.format(code=code), headers=headers)
            print(res.status_code)
            to_html_file(res.text, area, code)
            time.sleep(3)


if __name__ == "__main__":
    scrape_apartments()
