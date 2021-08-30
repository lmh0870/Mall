import os
import glob
import shutil
import pandas as pd

downPath = r'C:\Users\Newcrop\Downloads'
detailImage = glob.glob(f'{downPath}\\*\\详情-*')
folder = []
for i in detailImage:
    folder.append(i.split('\\')[-2])
folder = list(set(folder))

smartPath = r'C:\Users\Newcrop\Desktop\SmartStore'
df = pd.read_excel(f'{smartPath}\\02-ItemPricing.xlsx')
number = df['Number'].max() + 1
for i in folder:
    print(f'{downPath}\\{i}')

    shutil.copytree(f'{downPath}\\{i}',
                    f'{smartPath}\\ProductImage\\Original\\{number:04}')
    shutil.rmtree(f'{downPath}\\{i}')
    number += 1


path = r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage\Original'
option = glob.glob(f'{path}\\*\\SKU-*')
detailImage = glob.glob(f'{path}\\*\\*详情-*')
firstImage = glob.glob(f'{path}\\*\\*主图-*')

for i in option:
    folder, fname = os.path.split(i)
    number = folder[-4:]

    rname = f'{number}-{fname.replace("SKU", "옵션")}'
    # print(number)
    # print(f'{folder}\\{rname}')
    os.rename(i, f'{folder}\\{rname}')


for i in detailImage:
    folder, fname = os.path.split(i)
    number = folder[-4:]

    rname = f'{number}-{fname.replace("详情", "상세페이지")}'
    print(number)
    print(f'{folder}\\{rname}')
    os.rename(i, f'{folder}\\{rname}')

for i in firstImage:
    folder, fname = os.path.split(i)
    number = folder[-4:]

    rname = f'{number}-{fname.replace("主图", "대표이미지")}'
    # print(number)
    # print(f'{folder}\\{rname}')
    os.rename(i, f'{folder}\\{rname}')


folder = glob.glob(f'{path}/????')
folder = list(map(lambda x: x.split("\\")[-1], folder))
for i in glob.glob(f'{path}\\*\\*'):
    _, fname = os.path.split(i)
    print(fname[:4])

    if fname[:4] not in folder:
        print("True")
        print(i)
        os.unlink(i)
