#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len, device):
        super(PositionalEncoding, self).__init__()
        # encoding matrix
        self.encoding = torch.zeros(max_len, d_model, device = device)
        self.encoding.requires_grad = False # 논문에서 이를 학습하여 정해도 성능이 비슷했다고 함. 따라서, 학습은 하지 않음.

        # positon matrix
        pos = torch.arange(0, max_len, device = device)
        pos = pos.float().unsqueeze(dim=1)

        _2i = torch.arange(0, d_model, step = 2, device = device).float()
        self.encoding[:, 0::2] = torch.sin(pos / (10000 ** (_2i/d_model))) # 짝수 인덱스 ex. 0,2,4,6,8, ..
        self.encoding[:, 1::2] = torch.cos(pos / (10000 ** (_2i/d_model))) # 홀수 인덱스 ex. 1,3,5,7,9, ...

    def forward(self, x):
        batch_size, seq_len = x.size()

        # 입력 데이터의 길이에 맞추어 잘라서 리턴.
        pos = self.encoding[:seq_len, :].unsqueeze(0).repeat(batch_size, 1, 1)
        return pos
