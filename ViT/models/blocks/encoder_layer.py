#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import os
from models.layers.layer_norm import LayerNorm
from models.layers.multi_head_attention import MultiHeadAttention
from models.layers.position_wise_feed_forward import PositionwiseFeedForward

class EncoderLayer(nn.Module):
    def __init__(self, d_model, ffn_hidden, n_head, drop_prob):
        super(EncoderLayer, self).__init__()
        self.attention = MultiHeadAttention(d_model, n_head)
        self.norm1 = LayerNorm(d_model = d_model)
        self.dropout1 = nn.Dropout(p = drop_prob)

        self.ffn = PositionwiseFeedForward(d_model, ffn_hidden, drop_prob)
        self.norm2 = LayerNorm(d_model = d_model)
        self.dropout2 = nn.Dropout(p = drop_prob)

    def forward(self, x):
        # _x는 residual connection을 위하여 이전 값 저장하는 변수.
        # x는 forward를 진행하는 변수.
        _x = x
        x = self.norm1(x)
        x = self.attention(q = x, k = x, v = x)
        x = self.dropout1(x)
        x = x + _x
        _x = x

        x = self.norm2(x)
        x = self.ffn(x)
        x = self.dropout2(x)
        x = x + _x
        return x


