import os
import glob
import pandas as pd

path = r'C:\Users\Newcrop\Downloads'
dfList = []
for i in glob.glob(f'{path}\\itemscout_io_*'):
    dfList.append(i)
for i, dfPath in enumerate(dfList):
    if i == 0:
        df = pd.read_excel(dfPath)
        newDf = df
    else:
        df = pd.read_excel(dfPath)

    print(len(df))
    os.unlink(dfPath)
    newDf = newDf.append(df, ignore_index=True)

newDf.to_excel(f'{path}\\ItemKeyword.xlsx', index=False)
