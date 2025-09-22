# 👋 Introduction

본 발표는 **LLaVA: Large Language and Vision Assistant (arXiv, 2023)** 를 다룹니다.  

LLaVA는 BLIP-2 스타일의 **이미지 인코더 + LLM 결합 구조**를 기반으로, **Instruction Tuning** 을 통해 **대화형 멀티모달 어시스턴트**를 구현한 모델입니다.  
즉, 단순히 이미지–텍스트 매칭이나 캡셔닝에 그치지 않고, 사용자의 **자연어 지시(instruction)** 에 따라 다양한 비전–언어 태스크를 수행할 수 있도록 확장되었습니다. ✨  

핵심 아이디어는 **BLIP-2의 Q-Former 구조**로 이미지 특징을 추출한 뒤, 이를 LLM 입력으로 연결하고, **대규모 멀티모달 instruction 데이터**로 파인튜닝하는 것입니다. 이를 통해 LLaVA는 ChatGPT와 유사한 상호작용을 이미지까지 확장할 수 있게 되었습니다.  

> 결과적으로 LLaVA는 VQA, 이미지 설명, 자유형 질의응답 등에서 강력한 성능을 보였으며, 이후 멀티모달 ChatGPT 계열 연구의 대표적 베이스라인으로 자리잡았습니다. ✅  

---

## ✨ TL;DR
- **문제**: 기존 VLP 모델은 단순 이해/생성에 집중 → 대화형 멀티모달 인터페이스 부족  
- **아이디어**: 이미지 인코더 + LLM 결합 후, Instruction Tuning으로 대화형 VLM 구현  
- **구현**: BLIP-2 기반 Q-Former로 이미지 특징 추출 → LLM 입력 → 멀티모달 Instruction Fine-Tuning  
- **효과**: 멀티모달 ChatGPT 스타일 상호작용 가능  

---

## 🧩 How It Works (한 장 요약)
1. **Frozen Image Encoder**  
   - CLIP ViT 등 대규모 비전 인코더 사용  
2. **Q-Former**  
   - BLIP-2와 유사하게 Query Token으로 이미지 특징을 추출  
   - LLM 입력에 맞게 변환  
3. **LLM Backbone**  
   - Vicuna, LLaMA 등 사전학습된 LLM 사용  
   - 이미지 표현 + 텍스트 입력을 동시에 처리  
4. **Instruction Tuning**  
   - 대규모 (이미지, 질문, 답변) 데이터로 지도학습  
   - 대화형 멀티모달 어시스턴트로 진화  

---

## 🔍 강점(Strengths)
- **대화형 능력**: 단순 QA/Captioning을 넘어 대화형 멀티모달 어시스턴트 구현  
- **효율성**: BLIP-2 기반 설계로 자원 효율적  
- **범용성**: VQA, Captioning, Instruction Following 등 다양한 태스크 지원  

## ⚠️ 한계(Caveats)
- **LLM 품질 의존성**: 백본 LLM 성능에 크게 좌우됨  
- **데이터 편향**: Instruction 데이터 품질에 따라 응답 신뢰도 편차 발생  
- **후속 발전**: LLaVA-1.5, LLaVA-Next 등 최신 버전은 더 큰 데이터와 더 정교한 튜닝 적용  

---

## 🧭 실무 팁(Quick Tips)
- 기존 LLM에 이미지 입력을 붙이고 싶을 때, BLIP-2 → LLaVA 파이프라인이 좋은 출발점  
- Instruction Tuning 데이터셋 품질 관리가 핵심 → 작은 오류도 모델 응답에 크게 반영됨  
- 대화형 인터페이스 구축 시 LLaVA는 **멀티모달 ChatGPT 베이스라인**으로 활용 가능  

---

# 🚀 Presentation
