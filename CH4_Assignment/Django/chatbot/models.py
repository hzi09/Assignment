from django.db import models

class Chatbot(models.Model) :
    user_message = models.TextField()
    gpt_message = models.TextField()
