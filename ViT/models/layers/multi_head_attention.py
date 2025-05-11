#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch.nn

from models.layers.scale_dot_product_attention import ScaleDotProductAttention

class MultiHeadAttention(nn.Module):

    def __init__(self, d_model, n_head):
        super(MultiHeadAttention, self).__init__()
        self.n_head = n_head
        self.attention = ScaleDotProductAttention()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_concat = nn.Linear(d_model, d_model)

    def forward(self, q, k, v):
        q = self.w_q(q) # bath_size, num_patches, d_model
        q = self.split(q) # batch_szie, head, num_patches, d_model

        k = self.w_k(k) # bath_size, num_patches, d_model
        k = self.split(k) # batch_szie, head, num_patches, d_model

        v = self.w_v(v) # bath_size, num_patches, d_model
        v = self.split(v) # batch_szie, head, num_patches, d_model

        out, attention = self.attention(q, k, v)

        out = self.concat(out)
        out = self.w_concat(out)

        return out

    def split(self, tensor):
        # input: [batch_size, num_patches, d_model]
        # output: [batch_size, head, num_patches, d_model]

        batch_size, num_patches, d_model = tensor.size()
        d_tensor = d_model // self.n_head
        tensor = tensor.view(batch_size, num_patches, self.n_head, d_tensor).transpose(1,2)

        return tensor

    def concat(self, tensor):
        # input: [batch_size, head, num_patches, d_model]
        # output: [batch_size, num_patches, d_model]

        batch_size, head, num_patches, d_tensor = tensor.size()
        d_model = d_tensor * head

        # transpose -> [batch_size, length, head, d_model]
        # view -> [batch_size, length, d_model]
        # contiguous()는 transpose와 view의 메모리 구조 방식이 다르기 때문에 연속 실행 시 에러가 반환됨. 따라서, 메모리 구조를 변경하는 함수.
        tensor = tensor.transpose(1,2).contiguous().view(batch_size, num_patches, d_model)
        return tensor

