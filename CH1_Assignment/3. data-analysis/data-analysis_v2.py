import pandas as pd

from data-analysis_v2 import df_police

df_person = pd.read_csv('pop_kor.csv', index_col = '구별')
df_joined = df_person.join(df_police)
df_joined.sort_values(by = '검거율', ascending=True, inplace = True)

print(df_joined)