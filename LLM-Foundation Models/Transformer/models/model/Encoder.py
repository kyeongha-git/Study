#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
from models.blocks.encoder_layer import EncoderLayer
from models.embedding.transformer_embedding import TransformerEmbedding

class Encoder(nn.Module):

    def __init__(self, enc_voc_size, max_len, d_model, ffn_hidden, n_head, n_layers, drop_prob, device):
        super().__init__()
        self.emb = TransformerEmbedding(d_model = d_model,
                                        max_len = max_len,
                                        vocab_size = enc_voc_size,
                                        drop_prob = drop_prob,
                                        device = device)
        
        self.encoder = nn.ModuleList([EncoderLayer(d_model = d_model,
                                                   ffn_hidden = ffn_hidden,
                                                   n_head = n_head,
                                                   drop_prob = drop_prob)
                                      for _ in range(n_layers)]) # n_layers 만큼 Encoder 반복 생성.
        self.device = device

    def forward(self, x, src_mask):
        # Data Processing
        x = x.to(self.device)
        x = self.emb(x)

        # Encoder
        for layer in self.encoder:
            x = layer(x, src_mask)
        
        return x

