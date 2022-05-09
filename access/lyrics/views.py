import random
from time import sleep

from django.http import HttpResponse, JsonResponse

from lyrics.utils.GanHandler import GanHandler
from lyrics.models import MusicLog
from lyrics.utils.instruments_list import INSTRUMENT_MAP
import shutil
import os


gan_handler = GanHandler()
music_base_path = '/tmp/musicpath/'


# Create your views here.
def inner(request):
    return HttpResponse('access root')


def get_instru_list(request):
    res_list = []
    for instru_index in range(len(INSTRUMENT_MAP)):
        res_list.append({
            'value': str(instru_index),
            'name': INSTRUMENT_MAP[instru_index]
        })
    return JsonResponse({
        'INSTRUMENT_MAP': res_list
    })


def get_audio_synth(request):
    music_url = 'http://119.23.182.180/azur/t{}.mp3'.format(random.randint(1, 5))
    print('Audio url : {}'.format(music_url))
    sleep(0.5)
    music_log = MusicLog()
    music_log.sentence = request.GET.get('lyrics')
    music_log.instru_id = int(request.GET.get('instrumentID'))
    music_log.user_id = int(request.GET.get('uid'))
    music_log.file_path = '--'
    music_log.save()
    res_obj = {
        'music_url': music_url
    }

    return JsonResponse(res_obj)


def generate_music_from_no_lyrics(request):
    # desaturate
    music_url = gan_handler.test6()
    return HttpResponse(music_url)


def generate_music_from_lyrics(request):
    sentence = request.GET.get('lyrics')
    instru_type = int(request.GET.get('instru'))
    uid = int(request.GET.get('uid'))
    music_url = gan_handler.generate_audio_with_sentence_type(sentence=sentence, instru=instru_type)
    # music_url like '/home/b8313/coding/composer/access/lyrics/temp/composer_file/22_05_09/22_05_09_09_04_23/0d74914047a2b55cd8341c7b58529781.mp3'
    (file_path, server_file_name) = os.path.split(music_url)
    server_base_path = 'http://127.0.0.1:8081/'
    shutil.copyfile(music_url, os.path.join(music_base_path, server_file_name))
    server_file_path = os.path.join(server_base_path, server_file_name)
    print(server_file_path)
    music_log = MusicLog()
    music_log.sentence = sentence
    music_log.instru_id = instru_type
    music_log.user_id = uid
    music_log.file_path = server_file_path
    music_log.save()
    return JsonResponse({
        'music_url': server_file_path
    })
