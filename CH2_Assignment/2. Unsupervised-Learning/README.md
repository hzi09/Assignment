# 2. 비지도학습(Unsupervised Learning)


## 🗂️Directory Structure
```bash
📦2. Unsupervised-Learning
 ┣ 📜Mall_Customers.csv
 ┣ 📜README.md
 ┣ 📜Unsupervised_Learning_v1.ipynb
 ┣ 📜Unsupervised_Learning_v2.ipynb
 ┗ 📜Unsupervised_Learning_v3.ipynb
``` 
- `Mall_Customers.csv` : 데이터 CSV 파일
- `README.md` : 디렉토리 구조, 과제 내용, 문제 풀이
- `Unsupervised_Learning_v1.ipynb` : 메인 과제
- `Unsupervised_Learning_v1.ipynb` : 도전 과제 - 다양한 클러스터링 기법 비교
- `Unsupervised_Learning_v1.ipynb` : 도전 과제 - 고객 행동 예측 모델 구축


<br>

## 과제 내용
### 💡주제
고객 세분화 분석

### 🎯목표
고객 데이터셋을 사용하여 비슷한 행동을 보이는 고객 그룹을 식별합니다.

### 📖학습내용
- 비지도 학습의 개념을 이해하고, 클러스터링 기법을 통해 데이터의 패턴을 발견하는 능력
- 데이터 전처리 및 탐색: 비지도 학습에서의 데이터 준비 과정
- 클러스터링 기법 적용: 다양한 클러스터링 알고리즘의 이해와 실습
- 최적의 클러스터 수 결정: 모델의 성능을 평가하는 방법과 시각화 기술을 통해 인사이트 도출


## 과제 가이드
- **데이터셋 탐색 및 전처리**:
    - 결측치 처리
    - 스케일링
        - 데이터의 스케일을 조정하기 위해 표준화(Standardization) 또는 정규화(Normalization)를 수행합니다
- **클러스터링 기법 적용**:
    - K-means
    - 계층적 군집화
    - DBSCAN 등의 알고리즘
- **최적의 클러스터 수 결정**:
    - 엘보우 방법 또는 실루엣 점수를 사용하여 최적의 클러스터 수를 찾습니다.
- **결과 시각화**:
    - 클러스터링 결과를 2D 또는 3D로 시각화하여 고객 세분화 결과를 분석합니다.
        - **시각화**: matplotlib 또는 seaborn을 사용하여 클러스터를 색상으로 구분하여 시각화합니다. 2D 플롯을 사용하여 각 클러스터를 다른 색으로 표현합니다.



<br>

## 🔥추가 도전 과제
- **다양한 클러스터링 기법 비교** ⭐⭐⭐⭐
    - DBSCAN 외에 Gaussian Mixture Model(GMM)와 같은 다른 클러스터링 기법을 적용하고 성능을 비교합니다.
- **고객 행동 예측 모델 구축** ⭐⭐⭐⭐⭐
    - 클러스터링 결과를 바탕으로 특정 클러스터에 속하는 고객의 행동을 예측하는 분류 모델을 구축합니다. 예를 들어, 구매 가능성을 예측하는 모델을 만들 수 있습니다.
- **시계열 분석**⭐⭐⭐⭐
    - 고객의 행동 변화를 시간에 따라 분석하여 특정 그룹의 트렌드를 시계열 데이터로 시각화합니다.

- 참고 : 시계열 분석은 진행하지 못함.

<br>

## ✍️문제 풀이
### 데이터셋 탐색 및 전처리
#### 1. 데이터 불러오기 및 확인
- 학습을 진행하기 전에 데이터를 불러오고 확인
  - CSV 파일 데이터 불러오기 : `read_csv()`
  - 데이터 미리보기(5개의 행만 확인) : `head()`
  - 데이터셋의 기본 정보 확인 : `info()`
    - 데이터 타입, 인덱스 개수, 컬럼명 등을 확인 가능
  - 결측치 확인 `isna().sum()`
    - 결측치는 0으로 확인되어서 따로 처리할 필요가 없음
    ```python
    import pandas as pd

    # 데이터 불러오기
    mall = pd.read_csv('CSV/Mall_Customers.csv')

    # 데이터 미리보기
    mall.head()

    # 데이터 정보확인
    mall.info()

    # 결측치 확인
    mall.isna().sum()
    ```

