import openai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# API Key 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def gpt(message) :
    prompt = """
    너는 파이썬 함수를 알려주는 서포터야.
    내가 파이썬 함수를 입력하면, 함수의 역할과 사용방법에 대해 알려주고 간단한 예시도 알려줘.
    """
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