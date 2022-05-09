from lyrics.utils.model.GeneratorRMC import GeneratorRMC
from lyrics.utils.model.Dataloader import Dataloader
import torch
from torch.utils import data
import yaml
import time
import os
import numpy as np


class Gan():
    def __init__(self, gen_path=None):
        self.save_per_epoch: int = 10
        self.head_size: int = 256
        self.num_heads: int = 2
        self.mem_slots: int = 1
        self.discriminator_input_dim_music: int = 3
        self.lyrics_dis_rate: float = 0.5
        self.train_data_iterator = None
        self.sequence_len: int = 10
        self.train_D_steps: int = 1
        self.train_G_steps: int = 1
        self.total_epoch: int = 30
        self.this_time = time.strftime("%y_%m_%d_%H_%M_%S", time.localtime())
        self.this_day = time.strftime("%y_%m_%d", time.localtime())
        # default config, you should change in yaml file.
        self.data_params: dict = {'batch_size': 100,
                                  'shuffle': True,
                                  'num_workers': 6}
        # This dic to load data
        self.load_flag: bool = False
        self.learning_rate_D: float = 0.1
        self.learning_rate_G: float = 0.0001
        self.discriminator_out_dim: int = 1
        self.discriminator_input_dim: int = 1
        self.generator_out_dim: int = 3
        self.hidden_dim: int = 400
        self.ff1_out: int = 400
        self.lyrics_dim: int = 64
        self.embed_dim: int = 32
        self.cuda: bool = False
        self.read_yaml(os.path.join(os.getcwd(), 'lyrics/utils/model/config.yaml'))
        self.gen_path = os.path.join(os.getcwd(), 'lyrics/utils/model/static/gen_800.pth')

        self.device = torch.device('cuda:0' if self.cuda else 'cpu')

        # self.hidden_dim_for_rmc = self.mem_slots * self.num_heads * self.head_size

        self.gen = GeneratorRMC(mem_slots=self.mem_slots, num_heads=self.num_heads, head_size=self.head_size,
                                embed_dim=self.lyrics_dim, ff1_out=self.ff1_out,
                                hidden_dim_lstm_as_input_size=self.embed_dim, out_dim=self.generator_out_dim,
                                cuda=self.cuda, init_batch_size=self.data_params['batch_size'],
                                sentence_len=self.sequence_len)
        self.gen.load_state_dict(torch.load(self.gen_path))

        # self.load_data(from_pth=False)

        if self.cuda:
            self.gen.to(self.device)

    def read_yaml(self, path):
        with open(path, 'r') as config_yaml:
            data = yaml.load(config_yaml, yaml.FullLoader)
        self.cuda = data['cuda']
        self.embed_dim = data['embed_dim']
        self.lyrics_dim = 2 * self.embed_dim
        self.ff1_out = data['ff1_out']
        self.hidden_dim = data['hidden_dim']
        self.generator_out_dim = data['generator_out_dim']
        self.discriminator_input_dim = self.embed_dim + self.generator_out_dim
        self.discriminator_input_dim_music = self.generator_out_dim
        self.discriminator_out_dim = data['discriminator_out_dim']
        self.learning_rate_G = data['learning_rate_G']
        self.learning_rate_D = data['learning_rate_D']
        self.load_flag = data['load_model']
        self.data_params = data['data_params']
        self.total_epoch = data['epochs']
        self.train_G_steps = data['train_G_steps']
        self.train_D_steps = data['train_D_steps']
        self.sequence_len = data['sequence_len']
        self.lyrics_dis_rate = data['lyrics_dis_rate']
        self.mem_slots = data['mem_slots']
        self.num_heads = data['num_heads']
        self.head_size = data['head_size']
        self.save_per_epoch = data['save_per_epoch']

    def load_data(self, from_pth=False):
        if not from_pth:
            training_set = Dataloader('',
                                      '',
                                      self.sequence_len)
            self.train_data_iterator = data.DataLoader(training_set, **self.data_params)
            print('loaded data')
        else:
            self.train_data_iterator = torch.load('../teswt_set.pth')
            print('loaded data')

    def get_gen_data_test(self):
        # for test and no input
        epoch = 999
        self.gen.eval()

        with torch.no_grad():
            for i, test_data in enumerate(self.train_data_iterator):
                lyrics_seq = test_data[0].to(self.device)

                discrete_val_seq = test_data[1].to(self.device)

                gen_out = self.gen(lyrics_seq)
                base_data_root = os.path.join(os.getcwd(),
                                              'lyrics/temp/src/save_/{}/{}/'.format(self.this_day, self.this_time))
                if not os.path.exists(base_data_root):
                    os.makedirs(base_data_root)
                npy_file_path = os.path.join(base_data_root, 'epoch{}_gen_data_{}'.format(epoch, i))
                np.save(npy_file_path,
                        torch.cat((discrete_val_seq, gen_out), dim=2))

                return npy_file_path

    def npy2embedding_generator2npyUrl(self, seq_data):
        # 这里输入的就应该是300句的歌词,300为batch_size

        self.gen.eval()
        # seq_data=seq_data
        gen_out = self.gen(seq_data)
        base_data_root = os.path.join(os.getcwd(), 'lyrics/utils/lyrics/temp/src/save_/{}/{}/'.format(self.this_day, self.this_time))
        if not os.path.exists(base_data_root):
            os.makedirs(base_data_root)
        npy_file_path = os.path.join(base_data_root, 'lyrics_data')
        np.save(npy_file_path,
                torch.cat((gen_out, gen_out), dim=2))
        # 这里将两倍的输出拼接起来。
        # 然后将npy文件的路径然回，以便将其转化为MIDI

        return npy_file_path

    def npy2embedding_generator2npyData(self, seq_data):
        # 这里输入的就应该是300句的歌词,300为batch_size
        self.gen.eval()
        with torch.no_grad():
            gen_out = self.gen(seq_data)
            return torch.cat((gen_out, gen_out), dim=2)


if __name__ == '__main__':
    gan = Gan()
