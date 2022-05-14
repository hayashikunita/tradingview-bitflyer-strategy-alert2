import configparser

# from utils.utils import bool_from_str


conf = configparser.ConfigParser()
conf.read('settings.ini')

apiKey = conf['bitflyer']['apiKey']
secret = conf['bitflyer']['secret']
product_code = conf['bitflyer']['product_code']
symbol = conf['bitflyer']['symbol']