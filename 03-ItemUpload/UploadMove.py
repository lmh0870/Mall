import shutil
import os
import glob

imagePath = r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage\Step-5\대표이미지'
path = r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage'


for i in glob.glob(f'{path}\\Step-4\\*\\*-대표이미지-*'):
    # print(i)
    folder, fname = os.path.split(i)
    # print(folder)
    # print(fname)

    newName = f'{imagePath}\\{fname}'
    os.rename(i, newName)

for i in glob.glob(f'{path}\\Step-4\\*'):
    # print(i)
    folder, fname = os.path.split(i)
    # print(fname)
    print(f'{folder[:-7]}\\Step-5\\{fname}')
    newFolder = f'{folder[:-7]}\\Step-5\\{fname}'
    shutil.copytree(i, newFolder)