#### 2. 데이터 전처리
- 데이터 분석에 사용하지 않는 컬럼 제거 : `drop()`
  - 그냥 인덱스 역할을 하는 `CustomerID`와 0, 1로 될 `Gender`는 제외
    ```python
    # 분석에 사용하지 않는 컬럼 제거
    mall = mall.drop(columns=['CustomerID', 'Gender'])
    ```

- 이상치 확인 및 처리
  - 이상치 처리 전에 기존의 데이터와 비교를 하고 싶어서 `mall_processed` 변수를 만들어서 데이터를 복사(`copy()`)해 넣어줌
  - 이상치는 IQR 방식으로 처리하였으며 상한 및 하한값으로 대체하는 방법을 채택 
    ```python
    import numpy as np

    numerical_columns = mall.select_dtypes(include=[np.number]).columns
    mall_processed = mall.copy()

    for col in numerical_columns:
        Q1 = mall[col].quantile(0.25)
        Q3 = mall[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((mall[col] < lower_bound) | (mall[col] > upper_bound))
        if outliers.sum() > 0:
            # 이상치를 상한 및 하한값으로 대체
            mall_processed[col] = np.where(mall_processed[col] < lower_bound, lower_bound, mall_processed[col])
            mall_processed[col] = np.where(mall_processed[col] > upper_bound, upper_bound, mall_processed[col])
    ```

  - 이상치 처리 전 후를 시각화하여 표현
    ```python
    import matplotlib.pyplot as plt

    # 이상치 처리 전 데이터 시각화
    mall.boxplot()
    plt.xticks(rotation=90)
    plt.title('Before Boxplot')
    plt.tight_layout()
    plt.show()

    # 이상치 처리 후 데이터 시각화
    mall_processed.boxplot()
    plt.xticks(rotation=90)
    plt.title('After Boxplot')
    plt.tight_layout()
    plt.show()
    ```
    ![image](https://github.com/user-attachments/assets/e728ac21-2e57-4181-ae45-b58638632d79)


- 스케일링
  - StandardScaler를 사용하여 숫자형 피처 값들을 평균이 0이고 표준편차가 1이 되도록 변환
    ```python
    from sklearn.preprocessing import StandardScaler

    # 숫자형 컬럼 선택 및 스케일링
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(mall_processed[numerical_columns])
    ```

#### 3. 클러스터링 기법 적용

- K-means
  - 최적의 k를 찾기위한 '엘보우 방법' 사용
    ```python
    from sklearn.cluster import KMeans

    # 최적의 k찾기 (엘보우 방법)
    inertia = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data_scaled)
        inertia.append(kmeans.inertia_)
    
    # 엘보우 그래프
    plt.figure(figsize=(10, 5))
    plt.plot(K, inertia, 'bx-')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.show()
    ```
  - 엘보우 그래프
    - 4~6이 적당하다고 판단했지만, 정확하게 알 수가 없어서 실루엣 계수를 확인
    ![image](https://github.com/user-attachments/assets/08515199-80fa-4ede-a649-9bec7e0167fc)
  - 실루엣 계수
    ```python
    from sklearn.metrics import silhouette_score

    # 최적 클러스터 수(k = 6)로 모델 생성 및 학습
    optimal_k = 6
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    kmeans_labels = kmeans.fit_predict(data_scaled)
    kmeans_silhouette = silhouette_score(data_scaled, kmeans_labels)
    print(f'실루엣 계수: {kmeans_silhouette}')
    ```
    - 실루엣 계수가 6이 가장 좋은 결과를 보여주어 k = 6으로 시각화
      | 클러스터 수 |      4 |       5 |       6 |
      |------------:|-------:|--------:|--------:|
      | 실루엣 계수 | 0.4045 | 0.40922 | 0.43194 |

  - 계층적 군집화, DBSCAN도 진행


#### 4.결과 시각화
- 세개의 모델 모두 Annual Income vs Spending Score의 군집화가 가장 잘 되어있는 것을 확인
  ![image](https://github.com/user-attachments/assets/15dc40c3-79b6-4522-8c60-6f4180e94696)
- 각각의 모델의 실루엣 계수를 비교
  ```python
  # 모델별 성능 저장
  results = pd.DataFrame({
      'Model': ['K-means', 'Agglomerative Clustering', 'DBSCAN'],
      'Silhouette_score': [kmeans_silhouette, hc_silhouette, best_DBSCAN_silhouette]
  })

  # 서브플롯 생성
  fig = plt.figure(figsize=(18, 5))  

  plt.bar(results['Model'], results['Silhouette_score'], color='purple', width=0.5)
  plt.title('Silhouette_score Comparison')
  plt.ylabel('Silhouette_score Value')
  plt.xlabel('Model')
  plt.grid(axis='y', linestyle='--', alpha=0.7)

  # 레이아웃 조정 및 출력
  plt.show()
  ```
  ![image](https://github.com/user-attachments/assets/9cc3e2ea-94d0-4b18-a496-370479ccfd47)

- KMeans의 실루엣 계수가 가장 높음


## ✍️ 도전과제 문제 풀이
### 다양한 클러스터링 기법 비교
- Gaussian Mixture Model(GMM) 클리스터링 기법을 적용
  ```python
  from sklearn.mixture import GaussianMixture

  # GMM 모델 생성
  gmm = GaussianMixture(n_components=5, covariance_type='full')

  # 모델 학습 및 예측
  mall_processed['Cluster'] = gmm.fit_predict(data_scaled)
  ```
  - 실루엣 계수는 '0.4072'가 나옴
  ![image](https://github.com/user-attachments/assets/1df80739-2fc1-405c-9b4b-442b44a8a81e)



### 고객 행동 예측 모델 구축
- 계층적 군집화모델이 군집화가 잘되어있다고 생각되어 계층적 군집화 모델의 클리스터를 사용
- Gender을 포함시키는 것이 낫다고 판단되어 Geder 컬럼의 데이터 인코딩을 진행
  - One Hot Encoder를 사용하여 Gender_Male 컬럼을 생성(Gender 데이터가 Male이면 1, Female이면 0)
    ```python
    from sklearn.preprocessing import OneHotEncoder

    one_hot_encoder = OneHotEncoder(sparse_output=False, drop='first', dtype='int')
    gender_encoded = one_hot_encoder.fit_transform(mall[['Gender']])
    gender_encoded_df = pd.DataFrame(gender_encoded, columns=one_hot_encoder.get_feature_names_out(['Gender']))
    mall = pd.concat([mall.drop(columns=['Gender']), gender_encoded_df], axis=1)
    ```

- 분류모델
  - 클리스터를 타겟으로 결정
    ```python
    # 해당 클러스터를 타겟으로 결정
    mall_processed['Target'] = (mall_processed['Cluster'] == 5)
    mall_processed
    ```
  
  - 의사결정나무로 훈련진행
    ```python
    from sklearn.model_selection import train_test_split

    # 입력 변수와 타겟 변수
    X = mall_processed.drop(columns=['Cluster', 'Target']) 
    y = mall_processed['Target']

    # 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

    # 모델 생성 및 학습
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # 예측
    y_pred = model.predict(X_test)

    # 모델 평가
    accuracy = accuracy_score(y_test, y_pred)
    ppv = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {ppv}")
    print(f'Recall: {recall}')
    print(f'F1 scorer : {f1}')
    ```
    - 결과
      ```
      Accuracy: 0.925
      Precision: 1.0
      Recall: 0.7272727272727273
      F1 scorer : 0.8421052631578947
      ```