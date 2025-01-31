# 🗂️Directory Structure
```
📦main
 ┣ 📜Figure_1.png   # 상위 10개 단어 그래프 이미지
 ┣ 📜main.py        # 기본 예제
 ┣ 📜main2.py       # CPU/GPQ 비교
 ┣ 📜main3.py       # LLMA에게 번역까지 시킨 예제
 ┗ 📜main4.py       # DB 저장 예제
```

<br>

# Prompt Engineering 
- AI 모델(특히 LLM)과 효과적으로 상호작용하기 위해 프롬프트(입력 문구)를 최적화하는 기술
- 성능을 극대화하기 위한 기술로 다음의 요소가 포함됨
  - **프롬프트 최적화** : 특정 응답을 유도하는 문구를 설계
  - **Few-shot / Zero-shot Learning** : 적은 예제로 모델이 올바르게 답하도록 유도
  - **Chain-of-Thought Prompting** : 단계별 사고 과정을 유도하는 프롬프트 작성

## Prompt Engineering이 중요한 이유
- 같은 모델이라도 프롬프트를 어떻게 작성하느냐에 따라 결과가 극적으로 달라짐
- API 호출 비용 절감 및 실행 속도 최적화 가능
- 특정 도메인(법률, 의료, 코딩)에 최적화된 답변 유도

<br>

## 명령을 비교해보기
### 한국어로 번역하기
- 일반 모델과 같이 답변을 하고, 그 답변을 한국어로 번역해달라고 요청하여 번역을 받는 모델 생성

    ```python
    from transformers import AutoTokenizer, AutoModelForCausalLM

    # LLaMA 모델 load
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

    # 입력 메시지
    input_text = "What is the capital of England?"
    inputs = tokenizer(input_text, return_tensors="pt")

    # 응답 생성
    outputs = model.generate(**inputs, max_new_tokens=100)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("response : ", response)


    # LLaMA에게 번역 요청
    translation_prompt = (
        "You are a professional translator who translates English to Korean.\n\n"
        "Translate the following English text into fluent and natural Korean:\n\n"
        f"English: {response}\n\n"
        "Korean:"
    )
    translation_inputs = tokenizer(translation_prompt, return_tensors="pt")

    # 번역 실행
    translated_tokens = model.generate(**translation_inputs, max_new_tokens=100)
    korean_translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    print("한국어로 번역 :", korean_translation)
    ```

