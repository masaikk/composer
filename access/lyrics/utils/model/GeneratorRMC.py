import torch
import torch.nn as nn
import torch.nn.functional as F
from lyrics.utils.model.RelationalMemory import RelationalMemory


class GeneratorRMC(nn.Module):
    def __init__(self, embed_dim, ff1_out, hidden_dim_lstm_as_input_size, out_dim, head_size=256, num_heads=2,
                 mem_slots=1, drop=0.25, cuda=False, init_batch_size=100, sentence_len=20):
        super(GeneratorRMC, self).__init__()

        self.input_ff = nn.Linear(embed_dim, hidden_dim_lstm_as_input_size)
        self.hidden_dim_rmc = mem_slots * num_heads * head_size

        self.drop = nn.Dropout(drop)
        self.output_ff = nn.Linear(head_size * mem_slots, out_dim)
        self.gpu = cuda
        self.temperature = nn.Parameter(torch.Tensor([1.0]), requires_grad=False)
        # self.vocab_size = 10
        self.init_batch_size = init_batch_size
        self.sentence_len = sentence_len

        self.line1 = nn.Linear(sentence_len * embed_dim, hidden_dim_lstm_as_input_size * sentence_len)
        self.rmc = RelationalMemory(head_size=head_size * sentence_len,
                                    input_size=hidden_dim_lstm_as_input_size * sentence_len, mem_slots=mem_slots)

    def forward(self, lyrics):
        concat_lyrics = torch.cat((lyrics, torch.FloatTensor(lyrics.size()).uniform_()), 2)
        # concat_lyrics = torch.cat((lyrics, torch.zeros(lyrics.size())), 2)
        # print('concat_lyrics size:{}'.format(concat_lyrics.shape))
        hidden = self.init_hidden(self.init_batch_size)


        concat_lyrics = concat_lyrics.view(self.init_batch_size, 1, -1)
        out_line = F.relu(self.line1(concat_lyrics))
        out, hidden = self.rmc(out_line, hidden)
        out = out.view(self.init_batch_size, self.sentence_len, -1)

        tag = self.output_ff(out)
        # print('tag size:{}'.format(tag.shape))
        return tag

    def init_hidden(self, batch_size):
        memory = self.rmc.initial_state(batch_size)
        memory = self.rmc.repackage_hidden(memory)
        return memory.cuda() if self.gpu else memory
