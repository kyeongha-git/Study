#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn

class PatchEmbedding(nn.Module):
    def __init__(self, img_size, patch_size, in_channels, d_model, device):
        super(PatchEmbedding, self).__init__()
        self.img_size = img_size
        self.patch_size = patch_size
        self.num_patches = (img_size // patch_size) ** 2
        self.device = device

        # 패치 분할 후 d_model로 차원 맞추기
        self.projection = nn.Linear(patch_size * patch_size * in_channels, d_model)

        # [CLS] 토큰
        self.cls_token = nn.Parameter(torch.randn(1, 1, d_model, device = device))

        # Position Embedding (논문에서 positional encoding을 learnable 하게 만들어서 정하는게 더 적합하다고 나옴.)
        self.position_embedding = nn.Parameter(torch.randn(1, self.num_patches + 1, d_model, device = device))

    def forward(self, x):
      batch_size, channels, height, width = x.size()
      
      # 패치로 분할하고 Flatten: (Batch, Num_Patches, Patch_Size * Patch_Size * Channel)
      patches = x.unfold(2, self.patch_size, self.patch_size).unfold(3, self.patch_size, self.patch_size)
      patches = patches.contiguous().view(batch_size, channels, -1, self.patch_size * self.patch_size)
      patches = patches.permute(0, 2, 1, 3).flatten(2)  # (Batch, Num_Patches, Patch_Size * Patch_Size * Channel)
      
      # 선형 변환을 통해 임베딩: (Batch, Num_Patches, d_model)
      patch_embeddings = self.projection(patches)
      
      # [CLS] 토큰을 배치 크기만큼 복제하여 앞에 추가
      cls_tokens = self.cls_token.expand(batch_size, -1, -1)
      embeddings = torch.cat((cls_tokens, patch_embeddings), dim=1)  # (Batch, Num_Patches + 1, d_model)
      
      # Position Encoding 추가
      embeddings = embeddings + self.position_embedding
  
      return embeddings


