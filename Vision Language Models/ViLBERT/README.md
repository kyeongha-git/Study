# 👋 Introduction

본 발표는 **ViLBERT: Pretraining Task-Agnostic Visio-Linguistic Representations for Vision-and-Language Tasks (NeurIPS, 2019)** 를 다룹니다.  

ViLBERT는 **Vision–Language Pretraining (VLP)** 연구의 초기 대표 모델 중 하나로, 이미지와 텍스트를 **두 개의 Transformer 스트림**으로 독립적으로 처리한 뒤, **Co-Attention Layer**를 통해 상호작용하게 만든 구조입니다.  
즉, **이미지와 언어를 각각 인코딩 → 이후 서로 정보를 교환**하여 다중모달 표현을 학습하는 방식입니다. ✨  

기존의 이미지-텍스트 모델들은 주로 **Late Fusion**(이미지와 텍스트를 따로 처리한 후 결합) 혹은 **Single-Stream** 구조(하나의 Transformer로 같이 처리)를 사용했지만, ViLBERT는 이를 **Dual-Stream 구조**로 나누어 각각의 모달리티 특성을 유지하면서도 **Co-Attention**으로 정교하게 연결했다는 점이 핵심입니다.  

> 결과적으로 ViLBERT는 VQA, 캡셔닝, 이미지-텍스트 매칭 등 다양한 비전–언어 태스크에서 **멀티태스크 학습 기반 전이 성능**을 입증했습니다. ✅  

---

## ✨ TL;DR
- **문제**: 기존 멀티모달 모델은 이미지·텍스트를 효과적으로 정렬/융합하기 어려움  
- **아이디어**: 이미지와 텍스트를 **Dual-Stream Transformer**로 독립 처리 + **Co-Attention**으로 상호작용  
- **구현**: Faster R-CNN 기반 객체 특징 + BERT 기반 텍스트 인코더 → Co-Attention → 멀티모달 표현  
- **효과**: 다양한 V&L 태스크(VQA, Captioning 등)에서 SOTA 달성  

---

## 🧩 How It Works (한 장 요약)
1. **Input Features**  
   - **Vision Stream**: Faster R-CNN을 통해 객체 단위 Region Features 추출  
   - **Language Stream**: BERT Token Embedding 사용  
2. **Dual Transformer Streams**  
   - 각 모달리티는 독립적인 Transformer 블록에서 처리됨  
3. **Co-Attention Layers**  
   - Vision ↔ Language 간 교차 Attention을 통해 정보 교환  
   - 예: 질문 단어가 “dog”일 때, 이미지 내 “개” 관련 영역에 집중  
4. **Task Heads**  
   - 공통 멀티모달 표현을 기반으로 VQA, Captioning, Matching 등 다양한 다운스트림 태스크 적용  

---

## 🔍 강점(Strengths)
- **Dual-Stream 구조**: 각 모달리티 특성을 유지하면서 상호작용 가능  
- **전이성**: Pretraining 후 VQA, Retrieval 등 다수 태스크에서 성능 향상  
- **Co-Attention 시각화**: 어떤 단어가 어떤 시각적 영역과 연결되는지 해석 가능  

## ⚠️ 한계(Caveats)
- **복잡성**: Dual-Stream + Co-Attention으로 연산량/메모리 비용이 큼  
- **Region Feature 의존성**: Faster R-CNN 기반 객체 특징에 성능이 크게 좌우됨  
- **후속 연구의 진화**: 이후 UNITER, ALBEF, BLIP 등은 **Single-Stream** 혹은 더 효율적 구조로 발전  

---

## 🧭 실무 팁(Quick Tips)
- 객체 감지기(Faster R-CNN) 성능이 전체 결과에 강하게 영향 → 최신 Detectors로 교체 가능  
- Attention 맵 분석을 통해 모델이 “어떤 질문 단어와 어떤 이미지 영역을 연결했는지” 해석 가능  
- 실무 적용 시에는 **더 가벼운 Single-Stream 구조**(예: UNITER, CLIP 계열)를 선호하는 추세  

---

# 🚀 Presentation
