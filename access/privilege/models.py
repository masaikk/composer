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
