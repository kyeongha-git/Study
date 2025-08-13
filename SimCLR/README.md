# 👋 Introduction

본 발표는 **A Simple Framework for Contrastive Learning of Visual Representations (SimCLR; Chen et al., 2020)** 를 다룹니다.  
SimCLR는 **메모리뱅크나 모멘텀 인코더 없이**, **배치 내부의 모든 샘플을 음성(negative)으로 활용**하는 간결한 대조학습 프레임워크를 제안합니다. 강력한 데이터 증강과 **투영 헤드(projection head)**, **온도(temperature) 조절이 있는 NT-Xent(InfoNCE 계열) 손실**을 조합하여, **라벨 없이 학습한 표현**이 ImageNet에서 **선형 분류(Linear Eval)** 기준으로 당시 **SOTA에 근접/갱신**하는 것을 보였습니다.

## ✨ TL;DR
- **핵심 구성**: (강한 증강) → (백본 인코더, 보통 ResNet) → (투영 헤드 MLP) → (ℓ2 정규화) → **NT-Xent 손실**  
- **인배치 음성**: 메모리뱅크나 큐 없이 **배치 내의 다른 모든 뷰를 음성**으로 간주 → **큰 배치일수록** 유리  
- **투영 헤드의 가치**: 표현 공간(인코더 출력)과 대조 학습 공간(투영 후) **분리**가 성능 향상에 기여  
- **결과**: Self-Supervised임에도 **선형 프로브**에서 **감독학습에 근접/경쟁**하는 성능

## 🧩 어떻게 동작하나 (요지)
1. 각 이미지에 **두 가지 독립 증강**(랜덤 크롭/리사이즈, 컬러 왜곡, 그레이스케일, 가우시안 블러 등)을 적용 → **두 뷰** 생성  
2. 각 뷰를 **공유 가중치 인코더**와 **투영 헤드(MLP)** 를 통과 → **정규화 임베딩** 획득  
3. 한 쌍(같은 원본의 두 뷰)을 **양성(positive)**, 배치의 나머지 뷰들을 **음성(negative)** 으로 두고  
   **NT-Xent** 손실(코사인 유사도 + **온도 τ**)로 **양성은 가깝게**, **음성은 멀게** 학습  
4. 평가 시에는 **투영 헤드를 버리고 인코더 표상** 위에 **선형 분류기**를 얹어 성능을 측정

## 🔍 왜 중요한가?
- **단순하지만 강력**: 복잡한 큐/메모리 없이 **순수 인배치 대조학습**만으로 높은 성능을 달성  
- **설계 인사이트**: **강한 증강**, **투영 헤드**, **적절한 τ** 및 **큰 배치**가 대조학습의 핵심임을 정량 확인  
- **실무 출발점**: 이후 MoCo v2/ BYOL/ SimSiam/ CLIP 등 **표현학습 계열의 기준점**이 됨

## 🛠️ 실무 팁(요약)
- **증강 강도**가 결정적: 크롭+컬러왜곡(+블러)의 조합이 핵심  
- **배치 크기**는 클수록 안정적(음성 수↑). 자원 제약 시 **메모리 최적화/분산학습** 고려  
- **투영 헤드**: 2-layer MLP(+ReLU) 사용, 학습 후 **헤드는 폐기**하고 backbone의 표현을 사용  
- **온도 τ**와 **러닝레이트/스케줄**은 성능 민감 → 반드시 튜닝

## ⚠️ 한계
- **큰 배치 의존**: 충분한 음성이 필요해 자원 요구가 큼  
- **뷰 설계 민감**: 증강 레시피에 따라 학습 난이도/일반화가 크게 달라짐  
- **밀집 예측/정밀 로컬라이제이션** 등에서는 **전용 파인튜닝**이 추가로 필요할 수 있음

---

# 🚀 Presentation
<img width="1920" height="1080" alt="001" src="https://github.com/user-attachments/assets/e207e7b6-6e43-47ca-80d3-c546b347d83a" />
<img width="1920" height="1080" alt="002" src="https://github.com/user-attachments/assets/9777b83b-8bf7-4985-beb8-90e7c8c1f630" />
<img width="1920" height="1080" alt="003" src="https://github.com/user-attachments/assets/0d69f8be-5e89-45d8-91ec-08f22de06f57" />
<img width="1920" height="1080" alt="004" src="https://github.com/user-attachments/assets/5018d514-7ab5-48e3-8108-ebcf52e2e1dd" />
<img width="1920" height="1080" alt="005" src="https://github.com/user-attachments/assets/6a091638-0a73-4d40-8095-6e3d11ccca14" />
<img width="1920" height="1080" alt="006" src="https://github.com/user-attachments/assets/b5523874-e396-4dde-b500-4c4eb87651e4" />
<img width="1920" height="1080" alt="007" src="https://github.com/user-attachments/assets/86187cbb-cd7d-404a-b895-a6c47d1cc25e" />
<img width="1920" height="1080" alt="008" src="https://github.com/user-attachments/assets/679568bc-08e3-41ab-bc4a-7fc0344a13dc" />
<img width="1920" height="1080" alt="009" src="https://github.com/user-attachments/assets/96434e5c-6771-4c7c-80c1-c08a6d9e3c3f" />
<img width="1920" height="1080" alt="010" src="https://github.com/user-attachments/assets/604aea49-a10d-4a66-b119-9479c7237938" />
<img width="1920" height="1080" alt="011" src="https://github.com/user-attachments/assets/379bffa3-78c6-42d8-a6c0-f2c2792594dd" />
<img width="1920" height="1080" alt="012" src="https://github.com/user-attachments/assets/087986f9-0367-49fb-94a2-7dd10809de64" />
<img width="1920" height="1080" alt="013" src="https://github.com/user-attachments/assets/58bb15a7-a2dd-4e25-95f7-aac1375badb3" />
<img width="1920" height="1080" alt="014" src="https://github.com/user-attachments/assets/4d6b6a0e-696d-41de-9bcb-dead20300ced" />
<img width="1920" height="1080" alt="015" src="https://github.com/user-attachments/assets/38a27164-29f6-48f4-a0df-685704b7bd68" />
<img width="1920" height="1080" alt="016" src="https://github.com/user-attachments/assets/5f2b84f2-1cd3-4b22-8794-37b4a013772c" />
<img width="1920" height="1080" alt="017" src="https://github.com/user-attachments/assets/94d3bb58-9305-40b1-8260-e3edb09560c3" />
<img width="1920" height="1080" alt="018" src="https://github.com/user-attachments/assets/c5de13b9-0815-4f11-a296-6b6f64a567fa" />
<img width="1920" height="1080" alt="019" src="https://github.com/user-attachments/assets/05583895-f1d8-486c-9fa0-0b732c1aa89c" />
<img width="1920" height="1080" alt="020" src="https://github.com/user-attachments/assets/68109d74-f128-4bc3-b767-151fde570c78" />
<img width="1920" height="1080" alt="021" src="https://github.com/user-attachments/assets/31c24e4c-7aa9-4c77-ac7b-0a13cd258272" />
<img width="1920" height="1080" alt="022" src="https://github.com/user-attachments/assets/e07bffdb-a141-4b4e-a184-318868c5650d" />

