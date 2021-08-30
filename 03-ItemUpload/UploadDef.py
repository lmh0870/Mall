import numpy as np
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import *
import requests


def papagoTrans(text):
    client_id = "dpJZuWckxaLKQM558tDJ"  # <-- client_id 기입
    client_secret = "Ba9ZeVukmN"  # <-- client_secret 기입

    data = {'text': text,
            'source': 'zh-CN',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode == 200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        #         print("Error Code:" , rescode)
        return text


# Product Name


def prodName():
    xpaths = ['//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1',
              '//*[@id="J_Title"]/h3']
    for xpath in xpaths:
        elem = driver.find_elements_by_xpath(xpath)
        if len(elem) != 0:
            break

    Title = elem[0].text
    originalTitle = Title
    Title = papagoTrans(Title)
    print(f'Title: {Title}')
    return originalTitle, Title

# Option


def prodOption():
    xpaths = ['//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li',
              '//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li/a/span',
              '//*[@id="J_isku"]/div/dl[1]/dd/ul/li/a/span']
    for xpath in xpaths:
        Option = driver.find_elements_by_xpath(xpath)
        if len(Option) != 0:
            break

    optionList = []
    for i in Option:
        optionList.append(i.text.strip())

    Option = ",".join(optionList)
    Option = papagoTrans(Option)
    optionLength = len(optionList)

    print(f'Option: {Option}\nOptionLength: {optionLength}')
    return Option, optionLength

# Parameter


def prodPara():
    detail = {}
    xpaths = ['//*[@id="J_AttrList"]',
              '//*[@id="attributes"]/ul']
    for xpath in xpaths:
        elem = driver.find_elements_by_xpath(xpath)
        if len(elem) != 0:
            break

    AttrList = elem[0].text

    for para in AttrList.split('\n'):
        if '品牌名称：' in para:
            para = para.replace('品牌名称：', "")
            para = papagoTrans(para)
            detail["Brand"] = para
        elif '品牌: ' in para:
            para = para.replace('品牌: ', "")
            para = papagoTrans(para)
            detail["Brand"] = para
        elif '型号: ' in para:
            para = para.replace('型号: ', "")
            para = papagoTrans(para)
            detail["Model"] = para
        elif '安装方式: ' in para:
            para = para.replace('安装方式: ', "")
            para = papagoTrans(para)
            detail["Installation"] = para
        elif '颜色分类: ' in para:
            para = para.replace('颜色分类: ', "")
            para = papagoTrans(para)
            detail["Color"] = para
        elif '适用部位: ' in para:
            para = para.replace('适用部位: ', "")
            para = papagoTrans(para)
            detail["Applicable"] = para

    print(f'Detail: {detail}')
    return detail

# Papago


def papagoTrans(text):
    client_id = "dpJZuWckxaLKQM558tDJ"  # <-- client_id 기입
    client_secret = "Ba9ZeVukmN"  # <-- client_secret 기입

    data = {'text': text,
            'source': 'zh-CN',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode == 200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        #         print("Error Code:" , rescode)
        return text


global driver
path = r"C:\myPackage\chromedriver.exe"
options = Options()
driver = webdriver.Chrome(
    executable_path=path, options=options)
# options.add_argument("--window-size=1024,768")

filePath = r'C:\Users\Newcrop\Desktop\SmartStore\Setting'
df = pd.read_excel(f'{filePath}\\SelectedItem.xlsx')
df.Category = df.Category.astype(str)
df.Title = df.Title.astype(str)
df.OriginalTitle = df.OriginalTitle.astype(str)
df.Option = df.Option.astype(str)
df.Brand = df.Brand.astype(str)
df.Model = df.Model.astype(str)
for i in df[pd.isnull(df['Number'])].index:
    maxNumber = max(df.Number) + 1
    df.Number.values[i] = maxNumber
    url = df.URL.values[i]
    print(f'Number: {maxNumber}')
    print(f'URL: {url}')

    driver.get(url)
   # Crawling
    originalTitle, Title = prodName()
    df.Title.values[i] = Title
    df.OriginalTitle.values[i] = originalTitle

    Option, optionLength = prodOption()
    df.Option.values[i] = Option
    df.OptionLength.values[i] = optionLength

    para = prodPara()
    try:
        df.Brand.values[i] = para["Brand"]
    except:
        pass
    try:
        df.Model.values[i] = para["Model"]
    except:
        pass

df.to_excel(f'{filePath}\\Sample.xlsx', index=False)
driver.quit()
