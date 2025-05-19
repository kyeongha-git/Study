#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def get_cifar10_dataloader(batch_size=32, num_workers=4):
    # Transformations for training and validation
    train_transforms = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(32, padding=4),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])

    val_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])

    # CIFAR-10 Dataset
    train_dataset = datasets.CIFAR10(
        root="./data",
        train=True,
        download=True,  # 자동 다운로드
        transform=train_transforms
    )

    val_dataset = datasets.CIFAR10(
        root="./data",
        train=False,
        download=True,  # 자동 다운로드
        transform=val_transforms
    )

    # DataLoader
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    return train_loader, val_loader

