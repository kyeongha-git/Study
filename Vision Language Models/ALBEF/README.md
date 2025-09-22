# 👋 Introduction

본 발표는 **ALBEF: Align Before Fuse (NeurIPS, 2021)** 를 다룹니다.  

ALBEF는 Vision–Language Pretraining(VLP) 모델로, 핵심 아이디어는 **이미지와 텍스트를 단순히 결합하기 전에 먼저 정렬(Alignment)시키고, 그 후에 융합(Fusion)하자**는 것입니다.  
이를 위해 **대조학습(contrastive learning)** 과 **모멘텀 디스틸레이션(momentum distillation)** 을 결합하여, 이미지–텍스트 쌍을 보다 잘 정렬할 수 있게 했습니다. ✨  

기존의 UNITER와 같은 Single-Stream 모델은 강력했지만, 초기 정렬 과정이 부족해 잡음이 많은 웹 데이터에서는 일반화에 한계가 있었습니다. ALBEF는 먼저 **Cross-Modal Contrastive Loss**로 이미지–텍스트를 정렬한 뒤, 그 결과를 바탕으로 **Fusion Encoder**에서 결합하여 성능을 향상시켰습니다.  

> 결과적으로 ALBEF는 VQA, Image-Text Retrieval, NLVR² 등 다양한 태스크에서 강력한 성능을 보였으며, **대규모 웹 데이터의 잡음을 다루는 방법**을 제시했습니다. ✅  

---

## ✨ TL;DR
- **문제**: 웹에서 수집한 이미지–텍스트 쌍은 잡음이 많아 정렬이 어려움  
- **아이디어**: 이미지–텍스트를 먼저 **Align(대조학습)** 하고, 그 후 **Fuse(융합)**  
- **구현**: Dual Encoder로 Alignment 학습 + Fusion Encoder에서 결합  
- **효과**: 웹 데이터 기반 학습에서 강한 일반화와 높은 성능 확보  

---

## 🧩 How It Works (한 장 요약)
1. **Input Encoding**  
   - **Image Encoder**: ViT 기반 이미지 표현  
   - **Text Encoder**: BERT 기반 텍스트 표현  
2. **Align Stage**  
   - Cross-Modal Contrastive Loss로 이미지–텍스트 정렬  
   - 모멘텀 디스틸레이션으로 안정적 학습  
3. **Fuse Stage**  
   - Cross-Attention 기반 Fusion Encoder에서 모달리티 결합  
4. **Multi-Task Pretraining**  
   - ITC (Image-Text Contrastive)  
   - ITM (Image-Text Matching)  
   - MLM (Masked Language Modeling)  

---

## 🔍 강점(Strengths)
- **잡음 견고성**: noisy 웹 데이터에서도 안정적인 정렬 가능  
- **단계적 학습**: Align → Fuse 단계 구분으로 효율적인 학습  
- **범용성**: VQA, Retrieval, NLVR² 등 다양한 다운스트림 태스크에서 SOTA 달성  

## ⚠️ 한계(Caveats)
- **학습 복잡성**: Dual Encoder + Fusion Encoder 구조로 학습/추론 비용 증가  
- **데이터 의존성**: 여전히 대규모 웹 데이터 필요  
- **후속 발전**: BLIP, BLIP-2는 더 효율적이고 확장성 있는 방식으로 발전  

---

## 🧭 실무 팁(Quick Tips)
- 웹 데이터 기반 프로젝트에서 **잡음 제거 대신 정렬(Alignment) 전략** 활용 가능  
- Contrastive Loss는 downstream 태스크 전이력 개선에 핵심적 → 구현 시 튜닝 중요  
- Fusion Encoder는 비용이 크므로 실무에서는 Dual Encoder만 활용하는 경우도 많음  

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드27" src="https://github.com/user-attachments/assets/0212ccd1-fb1a-4326-8eee-7fef9e63fa4a" />
<img width="1920" height="1080" alt="슬라이드28" src="https://github.com/user-attachments/assets/ac82dbbc-419a-4de2-8311-92f1157b2a90" />
<img width="1920" height="1080" alt="슬라이드29" src="https://github.com/user-attachments/assets/11c77965-2135-4b56-b24b-b4d47cb0567b" />
<img width="1920" height="1080" alt="슬라이드30" src="https://github.com/user-attachments/assets/a83702fb-3c4f-4a42-902d-7b6678625b9a" />
<img width="1920" height="1080" alt="슬라이드31" src="https://github.com/user-attachments/assets/5ad22fcc-e51c-4e8b-9bbf-213b3368f138" />
<img width="1920" height="1080" alt="슬라이드32" src="https://github.com/user-attachments/assets/1445352d-2d39-4982-82b8-1f37cf187019" />
<img width="1920" height="1080" alt="슬라이드33" src="https://github.com/user-attachments/assets/09648f9e-87f7-46f7-bb85-90fe7d419d89" />
<img width="1920" height="1080" alt="슬라이드34" src="https://github.com/user-attachments/assets/3ba73b41-bba6-475d-8289-6a6fe33221dd" />
<img width="1920" height="1080" alt="슬라이드35" src="https://github.com/user-attachments/assets/486b452e-e399-4da3-aad0-5c6e325ef8f4" />
<img width="1920" height="1080" alt="슬라이드36" src="https://github.com/user-attachments/assets/7c556e89-a157-4c32-a5b4-d89b848db0c1" />










