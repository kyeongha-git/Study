#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn
from models.embedding.positional_encoding import PositionalEncoding
from models.embedding.token_embeddings import TokenEmbedding

class TransformerEmbedding(nn.Module):
    # 입력 데이터 처리.
    # 시퀀스 입력 -> 정수형 변환 (1)
    # 입력 시퀀스에 맞추어 positonal encoding 계산 (2)
    # (1) + (2) 후 dropout
    
    def __init__(self, vocab_size, d_model, max_len, drop_prob, device):
        super(TransformerEmbedding, self).__init__()
        self.tok_emb = TokenEmbedding(vocab_size, d_model)
        self.pos_emb = PositionalEncoding(d_model, max_len, device)
        self.dropout = nn.Dropout(p = drop_prob)

    def forward(self, x):
        tok_emb = self.tok_emb(x)
        pos_emb = self.pos_emb(x)
        return self.dropout(tok_emb + pos_emb)

