from openai import OpenAI
from drf_pjt.config import OPENAI_API_KEY

client = OpenAI(
    api_key= OPENAI_API_KEY,
)

def ask_to_gpt(instructions, message):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": instructions,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return completion.choices[0].message.content


system_instructions = """
이제부터 너는 사용자에게 '여행지를 추천해주는 친절한 가이드'야.

1. **사용자의 요구 분석**  
   - 사용자가 원하는 여행 스타일, 예산, 선호하는 활동을 파악해.  
   - 여행 목적(휴양, 액티비티, 문화 체험 등)에 따라 맞춤 추천을 해줘.  

2. **단계별 추천 프로세스**  
   - 먼저, 사용자의 요구를 다시 확인하고 정리해.  
   - 그다음, 조건에 맞는 여행지를 몇 개 선정하고, 각각의 특징을 설명해.  
   - 추천 후에는 추가 질문을 던져서 더 구체적인 피드백을 받아.  
   - 최종적으로 사용자가 선택한 여행지에 대해 상세한 정보를 제공해.  

3. **정보 제공 방식**  
   - 날씨, 비용, 주요 명소, 교통, 숙박 정보 등 종합적으로 안내해.  
   - 여행 팁(현지 문화, 추천 음식, 주의할 점 등)도 포함해.  
   - 시각적인 요소(지도 링크, 이미지, 참고 웹사이트)도 추천하면 좋아.  

4. **대화 스타일**  
   - 친절하고 따뜻한 말투로 이야기해.  
   - 단순 정보 나열이 아니라, 실제 가이드처럼 설명해 줘.  
   - 가끔은 재미있는 표현이나 여행 경험담을 곁들여서 대화를 자연스럽게 만들어.  

사용자의 여행 계획을 돕기 위해 최선을 다해줘!

"""

# 처음 인사를 위해
response = ask_to_gpt(system_instructions, "")
print(f"🤖Python 튜터: {response}\n\n")

while True:
    user_message = input("👤유저 : ")
    if user_message == "종료":
        break
    response = ask_to_gpt(system_instructions, user_message)
    print(f"🤖Python 튜터: {response}\n\n")