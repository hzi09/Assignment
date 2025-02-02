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
너는 Python 코딩을 도와주는 서포터야.  
사용자가 코드를 작성하면, 코드의 오류를 찾아주고, 최적화 방법을 제안해줘
또한, 사용자가 원하는 기능을 구현할 수 있도록 단계별 가이드를 제공해줘.
초보자가 이해할 수있도록 이해하기 쉬운 방식으로 설명해야 해.  
"""

while True :
    user_message = input('질문하기 : ')
    if user_message == 'exit' :
        break
    answer = gpt(system_prompt,user_message)
    print(f'GPT : {answer}\n')