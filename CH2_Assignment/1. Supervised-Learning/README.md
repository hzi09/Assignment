# 1. 지도학습(Supervised Learning)


## 🗂️Directory Structure
```bash
📦1. Supervised-Learning
 ┣ 📜housingdata.csv
 ┣ 📜README.md
 ┣ 📜Supervised_Learning_v1.ipynb
 ┣ 📜Supervised_Learning_v2.ipynb
 ┣ 📜Supervised_Learning_v3.ipynb
 ┗ 📜Supervised_Learning_v4.ipynb
``` 
- `housingdata.csv` : 데이터 CSV 파일
- `README.md` : 디렉토리 구조, 과제 내용, 문제 풀이
- `Supervised_Learning_v1.ipynb` : 메인 과제
- `Supervised_Learning_v1.ipynb` : 도전 과제 - 모델 앙상블
- `Supervised_Learning_v1.ipynb` : 도전 과제 - 하이퍼 파라미터 튜닝
- `Supervised_Learning_v1.ipynb` : 도전 과제 - 시간적 요소 추가


<br>

## 과제 내용
### 💡주제
주택 가격 예측 모델 구축

### 🎯목표
주어진 주택 데이터셋을 사용하여 주택 가격을 예측하는 회귀 모델을 구축합니다.

### 📖학습내용
- 지도 학습의 기본 개념과 회귀 분석을 이해하고, 실제 데이터에 적용하는 능력
- 데이터 전처리 및 탐색: 데이터의 품질을 높이는 방법과 특징 선택의 중요성
- 여러 회귀 모델의 이해: 다양한 회귀 기법의 원리와 적용 방법
- 모델 성능 평가: 성능 지표의 이해 및 비교 분석을 통해 최적의 모델 선택


## 과제 가이드
- **데이터셋 탐색 및 전처리**:
    - 결측치 처리
    - 이상치 탐지 및 제거
    - 특징 선택
- **여러 회귀 모델 비교**:
    - 선형 회귀
    - 의사결정나무
    - 랜덤 포레스트 등
- **모델 성능 평가**:
    - 지표를 사용하여 모델 성능을 비교합니다.
        - **Mean Absolute Error (MAE)**: 예측값과 실제값의 절대 오차의 평균.
        - **Mean Squared Error (MSE)**: 예측값과 실제값의 제곱 오차의 평균.
        - **R² Score**: 모델이 데이터의 변동성을 얼마나 설명하는지 나타내는 지표.
- **결과 분석**:
    - 각 모델의 성능을 비교하고 최적의 모델을 선택하여 결과를 시각화합니다.
        - **시각화**: 성능 지표를 막대 그래프로 시각화하여 쉽게 비교할 수 있도록 합니다. matplotlib 또는 seaborn을 사용하여 막대 그래프를 그립니다.


<br>

## 🔥추가 도전 과제
- **모델 앙상블** ⭐⭐⭐⭐⭐
    - 여러 모델의 예측 결과를 결합하여 성능을 향상시키는 앙상블 기법(예: 배깅, 부스팅)을 적용합니다.
    - 각 모델의 예측을 평균내거나 가중치를 부여하여 최종 예측을 생성합니다.
- **하이퍼파라미터 튜닝** ⭐⭐⭐⭐
    - Grid Search 또는 Random Search 기법을 이용해 모델의 하이퍼파라미터를 최적화합니다.
- **시간적 요소 추가** ⭐⭐⭐
    - 주택 데이터셋에 시간적 요소(예: 계절적 변화, 경제 지표 등)를 추가하여 모델의 예측력을 높입니다.


<br>

## ✍️문제 풀이
### 데이터셋 탐색 및 전처리

#### 1. 데이터 확인

- 머신러닝을 진행하기 전에 데이터를 불러오고 확인
  - CSV 파일 데이터 불러오기 : `read_csv()`
  - 데이터 미리보기(5개의 행만 확인) : `head()`
  - 데이터셋의 기본 정보 확인 : `info()`
    - 데이터 타입, 인덱스 개수, 컬럼명 등을 확인 가능
  - 데이터 정보 탐색 : `describe()` 
    - 각 컬럼별 데이터의 개수, 평균값, 최대값 등을 확인 가능
    ```python
    import pandas as pd

    # 데이터 불러오기
    housing = pd.read_csv('housingdata.csv')

    # 데이터 미리보기
    housing.head()

    # 데이터셋 기본 정보 확인
    housing.info() 

    # 데이터 정보 탐색
    housing.describe() 
    ```
