import numpy as np
import pretty_midi
import time
import hashlib
import os
from lyrics.utils.tools.npyHandler import pre_process_data


def get_melody_name() -> str:
    """
    暂时是使用时间来是作为哈希的标准
    计算名字，返回
    :return: 返回哈希后的字符串作为名字
    """
    day_time = time.strftime("%y_%m_%d_%H_%M_%S", time.localtime())
    md5 = hashlib.md5()
    md5.update(day_time.encode('utf-8'))
    return md5.hexdigest()


def get4mid_url() -> (str, str, str):
    """
    用于合成路径
    :return: 返回三个路径，分别代表总路径，文件夹路径以及文件名

    """

    base_url = os.path.join(os.getcwd(), 'lyrics/temp/composer_file/')
    local_path = os.path.join(base_url, '{}/{}'.format(time.strftime("%y_%m_%d", time.localtime()),
                                                       time.strftime("%y_%m_%d_%H_%M_%S", time.localtime())))
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    file_name = get_melody_name()
    mid_file_path = os.path.join(local_path, '{}.mid'.format(file_name))
    return mid_file_path, local_path, file_name


def npy2url(data, type: int = 1, convert: bool = False) -> (str, str):
    """

    :param data:
    :param type:
    :param convert:
    :return: mid_path, mp3path
    """
    data = pre_process_data(data)
    mid_path, local_path, file_name = get4mid_url()
    midi = pretty_midi.PrettyMIDI()
    program = pretty_midi.instrument_name_to_program('Cello')
    midi_data = pretty_midi.Instrument(program=program)

    npy_sentence = data[0]
    end = 0

    for pitch in npy_sentence:
        note_number = int(pitch[3])
        last_time = pitch[4]
        rest = pitch[5]

        start = end
        end = start + last_time
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=end)
        # Add it to our cello instrument
        midi_data.notes.append(note)

        if rest != 0:
            end += rest
    midi.instruments.append(midi_data)
    midi.write(mid_path)
    print('generated mid {}'.format(mid_path))
    if convert:
        import lyrics.utils.tools.convert_mid2mp3handler
        mp3path = lyrics.utils.tools.convert_mid2mp3handler.convert_mid2mp3(mid_path)
    else:
        mp3path = ''
    return mid_path, mp3path


if __name__ == '__main__':
    print(npy2url(None))
