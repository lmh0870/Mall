# import pywinmacro as pw

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def close_handles():
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
    time.sleep(2)
    close_handles()


def extrDetail():

    driver.find_element_by_xpath('//*[@id="divDriveOrderyBy"]/a').click()
    driver.find_element_by_xpath(
        '//*[@id="divDriveOrderyBy"]/div/ul/li[1]/a').click()
    time.sleep(0.3)

    driver.find_element_by_xpath('//*[@id="GalleryType"]/div[1]/label').click()
    time.sleep(0.3)

    driver.find_element_by_xpath(
        '//*[@id="divDriveBtnGroup"]/div/div/a').click()
    driver.find_element_by_xpath(
        '//*[@id="divDriveBtnGroup"]/div/div/div/ul/li[2]/a').click()
    time.sleep(0.3)

    contents = driver.find_element_by_xpath(
        '//*[@id="copyTagTextArea"]').get_attribute('value')

    xpath = '//*[@id="copiesThePath2"]/div[1]/a/img'
    driver.find_element_by_xpath(xpath).click()

    esmplus1 = 'http://gi.esmplus.com/lmhh0870/%EC%83%81%EB%8B%A8.png'
    esmplus2 = 'http://gi.esmplus.com/lmhh0870/%ED%95%98%EB%8B%A8.png'
    # <div align="center" class="shopngottl"><strong><font size="5">{productName}</font></strong></div>
    firstPage = f'<p align="center"><img class="shopngo__" src="{esmplus1}"></p>'
    lastPage = f'<p align="center"><img class="shopngo__" src="{esmplus2}"></p>'

    detailPage = f'{firstPage}<p align="center">{contents}</p>{lastPage}'
    return detailPage


def openList():
    url = 'http://im.esmplus.com/IHv2/ImgMain/ImgView'
    driver.get(url)

    xpath = '//*[@id="12502876"]/i'
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)
    xpath = '//*[@id="12502876"]/ul/li'
    folder = driver.find_elements_by_xpath(xpath)
    return folder


global driver
options = Options()
driver = webdriver.Chrome(
    executable_path=r"C:\myPackage\chromedriver.exe", options=options)
esmid = 'lmh0870'
esmpass = '8Z37^617!B3'
loginESM(esmid, esmpass)

folderDict = dict()
folder = openList()
for i in folder:
    folderDict[str(i.text.strip())] = i


path = r'C:\Users\Newcrop\Desktop\SmartStore'
df_template = pd.read_excel(f'{path}\\Setting\\ProductTemplateDone.xlsx')
productList = df_template['판매자 상품코드'].tolist()
productList = list(map(lambda x: f'{x:04}', productList))
productList = list(map(str, productList))


proNum = dict()
for i in productList:
    print(f"Check: {i}")
    folderDict[i].click()
    time.sleep(2)
    detailPage = extrDetail()
    proNum[i] = detailPage


for i in productList:
    mask = df_template[df_template['판매자 상품코드'] == int(i)].index
    df_template.loc[mask, "상품 상세정보"] = proNum[i]

df_template.to_excel(
    f'{path}\\Setting\\ProductTemplateDone.xlsx', index=False)

driver.quit()
