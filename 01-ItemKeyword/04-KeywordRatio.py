import numpy as np
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

path = r'C:\Users\Newcrop\Desktop\SmartStore\00-ItemSelect'
dfStep1 = pd.read_excel(f'{path}\\00-ItemKeyword.xlsx', sheet_name='Step1')
dfStep2 = pd.read_excel(f'{path}\\00-ItemKeyword.xlsx', sheet_name='Step2')
options = Options()
# options.add_argument("--window-size=1024,768")
options.add_argument("headless")
driver = webdriver.Chrome(
    executable_path=r"C:\myPackage\chromedriver.exe", options=options)

for i in dfStep1[dfStep1['Check'] == 2].itertuples():
    if pd.isnull(i.해외상품비율) != True:
        print("\tPass")
        continue

    driver.get(i._1)
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="app"]/div/main/div/div/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div'))
        )
        value1 = element.text.strip()
        mask = dfStep1[dfStep1['상세정보 확인'] == i._1].index
        dfStep1.loc[mask, '해외상품비율'] = value1
        print(f'Add: {value1} {mask}')

    except:
        pass

driver.quit()

with pd.ExcelWriter(f'{path}\\00-ItemKeyword.xlsx') as writer:
    dfStep1.to_excel(writer, sheet_name='Step1', index=False)
    dfStep2.to_excel(writer, sheet_name='Step2', index=False)
print('Done')
