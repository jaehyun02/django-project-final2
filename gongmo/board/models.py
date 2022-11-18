from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20,verbose_name= '글 제목')
    content = models.TextField(verbose_name='글 내용')
    user=models.ForeignKey('users.Member',on_delete=models.CASCADE,verbose_name='글 작성자')
    createdDate=models.DateTimeField(auto_now_add=True)
    updatedDate=models.DateTimeField(auto_now=True)