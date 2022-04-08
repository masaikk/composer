from django.urls import path, re_path

from lyrics import views

app_name = 'lyrics'

urlpatterns = [
    path('getI/', views.hello, name='hello'),
    path('t1/',views.generat),
    path('t2/',views.testg),
    path('t3/',views.generate_music_from_lyrics)


]
