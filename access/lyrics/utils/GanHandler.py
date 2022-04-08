from lyrics.utils.model.GeneratorRMC import GeneratorRMC
from lyrics.utils.model.Dataloader import Dataloader
from lyrics.utils.model.Gan import Gan
from lyrics.utils.model.seq2emb import Seq2EmbHandler
from lyrics.utils.tools.npyHandler import pre_process_data
from lyrics.utils.tools.npy2urlTools import npy2url
import torch
import torch.nn as nn
from torch.utils import data
import yaml
from torch import optim
import time

import os
import numpy as np


class GanHandler():
    def __init__(self):
        self.gan = Gan()
        print('model loaded!')
        self.embedding_handler = Seq2EmbHandler()
        print('embedding model loaded!')

    def processMelody(self, lyrics) -> str:
        """


        :param lyrics: 歌词
        :return:
        :rtype: str
        """
        return ''

    def test1(self):
        self.gan.get_gen_data_test()

    def test2(self):
        pass

    def test3(self):
        user_seq_data = self.embedding_handler.seq2EmbTest()
        user_seq_data = np.expand_dims(user_seq_data, 0)
        seq_data = torch.from_numpy(np.repeat(user_seq_data, 300, axis=0))
        midi_raw_data = self.gan.npy2embedding_generator2npyData(seq_data=seq_data)
        pass

    def test4(self):
        user_seq_data = self.embedding_handler.seq2EmbTest()
        user_seq_data = np.expand_dims(user_seq_data, 0)
        seq_data = torch.from_numpy(np.repeat(user_seq_data, 300, axis=0))
        midi_raw_data = self.gan.npy2embedding_generator2npyData(seq_data=seq_data).numpy()
        midi_data = pre_process_data(midi_raw_data)
        pass

    def test5(self):
        # 这里输出mp3的路径，整理一下就可以发到前端。
        user_seq_data = self.embedding_handler.seq2EmbTest()
        user_seq_data = np.expand_dims(user_seq_data, 0)
        seq_data = torch.from_numpy(np.repeat(user_seq_data, 300, axis=0))
        midi_raw_data = self.gan.npy2embedding_generator2npyData(seq_data=seq_data).numpy()
        midi_url,mp3_url = npy2url(midi_raw_data, convert=True)
        # print(midi_url)
        return mp3_url


if __name__ == '__main__':
    g = GanHandler()
    g.test5()
