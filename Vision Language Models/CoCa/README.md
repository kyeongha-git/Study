# 👋 Introduction

본 발표는 **CoCa: Contrastive Captioners are Image-Text Foundation Models (arXiv 2022 → CVPR 2023)** 를 다룹니다.  

CoCa는 Google Research에서 제안한 모델로, **대조학습(contrastive learning)** 과 **캡셔닝(captioning)** 을 결합한 통합적 Vision–Language Pretraining(VLP) 프레임워크입니다.  
즉, **이미지–텍스트 정렬(understanding)** 과 **텍스트 생성(generation)** 을 동시에 학습하여, 멀티모달 이해와 생성 과제 모두에서 뛰어난 성능을 발휘했습니다. ✨  

기존 CLIP은 강력한 제로샷 이해 성능을 보였지만 텍스트 생성을 다루지 못했고, BLIP은 생성까지 다루었으나 noisy 데이터 처리에 추가 모듈이 필요했습니다. CoCa는 **단일 Encoder–Decoder 구조** 안에서 **Contrastive Loss + Captioning Loss** 를 함께 학습함으로써 단순하면서도 강력한 성능을 달성했습니다.  

> 결과적으로 CoCa는 제로샷 분류·검색 등 이해 과제에서 CLIP을 능가하면서, 캡셔닝·생성 태스크에서도 우수한 성능을 보여 **멀티모달 파운데이션 모델**의 방향성을 제시했습니다. ✅  

---

## ✨ TL;DR
- **문제**: CLIP은 이해 전이에 강하지만, 텍스트 생성 능력 부재  
- **아이디어**: Contrastive 학습 + Captioning 학습을 **하나의 프레임워크**에서 동시 수행  
- **구현**: Encoder–Decoder Transformer 구조에서 Dual Loss 학습  
- **효과**: 이해와 생성 과제 모두에서 SOTA 수준 성능 달성  

---

## 🧩 How It Works (한 장 요약)
1. **Input Representation**  
   - Vision Encoder: ViT 기반 이미지 임베딩  
   - Text Encoder: Transformer 기반 텍스트 임베딩  
2. **Dual Objective**  
   - **Contrastive Loss**: 이미지–텍스트 쌍 정렬 (CLIP 스타일)  
   - **Captioning Loss**: 이미지에서 텍스트 생성 (Seq2Seq)  
3. **Unified Encoder–Decoder**  
   - Encoder: 이미지/텍스트 입력 임베딩  
   - Decoder: Captioning 및 생성  
4. **Zero-shot & Generation**  
   - 이해(Task: Retrieval, Classification)  
   - 생성(Task: Captioning, Free-form Generation)  

---

## 🔍 강점(Strengths)
- **단순+강력**: Contrastive + Captioning을 하나의 구조에서 통합  
- **범용성**: 이해와 생성 태스크 모두 지원  
- **SOTA 성능**: 제로샷/파인튜닝 모두에서 강력  

## ⚠️ 한계(Caveats)
- **데이터 의존성**: 여전히 초대규모 웹 데이터 필요  
- **계산 비용**: Contrastive + Captioning 병행으로 학습 자원 요구 ↑  
- **후속 발전**: Flamingo, BLIP-2, LLaVA 등 LLM 연계 모델 등장  

---

## 🧭 실무 팁(Quick Tips)
- 이해+생성을 모두 다루는 파운데이션 모델을 원할 때 적합  
- Contrastive Loss는 제로샷 전이력 강화, Captioning Loss는 생성 품질 개선 → 두 가지를 함께 유지하는 게 중요  
- CoCa 이후 연구는 **LLM 결합**으로 발전하므로, CoCa는 그 **중간 세대**로 이해하는 것이 유용  

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드53" src="https://github.com/user-attachments/assets/85917910-99bb-4479-8059-6ce432b64253" />
<img width="1920" height="1080" alt="슬라이드54" src="https://github.com/user-attachments/assets/2c062f97-5625-4b9e-b2d9-87baa1c83705" />
<img width="1920" height="1080" alt="슬라이드55" src="https://github.com/user-attachments/assets/62d54fd0-5f2e-4fdf-887a-9b9a17c6091d" />
<img width="1920" height="1080" alt="슬라이드56" src="https://github.com/user-attachments/assets/345d4f4c-ea77-4de5-b22e-d8f389bad27e" />
<img width="1920" height="1080" alt="슬라이드57" src="https://github.com/user-attachments/assets/e8d70257-89da-48bd-ad98-fefe6ae1fb0b" />
<img width="1920" height="1080" alt="슬라이드58" src="https://github.com/user-attachments/assets/d6c56d56-563e-4334-aba7-9682491085be" />
<img width="1920" height="1080" alt="슬라이드59" src="https://github.com/user-attachments/assets/11abc181-287d-4678-bb21-b90c7d7f3448" />
<img width="1920" height="1080" alt="슬라이드60" src="https://github.com/user-attachments/assets/ac39a70b-3ca9-4ecf-9f50-10f99e352e8b" />
<img width="1920" height="1080" alt="슬라이드61" src="https://github.com/user-attachments/assets/9052be45-91ac-499b-a3b5-245dd2b0e170" />









