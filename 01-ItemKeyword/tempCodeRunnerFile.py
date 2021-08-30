import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
# options.add_argument("headless")

driver = webdriver.Chrome(
    executable_path=r"C:\myPackage\chromedriver.exe", options=options)


urlList = []

urls = ['https://itemscout.io/category?c=4',
        'https://itemscout.io/category?c=9']
for url in urls:
    driver.get(url)
    time.sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="app"]/div/main/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]').click()
    boxList2 = driver.find_elements_by_xpath(
        '//*[@id="app"]/div[2]/div/div/div')
    print(f'Box2: {len(boxList2)}')
    try:
        for i in range(len(boxList2)):
            if i == 0:
                time.sleep(1)
                print(f'\t{boxList2[0].text}')
                boxList2[0].click()
            else:
                time.sleep(1)
                driver.find_element_by_xpath(
                    '//*[@id="app"]/div/main/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]').click()
                time.sleep(1)
                boxList2 = driver.find_elements_by_xpath(
                    '//*[@id="app"]/div[2]/div/div/div')
                print(f'\t{boxList2[i+1].text}')
                boxList2[i+1].click()
                time.sleep(1)