- 위 데이터를 시각화해서 확인
  - 히스토그램(Histogram) : `hist()`
    - `bins` : 가로축 구간의 개수는 좀 여유있게 50으로 결정
    - `figsize` : 가로길이와 세로길이는 작성하면서 여유있게 지정해주었다.(x=20, y=15)
    ```python
    import matplotlib.pyplot as plt

    housing.hist(bins=50, figsize=(20,15))
    plt.show()
    ```

#### 2. 데이터 전처리

- 결측치 처리
   - 결측치의 개수 확인 : `isna().sum()`
     - CRIM, ZN, INDUS, CHAS, AGE, LSTAT 컬럼에 20개씩의 결측치가 확인됨
        ```python
        # 결측치 개수 확인
        housing.isna().sum()
        ```
   - 결측치 비율 확인 
     - 결측치의 개수를 전체 데이터의 길이로 나눈후 *100을 하면 결측치의 비율을 확인할 수 있음
        ```python
        # 결측치 비율 확인
        missing_percentage= (housing.isnull().sum() / len(housing)) * 100
        ```
    - 결과
      - 그렇게 높은 수치는 아니라서 그냥 삭제를 할까 하다가, 결측치처리를 진행
        ```
        CRIM       3.952569
        ZN         3.952569
        INDUS      3.952569
        CHAS       3.952569
        NOX        0.000000
        RM         0.000000
        AGE        3.952569
        DIS        0.000000
        RAD        0.000000
        TAX        0.000000
        PTRATIO    0.000000
        B          0.000000
        LSTAT      3.952569
        MEDV       0.000000
        dtype: float64
        ```
- 결측치 처리
  - 수치형데이터는 `mean`과 `median` 중 고민하였지만, 데이터 범위가 큰 데이터도 있어서 중앙값으로 대체
  - 범주형 데이터는 `most_frequent`(최빈값)로 대체
    ```python
    # 결측치 처리
    from sklearn.impute import SimpleImputer

    # 수치형데이터 결측치 > 중앙값 대체
    imputer = SimpleImputer(strategy='median')

    for col in ['CRIM', 'ZN', 'INDUS', 'AGE', 'LSTAT'] :
        housing[col] = imputer.fit_transform(housing[[col]])

    # 범주형 데이터 결측치 > 최빈값 대체
    imputer2 = SimpleImputer(strategy= 'most_frequent')

    housing['CHAS'] = imputer2.fit_transform(housing[['CHAS']])
    ```

