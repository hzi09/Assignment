# 3. Python 라이브러리로 데이터 분석하기 


## 🗂️Directory Structure
- `README.md` : 디렉토리 구조, 과제 내용, 입출력 예시
- `data-analysis_v1` : 메인 과제 코드
- `data-analysis_v2` : 추가 도전 과제 코드
- `pop_kor.csv` : 추가 도전 과제 데이터 .csv 파일
- `관서별 5대범죄 발생 및 검거.xlsx` : 메인 과제 데이터 .xlsx 파일

<br>

## 📝과제 내용
- Python 라이브러리를 활용하여 주어진 데이터(.xlxs)를 분석 Quiz를 수행해주세요.

### Quiz
1. Python 라이브러리 함수를 사용하여 엑셀 파일을 불러오고, DataFrame을 출력해주세요.
2. 각 경찰서(`관서명`)를 해당 구 이름으로 매핑하여 '구별'이라는 새로운 column을 생성하고, DataFrame을 출력해주세요.
   - 매칭되지 않는 경찰서명에 대해서는 기본값 `'구 없음'`을 할당합니다.
3. `pivot_table` 을 사용하여 관서별 데이터를 구별 데이터로 변경하고, 같은 구의 경우에는 sum을 적용하여 더해주세요. (index : 관서명 -> 구별)
4. `구 없음`  행은 `drop` 을 활용하여 삭제해주세요.
5. 각 범죄 별로 검거율을 계산하고, 각 검거율 데이터 column을 DataFrame에 추가해주세요.
   - 추가해야할 cloumn
   ```
   강간검거율,
   강도검거율,
   살인검거율,
   절도검거율,
   폭력검거율,
   검거율
   ```
6. 필요없는 column을 `del`을 사용하여 삭제해주세요.
    - 삭제해야할 column
    ```
    강간(검거),
    강도(검거),
    살인(검거),
    절도(검거),
    폭력(검거),
    소계(발생),
    소계(검거)
    ```
7. DataFrame의 컬럼명을 `rename`을 사용하여 변경해주세요.
    - 변경해야할 column
    ```
    '강간(발생)':'강간',
    '강도(발생)':'강도',
    '살인(발생)':'살인',
    '절도(발생)':'절도',
    '폭력(발생)':'폭력'
    ```


### 입출력 예시
```
	강간	강도	살인	절도	폭력	강간검거율	강도검거율	살인검거율	절도검거율	폭력검거율	검거율
구별											
강남구	449	21	13	3850	4284	77.728285	85.714286	76.923077	42.857143	86.484594	66.519670
강동구	156	6	4	2366	2712	78.846154	100.000000	75.000000	33.347422	82.890855	60.469108
```


<br>

## 🔥추가 도전 과제
1. Python 라이브러리 함수를 사용하여 인구 데이터(pop_kor.csv) 파일을 불러오고, DataFrame을 출력해주세요.
   - Quiz에서 수행한 DataFrame의 구별 index를 기준으로 merge를 할 것이므로, index를 셋팅해서 불러와 주세요.
2. `join` 을 사용하여 Quiz에서 수행한 DataFrame과 인구 데이터 DataFrame을 merge하고, DataFrame을 출력해주세요.
   - `join` : Quiz에서 수행한 DataFrame의 index를 기준으로 인구 데이터 DataFrame index 중 매칭되는 값을 매김.
3. 새롭게 merge 된 DataFrame에서 `검거율` 기준으로 오름차순 정렬 후, DataFrame을 출력해주세요.


<br>

## ✍️문제 풀이
1. Python 라이브러리 함수를 사용하여 엑셀 파일을 불러오고, DataFrame을 출력
    - read_excel을 통해 엑셀파일 읽어오기(1. ImportError) )
        
        ```python
        import pandas as pd
        
        df_police = pd.read_excel('관서별 5대범죄 발생 및 검거.xlsx')
        print(df_police.head())
        ```
      > 실행 결과
    
       ```
            관서명  소계(발생)  소계(검거)  살인(발생)  ...  절도(발생)  절도(검거)  폭력(발생)  폭력(검거)
       0      계  126401   82680     163  ...   55307   21842   65206   55356
       1    중부서    2860    1716       2  ...    1395     477    1355    1170
       2    종로서    2472    1589       3  ...    1070     413    1278    1070
       3   남대문서    2094    1226       1  ...    1153     382     869     794
       4   서대문서    4029    2579       2  ...    1812     738    2056    1711
       ```
    
