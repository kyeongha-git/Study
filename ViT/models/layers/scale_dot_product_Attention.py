#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import torch.nn

class ScaleDotProductAttention(nn.Module):

    def __init__(self):
        super(ScaleDotProductAttention, self).__init__()
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, e=1e-12):
        # Process: Matmul(Q, K) -> Scale -> SoftMax (여기까지 Attention Score) -> MatMul(Score, V)

        #Scale은 k의 차원의 sqrt. -> k의 차원을 구해야 함.
        #input은 4차원. -> (batch_size, head, num_patches, d_tensor)
        batch_size, head, num_patches, d_tensor = k.size()

        # scale dot_prodct
        k_t = k.transpose(2,3)
        score = q@k_t / math.sqrt(d_tensor)

        # Softmax
        score = self.softmax(score)

        # MatMul(Score, V)
        v = score @ v

        return v, score