- 이상치 처리
  - 이상치 처리 전에 기존의 데이터와 비교를 하고 싶어서 `housing_processed` 변수를 만들어서 데이터를 복사(`copy()`)해 넣어줌
  - 이상치는 IQR 방식으로 처리하였으며 경계값으로 대체하는 방법을 채택 
    ```python
    import numpy as np

    numeric_cols = housing.select_dtypes(include=[np.number]).columns # 수치형 데이터를 가진 열들의 이름 가져오기
    housing_processed = housing.copy()


    for col in numeric_cols:
        Q1 = housing[col].quantile(0.25)
        Q3 = housing[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((housing[col] < lower_bound) | (housing[col] > upper_bound))
        outlier_count = outliers.sum()

        if outlier_count > 0:
            # 이상치를 경계값으로 대체 (Winsorization)
            housing_processed[col] = housing_processed[col].clip(lower=lower_bound, upper=upper_bound)
    ```

  - 이상치 처리 전 후를 시각화하여 표현
    ```python
    # 이상치 처리 전 데이터 시각화
    housing.boxplot()
    plt.xticks(rotation=90)
    plt.title('Before Boxplot')
    plt.tight_layout()
    plt.show()

    # 이상치 처리 후 데이터 시각화
    housing_processed.boxplot()
    plt.xticks(rotation=90)
    plt.title('After Boxplot')
    plt.tight_layout()
    plt.show()
    ```
    - 결과
        ![image](https://github.com/user-attachments/assets/8d30ff39-9477-4947-9d3f-f26e1fdfae7e)

- 상관관계
  - 학습을 시작하기 전에 타겟 데이터와 상관관계를 확인 : `corr()`
  - 상관관계가 높은 순으로 데이터 확인하기
    - 데이터를 절대값으로 바꾸어준 후 : `avs()`
    - 값을 기준으로 내림차순 정렬 : `sort_values(ascending=False)`
        ```python
        # 데이터 상관관계 확인
        corr_matrix = housing_processed.corr()
        corr_matrix['MEDV'].abs().sort_values(ascending=False)
        ```
    - 결과
        ```
        MEDV       1.000000
        LSTAT      0.782941
        RM         0.697645
        INDUS      0.553140
        TAX        0.543545
        PTRATIO    0.523993
        CRIM       0.522140
        NOX        0.506505
        AGE        0.454330
        RAD        0.452679
        DIS        0.333079
        B          0.321250
        ZN              NaN
        CHAS            NaN
        Name: MEDV, dtype: float64
        ```
  - 시각화 분석 : 선형 회귀선 확인
    - MEDV와 얼마나 선형적인 관계가 있는지 확인
      - `ZN`과 `CHAS`는 선형관계가 없다고 판단되어서 추가하지 않음
      - 오른쪽 아래로 내려가는 선 : 음의 상관관계
      - 오른쪽 위로 올라가는 선 : 양의 상관관계
        ```python
        import seaborn as sns

        # 시각화 분석
        plot_cols = ['MEDV', 'LSTAT', 'RM', 'INDUS', 'TAX', 'PTRATIO', 'CRIM', 'NOX', 'AGE', 'RAD', 'DIS', 'B']
        plot_housing = housing.loc[:, plot_cols]

        # 선형 회귀선 표시
        fig, axs = plt.subplots(figsize=(16, 10))
        for i, feature in enumerate(plot_cols[1:]) :
            ax1 = plt.subplot(3,4,i+1)
            sns.regplot(x=feature, y=plot_cols[0], data=plot_housing, ax=ax1)
        ```
        ![image](https://github.com/user-attachments/assets/8063c063-441f-4cc4-84f6-9ef0813b44d9)

  - 상관관계 히트맵 확인
    - 상관관계를 시각적으로 명확하게 확인할 수 있는 히트맵을 사용
    - `DIS`와 `B`가 상관관계가 낮은 걸 확인 가능
        ```python
        # 상관관계 히트맵
        plt.figure(figsize=(8, 6))
        sns.heatmap(plot_housing.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap')
        plt.show()
        ```
        ![image](https://github.com/user-attachments/assets/f0ba40d7-80d2-45a5-9d75-1ac1bd4b9c00)


### 여러 회귀 모델 비교
#### 3. 특성과 타겟 변수 분리
- 사용할 특성(독립변수)는 'LSTAT', 'RM', 'INDUS', 'TAX', 'PTRATIO', 'CRIM', 'NOX', 'AGE', 'RAD'
- 타겟 변수(말그대로 예측할 데이터)는 'MEDV'
    ```python
    # 특성과 타겟 변수 분리
    X = housing_processed[['LSTAT', 'RM', 'INDUS', 'TAX', 'PTRATIO', 'CRIM', 'NOX', 'AGE', 'RAD']]  # 독립 변수
    y = housing_processed['MEDV']  # 타겟 변수
    ```

#### 4. 모델 선택 및 훈련
- 선형회귀, 다항회귀, 의사결정나무, 랜덤포레스트, 리지 회귀, 라쏘 회귀에 대해서 훈련을 진행


### 모델 성능 평가 및 결과분석
#### 5. 모델 평가
- 모델 별로 성능(MAE, MSE, R2)를 구하여 결과를 비교
    ```python
    # 모델별 성능 저장
    results = pd.DataFrame({
        'Model': ['Linear Regression', 'Polynomial Regression', 'Decision Tree', 'Random Forest', 'Ridge Regression', 'Lasso Regression'],
        'MAE': [lr_mae, pr_mae, tree_mae, rf_mae, ri_mae, ls_mae],
        'MSE': [lr_mse, pr_mse, tree_mse, rf_mse, ri_mse, ls_mse],
        'R2': [lr_r2, pr_r2, tree_r2, rf_r2, ri_r2, ls_r2]
    })

    # 서브플롯 생성
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))  

    colors = ['skyblue', 'green', 'purple']

    # 그래프를 각각 생성
    for ax, metric, color in zip(axes, ['MAE', 'MSE', 'R2'], colors):
        ax.bar(results['Model'], results[metric], color=color, width=0.5)
        ax.set_title(f'{metric} Comparison')
        ax.set_ylabel(f'{metric} Value')
        ax.set_xlabel('Model')
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        # x축 기울기
        ax.set_xticks(np.arange(len(results['Model'])))
        ax.set_xticklabels(results['Model'], rotation=70)

    # 레이아웃 조정 및 출력
    plt.tight_layout()
    plt.show()    
    ```
    ![image](https://github.com/user-attachments/assets/70521ddb-ffc9-46f1-af3d-983b2c4827fb)


- 라쏘회귀가 R2값이 가장 높은 것으로 확인되었다.
  
    |                           | 선형회귀 | 다항회귀 | 의사결정나무 | 랜덤포레스트 | 리지회귀 | 라쏘회귀 |
    |--------------------------:|---------:|---------:|-------------:|-------------:|---------:|---------:|
    | Mean Absolute Error (MAE) |   2.4453 |   2.1346 |       2.6892 |       1.9230 |   2.4510 |   1.8711 |
    |  Mean Squared Error (MSE) |  13.0004 |   8.7704 |      13.7651 |       6.3052 |  13.0244 |   5.9593 |
    |                  R² Score |   0.7342 |   0.8207 |       0.7186 |       0.8711 |   0.7337 |   0.8781 |


## ✍️ 도전과제 문제 풀이
### 모델 앙상블
- 배깅 모델과 부스팅 모델을 추가한 후(여기서는 코드 생략), 가중 평균 앙상블을 진행
  - 가중 앙상블 : 성능이 높은 모델 5개를 선택
    ```python
    # r2점수를 저장할 리스트
    model_pred = [y_lr_pred, y_pr_pred, y_tree_pred, y_rf_pred, y_ri_pred, y_ls_pred, y_bagging_pred, y_boosting_pred]
    model_r2_score = [lr_r2, pr_r2, tree_r2, rf_r2, ri_r2, ls_r2, bagging_r2, boosting_r2]

    print(model_r2_score)

    # 성능이 높은 5개 모델 선택
    top_models_idx = np.argsort(model_r2_score)[-5:]  # 상위 5개 모델 인덱스
    top_pred = [model_pred[i] for i in top_models_idx]
    top_scores = [model_r2_score[i] for i in top_models_idx]

    # 가중치 계산 (성능 기반)
    weights = np.array(top_scores) / sum(top_scores)

    # 가중 평균 앙상블
    final_pred = sum(w * pred for w, pred in zip(weights, top_pred))
    
    # 성능평가
    final_mae = mean_absolute_error(y_test, final_pred)
    final_mse = mean_squared_error(y_test, final_pred)
    final_r2 = r2_score(y_test, final_pred)

    print(f'Mean Absolute Error (MAE) : {final_mae}')
    print(f'Mean Squared Error (MSE) : {final_mse}')
    print(f'R² Score : {final_r2}')
    ```
  - 결과
    ```
    Mean Absolute Error (MAE) : 1.920664657312724
    Mean Squared Error (MSE) : 6.670866427584049
    R² Score : 0.8636510323472387
    ```

- 라쏘 모델보다 결과가 낮게 나옴
  - 아마 가중치 부여를 하지 않아서가 아닐까 싶은데 이 부분은 추가 학습 후에 다시 수정이 필요할 것 같음


    |                           | 선형회귀 | 다항회귀 | 의사결정나무 | 랜덤포레스트 | 리지회귀 | 라쏘회귀 | 배깅모델 | 부스팅모델 | 가중평균앙상블 |
    |--------------------------:|---------:|---------:|-------------:|-------------:|---------:|---------:|---------:|-----------:|-----------------:|
    | Mean Absolute Error (MAE) |   2.4453 |   2.1346 |       2.6892 |       1.9230 |   2.4510 |   1.8711 |   1.9380 |     1.9168 |           1.9206 |
    |  Mean Squared Error (MSE) |  13.0004 |   8.7704 |      13.7651 |       6.3052 |  13.0244 |   5.9593 |   6.3964 |     6.4878 |           6.6708 |
    |                  R² Score |   0.7342 |   0.8207 |       0.7186 |       0.8711 |   0.7337 |   0.8781 |   0.8692 |     0.8673 |           0.8636 |


### 하이퍼파라미터 튜닝

- 랜덤포레스트 모델을 이용하여 하이퍼파라미터 튜닝 진행
  - 그리드 서치
    ```python
    from sklearn.model_selection import GridSearchCV

    # 하이퍼파라미터 그리드 설정
    param_grid = {
        'n_estimators': [300], 
        'max_depth': [3, 5, 7, 10], 
        'min_samples_split': [6 ,8, 12, 18],
        'min_samples_leaf': [6, 8, 16, 20],
    }


    rf_clf = RandomForestRegressor(random_state=0, n_jobs=-1) # n_jobs = -1 : 모든 CPU 코어를 사용하여 학습
    grid_cv = GridSearchCV(rf_clf, param_grid=param_grid, cv=5, n_jobs=-1)
    grid_cv.fit(X_train, y_train)

    # 데이터 분할 (훈련 데이터와 테스트 데이터)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 데이터 스케일링
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 최적 모델로 예측
    best_rf_model = RandomForestRegressor(n_estimators=300, max_depth=10, min_samples_leaf=6, min_samples_split=6)
    best_rf_model.fit(X_train_scaled, y_train)
    y_rf_pred = best_rf_model.predict(X_test_scaled)

    # 모델 평가
    rf_mae = mean_absolute_error(y_test, y_rf_pred)
    rf_mse = mean_squared_error(y_test, y_rf_pred)
    rf_r2 = r2_score(y_test, y_rf_pred)

    print(f'Mean Absolute Error (MAE): {rf_mae}')
    print(f'Mean Squared Error (MSE): {rf_mse}')
    print(f'R² Score: {rf_r2}')
    ```

- 랜덤 서치
    ```python
    from sklearn.model_selection import RandomizedSearchCV

    # 하이퍼파라미터 분포 설정
    param_dist = {
        'n_estimators': [300],
        'max_depth': [5, 7, 10, 15], 
        'min_samples_split': [4 ,6 ,8, 12],
        'min_samples_leaf': [6, 8, 16, 20],
        'bootstrap': [True, False]
    }


    rf_clf = RandomForestRegressor(random_state=0, n_jobs=-1) # n_jobs = -1 : 모든 CPU 코어를 사용하여 학습
    random_cv = RandomizedSearchCV(rf_clf, param_distributions=param_dist, cv=5, n_jobs=-1)
    random_cv.fit(X_train, y_train)

    # 데이터 분할 (훈련 데이터와 테스트 데이터)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 데이터 스케일링
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 최적 모델로 예측
    best_rf_model = RandomForestRegressor(n_estimators=300, max_depth=7, min_samples_leaf=6, min_samples_split=4, bootstrap=True)
    best_rf_model.fit(X_train_scaled, y_train)
    y_rf_pred = best_rf_model.predict(X_test_scaled)

    # 모델 평가
    rf_mae = mean_absolute_error(y_test, y_rf_pred)
    rf_mse = mean_squared_error(y_test, y_rf_pred)
    rf_r2 = r2_score(y_test, y_rf_pred)

    print(f'Mean Absolute Error (MAE): {rf_mae}')
    print(f'Mean Squared Error (MSE): {rf_mse}')
    print(f'R² Score: {rf_r2}')
    ```

- 결과
  - 하이퍼 파라미터를 진행했지만 그리드서치 랜덤서치 두개 모두 R²가 떨어진걸 확인
  - 이 부분도 학습이 조금 더 필요
    |                           | 랜덤포레스트 | 그리드서치 | 랜덤서치 |
    |--------------------------:|-------------:|-----------:|---------:|
    | Mean Absolute Error (MAE) |       1.9230 |     2.0244 |   2.0240 |
    |  Mean Squared Error (MSE) |       6.3052 |     8.1637 |   8.0601 |
    |                  R² Score |       0.8711 |     0.8331 |   0.8352 | 


### 시간적 요소 추가
- 데이터 전처리 후에 시간적 요소를 추가
  - 어떤 요소가 가장 적합할지 생각한 끝에 `TAX`로 결정 (TAX: 10,000달러당 재산세율)
- `TAX`를 기준으로 데이터 정렬
    ```python
    # 이상치가 처리된 housing 데이터에서 TAX 값으로 데이터 정렬
    housing_processed = housing_processed.sort_values(by="TAX").reset_index(drop=True)
    housing_processed
    ```
- `TAX`가 올라갈때마다 1이 올라가는 방향으로 진행
  - 실제 년도를 알 수 없어 데이터를 구분하기 위해 1씩 증가하는 것으로 표현함
  - 물론 세금이 떨어질때도 있어 이 데이터를 시간데이터로 바꾸는 것은 올바르지 않은 선택일수도 있음
    ```python
    # TAX값이 올라갈때마다 1을 더하여 시간의 흐름을 표현
    housing_processed['TIME'] = (housing_processed['TAX'] != housing_processed['TAX'].shift()).cumsum()
    housing_processed
    ```
- `MEDV`와 -0.51로 상관관계가 높은 것으로 확인
- 결과 비교
  - 기존 결과
    |                           | 선형회귀 | 다항회귀 | 의사결정나무 | 랜덤포레스트 | 리지회귀 | 라쏘회귀 | 배깅모델 | 부스팅모델 | 가중평균앙상블 |
    |--------------------------:|---------:|---------:|-------------:|-------------:|---------:|---------:|---------:|-----------:|-----------------:|
    | Mean Absolute Error (MAE) |   2.4453 |   2.1346 |       2.6892 |       1.9230 |   2.4510 |   1.8711 |   1.9380 |     1.9168 |           1.9206 |
    |  Mean Squared Error (MSE) |  13.0004 |   8.7704 |      13.7651 |       6.3052 |  13.0244 |   5.9593 |   6.3964 |     6.4878 |           6.6708 |
    |                  R² Score |   0.7342 |   0.8207 |       0.7186 |       0.8711 |   0.7337 |   0.8781 |   0.8692 |     0.8673 |           0.8636 |
    
  - `TAX` 추가 결과
    |                           | 선형회귀 | 다항회귀 | 의사결정나무 | 랜덤포레스트 | 리지회귀 | 라쏘회귀 | 배깅모델 | 부스팅모델 | 가중 평균 앙상블 |
    |--------------------------:|---------:|---------:|-------------:|-------------:|---------:|---------:|---------:|-----------:|-----------------:|
    | Mean Absolute Error (MAE) |   2.8446 |   2.1745 |       2.6267 |       2.0439 |   2.8482 |   3.3502 |   2.0510 |     1.9960 |           1.9760 |
    |  Mean Squared Error (MSE) |  13.6133 |  10.8285 |      11.5584 |       7.5495 |  13.6438 |  17.2110 |   7.6402 |     7.7054 |           7.1979 |
    |                  R² Score |   0.8076 |   0.8469 |       0.8366 |       0.8933 |   0.8072 |   0.7568 |   0.8920 |     0.8911 |           0.8982 |

  - 생각하기에는 너무 상관관계가 조금 있는 데이터가 들어오면서 R²가 높아진게 아닌가 생각이 든다(물론 낮아진 데이터도 있음)
  - MAE와 MSE가 낮아지지 않고 상승했으므로 좋은 모델이라고 판단하기에는 어려울 것 같다.