2. 각 경찰서(`관서명`)를 해당 구 이름으로 매핑하여 '구별'이라는 새로운 column을 생성하고, DataFrame을 출력

    ! 매칭되지 않는 경찰서명에 대해서는 기본값 `'구 없음'`을 할당
    
    - 매핑할 데이터를 딕셔너리 형태로 생성
        
        ```python
        division = {'서대문서': '서대문구', '수서서': '강남구', '강서서': '강서구', '서초서': '서초구',
                    '서부서': '은평구', '중부서': '중구', '종로서': '종로구', '남대문서': '중구',
                    '혜화서': '종로구', '용산서': '용산구', '성북서': '성북구', '동대문서': '동대문구',
                    '마포서': '마포구', '영등포서': '영등포구', '성동서': '성동구', '동작서': '동작구',
                    '광진서': '광진구', '강북서': '강북구', '금천서': '금천구', '중랑서': '중랑구',
                    '강남서': '강남구', '관악서': '관악구', '강동서': '강동구', '종암서': '성북구',
                    '구로서': '구로구', '양천서': '양천구', '송파서': '송파구', '노원서': '노원구',
                    '방배서': '서초구', '은평서': '은평구', '도봉서': '도봉구'}
        ```
        
    - '구별' 열을 생성하고 '관서명' 열을 복사한 후 division으로 매핑
        
        ```python
        df_police['구별'] = df_police['관서명'].map(division)
        ```
        
    - 매칭되지 않는 경찰서는 ‘구 없음’ 할당(2. FutureWarning)
        
        ```python
        df_police.fillna({'구별':'구 없음'}, inplace = True)
        ```
        
        - `inplace` 인수는 Pandas객체의 공통사항으로 원본의 변경여부를 의미, `True`일 경우 반환값 없이 원본이 변경
    
    > 실행결과
    
    ```
        관서명  소계(발생)  소계(검거)  살인(발생)  살인(검거)  ...  절도(발생)  절도(검거)  폭력(발생)  폭력(검거)    구별
    0     계  126401   82680     163     156  ...   55307   21842   65206   55356  구 없음
    1   중부서    2860    1716       2       2  ...    1395     477    1355    1170    중구
    2   종로서    2472    1589       3       3  ...    1070     413    1278    1070   종로구
    3  남대문서    2094    1226       1       0  ...    1153     382     869     794    중구
    4  서대문서    4029    2579       2       2  ...    1812     738    2056    1711  서대문구
    ```
    
3. `pivot_table` 을 사용하여 관서별 데이터를 구별 데이터로 변경하고, 같은 구의 경우에는 sum을 적용(index : 관서명 -> 구별)
    
    ```python
    df_police = pd.pivot_table(df_police,
                               values =['소계(발생)', '소계(검거)', '살인(발생)',
                                        '살인(검거)', '강도(발생)', '강도(검거)',
                                        '강간(발생)', '강간(검거)', '절도(발생)',
                                        '절도(검거)', '폭력(발생)', '폭력(검거)'],
                               index = '구별', aggfunc= 'sum')
    ```
    
    > 실행 결과
    
    ```
         강간(검거)  강간(발생)  강도(검거)  강도(발생)  ... 절도(검거)  절도(발생)  폭력(검거)  폭력(발생)
    구별                                   ...                               
    강남구     349     449      18      21  ...   1650    3850    3705    4284
    강동구     123     156       8       6  ...    789    2366    2248    2712
    강북구     126     153      13      14  ...    618    1434    2348    2649
    강서구     191     262      13      13  ...   1260    2096    2718    3207
    관악구     221     320      14      12  ...    827    2706    2642    3298
    ```
    

4. `구 없음`  행은 `drop` 을 활용하여 삭제
    
    ```python
    df_police.drop(labels = '구 없음',axis=0, inplace = True)
    ```
    
    > 실행결과 : 구 없음 행이 사라져야함

5. 각 범죄 별로 검거율을 계산하고, 각 검거율 데이터 column을 DataFrame에 추가
    
    ! 추가해야할 column
    ```
    강간검거율,
    강도검거율,
    살인검거율,
    절도검거율,
    폭력검거율,
    검거율
    ```
    
    - 하나하나 치려다가 약간 현타와서 함수를 만들었다..
    - 소계 검거율이 조금 아쉽지만 이정도면 만족!
    
    ```python
    def percent() :
        per_list = ['강간', '강도', '살인', '절도', '폭력']
        for i in per_list :
            df_police[f'{i}검거율']  = (df_police[f'{i}(검거)'] / df_police[f'{i}(발생)']) * 100
        df_police['검거율'] = (df_police['소계(검거)'] / df_police['소계(발생)']) * 100
    
    percent()
    ```
    
