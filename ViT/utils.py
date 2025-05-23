#!/usr/bin/env python
# coding: utf-8

import torch
from tqdm import tqdm

def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

<<<<<<< Updated upstream
    for images, labels in tqdm(dataloader, desc="Training", leave=False):
        images = images.to(device)
        labels = labels.to(device)  # CIFAR-10의 labels는 이미 정수형
=======
    for batch_idx, (images, labels) in enumerate(tqdm(dataloader, desc="Training", leave=False)):
        images = images.to(device)
        labels = labels.to(device)  # 수정: 직접 레이블 사용
>>>>>>> Stashed changes

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, preds = torch.max(outputs, 1)
        correct += torch.sum(preds == labels).item()
        total += len(labels)

        # 실시간 Loss와 Accuracy 출력
        if (batch_idx + 1) % 100 == 0:  # 100 배치마다 출력
            print(f"Batch {batch_idx+1}/{len(dataloader)}: Loss = {loss.item():.4f}, Accuracy = {correct / ((batch_idx + 1) * len(images)):.4f}")

    epoch_loss = running_loss / len(dataloader)
<<<<<<< Updated upstream
    epoch_acc = correct / total
=======
    epoch_acc = correct / len(dataloader.dataset)

    # 메모리 관리
    torch.cuda.empty_cache()

>>>>>>> Stashed changes
    return epoch_loss, epoch_acc

def evaluate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
<<<<<<< Updated upstream
        for images, labels in tqdm(dataloader, desc="Validating", leave=False):
            images = images.to(device)
            labels = labels.to(device)  # CIFAR-10의 labels는 이미 정수형
=======
        for batch_idx, (images, labels) in enumerate(tqdm(dataloader, desc="Validating", leave=False)):
            images = images.to(device)
            labels = labels.to(device)  # 수정: 직접 레이블 사용
>>>>>>> Stashed changes

            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item()
            _, preds = torch.max(outputs, 1)
            correct += torch.sum(preds == labels).item()
            total += len(labels)

            # 실시간 Loss와 Accuracy 출력
            if (batch_idx + 1) % 100 == 0:  # 100 배치마다 출력
                print(f"Batch {batch_idx+1}/{len(dataloader)}: Val Loss = {loss.item():.4f}, Val Accuracy = {correct / ((batch_idx + 1) * len(images)):.4f}")

    epoch_loss = running_loss / len(dataloader)
<<<<<<< Updated upstream
    epoch_acc = correct / total
=======
    epoch_acc = correct / len(dataloader.dataset)

    # 메모리 관리
    torch.cuda.empty_cache()

>>>>>>> Stashed changes
    return epoch_loss, epoch_acc
