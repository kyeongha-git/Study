# Introduction  

본 발표는 **DINO (Emerging Properties in Self-Supervised Vision Transformers, 2021)** 를 다룹니다.  

DINO는 **라벨 없이(self-supervised)** Vision Transformer(ViT)를 학습시켜,  
객체 경계 인식과 강력한 전이 성능을 보여주는 **자기지도 학습 프레임워크**입니다.  
핵심은 **Self-Distillation with No Labels** 로, teacher–student 구조와 momentum encoder를 활용해 collapse를 방지하고,  
간단한 k-NN 분류기만으로도 **ImageNet 78.3%** 를 달성합니다.

---

## TL;DR
- **Self-Distillation w/o Labels**: teacher–student 구조, teacher는 student의 EMA로 업데이트  
- **중요 요소**: momentum encoder, multi-crop augmentation, 작은 patch size (예: 8×8)  
- **성능**: ViT-B/8 → **80.1% (linear eval)**, **77.4% (k-NN)** on ImageNet  
- **Emergent Properties**: 객체 경계와 장면 레이아웃이 attention에서 자연스럽게 학습됨  

---

## How DINO Works (한 장 요약)
1. **Teacher–Student 구조**  
   - teacher는 EMA 업데이트, student는 학습 대상  
2. **Multi-crop Augmentation**  
   - Global (224×224) + Local (96×96) crops 입력  
3. **Loss Function**  
   - teacher 출력(softmax, centered+sharpened)을 student가 예측  
4. **Emergent Attention**  
   - Self-attention map에서 객체 마스크가 자연 발생  

---

## Experiments & Results
- **ImageNet Linear Eval**: ViT-B/8 → 80.1%  
- **k-NN Classification**: ViT-S/8 → 78.3%  
- **Object Discovery**: attention 기반 객체 분할 가능  
- **Transfer Learning**: 다양한 데이터셋에서 supervised 대비 우수  
- **Image Retrieval & Copy Detection**: 경쟁력 있는 성능 확보  

---

## 강점
- 라벨 없이 self-supervised 학습  
- Attention에서 **객체 경계·레이아웃 정보** 자연 학습  
- 분류·검색·세그멘테이션 등 범용성 높음  
- ConvNet 기반 SSL 대비 연산 효율적  

---

## 한계
- 여전히 GPU compute 자원 부담  
- Dense prediction 작업에는 한계 존재  
- Teacher–student 안정성에 민감  

---

## 실무 팁
- **작은 patch size (8×8)** → 더 나은 feature 학습  
- **Multi-crop augmentation** 적극 활용  
- k-NN 평가로 feature 품질 빠른 점검 가능  
- Transfer 학습 시 strong baseline 확보  

---

# Presentation
<img width="1920" height="1080" alt="슬라이드1" src="https://github.com/user-attachments/assets/82683a66-387b-4790-9af2-c4b5c0e90544" />
<img width="1920" height="1080" alt="슬라이드2" src="https://github.com/user-attachments/assets/18170576-5894-40e0-8e4f-6cc4599fb571" />
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/4079cf3a-d92d-4c3f-ab6e-4ef431c8b236" />
<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/aad21a91-daa9-43ae-91c5-787ae73a70de" />
<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/263bb86f-94e1-45b5-80aa-c6c822401ccb" />
<img width="1920" height="1080" alt="슬라이드6" src="https://github.com/user-attachments/assets/d5263956-cee2-4dfb-a582-a18211aa2412" />
<img width="1920" height="1080" alt="슬라이드7" src="https://github.com/user-attachments/assets/a8b1ead6-a9c8-4527-bf5e-172e36a988ee" />
<img width="1920" height="1080" alt="슬라이드8" src="https://github.com/user-attachments/assets/2fb4c663-babf-4b71-b2f2-98df9323e60a" />
<img width="1920" height="1080" alt="슬라이드9" src="https://github.com/user-attachments/assets/591caa53-5124-4ec9-b7f9-d8434bbdb28a" />
<img width="1920" height="1080" alt="슬라이드10" src="https://github.com/user-attachments/assets/0ee5687a-3321-4de4-af8c-a3b5ac310e91" />
<img width="1920" height="1080" alt="슬라이드11" src="https://github.com/user-attachments/assets/96e43cc4-0e9c-4c74-a924-b8b643447f5e" />
<img width="1920" height="1080" alt="슬라이드12" src="https://github.com/user-attachments/assets/51b7fb17-01fa-4b76-a490-c24794561e63" />
<img width="1920" height="1080" alt="슬라이드13" src="https://github.com/user-attachments/assets/c0a8c72c-b4cb-4cce-b392-b5dd9780e489" />
<img width="1920" height="1080" alt="슬라이드14" src="https://github.com/user-attachments/assets/0d0b55b8-4f48-4759-aaed-b8b8a61a22a3" />
<img width="1920" height="1080" alt="슬라이드15" src="https://github.com/user-attachments/assets/b5d29d82-a91e-4dde-b7e0-75ec9557b618" />
<img width="1920" height="1080" alt="슬라이드16" src="https://github.com/user-attachments/assets/402b0bab-0d74-4bbf-81fb-39b396c54fe6" />
<img width="1920" height="1080" alt="슬라이드17" src="https://github.com/user-attachments/assets/2e274c2d-f296-44d1-8ae3-9d41f084eae1" />
<img width="1920" height="1080" alt="슬라이드18" src="https://github.com/user-attachments/assets/6b3c183c-8f9f-4a6f-be62-50598b654616" />





