3. 필요없는 column을 `del` 을 사용하여 삭제
    
    ! 삭제해야할 column
    
    ```
    강간(검거),
    강도(검거),
    살인(검거),
    절도(검거),
    폭력(검거),
    소계(발생),
    소계(검거)
    ```
    
    - 위의 검거율과 비슷하게 함수로 표현하였다.
    - 다른점은 list에 ‘소계’를 추가..!
    - 소계 발생은 또 따로 지워주었다.
    
    ```python
    def delete() :
        del_list = ['강간', '강도', '살인', '절도', '폭력', '소계']
        for i in del_list :
            del df_police[f'{i}(검거)']
        del df_police['소계(발생)']
    delete()
    ```
    
4. DataFrame의 컬럼명을 `rename` 을 사용하여 변경
    
    ! 변경해야할 컬럼
    
    ```
    '강간(발생)':'강간',
    '강도(발생)':'강도',
    '살인(발생)':'살인',
    '절도(발생)':'절도',
    '폭력(발생)':'폭력'
    ```
    
    - 이것도 함수로 풀었다.
    
    ```python
    def rename() :
        name = ['강간', '강도', '살인', '절도', '폭력']
        for i in name :
            df_police.rename(columns= {f'{i}(발생)' : f'{i}'}, inplace= True)
    
    rename()
    ```

## 🔥 도전 과제 풀이

1. Python 라이브러리 함수를 사용하여 인구 데이터(pop_kor.csv) 파일을 불러오고, DataFrame을 출력
    - 코드를 다시 넣을까 하다가 간단하게 풀릴 문제인데 싶어서 `for _ imoport`를 사용하기로 했다.
    - 여기서 이슈가 발생!
        - 앞서 `print(df_police)`를 사용했기 때문에 이 결과 값이 출력된다.
        - 그래서 생각해낸 방법이 아래의 코드를 메인 과제 코드에 추가해줌!
            
          ```python
          # 추가도전과제 코드에서 print 되는 것을 막기 위해 사용
          if __name__ == "__main__" :
              # 데이터 프레임 출력
              print(df_police)
          ```

    ```python
    import pandas as pd
    
    # 메인 과제 코드(data_analysis_v1)에서 df_police를 불러옴
    from data_analysis_v1 import df_police
    
    # csv 파일을 불러오고, index는 '구별'로 설정
    df_person = pd.read_csv('pop_kor.csv', index_col = '구별')
    ```
    

2. `join` 을 사용하여 Quiz에서 수행한 DataFrame과 인구 데이터 DataFrame을 merge하고, DataFrame을 출력
    - `join`을 사용하여 merge 하였다.
    - 검거율은 오름차순으로 `sort_values`를 사용하여 정렬하였다.
    
    ```python
    # 두 데이터 프레임을 merge 해줌
    df_joined = df_person.join(df_police)
    
    # 검거율을 기준으로 오름차수 정렬
    df_joined.sort_values(by = '검거율', ascending=True, inplace = True)
    
    # 데이터 프레임 출력
    print(df_joined)
    ```


<br>    

## 🚫 에러 모으기

### 1. ImportError

```powershell
ImportError: Missing optional dependency 'openpyxl'. Use pip or conda to install openpyxl.
```

- openpyxl이 없음!
- 가상환경에서는 설치한 적이 없어서 발생한 오류,,!

#### 🤟 해결 방법

- 해결방법은 꽤나 간단.. 터미널에서 openpyxl을 깔면된다..
    
    ```powershell
    pip install openpyxl
    ```
    

### 2. FutureWarning

```
C:\Users\hzi28\PycharmProjects\mypython\data.py:19: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.

  df_police['구별'].fillna('구 없음', inplace = True)
```

- `fillna()` 를 사용하여 결측치를 채우려고 했는데, 에러 발생.
    - 근데 또 실행은 되긴해서 그냥 넘어갈까 하다보니.. value 인자를 수정하면 해결 할 것 같다.

#### 🤟 해결방법

- velue 인자를 딕셔너리 형태로 바꾸어 해결하였다.
    
    ```python
    # 경고 메세지가 나오는 코드
    df_police['구별'].fillna('구 없음', inplace = True)
    
    # 해결 완료 코드
    df_police.fillna({'구별':'구 없음'}, inplace = True)
    ```