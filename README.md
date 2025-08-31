# VLM Study — Paper Reviews & PyTorch Implementations

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red)
![Topic](https://img.shields.io/badge/Topics-VLM%20%7C%20LLM%20%7C%20SSL%20%7C%20CNN-lightgrey)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2025--08--13-success)

![Image](https://github.com/user-attachments/assets/fff6081e-1eb1-4289-b7c3-c7e3c80311d9)

본 저장소는 Vision-Language Models(VLM)을 중심으로, 핵심 기초 논문들을 **직접 구현(PyTorch)** 하고 **해설/주석** 및 **발표 자료**로 정리한 스터디 기록입니다. 구현의 정확성뿐 아니라 **설계 의도와 방법론적 맥락**을 해석하는 데 초점을 두었습니다.

> 본 논문 리뷰는 **수원대학교 데이터과학부 김진현 교수님**과 함께한 스터디 내용을 토대로 하며,  
> 모든 정리와 코드는 **황경하**가 작성했고, 발표와 피드백을 거쳐 지속 보완하고 있습니다.

---

## 🔎 Why this repo?
- **VLM의 전후 맥락**: LLM·CNN·SSL의 흐름 속에서 VLM을 이해하기 위한 전단(前段) 개념 정리  
- **재현성과 가독성**: 원 논문 의도를 해치지 않는 범위에서 **깨끗한 PyTorch 구현**과 **풍부한 주석** 제공  
- **학습·발표 친화**: 각 폴더에 **발표 슬라이드(PPT)** 와 **설명 글**을 연결해 빠르게 훑고 깊게 들어갈 수 있게 구성

---

## 📝 Contents
- 📖 **Paper List** — 읽은 논문과 원문 링크  
- 💻 **Code Implementations** — PyTorch 구현(데이터셋·실험 조건 명시)  
- 🗒️ **Annotations & Explanations** — 개념/아이디어 해설, 설계 선택의 근거  
- 📈 **Presentation (PPT)** — 발표용 슬라이드(각 폴더 README 참고)

> 실행 방법과 하이퍼파라미터는 **각 폴더의 README** 를 참고하세요.

---

## 📖 Paper List

### LLM / Foundation Models
- **Attention Is All You Need (Transformer)**  
  - [Paper](http://arxiv.org/abs/1706.03762)
  - [Code](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/Transformer) *(Dataset: Multi30k)*  
  - [Explanations](https://kyeongha-blog.tistory.com/entry/Transformer-Attention-Is-All-You-Need)
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/Transformer) *(See folder README)*

- **An Image Is Worth 16×16 Words (Vision Transformer)**  
  - [Paper](http://arxiv.org/abs/2010.11929)  
  - [Code](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/Vision%20Transformer) *(Dataset: CIFAR-10)*  
  - [Explanations](https://kyeongha-blog.tistory.com/entry/Vision-Transformer-AN-IMAGE-IS-WORTH-16X16-WORDS-TRANSFORMERS-FOR-IMAGE-RECOGNITION-AT-SCALE) 
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/Vision%20Transformer) *(See folder README)*

- **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**  
  - [Paper](https://arxiv.org/abs/1810.04805)
  - [Code](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/BERT)
  - [Explanations](https://kyeongha-blog.tistory.com/entry/LLM-BERT-Pre-training-of-Deep-Bidirectional-Transformers-for-Language-Understanding-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-%EA%B8%B0%EC%B4%88%EB%B6%80%ED%84%B0-%EA%BC%BC%EA%BC%BC%ED%9E%88)
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/BERT) *(See folder README)*

- **Language Models are Unsupervised Multitask Learners (GPT-2)**  
  - [Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/GPT-2) *(See folder README)*

- **Language Models are Few-Shot Learners (GPT-3)**  
  - [Paper](https://papers.nips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)  
  - [Explanations](https://kyeongha-blog.tistory.com/entry/GPT-3-Language-Models-are-Few-Shot-Learners-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-%EA%B8%B0%EC%B4%88%EB%B6%80%ED%84%B0-%EA%BC%BC%EA%BC%BC%ED%9E%88)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/GPT-3) *(See folder README)*

- **Scaling Laws for Neural Language Models**  
  - [Paper](http://arxiv.org/abs/2001.08361)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/LLM-Foundation%20Models/Scailng-Law) *(See folder README)*

### Basic CNN
- **CNN Case Study (AlexNet · VGG · GoogLeNet)**  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/Basic%20CNN/CNN%20(AlexNet%2CVGG%2CGoogLeNet)) *(See folder README)*

- **Deep Residual Learning for Image Recognition (ResNet)**  
  - [Paper](https://arxiv.org/abs/1512.03385)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/Basic%20CNN/ResNet) *(See folder README)*

### SSL (Self-Supervised Learning)
- **Unsupervised Representation Learning by Predicting Image Rotations (RotNet)**  
  - [Paper](http://arxiv.org/abs/1803.07728)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/SSL/RotNet) *(See folder README)*

- **SimCLR: A Simple Framework for Contrastive Learning of Visual Representations**  
  - [Paper](http://arxiv.org/abs/2002.05709)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/SSL/SimCLR) *(See folder README)*

- **MoCo: Momentum Contrast for Unsupervised Visual Representation Learning**  
  - [Paper](http://arxiv.org/abs/1911.05722)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/SSL/MoCo) *(See folder README)*

- **CLIP: Learning Transferable Visual Models From Natural Language Supervision**  
  - [Paper](http://arxiv.org/abs/2103.00020)  
  - [Presentation](https://github.com/kyeongha-git/Study/tree/main/SSL/CLIP) *(See folder README)*

---

## 🧭 How to Navigate
- **입문자**: *Presentation* → *Explanations* → *Code* 순서로 큰 그림부터  
- **재현/확장**: *Code*의 주석과 README의 실험 조건을 따라 baseline 재현 → ablation 적용  
- **VLM 맥락화**: ViT·SSL·CLIP을 축으로 LLM 파트의 스케일링 통찰을 연결해 이해

---

## 📬 Contact
- Author: **황경하 (Kyeongha Hwang)**  
- Blog: https://kyeongha-blog.tistory.com  
- GitHub: https://github.com/kyeongha-git
