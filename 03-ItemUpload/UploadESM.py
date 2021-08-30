import pywinmacro as pw

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import pyperclip
import glob

path = r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage\Translation'
productNumber = []
for i in glob.glob(f"{path}\\????"):
    productNumber.append(i[-4:])

productNumber = list(set(productNumber))


def close_handles(driver):
    global main_handle

    handles = driver.window_handles
    size = len(handles)

    main_handle = driver.current_window_handle
    for x in range(size):
        if handles[x] != main_handle:
            driver.switch_to.window(handles[x])
            driver.close()

    driver.switch_to.window(main_handle)

    driver.switch_to.frame(0)


def loginESM(esmid, esmpass):
    url = 'https://www.esmplus.com/Member/SignIn/LogOn'
    driver.get(url)

    driver.find_element_by_xpath('//*[@id="Id"]').send_keys(esmid)
    driver.find_element_by_xpath('//*[@id="Password"]').send_keys(esmpass)

    driver.find_element_by_xpath('//*[@id="btnLogOn"]').send_keys(Keys.RETURN)

    time.sleep(1)
    close_handles(driver)


def uploadESM():
    url = 'http://im.esmplus.com/IHv2/ImgMain/ImgView'
    driver.get(url)

    pyperclip.copy(
        r"C:\Users\Newcrop\Desktop\SmartStore\ProductImage\Translation")

    xpath = '//*[@id="fileUploadButton"]/span'
    driver.find_element_by_xpath(xpath).click()
    xpath = '//*[@id="folderUploadButton"]'
    driver.find_element_by_xpath(xpath).click()

    pw.alt_tab()

    time.sleep(1)
    pw.alt_d()
    pw.ctrl_v()

    time.sleep(1)
    pw.key_press_once('enter')
    pw.key_press_once('enter')


global driver
options = Options()
driver = webdriver.Chrome(
    executable_path=r"C:\myPackage\chromedriver.exe", options=options)
esmid = 'lmh0870'
esmpass = '8Z37^617!B3'

loginESM(esmid, esmpass)
time.sleep(2)
uploadESM()
