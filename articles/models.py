from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Article모델 인스턴스가 문자열로 표현될 때, title필드의 값을 사용하도록 
    def __str__(self):
      return str(self.title)
    