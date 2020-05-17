import requests
import time
import config
import random
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep

from crawler import crawler_apartments

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def to_html_file(html, filename, out_path):
    filename = f'{filename}.html'
    out_path = os.path.join(out_path, filename)
    with open(out_path, 'w', encoding="utf8") as html_file:
        html_file.write(html)


def generate_headers():
    headers = config.HEADERS
    headers['User-Agent'] = random.choice(config.AGENTS)
    return headers


# Last call was: [0]
def extract_info(id_list):
    for item_id in id_list[5:10]:
        url = config.ITEM_URL.format(item_id=item_id)
        filename = f'{item_id}.html'
        out_path = os.path.join(config.SOUT_EAST_PATH, filename)
        print("saving ", item_id, " to: ", out_path)
        save_html_using_selenium(url, out_path, driver)
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
            os.path.join(config.NORTH_PATH, 'tb2y4n.html')
            to_html_file(res.text, filename, config.SEARCH_RESULTS_PATH)
            time.sleep(3)


def save_html_using_selenium(url, app_file_path, sel_driver):
    sel_driver.get(url)
    sleep(5)
    with open(app_file_path, 'w', encoding='utf-8') as f:
        f.write(sel_driver.page_source)


def test_files():
    for file_name in os.listdir(config.SOUT_EAST_PATH):
        n = os.path.abspath(os.path.join(config.SOUT_EAST_PATH, file_name))
        with open(n, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            title = soup.find(attrs={'class': 'main_title'}).text
            print("title is: ", title)


if __name__ == "__main__":
    #scrape_apartments()
    apt_ids = extract_apartments_ids()
    extract_info(apt_ids)
    crawler_apartments()
    test_files()
