#!/usr/bin/env python
# coding: utf-8

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def get_cifar10_dataloader(batch_size=32, num_workers=4):
    # Transformations for training
    train_transforms = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomCrop(32, padding=4),
        transforms.Resize((224, 224)),  # Resize 추가 (ViT 등 입력 크기 맞추기용)
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])

    # Transformations for validation
    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),  # 단순히 사이즈 맞춤
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])

    # CIFAR-10 Dataset
    train_dataset = datasets.CIFAR10(
        root="./data",
        train=True,
        download=True,
        transform=train_transforms
    )

    val_dataset = datasets.CIFAR10(
        root="./data",
        train=False,
        download=True,
        transform=val_transforms
    )

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    return train_loader, val_loader
