import pandas as pd

df_police = pd.read_excel('관서별 5대범죄 발생 및 검거.xlsx')

# 매핑할 데이터 딕셔너리 형태로 생성
division = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
            '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
            '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
            '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
            '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
            '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구',
            '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구',
            '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}

# 새로운 열 추가 : '구별' 열을 생성하고 '관서명' 열을 복사한 후 division으로 매핑
df_police['구별'] = df_police['관서명'].map(division)

df_police.fillna({'구별':'구 없음'}, inplace = True)

df_police = pd.pivot_table(df_police,
                           values =['소계(발생)', '소계(검거)', '살인(발생)',
                                    '살인(검거)', '강도(발생)', '강도(검거)',
                                    '강간(발생)', '강간(검거)', '절도(발생)',
                                    '절도(검거)', '폭력(발생)', '폭력(검거)'],
                           index = '구별', aggfunc= 'sum')



df_police.drop(labels = '구 없음',axis=0, inplace = True)

def percent() :
    per_list = ['강간', '강도', '살인', '절도', '폭력']
    for i in per_list :
        df_police[f'{i}검거율']  = (df_police[f'{i}(검거)'] / df_police[f'{i}(발생)']) * 100
    df_police['검거율'] = (df_police['소계(검거)'] / df_police['소계(발생)']) * 100
percent()

def delete() :
    del_list = ['강간', '강도', '살인', '절도', '폭력', '소계']
    for i in del_list :
        del df_police[f'{i}(검거)']
    del df_police['소계(발생)']
delete()

def rename() :
    name = ['강간', '강도', '살인', '절도', '폭력']
    for i in name :
        df_police.rename(columns= {f'{i}(발생)' : f'{i}'}, inplace= True)

rename()


if __name__ == "__main__" :
    print(df_police)