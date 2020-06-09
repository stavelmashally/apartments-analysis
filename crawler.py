from config import *
from csv import DictWriter
import requests
import time
import config
import random
import os
import pandas as pd
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def to_csv(data):
    # Save data to csv file
    with open(CSV_FILE, 'a+') as file:
        headers = list(data[0].keys())
        csv_writer = DictWriter(file, fieldnames=headers)
        if not os.path.getsize(CSV_FILE):
            csv_writer.writeheader()
        csv_writer.writerows(data)


def can_extract(soup):
    # Check if there is content to extract
    if not soup.find('h4', attrs={'class': 'main_title'}):
        return False
    return True


def extract_apartment_info(folder_path):
    items = [apt_id for apt_id in os.listdir(folder_path)]
    apartments = []
    for item in items:
        item_path = os.path.join(folder_path, item)
        with open(item_path, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            if can_extract(soup):
                apartment = {}
                apartment['Address'] = soup.find('h4', attrs={'class': 'main_title'}).text
                apartment['Area'] = folder_path[5:]
                apartment['Price'] = soup.find('strong', attrs={'class': 'price'}).text
                apartment['Rooms'] = soup.findAll('dd', attrs={'class': 'value'})[ROOM].text
                apartment['Floor'] = soup.findAll('dd', attrs={'class': 'value'})[FLOOR].text
                apartment['Square-meter'] = soup.findAll('dd', attrs={'class': 'value'})[SQUARE_METER].text
                apartment['Area-text'] = soup.find('span', attrs={'class': 'description'}).text
                apartment['Elevator'] = False
                apartment['Air-condition'] = False
                apartment['Refurbished'] = False
                apartment['Furniture'] = False
                features = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['info_feature'])
                for feature in features:
                    if feature.text.strip() in FEATURES.keys():
                        apartment[FEATURES[feature.text.strip()]] = True
                apartments.append(apartment)
    to_csv(apartments)


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
    for item_id in id_list[0:60]:
        url = config.ITEM_URL.format(item_id=item_id)
        print('scraping: ', url)
        # Open website
        browser.get(url)
        # Wait until page has loaded
        WebDriverWait(browser, 30)
        time.sleep(5)
        # Get the content
        html = browser.page_source
        print(html)
        to_html_file(html, item_id, config.ITEMS_PATH)
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


def get_coordinates():
    apartments = pd.read_csv(CSV_FILE)
    geolocator = Nominatim(user_agent="apartments")
    for index, apartment in apartments.iterrows():
        location = geolocator.geocode(f"תל אביב יפו {apartment['Title']}")
        if location:
            apartments.loc[index, 'lon'] = location.longitude
            apartments.loc[index, 'lat'] = location.latitude
        else:
            apartments.loc[index, 'lon'] = None
            apartments.loc[index, 'lat'] = None
    # print(apartments['lat'].head())
    apartments.to_csv(CSV_FILE)

def main():
    # scrape_apartments()
    # apt_ids = extract_apartments_ids()
    # scrape_items(apt_ids)
    # folder = NORTH_PATH
    # for folder in ALL:
    #     extract_apartment_info(folder)
    get_coordinates()


if __name__ == "__main__":
    main()
