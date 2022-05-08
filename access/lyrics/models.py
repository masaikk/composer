from django.db import models

# Create your models here.
from privilege.models import User

class MusicLog(models.Model):
    mid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instru_id = models.IntegerField(default=1)
    sentence = models.CharField(max_length=256)
    create_time = models.DateTimeField(auto_now=True)
    duration_time = models.FloatField(default=0.0)
    file_path = models.CharField(max_length=256, default='-')

    class Meta:
        db_table = 'lyrics_music'