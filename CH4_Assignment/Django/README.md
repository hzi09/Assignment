# Django에 Chatbot app 추가하기

- models.py
    ```python
    class Chatbot(models.Model) :
        user_message = models.TextField()
        gpt_message = models.TextField()
    ```

- views.py
    ```python
    def py_tutor(request) :
        if request.method == 'POST' :
            user_message = request.POST.get('user_message')
            if user_message :
                bot_response = gpt(user_message)
                Chatbot.objects.create(user_message=user_message, gpt_message=bot_response)
                
                # 최근 10개의 데이터만 가져오기
                chat_history = Chatbot.objects.all().order_by('-pk')[:10]
                context ={
                    "chat_history" : chat_history,
                }
                return render(request, 'chatbot/chatbot.html', context)
        return render(request, 'chatbot/chatbot.html')
    ```

- 구현 화면
    ![Image](https://github.com/user-attachments/assets/33f589cd-3eb4-4fb3-b20a-15e6e41b071f)