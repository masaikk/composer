import random
from time import sleep

from django.http import HttpResponse, JsonResponse

from lyrics.utils.GanHandler import GanHandler
from lyrics.models import MusicLog
from lyrics.utils.instruments_list import INSTRUMENT_MAP

gan_handler = GanHandler()


# Create your views here.
def inner(request):
    return HttpResponse('ａｃｃｅｓｓ')


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


def getAudioSynth(request):
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


def testg(request):
    return None


def generate_music_from_lyrics(request):
    music_url = gan_handler.test5()
    return HttpResponse(music_url)
