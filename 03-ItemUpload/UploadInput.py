import numpy as np
import pandas as pd
import glob

path = r'C:\Users\Newcrop\Desktop\SmartStore'
df_01 = pd.read_excel(f'{path}\\00-ItemSelect\\01-ItemSelect.xlsx')
df_02 = pd.read_excel(f'{path}\\01-ItemEdit\\02-ItemPricing.xlsx')
df_03 = pd.read_excel(f'{path}\\01-ItemEdit\\03-ItemNaming.xlsx')
df_temp = pd.read_excel(f'{path}\\Setting\\ProductTemplate.xlsx')

imageList = glob.glob(
    r'C:\Users\Newcrop\Desktop\SmartStore\ProductImage\Step-5\대표이미지\*')
imageList = list(map(lambda x: x.split('\\')[-1], imageList))

for r in df_03.itertuples():
    priceList = df_02[df_02['Number'] == r.Number]['판매가'].tolist()
    priceLength = len(priceList)
    if priceLength > 1:
        optionStock = ",".join(["1000" for i in range(priceLength)])
    else:
        optionStock = np.NaN
    priceBasic = priceList[0]  # priceBasic
    priceList = list(map(lambda x: x - priceBasic, priceList))
    priceList = list(map(str, priceList))
    priceList = ",".join(priceList)
    print(f'Number: {r.Number}')
    print(f'\tOption: {r.Option}')
    print(f'\tStock: {optionStock}')
    print(f'\tOptionLength: {priceLength}')
    print(f'\tPrice: {priceBasic}')

    Category = df_01[df_01['Number'] == r.Number]['Category'].values[0]
    Brand = df_01[df_01['Number'] == r.Number]['Brand'].values[0]
    Model = df_01[df_01['Number'] == r.Number]['Model'].values[0]
    print(f'\tCategory: {Category}')
    print(f'\tBrand: {Brand}')
    print(f'\tModel: {Model}')

    ProductName = df_03[df_03['Number'] == r.Number]['Keyword'].values[0]
    ProductNamePlus = df_03[df_03['Number'] == r.Number]['Name'].values[0]
    print(f'\tName: {ProductName}')
    print(f'\tNamePlus: {ProductNamePlus}')

    imageNumber = [i for i in imageList if i.split('-')[0] == f'{r.Number:04}']
    imageFirst = imageNumber[0]
    imageOther = imageNumber[1:]
    if len(imageOther) != 0:
        imageOther = ",".join(imageOther)
    else:
        imageOther = np.NaN
    print(f'\timageFirst: {imageFirst}')
    print(f'\timageOther: {imageOther}\n')

    inputValue = {
        '톡톡친구/스토어찜고객 리뷰 작성시 지급 포인트': 500,

        '카테고리ID': Category,
        '상품명': ProductName[:100],
        '판매가': priceBasic,
        '대표 이미지 파일명': imageFirst,
        '추가 이미지 파일명': imageOther,
        '상품 상세정보': np.NaN,
        '판매자 상품코드': r.Number,
        '브랜드': Brand,

        '상품정보제공고시 모델명': Model,
        '옵션형태': "단독형",
        '옵션명': "선택",
        '옵션값': r.Option,
        '옵션가': priceList,
        '옵션 재고수량': optionStock,
        '상품정보제공고시 품명': ProductNamePlus,

        '상품상태': "신상품",
        '재고수량': 1000,
        'A/S 안내내용': '해외구매 대행 특성상 AS는 불가합니다.',
        'A/S 전화번호': '010-5033-0870',
        '부가세': '과세상품',
        '미성년자 구매': "Y",
        '구매평노출여부': "Y",
        '원산지 코드': "0200037",
        '수입사': "Ever Try",
        '복수원산지 여부': "N",
        '배송방법': "택배‚ 소포‚ 등기",
        '배송비 유형': "수량별",
        '기본배송비': 6000,
        '배송비 결제방식': "선결제",
        '수량별부과-수량': 1,
        '반품배송비': 6000,
        '교환배송비': 6000,
        '판매자 특이사항': "상품, 배송문의는 톡톡상담으로 남겨주시면 최대한 빠르게 답변드리겠습니다.",
        '즉시할인 값': 6000,
        '즉시할인 단위': '원',

        '스토어찜회원 전용여부': "N"
        # '상품구매시 포인트 지급 값',
        # '상품구매시 포인트 지급 단위': "%",
        # '텍스트리뷰 작성시 지급 포인트': 5,
        # '포토/동영상 리뷰 작성시 지급 포인트',
        # '한달사용 텍스트리뷰 작성시 지급 포인트',
        # '한달사용 포토 / 동영상리뷰 작성시 지급 포인트',

    }

    df_tem = pd.DataFrame([inputValue])
    df_temp = df_temp.append(df_tem, ignore_index=True)
    # df_template = df_template.append(inputValue, ignore_index=True)

df_temp.to_excel(
    f'{path}\\Setting\\ProductTemplateDone.xlsx', index=False)
