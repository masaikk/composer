from django.contrib import admin

# Register your models here.
from privilege.models import User, Comment
from lyrics.models import MusicLog


@admin.register(User)
@admin.register(MusicLog)
@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    pass
