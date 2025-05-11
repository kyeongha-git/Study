#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from torch.utils.data import DataLoader
from torchvision import transforms, datasets

def get_coco_dataloader(data_dir, batch_size=32, num_workers=4):
    # Transformations for training and validation
    train_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # COCO Dataset
    train_dataset = datasets.CocoDetection(
        root=f"{data_dir}/train2017",
        annFile=f"{data_dir}/annotations/instances_train2017.json",
        transform=train_transforms
    )

    val_dataset = datasets.CocoDetection(
        root=f"{data_dir}/val2017",
        annFile=f"{data_dir}/annotations/instances_val2017.json",
        transform=val_transforms
    )

    # DataLoader
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    return train_loader, val_loader

