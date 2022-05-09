import numpy as np
import os
import re
from gensim.models import Word2Vec


class Seq2EmbHandler():
    def __init__(self):
        self.w2e_model = None
        self.s2e_model = None
        self.ws_dict = None
        self.word_dict_path = os.path.join(os.getcwd(), 'lyrics/utils/model/static/word_syll_dic1.npy')
        self.word2vec_path = os.path.join(os.getcwd(), 'lyrics/utils/model/static/wordLevelEncoder_20190419.bin')
        self.syll2vec_path = os.path.join(os.getcwd(), 'lyrics/utils/model/static/syllEncoding_20190419.bin')
        self.load_embedding_model()

    def processMelody(self, lyrics: str) -> str:
        """
        格式化歌词数据，去标点以及补齐或者剪切。

        :param lyrics: 歌词
        :return:
        :rtype: str
        """
        remove_chars = '[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
        return re.sub(remove_chars, '', lyrics)

    def load_embedding_model(self):
        self.ws_dict = np.load(self.word_dict_path, allow_pickle=True).tolist()
        self.w2e_model = Word2Vec.load(self.word2vec_path)
        self.s2e_model = Word2Vec.load(self.syll2vec_path)

    def seq2Emb(self, sentence: str) -> (np.ndarray, int):
        data_matrix = np.zeros(shape=(400))
        total_syll_number = 0
        for word in sentence.split(' '):
            if word not in self.ws_dict.keys():
                pass
            else:
                try:
                    word_embedding = self.w2e_model.wv[word]
                except KeyError:
                    word_embedding = np.zeros(shape=(10))
                syll_list = self.ws_dict[word][0]
                # 选择第0个列表
                for syll in syll_list:
                    try:
                        syll_embedding = self.s2e_model.wv[syll]
                    except:
                        syll_embedding = np.zeros(shape=(10))
                    word_syll_embedding = np.concatenate((syll_embedding, word_embedding))
                    # 先是音节嵌入后是单词嵌入，是个20维的向量
                    data_matrix[total_syll_number * 20:(total_syll_number + 1) * 20] = word_syll_embedding
                    total_syll_number += 1
                    if total_syll_number == 20:
                        return data_matrix, total_syll_number
        return data_matrix, total_syll_number

    def seq2EmbTest(self, seq=None):
        seq_test_data_url = os.path.join(os.getcwd(), 'model/static/test_seq_emb.npy')
        test_data = np.load(seq_test_data_url, allow_pickle=True)
        return test_data
