#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from tqdm import tqdm

def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0

    for images, targets in tqdm(dataloader, desc="Training", leave=False):
        images = images.to(device)
        labels = torch.tensor([t[0]['category_id'] for t in targets]).to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, preds = torch.max(outputs, 1)
        correct += torch.sum(preds == labels).item()

    epoch_loss = running_loss / len(dataloader)
    epoch_acc = correct / len(dataloader.dataset)
    return epoch_loss, epoch_acc

def evaluate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0

    with torch.no_grad():
        for images, targets in tqdm(dataloader, desc="Validating", leave=False):
            images = images.to(device)
            labels = torch.tensor([t[0]['category_id'] for t in targets]).to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item()
            _, preds = torch.max(outputs, 1)
            correct += torch.sum(preds == labels).item()

    epoch_loss = running_loss / len(dataloader)
    epoch_acc = correct / len(dataloader.dataset)
    return epoch_loss, epoch_acc

