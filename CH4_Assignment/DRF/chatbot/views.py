from rest_framework.response import Response
from rest_framework.views import APIView
from openai import OpenAI
from django.conf import settings
from .models import Chat

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class ChatView(APIView):
    def post(self, request):
        user_message = request.data.get("message")

        if not user_message:
            return Response({"error": "message is required"}, status=400)

        # DB에서 최근 5개 대화 불러오기
        previous_chats = Chat.objects.all().order_by('-timestamp')[:5]
        chat_history = [{"role": chat.role, "content": chat.content} for chat in previous_chats]

        # OpenAI API 요청
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "너는 Python 튜터야. 사용자가 코드를 직접 작성하도록 도와줘."},
                *chat_history,  # 이전 대화 전달
                {"role": "user", "content": user_message},
            ]
        )
        
        response_message = completion.choices[0].message.content

        # DB에 사용자 질문과 GPT 응답 저장
        Chat.objects.create(role="user", content=user_message)
        Chat.objects.create(role="assistant", content=response_message)

        return Response({"response": response_message})
