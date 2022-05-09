from django.urls import path, re_path

from lyrics import views

app_name = 'lyrics'

urlpatterns = [
    path('getInstruList/', views.get_instru_list, name='instru'),
    path('', views.inner),
    path('getAudioPath/', views.get_audio_synth),
    path('generateAudio/', views.generate_music_from_lyrics)

]
