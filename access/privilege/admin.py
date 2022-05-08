from django.contrib import admin

# Register your models here.
from privilege.models import User
from lyrics.models import MusicLog


@admin.register(User)
@admin.register(MusicLog)
class UserAdmin(admin.ModelAdmin):
    pass
