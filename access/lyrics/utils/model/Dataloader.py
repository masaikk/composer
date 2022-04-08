import torch
import numpy as np
from torch.utils import data
import os

class Dataloader(data.Dataset):


    def __init__(self, embeddings_fname, vocab_fname, seq_len):


        self.lyrics_seq = torch.Tensor(np.load(os.path.join(os.getcwd(), 'lyrics/utils/model/static/data(11149,20,20).npy'),allow_pickle=True))
        # (11148*20*20)
        print('load lyrics_seq')

        # self.cont_attr_seq = torch.zeros(self.lyrics_seq.size())
        # print('load cont_attr_seq')
        # print(self.cont_attr_seq.shape)

        self.discrete_attr_seq = torch.tensor(np.load(os.path.join(os.getcwd(), 'lyrics/utils/model/static/data(11149,20,3).npy'),allow_pickle=True))
        print('load discrete_attr_seq')
        # , ,  = self.create_training_data()
        # (11148*20*3)

    def __len__(self):
        #         print(len(self.lyrics_seq))
        return len(self.lyrics_seq)

    def __getitem__(self, i):
        lyrics_seq = self.lyrics_seq[i]
        discrete_val_seq = self.discrete_attr_seq[i]
        return lyrics_seq,  discrete_val_seq
