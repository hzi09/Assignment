from django.shortcuts import render, redirect
from .models import Chatbot 
from .bot import gpt


def py_tutor(request) :
    if request.method == 'POST' :
        user_message = request.POST.get('user_message')
        if user_message :
            bot_response = gpt(user_message)
            Chatbot.objects.create(user_message=user_message, gpt_message=bot_response)
            chat_history = Chatbot.objects.all().order_by('-pk')[:10]
            context ={
                "chat_history" : chat_history,
            #     "user_message": user_message,
            #     "bot_response": bot_response,
            }
            return render(request, 'chatbot/chatbot.html', context)
    return render(request, 'chatbot/chatbot.html')
