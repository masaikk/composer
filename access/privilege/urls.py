from django.urls import path, re_path

from privilege import views

app_name = 'privilege'

urlpatterns = [
    path('', views.my, name='my'),
    path('add_usr/', views.add_usr, name='add_usr'),
    path('add_sen/', views.add_sen, name='add_sen'),
    path('get_log/', views.get_log, name='find_log'),
    path('user_info/', views.get_user_info, name='user_info'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('get_comments_by_id/', views.get_comments_by_uid, name='comment_by_id'),
    path('get_comments/', views.get_comments, name='comments_list')

]
