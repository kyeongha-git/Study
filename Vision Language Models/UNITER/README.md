# 👋 Introduction

본 발표는 **UNITER: UNiversal Image-TExt Representation Learning (ECCV, 2020)** 를 다룹니다.  

UNITER는 Vision–Language Pretraining(VLP) 분야에서 **Single-Stream Transformer** 구조를 도입하여, 이미지와 텍스트를 **하나의 Transformer 안에서 통합적으로 학습**하는 모델입니다.  
이전의 ViLBERT가 **Dual-Stream (Vision/Language 각각 Transformer)** 구조를 채택했던 것과 달리, UNITER는 **모달리티를 일찍 결합(early fusion)** 하여 더 정교한 cross-modal 표현을 학습할 수 있게 했습니다. ✨  

또한, UNITER는 학습 과정에서 **여러 가지 프리트레이닝 목표(Objectives)** 를 함께 사용하여 범용적인 비전–언어 표현을 학습합니다. 대표적으로 **Masked Language Modeling (MLM)**, **Masked Region Modeling (MRM)**, **Image-Text Matching (ITM)**, **Word-Region Alignment (WRA)** 등이 포함됩니다.  

> 결과적으로 UNITER는 VQA, Retrieval, Captioning 등 다양한 Vision–Language 벤치마크에서 당시 최고 성능(SOTA)을 달성하며, **Single-Stream 구조의 가능성**을 보여주었습니다. ✅  

---

## ✨ TL;DR
- **문제**: ViLBERT 등 Dual-Stream 모델은 강력하나 연산량이 크고 융합이 제한적  
- **아이디어**: 이미지·텍스트를 **Single-Stream Transformer**에서 공동 학습  
- **구현**: 다양한 Pretraining 목표(MLM, MRM, ITM, WRA)를 결합  
- **효과**: VQA, Retrieval, Captioning 등 다수 벤치마크에서 SOTA  

---

## 🧩 How It Works (한 장 요약)
1. **Input Representation**  
   - **Vision**: Faster R-CNN으로 객체 Region Features 추출  
   - **Language**: BERT-style Token Embeddings  
   - 둘 다 동일 Transformer 입력 포맷으로 인코딩  
2. **Single-Stream Transformer**  
   - 모든 토큰(단어 + Region)을 하나의 Transformer에서 공동 처리  
   - Self-Attention으로 모달 간 상호작용 자동 학습  
3. **Pretraining Objectives**  
   - **MLM**: 언어 마스크 예측  
   - **MRM**: 객체 특징/클래스 마스크 예측  
   - **ITM**: 이미지–텍스트 쌍이 일치하는지 여부 판별  
   - **WRA**: 단어–Region 정렬 학습  
4. **Downstream Transfer**  
   - VQA, Retrieval, NLVR² 등 다양한 태스크에 적용  

---

## 🔍 강점(Strengths)
- **Single-Stream 구조**: 모달리티 간 상호작용을 자연스럽게 학습  
- **다양한 프리트레이닝 목표**: 범용성 높은 표현 학습 가능  
- **SOTA 성능**: 다수의 V&L 벤치마크에서 강력한 성능  

## ⚠️ 한계(Caveats)
- **Region Feature 의존성**: Faster R-CNN 기반 객체 특징 필요  
- **대규모 연산 자원**: 단일 스트림 Transformer로 모든 토큰 처리 → 비용 증가  
- **후속 연구 발전**: 이후 ALBEF, BLIP 계열은 더 효율적이고 라이트한 방식으로 진화  

---

## 🧭 실무 팁(Quick Tips)
- Region Feature가 중요 → 실무에선 더 효율적인 Detectors로 대체 가능  
- ITM, WRA 등 프리트레이닝 목표는 응용 태스크 성능에 큰 영향 → 선택적 활용 고려  
- 현재는 CLIP, BLIP 계열이 주류이지만, **Single-Stream Transformer 기초**를 이해하려면 필수  

---

# 🚀 Presentation
