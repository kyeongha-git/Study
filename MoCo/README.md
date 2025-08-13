# 👋 Introduction

본 발표는 **FAIR(Facebook AI Research)의 MoCo — Momentum Contrast for Unsupervised Visual Representation Learning (He et al., 2019)** 를 다룹니다.

**MoCo**는 대조학습(contrastive learning)에서 성능을 좌우하는 두 축—① **큰 사전(dictionary)** 과 ② **키 임베딩의 일관성(consistency)**—을 동시에 달성하기 위해 **FIFO 큐(Queue)** 와 **모멘텀 인코더(EMA 업데이트)** 를 결합한 방법입니다. 🔧🧠

### 문제의식
- **많은 음성(negative) 샘플**이 필요하지만, 일반적인 within-batch 방식은 **배치 크기 한계**로 사전이 작아집니다.
- **메모리뱅크(memory bank)** 는 큰 사전을 제공하지만, **키 분포가 오래되어(stale) 불일치**가 커져 학습이 불안정할 수 있습니다.

### 핵심 아이디어
- **Larger Dictionary → Queue**  
  학습 중 생성된 키 임베딩을 **FIFO 큐에 적재/교체**하여, **배치와 무관하게 매우 큰 사전**(수만 개 수준)을 유지합니다. 📚
- **Consistency → Momentum Encoder**  
  키 인코더의 파라미터를 쿼리 인코더의 파라미터로 **모멘텀(지수이동평균) 업데이트**하여, 시간에 따른 **키 분포 변화를 완화**합니다. 🔒  
  `θ_key ← m · θ_key + (1−m) · θ_query`  *(보통 m은 0.99~0.999대)*

### 학습 방식(요지)
1) 같은 이미지에 **두 가지 증강**을 적용해 **쿼리 q**와 **양성 키 k⁺**를 만듭니다.  
2) 큐에 저장된 **다수의 음성 키 {k⁻}** 와 함께 **InfoNCE** 손실로 학습합니다.  
3) 매 스텝마다 k⁺를 큐에 **enqueue**, 가장 오래된 키를 **dequeue**하여 **큰 사전**을 유지합니다.

> **유사도**는 보통 **dot product**를 사용하며, **특징을 정규화**하면 코사인 유사도와 동치가 됩니다.  
> **온도(τ)** 로 스케일을 조절합니다 *(예: τ≈0.07)*.

---

## ✨ TL;DR
- **큰 사전**(Queue) + **일관된 키**(Momentum Encoder) → **작은 배치**로도 **강한 대조학습** 가능  
- **선형 분류(linear eval)**, **감지/세그멘테이션 전이**에서 **감독학습 사전학습**과 **경쟁적 성능**  
- **메모리 효율/안정성**: 언제나 최신 배치에만 의존하지 않고, 시간적으로 부드러운 키 분포를 유지

---

## 🧩 SimCLR / Memory Bank와의 차이
- **SimCLR**: 음성 샘플을 **배치 내**에서 확보 → **아주 큰 배치**가 필요  
  **MoCo**: **큐**로 큰 사전을 유지 → **배치 크기 의존도↓**, 모멘텀 인코더로 **분포 일관성↑**
- **Memory Bank(InstDisc 등)**: 큰 사전은 가능하지만 **키 최신성/일관성** 문제가 큼  
  **MoCo**: **EMA 업데이트**로 **키 최신성**을 개선

---

## 🛠️ 구현 체크리스트(실무 팁)
- **Queue size**: 수만 단위 *(예: 65,536)*  
- **Momentum m**: 0.99~0.999대 *(높을수록 업데이트가 느려져 일관성↑)*  
- **Temperature τ**: ~0.07 전후  
- **Projection head**: 2-layer MLP(ℓ2 정규화) 권장 *(MoCo v2 스타일)*  
- **BN 주의**: 멀티GPU에서 **ShuffleBN** 트릭으로 통계 누수 방지  
- **Augmentations**: 강한 증강(RandAug/ColorJitter 등) + 그레이스케일/가우시안 블러 조합

---

## ⚠️ 한계와 유의
- **양의/음의 샘플 정의**가 증강에 의존 → **뷰 선택**이 성능에 큰 영향  
- **Dense 예측**(정밀 로컬라이제이션 등)에는 추가 기법/파인튜닝이 필요할 수 있음  
- 큐 크기·m·τ 등의 **하이퍼파라미터 감도** 존재

---

# 🚀 Presentation
<img width="1920" height="1080" alt="001" src="https://github.com/user-attachments/assets/10714b00-3e27-4554-8f84-12fa821891de" />
<img width="1920" height="1080" alt="002" src="https://github.com/user-attachments/assets/37b1ab75-aa79-43ca-9d3e-70d592f91789" />
<img width="1920" height="1080" alt="003" src="https://github.com/user-attachments/assets/6457815b-a311-460a-bcbb-1cd81935a571" />
<img width="1920" height="1080" alt="004" src="https://github.com/user-attachments/assets/7192022d-e911-4855-bb9d-d8f56625e46c" />
<img width="1920" height="1080" alt="005" src="https://github.com/user-attachments/assets/3fe6d78c-3736-4a62-87da-c14043735f73" />
<img width="1920" height="1080" alt="006" src="https://github.com/user-attachments/assets/982f3b89-1888-4e74-b7da-3c46126ed531" />
<img width="1920" height="1080" alt="007" src="https://github.com/user-attachments/assets/9f4e7ca9-933c-4d6c-b345-bd8b396bf548" />
<img width="1920" height="1080" alt="008" src="https://github.com/user-attachments/assets/ca76a473-4883-4f35-bf6e-0af1cee268db" />
<img width="1920" height="1080" alt="009" src="https://github.com/user-attachments/assets/bd27d570-63f9-4135-a9fd-df31612ce61d" />
<img width="1920" height="1080" alt="010" src="https://github.com/user-attachments/assets/e9ff20e6-cf7e-4ab3-8756-8afd5dd3c983" />
<img width="1920" height="1080" alt="011" src="https://github.com/user-attachments/assets/dbb7a240-15aa-4bb7-851c-752eb5613db6" />
<img width="1920" height="1080" alt="012" src="https://github.com/user-attachments/assets/e397314f-b872-4ba8-888b-5b3e8634df85" />
<img width="1920" height="1080" alt="013" src="https://github.com/user-attachments/assets/cab9cf4c-925b-48ce-a280-4def72d4c80e" />
<img width="1920" height="1080" alt="014" src="https://github.com/user-attachments/assets/e4d837bf-ed53-4aa5-89ff-7febc33ca000" />
<img width="1920" height="1080" alt="015" src="https://github.com/user-attachments/assets/40889c6f-7089-4f83-819c-f09274a343b0" />
<img width="1920" height="1080" alt="016" src="https://github.com/user-attachments/assets/fa60854a-5315-47f4-8d32-60e8f430b70a" />
<img width="1920" height="1080" alt="017" src="https://github.com/user-attachments/assets/1eafd6c0-683a-4162-a956-5e4fe9b5e752" />
<img width="1920" height="1080" alt="018" src="https://github.com/user-attachments/assets/12cfadc1-c49b-4347-ba68-135f4dbbc366" />
<img width="1920" height="1080" alt="019" src="https://github.com/user-attachments/assets/93a7c58a-355d-40ea-badc-028d04b7d3f1" />
