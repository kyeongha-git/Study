#!/usr/bin/env python
# coding: utf-8

import torch
from tqdm import tqdm

def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for batch_idx, (images, labels) in enumerate(tqdm(dataloader, desc="Training", leave=False)):
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, preds = torch.max(outputs, 1)
        correct += torch.sum(preds == labels).item()
        total += len(labels)

        if (batch_idx + 1) % 100 == 0:
            print(f"Batch {batch_idx+1}/{len(dataloader)}: Loss = {loss.item():.4f}, Accuracy = {correct / total:.4f}")

    epoch_loss = running_loss / len(dataloader)
    epoch_acc = correct / total
    torch.cuda.empty_cache()
    return epoch_loss, epoch_acc

def evaluate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for batch_idx, (images, labels) in enumerate(tqdm(dataloader, desc="Validating", leave=False)):
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item()
            _, preds = torch.max(outputs, 1)
            correct += torch.sum(preds == labels).item()
            total += len(labels)

            if (batch_idx + 1) % 100 == 0:
                print(f"Batch {batch_idx+1}/{len(dataloader)}: Val Loss = {loss.item():.4f}, Val Accuracy = {correct / total:.4f}")

    epoch_loss = running_loss / len(dataloader)
    epoch_acc = correct / total
    torch.cuda.empty_cache()
    return epoch_loss, epoch_acc
