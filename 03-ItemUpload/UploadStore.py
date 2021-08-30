import pywinmacro as pw
import glob
from datetime import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup
import pyperclip
import telepot
import glob
import os

path = r"C:\myPackage\chromedriver.exe"
options = Options()
options.add_argument("--window-size=1024,768")
# options.add_argument("headless")


def naverLog(user, password):
    driver.get('https://sell.smartstore.naver.com/#/login')
    time.sleep(1)

    tag_id = driver.find_element_by_id('loginId')
    tag_pw = driver.find_element_by_id('loginPassword')
    tag_id.clear()

    tag_id.click()
    pyperclip.copy(user)
    tag_id.send_keys(Keys.CONTROL, 'v')

    tag_pw.click()
    pyperclip.copy(password)
    tag_pw.send_keys(Keys.CONTROL, 'v')

    login_btn = driver.find_element_by_id('loginButton')
    login_btn.click()
    print('Login')
    time.sleep(2)


def imageUpload():
    pyperclip.copy(r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage\대표이미지')

    xpath = '//*[@id="seller-content"]/ui-view/div/div[1]/div/div[1]/div[2]/div/button[1]'
    driver.get('https://sell.smartstore.naver.com/#/products/bulkadd')
    time.sleep(1)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])
    xpath = '/html/body/div/div[2]/div[4]/button[1]'
    driver.find_element_by_xpath(xpath).click()

    time.sleep(1)
    pw.alt_d()
    pw.ctrl_v()

    time.sleep(1)
    pw.key_press_once('enter')


print(datetime.now().isoformat(' ')[:16])

global driver
driver = webdriver.Chrome(
    executable_path=r"C:\myPackage\chromedriver.exe", options=options)

path = r'C:\Users\Newcrop\Desktop\SmartStore'
user = 'lmh0870@naver.com'
password = 'aydgks15!'

naverLog(user, password)
imageUpload()
driver.switch_to.window(driver.window_handles[0])
xpath = '//*[@id="seller-content"]/ui-view/div/div[1]/div/div[1]/div[2]/div/button[2]'
driver.find_element_by_xpath(xpath).click()
pyperclip.copy(r'C:\Users\Newcrop\Desktop\SmartStore\SmartStoreOutput.xlsx')


time.sleep(1)
pw.ctrl_v()
pw.key_press_once("enter")
