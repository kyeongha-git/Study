#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn

class TokenEmbedding(nn.Embedding):
    
    # 시퀀스 -> 정수로 변환하는 클래스.
    # paddnig_idx = 1로 설정하여 같은 배치 내 시퀀스 길이가 다를 때 패딩을 추가하여 정렬
    def __init__(self, vocab_size, d_model):
        super(TokenEmbeddingm, self).__init__(vocab_size, d_model, padding_idx=1)

