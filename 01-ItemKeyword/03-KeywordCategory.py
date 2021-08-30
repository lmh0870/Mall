import re
import numpy as np
import pandas as pd
import item


pathSmart = r'C:\Users\Newcrop\Desktop\SmartStore'


def reLetter(string):
    return re.sub(r"[^\w]", "", string)


dfCategory = pd.read_excel(f'{pathSmart}\\Setting\\Category.xlsx')[
    ['카테고리코드', '대표 카테고리', '세부카테고리']]
dfCategory['대표 카테고리'] = dfCategory['대표 카테고리'].apply(reLetter)
dfCategory['세부카테고리'] = dfCategory['세부카테고리'].apply(reLetter)
dfBefore = pd.read_excel(f'{pathSmart}\\00-ItemSelect\\00-ItemKeyword.xlsx')

pathDown = r'C:\Users\Newcrop\Downloads'
dfKeyword = pd.read_excel(f'{pathDown}\\ItemKeyword.xlsx')
dfKeyword['Check'] = 2
dfKeyword['세부카테고리'] = np.nan
dfKeyword['카테고리코드'] = np.nan
dfKeyword['해외상품비율'] = np.nan
dfKeyword['키워드Split'] = dfKeyword['키워드']
dfKeyword = dfKeyword[['상세정보 확인', '세부카테고리',
                       'Check', '키워드', '키워드Split', '대표 카테고리', '카테고리코드', '해외상품비율']]
dfKeyword = dfKeyword.append(dfBefore, ignore_index=True)
dfKeyword = dfKeyword.drop_duplicates(['키워드'], keep='last')
dfKeyword['대표 카테고리'] = dfKeyword['대표 카테고리'].apply(reLetter)
for i in dfKeyword['대표 카테고리'].unique():
    # print(i)
    mask = dfCategory[dfCategory['대표 카테고리'] == i].index
    if len(mask) == 1:
        mask = dfCategory.loc[mask, ['세부카테고리', '카테고리코드']]
        deta = mask.values[0][0]
        cate = mask.values[0][1]
        # print(deta, cate)

    mask = dfKeyword[dfKeyword['대표 카테고리'] == i].index
    dfKeyword.loc[mask, '세부카테고리'] = deta
    dfKeyword.loc[mask, '카테고리코드'] = cate
dfKeyword = dfKeyword.sort_values('Check', ascending=False)
# dfKeyword.to_excel(r'C:\Users\Newcrop\Desktop\sample.xlsx', index=False)


key = []
val = []
dfKeyword_2 = dfKeyword[dfKeyword['Check'] == 1]
for i in dfKeyword_2['카테고리코드'].dropna().unique():
    # print(i)
    df = dfKeyword_2[dfKeyword_2['카테고리코드'] == i]
    df = df['키워드Split']
    df = df.tolist()
    df = list(set(" ".join(df).split(" ")))
    joinKeyword = " ".join(df)

    key.append(int(i))
    val.append(joinKeyword)

keyword = {'카테고리코드': key,
           '키워드분리': val}
keyword = pd.DataFrame(keyword)
keyword['세부카테고리'] = np.nan
for i in keyword['카테고리코드']:
    print(i)
    mask = dfCategory[dfCategory['카테고리코드'] == i].index
    deta = dfCategory.loc[mask, '세부카테고리'].values[0]

    mask = keyword[keyword['카테고리코드'] == i].index
    keyword.loc[mask, '세부카테고리'] = deta

keyword = keyword[['카테고리코드', '세부카테고리', '키워드분리']]
with pd.ExcelWriter(f'{pathSmart}\\00-ItemSelect\\00-ItemKeyword.xlsx') as writer:
    dfKeyword.to_excel(writer, sheet_name='Step1', index=False)
    keyword.to_excel(writer, sheet_name='Step2', index=False)
