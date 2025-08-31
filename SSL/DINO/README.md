# 👋 Introduction  

본 발표는 **DINO (Emerging Properties in Self-Supervised Vision Transformers, 2021)** 를 다룹니다.  

DINO는 **라벨 없이(self-supervised)** Vision Transformer(ViT)를 학습시켜,  
객체 경계 인식과 강력한 전이 성능을 보여주는 **자기지도 학습 프레임워크**입니다.  
핵심은 **Self-Distillation with No Labels** 로, teacher–student 구조와 momentum encoder를 활용해 collapse를 방지하고,  
간단한 k-NN 분류기만으로도 **ImageNet 78.3%** 를 달성합니다. ✨  

---

## ✨ TL;DR
- **Self-Distillation w/o Labels**: teacher–student 구조, teacher는 student의 EMA로 업데이트  
- **중요 요소**: momentum encoder, multi-crop augmentation, 작은 patch size (예: 8×8)  
- **성능**: ViT-B/8 → **80.1% (linear eval)**, **77.4% (k-NN)** on ImageNet  
- **Emergent Properties**: 객체 경계와 장면 레이아웃이 attention에서 자연스럽게 학습됨  

---

## 🧩 How DINO Works (한 장 요약)
1. **Teacher–Student 구조**  
   - teacher는 EMA 업데이트, student는 학습 대상  
2. **Multi-crop Augmentation**  
   - Global (224×224) + Local (96×96) crops 입력  
3. **Loss Function**  
   - teacher 출력(softmax, centered+sharpened)을 student가 예측  
4. **Emergent Attention**  
   - Self-attention map에서 객체 마스크가 자연 발생  

---

## 🧪 Experiments & Results
- **ImageNet Linear Eval**: ViT-B/8 → 80.1%  
- **k-NN Classification**: ViT-S/8 → 78.3%  
- **Object Discovery**: attention 기반 객체 분할 가능  
- **Transfer Learning**: 다양한 데이터셋에서 supervised 대비 우수  
- **Image Retrieval & Copy Detection**: 경쟁력 있는 성능 확보  

---

## 🔍 강점 (Strengths)
- 라벨 없이 self-supervised 학습  
- Attention에서 **객체 경계·레이아웃 정보** 자연 학습  
- 분류·검색·세그멘테이션 등 범용성 높음  
- ConvNet 기반 SSL 대비 연산 효율적  

---

## ⚠️ 한계 (Caveats)
- 여전히 GPU compute 자원 부담  
- Dense prediction 작업에는 한계 존재  
- Teacher–student 안정성에 민감  

---

## 🧭 실무 팁 (Quick Tips)
- **작은 patch size (8×8)** → 더 나은 feature 학습  
- **Multi-crop augmentation** 적극 활용  
- k-NN 평가로 feature 품질 빠른 점검 가능  
- Transfer 학습 시 strong baseline 확보  

---

# 🚀 Presentation  
