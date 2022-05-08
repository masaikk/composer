from django.urls import path, re_path

from privilege import views

app_name = 'privilege'

urlpatterns = [
    path('', views.my, name='my'),
    path('add_usr/', views.add_usr, name='add_usr'),
    path('add_sen/', views.add_sen, name='add_sen'),
    path('get_log/', views.get_log, name='find_log')

]
