from django.urls import path, re_path

from privilege import views

app_name = 'privilege'

urlpatterns = [
    path('/', views.my, name='my'),

]