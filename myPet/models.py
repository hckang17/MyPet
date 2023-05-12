from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Poster(models.Model):     #게시글 class
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Poster_author')
    subject = models.CharField(max_length=40)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Comment_author')
    poster = models.ForeignKey(Poster, on_delete=models.CASCADE)    # 코멘트는 포스터에 연결될 예정
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

