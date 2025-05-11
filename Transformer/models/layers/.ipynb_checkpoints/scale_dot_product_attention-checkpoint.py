#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import torch.nn

class ScaleDotProductAttention(nn.Module):

    def __init__(self):
        super(ScaleDotProductAttention, self).__init__()
        self.softmax = nn.Sorftmax(dim=-1)

    def forward(self, q, k, v, mask = None, e=1e-12):
        # Process: Matmul(Q, K) -> Scale -> Mask (opt.) -> SoftMax (여기까지 Attention Score) -> MatMul(Score, V)

        #Scale은 k의 차원의 sqrt. -> k의 차원을 구해야 함.
        #input은 4차원. -> (batch_size, head, length, d_tensor)
        batch_size, head, length, d_tensor = k.size()

        # scale dot_prodct
        k_t = k.transpose(2,3)
        score = q@k / math.sqrt(d_tensor)

        # mask (opt.)
        # masked_fill은 삼각행렬을 만들고 0의 위치에 있는 어텐션 함수 행렬의 값을 -10000으로 대체하는 것.
        if mask is not None:
            scroe = score.masked_fill(mask == 0, -10000)
            
        # Softmax
        score = self.softmax(score)

        # MatMul(Score, V)
        v = score @ v

        return v, score

