#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn
from models.blocks.decoder_layer import DecoderLayer
from models.embedding.transformer_embedding import TransformerEmbedding

class Decoder(nn.Module):

    def __init__(self, dec_voc_size, max_len, d_model, ffn_hidden, n_head, n_layers, drop_prob, device):
        super().__init__()
        self.emb = TransformerEmbedding(d_model = d_model,
                                        max_len = max_len,
                                        vocab_size = dec_voc_size,
                                        drop_prob = drop_prob,
                                        device = device)
        
        self.layers = nn.ModuleList([DecoderLayer(d_model = d_model,
                                                   ffn_hidden = ffn_hidden,
                                                   n_head = n_head,
                                                   drop_prob = drop_prob)
                                      for _ in range(n_layers)]) # n_layers 만큼 Encoder 반복 생성.
        
        # 마지막에 출력 차원과 맞추기 위하여 dec_voc_size로 출력 차원을 맞춤.
        self.linear = nn.Linear(d_mdoel, dec_voc_size)
        self.softmax = nn.Softmax(dim = -1)
        
    def forward(self, trg, enc_src, trg_mask, src_mask):
        # enc_src: 인코더의 출력
        
        # Data Processing
        trg = self.emb(trg)

        # Decoder
        for layer in self.layers:
            x = layer(trg, enc_src, trg_mask, src_mask)

        output = self.linear(trg)
        return output

