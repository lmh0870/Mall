import pandas as pd
import glob
import os
import papagoApi
path = r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage\Step-1'


df = pd.DataFrame(columns=['Number', 'OptionNumber', 'Option'])
for i in glob.glob(f'{path}\\????\\????-옵션-*'):
    _, fname = os.path.split(i)
    print(fname)
    splitName = fname.split('-')
    print(splitName)

    df1 = pd.DataFrame({
        'Number': splitName[0],
        'OptionNumber': splitName[2],
        'Option': papagoApi.papagoTrans(splitName[3][:-4])}, index=[0])
    df = df.append(df1, ignore_index=True)


print(df)
df.to_excel(r'C:\Users\Newcrop\Desktop\SmartStore\Option.xlsx', index=False)
