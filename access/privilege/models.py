from django.db import models


# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=16, default='-')
    user_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lyrics_user'


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_sentence = models.CharField(max_length=256, default='该用户没有留下评论')
    comment_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
