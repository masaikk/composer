from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from privilege.models import User
from lyrics.models import MusicLog


# Create your views here.
def my(request):
    return HttpResponse('user config site')


def mainPage(request):
    return HttpResponse('Welcome to Composer')


def add_usr(request):
    user_name = request.GET.get('name')
    user_pwd = request.GET.get('pwd')
    new_user = User()

    new_user.username = user_name
    new_user.password = user_pwd
    new_user.save()

    return HttpResponse('Added user {} with password {} .'.format(user_name, user_pwd))


def add_sen(request):
    user_id = request.GET.get('uid')
    sen = request.GET.get('sen')
    instru_id = request.GET.get('instru')
    new_music_log = MusicLog()
    new_music_log.instru_id = instru_id
    new_music_log.user_id = user_id
    new_music_log.sentence = sen
    new_music_log.save()
    return HttpResponse('uid : {} , sen : {} '.format(user_id, sen))


def get_log(request):
    uid = request.GET.get('uid')

    logs = MusicLog.objects.filter(user_id=int(uid))
    response_logs = {"logs": []}
    for log in logs:
        response_logs['logs'].append({
            'mid': log.mid,
            "uid": log.user_id,
            "instru_id": log.instru_id,
            "create_time": log.create_time,
            "duration_time": log.duration_time,
            "file_path": log.file_path
        })

    return JsonResponse(response_logs)
