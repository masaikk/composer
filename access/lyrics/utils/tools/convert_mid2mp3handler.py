import os
from midi2audio import FluidSynth


def convert_mid2mp3(mid_path) -> str:
    fs = FluidSynth()
    path, temp = os.path.split(mid_path)
    file_name, extension = os.path.splitext(temp)
    mp3path = os.path.join(path, '{}.mp3'.format(file_name))
    # print(mp3path)
    fs.midi_to_audio(mid_path, mp3path)
    return mp3path
