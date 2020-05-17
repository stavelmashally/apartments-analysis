from bs4 import BeautifulSoup
import os
import requests
import time
import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui

PARTNER = 'לשותפים'
ELEVATORS = 'מעלית'
LONG_TERM = 'לטווח ארוך'
AIR_CONDITIONING = 'מיזוג'
REFURBISHED = 'משופצת'
FURNITURE = 'ריהוט'


def get_script(soup_scripts_list):
    for item in soup_scripts_list:
        if item.string is not None:
            if item.string.startswith('window.__NUXT__'):
                return item


class Apartment:
    def __init__(self, file_apartment):
        self.Possibilities = {PARTNER: False, ELEVATORS: False, LONG_TERM: False, AIR_CONDITIONING: False,
                              REFURBISHED: False, FURNITURE: False}
        # use_sel(file_apartment)
        # apartment = BeautifulSoup(file_apartment.read(), 'html.parser')
        # s = get_script(apartment.findAll('script'))
        # self.name = apartment.find({'class': 'main_title'})
        print("sara")
