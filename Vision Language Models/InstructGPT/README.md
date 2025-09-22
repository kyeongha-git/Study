# 👋 Introduction

본 발표는 **InstructGPT: Training language models to follow instructions with human feedback (NeurIPS, 2022)** 를 다룹니다.  

InstructGPT는 GPT-3를 기반으로, 단순한 대규모 언어 모델이 아닌 **“사용자의 지시를 따르는 모델”** 로 개선하기 위해 제안되었습니다.  
핵심 아이디어는 **Human Feedback을 통한 강화학습(RLHF, Reinforcement Learning with Human Feedback)** 으로, 사람이 원하는 출력을 보상 신호로 삼아 모델을 튜닝하는 것입니다. ✨  

기존 GPT-3는 강력한 언어 능력을 보였지만, **사용자 지시와 동떨어진 답변**이나 **비윤리적/편향적 출력**을 생성하는 경우가 많았습니다. InstructGPT는 이를 개선하여, 더 안전하고 유용하며 사람의 의도를 따르는 모델로 진화했습니다.  

> 결과적으로 InstructGPT는 단순 성능 지표(perplexity)가 아니라, **사람이 선호하는 출력** 기준에서 GPT-3보다 훨씬 우수한 평가를 받았으며, 이는 이후 ChatGPT 개발의 직접적인 기반이 되었습니다. ✅  

---

## ✨ TL;DR
- **문제**: GPT-3는 강력하지만, 사람 지시를 따르지 못하거나 비윤리적 출력 생성  
- **아이디어**: RLHF를 통해 사람이 선호하는 방향으로 모델을 조정  
- **구현**: Supervised Fine-Tuning → Reward Model 학습 → RLHF 단계적 적용  
- **효과**: GPT-3 대비 사람 선호도와 유용성이 크게 향상  

---

## 🧩 How It Works (한 장 요약)
1. **Supervised Fine-Tuning (SFT)**  
   - 프롬프트와 사람 작성 답변 데이터로 GPT-3를 먼저 튜닝  
2. **Reward Model Training**  
   - 여러 모델 답변 중 사람 선호 순위를 학습하여 Reward Model 생성  
3. **RLHF (PPO 기반 강화학습)**  
   - GPT 출력 → Reward Model 점수 → 보상 기반 업데이트  
   - PPO(Proximal Policy Optimization)로 안정적 학습  
4. **Outcome**  
   - 사람 지시를 더 잘 따르고, 유해/편향 출력 감소  

---

## 🔍 강점(Strengths)
- **사람 중심**: Perplexity 대신 사람 선호 기준에서 성능 평가  
- **안전성 개선**: 유해·편향적 응답을 줄이고 더 유용한 답변 생성  
- **ChatGPT 기반**: 이후 ChatGPT 제품의 핵심 기술적 기초  

## ⚠️ 한계(Caveats)
- **데이터 비용**: 인간 피드백 수집이 고비용  
- **Reward Model 한계**: 사람의 편향이 반영될 수 있음  
- **완전 해결 아님**: 여전히 안전성·윤리 문제는 존재  

---

## 🧭 실무 팁(Quick Tips)
- RLHF는 LLM을 **사용자 지향적**으로 만드는 핵심 → 멀티모달 VLM에도 확장 가능  
- Reward Model 품질이 전체 성능을 좌우 → annotation 품질 관리 중요  
- 실무에선 **SFT 데이터 + RLHF** 조합으로 빠른 도입 가능  

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드80" src="https://github.com/user-attachments/assets/e60ee280-a1fb-4906-97e7-339441e0de6c" />
<img width="1920" height="1080" alt="슬라이드81" src="https://github.com/user-attachments/assets/fd75544f-48a8-4424-898f-6d9144f69f50" />
<img width="1920" height="1080" alt="슬라이드82" src="https://github.com/user-attachments/assets/f08e20ee-3aac-499a-aba0-9547af45cd7e" />
<img width="1920" height="1080" alt="슬라이드83" src="https://github.com/user-attachments/assets/a3b492fc-5f59-490a-90fb-611c848be240" />
<img width="1920" height="1080" alt="슬라이드84" src="https://github.com/user-attachments/assets/f941f0e5-ad53-41f9-aaa5-ea8a4ee91bfd" />
<img width="1920" height="1080" alt="슬라이드85" src="https://github.com/user-attachments/assets/19e1d4ed-0b25-4ff8-ad02-6a714f49d8a1" />
<img width="1920" height="1080" alt="슬라이드86" src="https://github.com/user-attachments/assets/02a3b9ff-a6a5-48d0-8f17-eee7c5daecf4" />
<img width="1920" height="1080" alt="슬라이드87" src="https://github.com/user-attachments/assets/cc7d4f62-b680-4dff-a63a-4bb326351b99" />
<img width="1920" height="1080" alt="슬라이드88" src="https://github.com/user-attachments/assets/f115c70a-9b91-4256-8d6a-ccd07627e6f2" />









