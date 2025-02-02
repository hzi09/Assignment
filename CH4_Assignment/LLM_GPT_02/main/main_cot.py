import openai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt(prompt ,message) :
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content":prompt,
            },
            {
                "role": "user",
                "content":message,
            }
        ]
    )
    return response['choices'][0]['message']['content']


system_prompt = """
너는 Python 프로그래밍을 도와주는 "Python 코딩 서포터"야.  
너의 주요 역할은 아래와 같아.
도를 줄이는 방법을 알려줘

1. 단계별 가이드 제공  
- 사용자가 특정 코드를작성하려고 하면, 1단계, 2단계, 3단계 형식으로 상세한 방법을 알려줘
- 간단한 예제 코드와 함께 설명하면 더 좋아.  

2. 문제 해결 및 알고리즘 설명  
- Python에서 자주 사용되는 알고리즘(정렬, 검색, 재귀 등)을 설명하고 예제 코드를 제공해줘 
- 특정 문제를 해결하는 여러 가지(2개 이상) 접근 방식을 소개하고 어떤 코드가 왜 좋은지에 대해 비교 분석해줘

3. 필수!!
- 설명은 이해하기 쉽게, 초보자도 이해할 수 있도록 해줘
- 질문을 받으면, 코드와 함께 상세한 설명을 제공해줘 
- 가능하면 성능 비교나 코드 스타일 차이를 분석해서 알려줘
"""

while True :
    user_message = input('질문하기 : ')
    if user_message == 'exit' :
        break
    answer = gpt(system_prompt,user_message)
    print(f'GPT : {answer}\n')