- 결과
  - 번역 품질이 너무 떨어짐
  - 한국어를 지원하는 모델을 사용하거나 다른 번역 모델이 필요할 것 같음

  ![Image](https://github.com/user-attachments/assets/cd7bff10-9164-4be7-853d-ff37bd56dd7d)


### 1가지 직무를 1줄로 매우 간결하게 작성
- 질문

  ```python
  input_text = "You are an AI tutor. What are the best resources for learning Python?"
  ```


- 답변

  ```
  Python is a popular programming language used in a wide range of applications, including web development, data science, machine learning, and more. Here are some of the best resources for learning Python:    

  1. Codecademy: Codecademy is an online platform that offers interactive coding lessons in Python and other programming languages. Their Python course covers the basics of Python syntax, data types, control structures, functions, and more.
  2. Python.org: The official Python website is a great resource for learning Python. It includes a comprehensive tutorial for beginners, as well as reference materials for advanced users.
  3. Udemy: Udemy offers a wide range of Python courses, from beginner to advanced levels. You can find courses on specific topics like data science, machine learning, and web development, as well as more general courses on Python programming.
  ```


- 견해
  - 필요하지 않는 내용을 포함하지만, 그래도 자료를 추천해주고 자료에 대한 내용을 명시함

### 1가지 직무를 최소 5줄 이상로 매우 상세하게 작성
- 질문

```python
input_text = """
    I am new to programming and want to learn Python. 
    My goal is to create an AI-powered webpage. However, I'm not sure where to start. 
    Could you recommend some good learning resources or courses for beginners? 
    Also, any tips on how to study efficiently and suggestions on what else I should learn would be greatly appreciated.
    """
```


- 답변

  ```
  Congratulations on taking the first step towards learning Python and creating an AI-powered webpage! It's an exciting and rewarding journey, and I'm happy to help you get started.

  Here are some excellent learning resources and courses for beginners:

  1. Codecademy: Codecademy is an excellent platform for learning Python. They offer interactive coding lessons and exercises that cover the basics of Python programming. Their courses are designed for beginners and cover topics such as data types, functions, and control structures.
  2. Python.org: The official Python website is an excellent resource for learning Python. They offer a comprehensive tutorial that covers the basics of Python programming, including data types, functions, and control structures. They also provide links to other resources and tutorials that can help you deepen your understanding of Python.
  3. Coursera: Coursera is an online learning platform that offers a wide range of courses on Python programming. They have courses taught by experienced instructors from top universities, including Stanford, Duke, and UVA. Their courses are designed for beginners and cover topics such as Python basics, data analysis, and machine learning.
  4. edX: edX is another online learning platform that offers a wide range of courses on Python programming. They have courses taught by experienced instructors from top universities, including MIT, Harvard, and UC Berkeley. Their courses are designed for beginners and cover topics such as Python basics, data science, and machine learning.
  5. Udemy: Udemy is an online learning platform that offers a wide range of courses on Python programming. They have courses taught by experienced instructors who cover a variety of topics, including Python basics, data analysis, and machine learning.

  In addition to these resources, here are some tips on how to study efficiently:
  ```

- 견해
  - 내용이 조금 더 풍부해지고, 어떤 것을 가르쳐 주는지 더 자세히 서술되어 있음

### 3가지 이상 직무를 많이 풀어서 상세하고 복잡하게 작성
- 질문
  ```python
  input_text = """
      I want to develop an AI-powered web service and focus on three key areas: model development, web integration, and cloud deployment.
      Model Development: I want to train AI models and make them practical for real-world applications.
      Web Integration: I plan to integrate AI models into a web application using Django.
      Cloud Deployment: I aim to efficiently deploy my web service using platforms like AWS, Google Cloud, or Azure.
      Could you recommend learning resources that cover these topics?
      """
  ```

- 답변
  
    ```
      Sure! Here are some learning resources that can help you develop AI-powered web services:
    1. Andrew Ng's Machine Learning Course on Coursera: This course provides a comprehensive introduction to machine learning and deep learning.
    2. TensorFlow Tutorials: TensorFlow offers a range of tutorials and guides for building and deploying AI models.
    3. AWS AI and Machine Learning Blog: This blog provides insights and best practices for deploying AI models on AWS.
    4. Google Cloud AI Platform: This platform offers a range of tools and services for building and deploying AI models.
    5. Azure Machine Learning: This platform provides a range of tools and services for building and deploying AI models.
    6. Django Tutorials: Django is a popular web framework for building web applications. These tutorials can help you integrate AI models into your web application.
    7. AWS Lambda Tutorials: AWS Lambda is a serverless computing platform that can help you deploy your web service efficiently.
    8. Python Machine Learning Library: This library provides a range of tools and libraries for building and deploying AI models.
    9. Data Science Handbook: This handbook provides insights and best practices for building and deploying data-driven web applications.
    10. AI for Everyone: This book provides a comprehensive introduction to AI and its applications in various industries.

    I hope these resources help you develop your AI-powered web service!
    ```

- 견해
  - 답변이 조금 더 상세해지고, 내용이 조금 더 깔끔해지며 필요한 것만 콕콕 찝어 보여줌

<br>

# Cloud와 On-premis
## ☁️Cloud 
### 개념
- 클라우드는 인터넷을 통해 제공되는 컴퓨팅 리소스(서버, 스토리지, 네트워크, AI 서비스 등)를 사용하는 방식
- 사용자는 물리적인 서버를 직접 관리할 필요없이, 필요한만큼만 빌려쓰고 비용을 지불하는 구독형 모델이 일반적
- 예시
  - AI 모델 훈련 시 GPU 서버 임대 (AWS EC2, Google Cloud Vertex AI)
  - 데이터 저장/관리 (AWS S3, Google Cloud Storage)
  - 서버리스 컴퓨팅 활용 (AWS Lambda, Google Cloud Functions)

### 장단점
- ✅장점
  - 초기 비용이 낮음 : 하드웨어를 직접 구매하지 않아도 됨
  - 유연한 확장성 : 필요할 때 리소스를 즉시 추가 가능
  - 운영 및 유지보수 부담 감소 : 클라우드 업체(AWS, GCP 등)가 관리
  - 다양한 AI 및 빅데이터 서비스 제공 : GPU/TPU 등 고성능 연산 장비 사용 가능
- ❌단점
  - 장기적으로 비용이 증가할 수 있음 : 지속적인 사용 시 온프레미스보다 비싸질 수 있음
  - 보안 및 데이터 주권 문제 : 클라우드에 저장된 데이터는 외부 해킹의 대상이 될 가능성이 있음
  - 인터넷 연결 의존 : 네트워크 속도에 따라 성능이 좌우됨

<br>

## 🏢On-premis
### 개념
- 기업이나 기관이 직접 소유한 데이터센터나 서버에서 IT 시스템을 운영하는 방식
- 즉, 모든 하드웨어 및 소프트웨어를 자체적으로 구축하고 관리하는 방식
- 예
  - 금융기관: 고객 데이터 보안을 위해 내부 데이터센터 운영
  - 의료기관: 민감한 환자 정보를 보호하기 위해 자체 서버 운영
  - AI 연구소: 대규모 GPU 클러스터를 직접 구축하여 AI 모델 학습

### 장단점
- ✅장점
  - 데이터 보안 및 통제력 : 외부 클라우드에 의존하지 않으므로, 데이터 주권이 보장됨
  - 장기적으로 비용 절감 가능 : 지속적인 사용 시 클라우드보다 저렴할 수 있음
  - 네트워크 지연(Latency) 최소화 : 내부 서버에서 직접 처리하므로 속도가 빠름
  - 특수 환경에 적합 : 금융, 의료, 정부기관 등의 보안이 중요한 환경
- ❌단점
  - 초기 비용이 높음 : 서버, 스토리지, 네트워크 장비 등의 초기 투자 비용이 큼
  - 확장성이 낮음 : 리소스를 늘리려면 새로운 장비를 구매해야 함
  - 운영 및 유지보수 필요 : IT 인력이 직접 서버를 관리해야 하며, 장애 발생 시 직접 대응해야 함

<br>

## Cloud vs On-premise

| 비교 항목          | Cloud (클라우드)              | On-premise (온프레미스)   |
|:------------------:|:-----------------------------:|:-------------------------:|
| 초기 비용          | 낮음 (필요한 만큼 사용)       | 높음 (서버 직접 구매)     |
| 운영 및 유지보수   | 클라우드 업체가 관리          | 자체 유지보수 필요        |
| 확장성             | 즉시 확장 가능                | 하드웨어 추가 필요        |
| 보안 & 데이터 주권 | 보안 이슈 가능 (외부 저장소)  | 내부망에서 보안 유지 가능 |
| 네트워크 속도      | 인터넷 속도에 의존            | 로컬 환경이므로 빠름      |
| 장기 비용          | 사용량 증가 시 비용 증가      | 장기적으로 비용 절감 가능 |


# CPU와 GPU
- CPU: 범용적인 연산을 수행하며, 적은 수의 코어에서 직렬(Sequential)로 연산을 수행
- GPU: 병렬 연산에 특화되어 있어 대량의 데이터 연산을 빠르게 수행
- CPU + GPU: 일부 연산을 CPU에서 처리하고, 주요 연산을 GPU에서 수행하여 속도를 높이는 방식

## 직접 비교해보기
### CPU만 사용
```python
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="cpu",
    offload_folder="offload",
    offload_state_dict=True
)
```

- ⏰실행 시간 : 108.83초

### GPU만 사용
```python
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="cuda",
    offload_folder="offload",
    offload_state_dict=True
)
```
- 현재 노트북의 RTX 3050은 VRAM이 4GB라서 대형 모델을 로드할때 메모리가 부족하여 실행 불가

### CPU + GPU를 사용
```python
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    offload_folder="offload",
    offload_state_dict=True
)
```

- ⏰실행 시간 : 105.84초

### 결론
사실 큰 차이는 못 느끼겠어서 검색을 해보니 CPU > CPU+GPU > GPU 순이라고 한다. 
- CPU는 속도가 느리고, CPU 사용률이 급격히 증가
- GPU는 속도가 빠르며, VRAM을 많이 사용
- GPU+CPU의 경우 GPU의 메모리가 부족한 경우 유용

<br>

# DB 저장하기
- 번역의 퀄리티가 너무 좋지 않아서 이상한 단어도 추출하고 '~의'가 붙는 것도 단어로 판정
  - 이건 내가 수정할 필요가 있음🤔
- 한국의 여행지를 추천해달라고 해서 '한국'이 가장 많이 나온 것으로 예상

  ![Image](https://github.com/user-attachments/assets/e716ba21-9d3d-40d7-ade8-2314502abc09)