import pandas as pd

# 메인 과제 코드(data_analysis_v1)에서 df_police를 불러옴
from data_analysis_v1 import df_police

# csv 파일을 불러오고, index는 '구별'로 설정
df_person = pd.read_csv('pop_kor.csv', index_col = '구별')

# 두 데이터 프레임을 merge 해줌
df_joined = df_person.join(df_police)

# 검거율을 기준으로 오름차수 정렬
df_joined.sort_values(by = '검거율', ascending=True, inplace = True)

# 데이터 프레임 출력
print(df_joined)