#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn
from models.layers.layer_norm import LayerNorm

class MLPHead(nn.Module):
    def __init__(self, d_model, ffn_hidden, n_classes, drop_prob):
        super(MLPHead, self).__init__()
        self.norm = LayerNorm(d_model)
        self.linear1 = nn.Linear(d_model, ffn_hidden)
        self.dropout = nn.Dropout(p = drop_prob)
        self.gelu = nn.GELU()
        self.linear2 = nn.Linear(ffn_hidden, n_classes)

    def forward(self, x):
        x = self.norm(x[:, 0])
        x = self.linear1(x)
        x = self.gelu(x)
        x = self.dropout(x)

        x = self.linear2(x)
        return x

