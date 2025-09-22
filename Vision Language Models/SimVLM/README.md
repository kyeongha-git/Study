# 👋 Introduction

본 발표는 **SimVLM: Simple Visual Language Model Pretraining with Weak Supervision (ICLR, 2022)** 를 다룹니다.  

SimVLM은 이름 그대로 **단순화(Simple)** 를 핵심 설계 철학으로 삼은 Vision–Language Pretraining(VLP) 모델입니다.  
기존의 UNITER, ALBEF 등이 복잡한 멀티태스크 목표(MLM, ITM, MRM 등)를 활용했던 것과 달리, SimVLM은 **Prefix Language Modeling (PrefixLM)** 단일 목표만을 사용하여 효율적이면서도 강력한 성능을 달성했습니다. ✨  

또한, SimVLM은 **대규모 웹 이미지–텍스트 쌍(Conceptual Captions, ALIGN, COYO 등)** 을 활용하여 **weak supervision** 환경에서 학습되었으며, 단순한 구조와 목표만으로도 강한 범용성을 보여주었습니다.  

> 결과적으로 SimVLM은 COCO Captions, NoCaps, VQA 등 다양한 비전–언어 태스크에서 당시 SOTA에 근접하거나 능가하는 성능을 보여주며, **“단순함이 강점”** 이 될 수 있음을 증명했습니다. ✅  

---

## ✨ TL;DR
- **문제**: 기존 VLP 모델은 프리트레이닝 목표가 복잡하고 학습 비용이 큼  
- **아이디어**: 단일 목표인 **PrefixLM** 만으로 Vision–Language 공동 학습  
- **구현**: 이미지를 텍스트 prefix로 넣고 Transformer LM으로 문장 예측  
- **효과**: 단순하지만 대규모 데이터에서 강력한 성능 달성  

---

## 🧩 How It Works (한 장 요약)
1. **Input Representation**  
   - **Vision**: CNN/ViT 기반 패치 임베딩  
   - **Language**: 텍스트 토큰 임베딩  
   - 이미지를 텍스트 prefix로 취급하여 Transformer 입력에 포함  
2. **Prefix Language Modeling (PrefixLM)**  
   - 입력: [Image Patch Prefix] + [Text Tokens]  
   - 목표: 다음 텍스트 토큰을 autoregressive하게 예측  
3. **Weakly-Supervised Learning**  
   - 수억 규모의 웹 이미지–텍스트 쌍 활용  
   - 별도의 복잡한 라벨링 불필요  
4. **Downstream Tasks**  
   - Captioning, VQA, Retrieval 등 다양한 V&L 태스크로 전이  

---

## 🔍 강점(Strengths)
- **단순성**: PrefixLM 하나만으로도 범용 학습 가능  
- **스케일 친화적**: 대규모 웹 데이터에서 강력한 성능  
- **범용성**: Captioning, VQA, Retrieval 등 다양한 태스크에 적용 가능  

## ⚠️ 한계(Caveats)
- **데이터 의존성**: 성능은 초대규모 웹 데이터에 크게 의존  
- **Fine-grained 태스크**: 세밀한 지역 수준 이해(Detection 등)는 상대적으로 제한적  
- **후속 발전**: BLIP, CoCa 등은 더 정교한 학습 전략과 멀티태스크 목표를 채택  

---

## 🧭 실무 팁(Quick Tips)
- SimVLM 스타일의 단순 목표 학습은 **빠른 프로토타입** 구현에 적합  
- PrefixLM은 기존 LLM 파이프라인과 통합하기 용이 → Vision-Language 확장에 활용 가능  
- 대규모 데이터 확보가 어려운 경우, 성능이 제한될 수 있음  

---

# 🚀 Presentation
