import numpy as np
import os


class Seq2EmbHandler():
    def __init__(self):
        self.w2e_model = None
        self.l2e_model = None
        self.load_embedding_model()

    def load_embedding_model(self):
        pass

    def seq2Emb(self, seq):
        pass

    def seq2EmbTest(self, seq=None):
        seq_test_data_url = os.path.join(os.getcwd(), 'lyrics/utils/model/static/test_seq_emb.npy')
        test_data = np.load(seq_test_data_url, allow_pickle=True)
        return test_data


