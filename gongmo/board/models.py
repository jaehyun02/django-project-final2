from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20,verbose_name= '공모전 이름& 구인인원')
    content = models.TextField(verbose_name='카카오톡 오픈 채팅방 url')
    user=models.ForeignKey('users.Member',on_delete=models.CASCADE,verbose_name='글 작성자')
    createdDate=models.DateTimeField(auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True)