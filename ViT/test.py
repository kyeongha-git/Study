#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from models.vit import ViT
from data_loader import get_cifar10_dataloader

def test_model(model, dataloader, device):
    model.eval()
    correct = 0

    with torch.no_grad():
        for images, targets in tqdm(dataloader, desc="Testing", leave=False):
            images = images.to(device)
            labels = torch.tensor([t[0]['category_id'] for t in targets]).to(device)

            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            correct += torch.sum(preds == labels).item()

    accuracy = correct / len(dataloader.dataset)
    print(f"Test Accuracy: {accuracy:.4f}")

# 환경 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 모델 초기화 및 로드
model = ViT(img_size=224, patch_size=16, d_model=768, num_classes=10, 
            ffn_hidden=3072, n_head=12, n_layers=12, drop_prob=0.1, device=device).to(device)
model.load_state_dict(torch.load("vit_epoch_10.pth"))

# 데이터 로더
_, val_loader = get_cifar10_dataloader(batch_size=32)

# 테스트
test_model(model, val_loader, device)

