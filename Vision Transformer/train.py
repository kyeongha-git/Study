#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import torch.optim as optim
from models.model.vit import ViT
from util.data_loader import get_cifar10_dataloader
from util.utils import train_epoch, evaluate

# 환경 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 데이터 로더
train_loader, val_loader = get_cifar10_dataloader(batch_size=32)

# 모델 초기화
model = ViT(img_size=224, patch_size=16, d_model=768, num_classes=10, 
            ffn_hidden=3072, n_head=12, n_layers=12, drop_prob=0.1, device=device).to(device)

# 손실 함수와 최적화기
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=3e-4, weight_decay=1e-2)

# 학습 루프
num_epochs = 10

for epoch in range(num_epochs):
    print(f"Epoch {epoch+1}/{num_epochs}")
    train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
    val_loss, val_acc = evaluate(model, val_loader, criterion, device)

    print(f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f}")
    print(f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")

    # 모델 저장
    torch.save(model.state_dict(), f"vit_epoch_{epoch+1}.pth")
