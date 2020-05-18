import os
from config import *
from bs4 import BeautifulSoup
from csv import DictWriter


def to_csv(data):
    # Save data to csv file
    with open(f'apartments.csv', 'w') as file:
        headers = list(data[0].keys())
        csv_writer = DictWriter(file, fieldnames=headers)
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
        with open(item_path, 'r') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            if can_extract(soup):
                apartment = {}
                apartment['title'] = soup.find('h4', attrs={'class': 'main_title'}).text
                apartment['area'] = folder_path[5:]
                apartment['price'] = soup.find('strong', attrs={'class': 'price'}).text
                apartment['rooms'] = soup.findAll('dd', attrs={'class': 'value'})[ROOM].text
                apartment['floor'] = soup.findAll('dd', attrs={'class': 'value'})[FLOOR].text
                apartment['square-meter'] = soup.findAll('dd', attrs={'class': 'value'})[SQUARE_METER].text
                apartment['elevator'] = False
                apartment['air-condition'] = False
                apartment['refurbished'] = False
                apartment['furniture'] = False
                features = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['info_feature'])
                for feature in features:
                    if feature.text.strip() in FEATURES.keys():
                        apartment[FEATURES[feature.text.strip()]] = True
                apartments.append(apartment)
    to_csv(apartments)


def main():
    folder = SOUTH_PATH
    extract_apartment_info(folder)


if __name__ == "__main__":
    main()