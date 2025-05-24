#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
from models.model.Decoder import Decoder
from models.model.Encoder import Encoder

class Transformer(nn.Module):
    def __init__(self, src_pad_idx, trg_pad_idx, trg_sos_idx, enc_voc_size, dec_voc_size, d_model, n_head, max_len,
                 ffn_hidden, n_layers, drop_prob, device):
        super().__init__()
        self.src_pad_idx = src_pad_idx
        self.trg_pad_idx = trg_pad_idx
        self.trg_sos_idx = trg_sos_idx
        self.device = device
        self.encoder = Encoder(d_model = d_model,
                                enc_voc_size = enc_voc_size,
                                max_len = max_len,
                                ffn_hidden = ffn_hidden,
                                n_head = n_head,
                                n_layers = n_layers,
                                drop_prob = drop_prob,
                                device = device)

        self.decoder = Decoder(d_model = d_model,
                                dec_voc_size = dec_voc_size,
                                max_len = max_len,
                                ffn_hidden = ffn_hidden,
                                n_head = n_head,
                                n_layers = n_layers,
                                drop_prob = drop_prob,
                                device = device)

    def forward(self, src, trg):
        src_mask = self.make_src_mask(src)
        trg_mask = self.make_trg_mask(trg)
        enc_src = self.encoder(src, src_mask)
        output = self.decoder(trg, enc_src, trg_mask, src_mask)
        return output

    def make_src_mask(self, src):
        # padding idx는 모두 False로 나머지는 다 True로 표시.
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)
        return src_mask

    def make_trg_mask(self, trg):
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(3)
        trg_len = trg.shape[1]
        trg_sub_mask = torch.tril(torch.ones((trg_len, trg_len), device = trg.device)).bool().unsqueeze(0)
        trg_mask = trg_pad_mask & trg_sub_mask
        return trg_mask

