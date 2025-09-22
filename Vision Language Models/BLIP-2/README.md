# 👋 Introduction

본 발표는 **BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (ICML, 2023)** 를 다룹니다.  

BLIP-2는 Vision–Language 모델과 LLM(대규모 언어 모델)을 연결하는 **효율적인 브릿지 아키텍처**를 제안했습니다.  
핵심 아이디어는 **이미지 인코더(예: ViT, EVA-CLIP)** 와 **거대한 LLM(GPT 계열, OPT 등)** 을 **동결(frozen)** 한 채로, 중간에 **Q-Former(Querying Transformer)** 를 삽입하여 두 모달리티를 효과적으로 이어주는 것입니다. ✨  

기존 Flamingo는 강력했지만 초대규모 모델과 많은 계산 자원을 필요로 했습니다. BLIP-2는 **프리트레이닝된 모듈을 동결**하고, 얇은 Q-Former만 학습함으로써 자원 효율성을 확보하면서도 강력한 성능을 달성했습니다.  

> 결과적으로 BLIP-2는 VQA, Captioning, Reasoning 등 다양한 멀티모달 태스크에서 SOTA를 달성했고, 이후 LLaVA 등 **Instruction-following VLM** 연구의 기반이 되었습니다. ✅  

---

## ✨ TL;DR
- **문제**: 초대규모 VLM은 연산/메모리 비용이 너무 큼  
- **아이디어**: 이미지 인코더·LLM을 **동결**하고, 얇은 Q-Former로 연결  
- **구현**: Q-Former가 이미지 특징을 압축·질의 형태로 변환 → LLM 입력으로 투영  
- **효과**: 자원 효율성과 성능을 동시에 확보  

---

## 🧩 How It Works (한 장 요약)
1. **Frozen Image Encoder**  
   - ViT, EVA-CLIP 등 대규모 비전 인코더는 그대로 사용  
2. **Q-Former (Querying Transformer)**  
   - 학습 가능한 Query Token을 통해 이미지 특징 요약  
   - LLM에 적합한 크기의 벡터로 변환  
3. **Frozen LLM**  
   - GPT, OPT 등 대규모 LLM은 동결  
   - 입력으로 Q-Former 출력 + 텍스트 토큰  
4. **Training Objectives**  
   - ITM, ITC, Captioning 등 다중 태스크 학습  
   - 생성/이해 모두 지원  

---

## 🔍 강점(Strengths)
- **자원 효율성**: 거대한 Image Encoder와 LLM을 동결 → Q-Former만 학습  
- **범용성**: 이해(VQA, Retrieval) + 생성(Captioning, QA) 모두 지원  
- **확장성**: 다양한 LLM과 연결 가능 → 멀티모달 어댑터 역할  

## ⚠️ 한계(Caveats)
- **성능 한계**: 동결된 LLM의 한계를 직접적으로 극복하긴 어려움  
- **Q-Former 의존성**: 연결 품질이 Q-Former 설계/학습에 크게 좌우됨  
- **후속 발전**: LLaVA 등 Instruction-tuned VLM은 BLIP-2를 기반으로 더 발전  

---

## 🧭 실무 팁(Quick Tips)
- 기존 LLM에 멀티모달 입력을 연결하고 싶을 때 효율적 접근  
- Q-Former는 일종의 **Adapter** 역할 → 파라미터 효율적 학습 가능  
- Instruction-following 멀티모달 시스템 설계 시, BLIP-2가 좋은 출발점  

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드71" src="https://github.com/user-attachments/assets/69f35ace-e522-4348-8ca6-0249caabd56a" />
<img width="1920" height="1080" alt="슬라이드72" src="https://github.com/user-attachments/assets/3972ba7a-d0a3-4361-87a0-95a56a6d0896" />
<img width="1920" height="1080" alt="슬라이드73" src="https://github.com/user-attachments/assets/be560a29-26e7-465a-8281-8d86fb118ae3" />
<img width="1920" height="1080" alt="슬라이드74" src="https://github.com/user-attachments/assets/ca7ab4bd-c6c2-4095-a151-62c5327a0aa7" />
<img width="1920" height="1080" alt="슬라이드75" src="https://github.com/user-attachments/assets/f12501e2-5cdb-4b89-b907-eaaa4e1ebf18" />
<img width="1920" height="1080" alt="슬라이드76" src="https://github.com/user-attachments/assets/889fb5e9-ded4-4dc7-bbc7-454ce9562470" />
<img width="1920" height="1080" alt="슬라이드77" src="https://github.com/user-attachments/assets/8a9d3931-ae2c-4442-90f7-69b8f13bae36" />
<img width="1920" height="1080" alt="슬라이드78" src="https://github.com/user-attachments/assets/04436a66-ed47-45aa-a5d2-2f2625ed6f06" />
<img width="1920" height="1080" alt="슬라이드79" src="https://github.com/user-attachments/assets/588c63ac-1c6c-49a8-9265-fd1e8b4b0157" />

















