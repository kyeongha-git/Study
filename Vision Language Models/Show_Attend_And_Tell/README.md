# 👋 Introduction

본 발표는 **Show, Attend and Tell: Neural Image Caption Generation with Visual Attention (ICML, 2015)** 를 다룹니다.  

이 연구는 **이미지 캡셔닝(image captioning)** 과제에 **Attention 메커니즘**을 최초로 본격 도입하여, 모델이 **이미지의 특정 영역에 “집중(attend)”** 하면서 자연어 설명을 생성할 수 있음을 보여주었습니다. 이는 이후 **Neural Machine Translation의 Attention**, 더 나아가 **Transformer** 기반 연구의 초석이 되었습니다. ✨  

기존의 캡셔닝 모델은 CNN으로 특징을 추출한 뒤, 전체 이미지를 요약한 하나의 벡터만을 RNN/LSTM에 입력하여 문장을 생성했습니다. 하지만 이런 접근은 **공간적 정보 손실**이 크고, 세밀한 디테일 반영이 어려웠습니다. Show, Attend and Tell은 **Soft/Hard Attention**을 통해 단어를 생성할 때마다 이미지의 다른 부분을 선택적으로 바라볼 수 있게 했습니다.  

> 결과적으로 모델은 “고양이가 소파 위에 앉아 있다” 같은 설명을 만들 때, **“고양이”라는 단어를 생성할 때는 고양이 부분**, **“소파”를 생성할 때는 소파 영역**을 주목하는 등, **시각적 정렬(visual grounding)** 을 자연스럽게 학습할 수 있게 되었습니다. ✅  

---

## ✨ TL;DR
- **문제**: 기존 CNN+RNN 캡셔닝은 이미지 전체를 하나의 벡터로 요약 → 세밀한 정보 손실  
- **아이디어**: 단어 생성 시마다 이미지 특정 부분에 **Attention 가중치** 할당  
- **구현**: CNN 특징맵을 위치 단위로 유지, LSTM이 단어를 생성할 때 Soft/Hard Attention 사용  
- **효과**: 더 자연스럽고 구체적인 캡션 생성 + 모델의 “어디를 보는지” 해석 가능  

---

## 🧩 How It Works (한 장 요약)
1. **Feature Extraction**  
   - CNN(예: GoogLeNet, VGG) → 지역 특징맵 \( \{a_1, a_2, ..., a_L\} \) 추출  
2. **Attention Mechanism**  
   - 단어 \( y_t \) 생성 시, LSTM hidden state \( h_{t-1} \)를 이용해 각 위치 \( i \)의 가중치 \( \alpha_i \) 계산  
   - \( z_t = \sum_i \alpha_i a_i \) (Soft Attention)  
   - 또는 위치를 샘플링해 선택 (Hard Attention)  
3. **Caption Generation**  
   - \( z_t \) + 이전 단어 임베딩으로 LSTM 업데이트  
   - 새로운 단어 \( y_t \) 생성  
4. **Interpretability**  
   - Attention map을 시각화하면 모델이 단어마다 어디를 보는지 확인 가능  

---

## 🔍 강점(Strengths)
- **해석 가능성**: Attention 맵을 통해 모델의 시각적 집중 영역을 직접 확인 가능  
- **성능 향상**: 기존 CNN+RNN보다 더 정확하고 자연스러운 캡션 생성  
- **일반화**: Attention 개념이 이후 **NLP, Vision, Multimodal 연구**로 폭넓게 확산  

## ⚠️ 한계(Caveats)
- **연산 비용**: Attention 계산으로 학습/추론 비용 증가  
- **Hard Attention 학습 난이도**: 비연속적 샘플링은 REINFORCE 같은 강화학습 필요 → 불안정  
- **대규모 데이터 한계**: 당시엔 COCO 캡셔닝 정도에서 검증, 지금 기준에선 작은 스케일  

---

## 🧭 실무 팁(Quick Tips)
- Attention 맵 시각화로 **모델 오류 분석** 가능  
- Soft Attention은 안정적이고 학습 용이, Hard Attention은 해석력은 높으나 학습 난이도 ↑  
- 현대 Transformer 계열 모델(예: ViT, VLM)의 Attention을 이해할 때 기초가 됨  

---

# 🚀 Presentation
