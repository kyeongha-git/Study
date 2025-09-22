# 👋 Introduction

본 발표는 **BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation (ICML, 2022)** 를 다룹니다.  

BLIP은 Vision–Language Pretraining(VLP) 분야에서 **이해(understanding)** 와 **생성(generation)** 을 동시에 다룰 수 있는 통합 모델을 제안했습니다.  
핵심은 **노이즈 많은 웹 데이터**에서 신뢰할 수 있는 학습 신호를 얻기 위해, 모델 스스로 **데이터를 정제(bootstrapping)** 하는 전략을 사용한 것입니다. ✨  

기존의 ALBEF, SimVLM은 강력했지만 여전히 noisy 데이터에 취약했습니다. BLIP은 **Caption Filtering** 과 **Caption Generation** 모듈을 함께 학습하여, 데이터 품질을 자동으로 개선하면서 학습할 수 있도록 설계되었습니다.  

> 결과적으로 BLIP은 VQA, Image-Text Retrieval 등 이해 과제뿐만 아니라, Captioning, Image-to-Text Generation 등 생성 과제에서도 강력한 성능을 보였습니다. ✅  

---

## ✨ TL;DR
- **문제**: 웹 이미지–텍스트 데이터는 노이즈가 많아 학습 품질 저하  
- **아이디어**: 모델이 스스로 **데이터를 정제(bootstrapping)** 하고, **이해+생성**을 동시에 학습  
- **구현**: Caption Filtering + Caption Generation + Unified Encoder-Decoder  
- **효과**: 이해/생성 과제 모두에서 강력한 범용 성능  

---

## 🧩 How It Works (한 장 요약)
1. **Input Encoding**  
   - Vision: ViT 기반 패치 임베딩  
   - Language: Transformer 기반 텍스트 임베딩  
2. **Bootstrapping**  
   - **Caption Filtering**: noisy 캡션을 걸러내고 신뢰도 높은 쌍만 학습  
   - **Caption Generation**: 이미지로부터 새로운 캡션 생성, 학습 데이터 보강  
3. **Unified Framework**  
   - Encoder: Vision-Language joint encoding  
   - Decoder: 텍스트 생성 (captioning, VQA 답변 등)  
4. **Multi-Task Pretraining**  
   - ITM, MLM, Captioning 등 다양한 목표 학습  

---

## 🔍 강점(Strengths)
- **데이터 품질 향상**: noisy 웹 데이터를 스스로 정제 가능  
- **범용성**: 이해와 생성 과제를 동시에 지원  
- **확장성**: VQA, Retrieval, Captioning 등 다양한 태스크 적용  

## ⚠️ 한계(Caveats)
- **학습 비용**: Filtering + Generation 추가로 연산량 증가  
- **데이터 의존성**: 여전히 대규모 웹 데이터 필요  
- **후속 발전**: BLIP-2는 LLM과 결합하여 더 큰 성능 향상  

---

## 🧭 실무 팁(Quick Tips)
- 데이터 품질이 낮은 환경에서도 활용 가능 → **자체 정제 기능** 덕분  
- 생성/이해 태스크를 동시에 다루는 경우 BLIP 구조가 적합  
- 최근에는 **BLIP-2, LLaVA** 등으로 확장 → LLM 연결 시 더 강력  

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드37" src="https://github.com/user-attachments/assets/06bc38ef-2ec0-42c3-a11d-61ad64329be2" />
<img width="1920" height="1080" alt="슬라이드38" src="https://github.com/user-attachments/assets/520a8f55-0daa-4b7c-8f10-7b0ced138522" />
<img width="1920" height="1080" alt="슬라이드39" src="https://github.com/user-attachments/assets/e06db907-72bd-41e4-8678-945e3a4d49cb" />
<img width="1920" height="1080" alt="슬라이드40" src="https://github.com/user-attachments/assets/9fd54519-2361-4570-8d78-d2b4584a624a" />
<img width="1920" height="1080" alt="슬라이드41" src="https://github.com/user-attachments/assets/e50cf6dd-b93c-42d2-b67f-abcd0622cd35" />
<img width="1920" height="1080" alt="슬라이드42" src="https://github.com/user-attachments/assets/c3d93c6c-30f2-45cd-b72d-f85763fa5735" />
<img width="1920" height="1080" alt="슬라이드43" src="https://github.com/user-attachments/assets/4a7e4156-f92c-488a-804b-05a14585be39" />
<img width="1920" height="1080" alt="슬라이드44" src="https://github.com/user-attachments/assets/9cb9c536-084d-4940-ace8-3e665ccc47d0" />
<img width="1920" height="1080" alt="슬라이드45" src="https://github.com/user-attachments/assets/f66ddd3a-63fa-4662-a48a-fb285a961f82" />











