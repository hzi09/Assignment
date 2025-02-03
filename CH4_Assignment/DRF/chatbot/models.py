from django.db import models

class Chat(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('assistant', 'Assistant'),
    )
    
    chat_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.role}"
