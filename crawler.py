import os
import requests
import time
import config
from Apartment import Apartment


def crawler_apartments():
    apartments = []
    f_path = os.path.join(config.NORTH_PATH, 'tb2y4n.html')
    apartments.append(Apartment(f_path))
    # with open(f_name, 'r', encoding="utf8") as file_apartment:
    #     apartments.append(Apartment(file_apartment))

    #
    # for file_name in os.listdir(config.NORTH_PATH)[:1]:
    #     with open(os.path.join(config.NORTH_PATH, file_name), 'r', encoding="utf8") as file_apartment:
    #         apartments.append(Apartment(file_apartment))
