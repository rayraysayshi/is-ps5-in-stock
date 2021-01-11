import pandas as pd
import time; import datetime;from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = 'https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815'

while True:
    driver.get(url);
    time.sleep(2)
    priceSection = driver.find_elements_by_xpath('.//section[@class="prod-PriceSection"]')[0]
    if priceSection.text.find('Out of stock') > 0:
        print(datetime.datetime.now()); print('no change')
    else:
        print(datetime.datetime.now());
        print('_________website updated!_____________');
        # place a script to send email or play sound here
    time.sleep(18)
