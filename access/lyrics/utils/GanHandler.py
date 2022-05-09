from lyrics.utils.model.Gan import Gan
from lyrics.utils.model.seq2emb import Seq2EmbHandler
from lyrics.utils.tools.npyHandler import pre_process_data
from lyrics.utils.tools.npy2urlTools import npy2url
import torch


import os
import numpy as np


class GanHandler():
    def __init__(self):
        self.gan = Gan()
        print('model loaded!')
        self.embedding_handler = Seq2EmbHandler()
        print('embedding model loaded!')

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
        midi_url, mp3_url = npy2url(midi_raw_data, convert=True)
        # print(midi_url)
        return mp3_url

    def test6(self):
        user_seq_data, number = self.embedding_handler.seq2Emb('what a nice day it is at all.')
        user_seq_data = user_seq_data.reshape((20, -1))
        user_seq_data = np.expand_dims(user_seq_data, 0)

        seq_data = torch.from_numpy(np.repeat(user_seq_data, 300, axis=0))
        seq_data = seq_data.to(torch.float32)

        midi_raw_data = self.gan.npy2embedding_generator2npyData(seq_data=seq_data).numpy()
        midi_url, mp3_url = npy2url(midi_raw_data, instru_type=56, convert=True)
        # print(midi_url)
        return mp3_url


if __name__ == '__main__':
    g = GanHandler()
    g.test6()
