import os


AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}

SEARCH_RESULTS_PATH = os.path.join('data', 'search-results')
ITEMS_PATH = os.path.join('data', 'items')
SOUTH_PATH = os.path.join('data', 'south')
NORTH_PATH = os.path.join('data', 'north')
CENTER_LEV_TLV_PATH = os.path.join('data', 'center-lev-tlv')
CENTER_EAST_PATH = os.path.join('data', 'center-east')
CENTER_KEREM_PATH = os.path.join('data', 'center-kerem')
ALL = [SOUTH_PATH, NORTH_PATH, CENTER_EAST_PATH, CENTER_LEV_TLV_PATH, CENTER_KEREM_PATH]

ROOM = 0
FLOOR = 1
SQUARE_METER = 2

ELEVATOR = 'מעלית'
AIR_CONDITION = 'מיזוג'
REFURBISHED = 'משופצת'
FURNITURE = 'ריהוט'

FEATURES = {ELEVATOR: 'Elevator',
            AIR_CONDITION: 'Air-condition',
            REFURBISHED: 'Refurbished',
            FURNITURE: 'Furniture'}


URL = 'https://www.yad2.co.il/realestate/rent/map?city=5000&neighborhood={area_code}'
ITEM_URL = 'https://www.yad2.co.il/item/{item_id}'
CSV_FILE = 'apartments.csv'


NEIGBORHOODS = {
    'tzahala': [1513],
    #'north': [ 1461]#204, 1516, 1519, 1483,
    # 'centerLevTlv': [1520, 848],
    # 'centerKerem': [1521],
    #'centerEast': [485, 486, 206, 317, 318],
    # 'soutWest': [4958, 3078, 2158, 2058, 8478, 4908, 2128],
    # 'soutEast': [487, 1649, 2078, 2098, 3088, 2088, 1650, 4898, 4888, 3198, 2108],
    # 'south' : [205, 307, 308, 212, 215]
}