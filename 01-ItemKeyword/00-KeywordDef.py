import pandas as pd
import numpy as np
from datetime import *
import time
import glob
import os
from selenium.webdriver.common.keys import Keys


def itemLogin(driver):
    driver.get('https://itemscout.io/login')

    xpath = '//*[@id="input-38"]'
    driver.find_element_by_xpath(xpath).send_keys('lmh0870@naver.com')
    xpath = '//*[@id="input-40"]'
    driver.find_element_by_xpath(xpath).send_keys('aydgks15!')

    xpath = '//*[@id="app"]/div/main/div/div/div/div/button[2]'
    driver.find_element_by_xpath(xpath).send_keys(Keys.RETURN)
    print('Login: Done')
    time.sleep(2)


def itemDown(urls, driver):
    print('Download:')
    for i, url in enumerate(urls):
        driver.get(url)
        time.sleep(2)
        if i == 0:
            time.sleep(3)
            xpath = '//*[@id="app"]/div/main/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div'
            driver.find_element_by_xpath(xpath).click()  # 중소형 키워드
            filters = driver.find_elements_by_class_name('filters-container')
            for fil in filters:
                # print(fil.text)
                if fil.text == '새 필터 2':
                    fil.click()
                    print('\tFilter: True')
                    time.sleep(2)
                else:
                    print('\tFilter: False')
        # Excel Download
        xpath = '//*[@id="app"]/div/main/div/div/div/div[2]/div[2]/div[1]/div/button'
        driver.find_element_by_xpath(xpath).click()
