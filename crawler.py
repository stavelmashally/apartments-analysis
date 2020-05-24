import os
from config import *
from bs4 import BeautifulSoup
from csv import DictWriter


def to_csv(data):
    # Save data to csv file
    with open(f'apartments.csv', 'a+') as file:
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
        with open(item_path, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            if can_extract(soup):
                apartment = {}
                apartment['Title'] = soup.find('h4', attrs={'class': 'main_title'}).text
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


def main():
    # folder = NORTH_PATH
    for folder in ALL:
        folder = os.path.join(os.getcwd(), folder)
        extract_apartment_info(folder)


if __name__ == "__main__":
    main()