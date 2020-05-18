import requests
import urllib3
import certifi
import gzip
import time
import config
import random
import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def to_html_file(html, filename, path):
    filename = f'{filename}.html'
    path = os.path.join(path, filename)
    with open(path, 'w', encoding="utf8") as file:
        file.write(html)


def generate_headers():
    headers = config.HEADERS
    headers['User-Agent'] = random.choice(config.AGENTS)
    return headers


def initialize_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    return browser


# Last call was: [65:80]
def scrape_items(id_list):
    browser = initialize_selenium()
    for item_id in id_list[0:100]:
        url = config.ITEM_URL.format(item_id=item_id)
        print('scraping ', url)
        browser.get(url)
        wait = WebDriverWait(browser, 30)
        time.sleep(5)
        html = browser.page_source
        print(html)
        to_html_file(html, item_id, config.ITEMS_PATH)
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
    browser.close()


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
            filename = f'{area}{code}'
            to_html_file(res.text, filename, config.SEARCH_RESULTS_PATH)
            time.sleep(3)


if __name__ == "__main__":
    # scrape_apartments()
    apt_ids = extract_apartments_ids()
    scrape_items(apt_ids)