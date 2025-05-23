#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import sys
import os
from .encoder_layer import EncoderLayer
from .embedding.patch_embeddings import PatchEmbedding
from .layers.mlp_head import MLPHead

class ViT(nn.Module):

    def __init__(self, img_size, patch_size, d_model, num_classes, ffn_hidden, n_head, n_layers, drop_prob, device):
        super().__init__()
        self.emb = PatchEmbedding(img_size = img_size,
                                    patch_size = patch_size,
                                    d_model = d_model,
                                    in_channels = 3,
                                    device = device)

        self.encoder = nn.ModuleList([EncoderLayer(d_model = d_model,
                                                   ffn_hidden = ffn_hidden,
                                                   n_head = n_head,
                                                   drop_prob = drop_prob)
                                    for _ in range(n_layers)]) # n_layers 만큼 Encoder 반복 생성.
        self.mlp_head = MLPHead(d_model = d_model,
                                ffn_hidden = ffn_hidden,
                                n_classes = num_classes,
                                drop_prob = drop_prob)

    def forward(self, x):
        # Data Processing
        x = self.emb(x)

        # Encoder
        for layer in self.encoder:
            x = layer(x)

        # MLP Head
        x = self.mlp_head(x)

        return x

