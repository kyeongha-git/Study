#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn
from models.layers.layer_norm import LayerNorm
from models.layers.multi_head_attention import MultiHeadAttention
from models.layers.position_wise_feed_forward import PositionwiseFeedForward

class DecoderLayer(nn.Module):
    def __init__(self, d_model, ffn_hidden, n_head, drop_prob):
        super(DecoderLayer, self).__init__()
        self.attention = MultiHeadAttention(d_model, n_head)
        self.norm1 = LayerNorm(d_model)
        self.dropout1 = nn.Dropout(p = drop_prob)

        self.enc_dec_attention = MultiHeadAttention(d_model, n_head)
        self.norm2 = LayerNorm(d_model)
        self.dropout2 = nn.Dropout(p = drop_prob)
        
        self.ffn = PositionwiseFeedForward(d_model, ffn_hidden, drop_prob)
        self.norm3 = LayerNorm(d_model)
        self.dropout3= nn.Dropout(p = drop_prob)

    def forward(self, dec, enc, trg_mask, src_mask):
        # dec: 디코더의 입력
        # enc: 인코더의 출력
        # trg_mask: mask multi-head attention 시 사용될 미래 단어를 가리는 mask
        # src_mask: 기존 multi-head attnetion 시 사용될 mask
        
        _x = dec
        x = self.attention(q = dec, k = dec, v = dec, mask = trg_mask) # Mask Multi-Head Attention
        x = self.dropout1(x)
        x = self.norm1(x + _x)

        if enc is not None: # Encoder의 출력이 있는 경우.
            x = self.enc_dec_attention(q = x, k = enc, v =enc, mask = src_mask)
            x = self.dropout2(x)
            x = self.norm2(x + _x)            
        _x = x
        
        x = self.ffn(x)
        x = self.dropout3(x)
        x = self.norm3(x + _x)

        return x

