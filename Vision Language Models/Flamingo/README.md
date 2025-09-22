# 👋 Introduction

본 발표는 **Flamingo: a Visual Language Model for Few-Shot Learning (NeurIPS, 2022)** 를 다룹니다.  

Flamingo는 DeepMind가 제안한 멀티모달 모델로, **Few-Shot 학습**을 중심으로 설계되었습니다.  
핵심 아이디어는 **사전 학습된 거대한 LLM** 과 **비전 인코더**를 결합하되, 중간에 **Cross-Attention 모듈(Perceiver-style Resampler)** 을 삽입하여, LLM이 이미지 시퀀스를 유연하게 다룰 수 있도록 하는 것입니다. ✨  

기존 CLIP, BLIP 계열은 강력한 성능을 보였지만, **Few-Shot 적응**에는 한계가 있었습니다. Flamingo는 LLM의 in-context learning 능력을 활용해, 단 몇 개의 이미지–텍스트 예시만 주어도 새로운 태스크에 적응할 수 있음을 보여주었습니다.  

> 결과적으로 Flamingo는 VQA, 이미지 설명, 멀티이미지 추론 등 다양한 태스크에서 **Few-Shot 세팅에서의 강력한 성능**을 달성했습니다. ✅  

---

## ✨ TL;DR
- **문제**: 기존 멀티모달 모델은 Few-Shot 적응력이 약함  
- **아이디어**: 사전 학습된 LLM + Vision Encoder 사이에 Cross-Attention 모듈 삽입  
- **구현**: Frozen LLM + Perceiver Resampler 기반 멀티모달 연결  
- **효과**: Few-Shot VQA, Captioning 등에서 SOTA 성능  

---

## 🧩 How It Works (한 장 요약)
1. **Vision Encoder**  
   - CLIP/ViT 기반 이미지 임베딩 추출  
2. **Perceiver Resampler**  
   - 고차원 이미지 특징을 소수의 latent token으로 요약  
   - LLM에 입력 가능한 크기로 축소  
3. **Frozen LLM + Cross-Attention**  
   - 대규모 사전학습된 LLM은 고정  
   - 중간 Cross-Attention 레이어에서 Vision token과 상호작용  
4. **Few-Shot Inference**  
   - LLM의 In-Context Learning 활용  
   - 몇 개의 (이미지, 텍스트) 예시만으로 새로운 태스크 수행  

---

## 🔍 강점(Strengths)
- **Few-Shot 강점**: 새로운 태스크를 소량의 예시만으로 빠르게 적응  
- **LLM 활용**: 거대한 사전학습 LLM의 지식과 추론 능력 활용  
- **범용성**: VQA, 멀티이미지 추론, Captioning 등 다양한 태스크 적용  

## ⚠️ 한계(Caveats)
- **자원 요구**: 초대규모 LLM + Vision Encoder 조합 → 학습·추론 비용 큼  
- **데이터 효율성**: Few-Shot 적응은 강력하지만, Zero-Shot 성능은 제한적  
- **후속 연구 발전**: BLIP-2, LLaVA 등은 Flamingo의 구조를 단순화/개선  

---

## 🧭 실무 팁(Quick Tips)
- 멀티모달 Few-Shot 학습이 필요한 경우 적합  
- 사전학습된 LLM과 결합 시 **Cross-Attention 모듈 설계**가 핵심  
- 최근 VLM(예: BLIP-2, LLaVA)은 Flamingo의 아이디어를 더 가볍게 재현  

---

# 🚀 Presentation
