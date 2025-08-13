# 👋 Introduction

본 발표는 **Unsupervised Representation Learning by Predicting Image Rotations (Gidaris, Singh, Komodakis, 2018)**, 일명 **RotNet**을 다룹니다.

**핵심 아이디어**는 매우 단순합니다: 입력 이미지를 **{0°, 90°, 180°, 270°}** 로 회전시키고, 네트워크가 **회전 각도를 분류**하도록 학습합니다. 이때 라벨은 사람이 아니라 **증강으로부터 자동 생성**되므로, **Self-Supervised Learning(SSL)** 으로 대규모 비라벨 데이터에 쉽게 적용할 수 있습니다.

## ✨ TL;DR
- **Pretext Task**: 4-클래스 **회전 예측**(cross-entropy)으로 표현 학습  
- **동기**: 회전을 올바르게 맞추려면 **객체의 위치·형태·자세(semantic cues)** 를 이해해야 함 → **의미 기반 표현**으로 연결  
- **전이(Transfer)**: 학습된 백본을 고정(Linear Eval)하거나 파인튜닝하여 **분류·탐지 등 다운스트림**에 활용  
- **효과**: 기존 비지도/자기지도 기법과 **경쟁적 성능**을 보이며, **Supervised 대비 격차를 축소**

## 🧩 어떻게 동작하나 (요지)
1. 원본 이미지 \(x\)에 회전 변환 \(g \in \{0°,90°,180°,270°\}\) 적용 → \(\tilde{x}=g(x)\)  
2. 백본 CNN을 통과시켜 특징 \(\mathbf{h}\) 추출  
3. 4-way 분류 헤드로 **회전 각도** 예측(softmax)  
4. **손실**: 표준 cross-entropy (라벨은 변환에서 자동 생성)

> **포인트**: 네트워크가 단순한 저수준 패턴이 아닌, **‘올바른 방향’** 을 판별하기 위해 **객체 중심의 의미 정보**를 포착하도록 유도합니다.

## 🔍 무엇을 배우나 (학습되는 성질)
- **객체 중심 표현**: 위치·윤곽·포즈 등 **고수준 단서**에 민감  
- **간결한 학습 신호**: 보조 헤드 1개, 표준 CE 손실 → **안정적·가벼운** 학습  
- **라벨 효율성**: 대규모 비라벨 데이터에서 **자동 라벨**로 손쉬운 확장

## 🛠️ 구현 체크리스트
- **백본**: ResNet-18/50 등 임의의 CNN 사용 가능(헤드는 4-way fc)  
- **증강 순서**: **자르기/정규화 → 회전** 순으로 적용해 가장자리 artifact 영향 최소화  
- **배치 구성**: 4각도 샘플을 균형 있게 포함하면 학습 안정  
- **전이 평가**:  
  - **Linear eval**: 백본 freeze, 선형 분류기만 학습  
  - **Fine-tune**: 다운스트림 데이터로 전층 미세조정

## ⚠️ 한계와 주의
- **회전 불변 도메인**(텍스처·위성/의학 영상 등)에서는 신호가 약해질 수 있음  
- **회전 대칭 물체**(원형·패턴 등)는 모호성 증가 → 보조 증강/데이터 구성이 필요  
- 회전 민감한 표현이 항상 유리한 것은 아님(태스크에 따라 **회전 불변성**이 더 적합할 수 있음)

> 실무에서는 RotNet을 **간단한 사전학습 베이스라인**으로 쓰고, 필요하면 **대조학습(예: SimCLR/MoCo)** 등과 병행·비교하는 것을 권장합니다.

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드1" src="https://github.com/user-attachments/assets/c1a81049-9963-4edc-8e50-47272eec5d0e" />
<img width="1920" height="1080" alt="슬라이드2" src="https://github.com/user-attachments/assets/d2f6dafe-4ae7-4e2d-a460-3e0aae0b90bb" />
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/deef2e42-c9ae-4b09-9f99-90e2e08f7960" />
<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/927eff1c-0e57-4a2f-b3b1-5d3447e28aad" />
<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/d83d978b-caec-460f-beda-08f1974c21b5" />
<img width="1920" height="1080" alt="슬라이드6" src="https://github.com/user-attachments/assets/43e099fb-9e46-45c0-b5b1-f4d87c7cfb65" />
<img width="1920" height="1080" alt="슬라이드7" src="https://github.com/user-attachments/assets/2af22f8e-ffb6-4a55-8f6e-9064f0a5418b" />
<img width="1920" height="1080" alt="슬라이드8" src="https://github.com/user-attachments/assets/834aa761-47fa-47e2-9d5c-ca438bf64949" />
<img width="1920" height="1080" alt="슬라이드9" src="https://github.com/user-attachments/assets/00353e7f-61b4-4296-bb4d-4162dde525b3" />
<img width="1920" height="1080" alt="슬라이드10" src="https://github.com/user-attachments/assets/81ef4f13-dcc6-436b-a28e-57b871d8982b" />
<img width="1920" height="1080" alt="슬라이드11" src="https://github.com/user-attachments/assets/47169282-77cc-41c4-8725-3636dee0a405" />
<img width="1920" height="1080" alt="슬라이드12" src="https://github.com/user-attachments/assets/4e102ae3-f9da-43d3-a357-10519ccb3967" />
<img width="1920" height="1080" alt="슬라이드13" src="https://github.com/user-attachments/assets/88759e11-532a-4547-8343-91f7301cddab" />
<img width="1920" height="1080" alt="슬라이드14" src="https://github.com/user-attachments/assets/1e96c269-05df-4780-8860-a5cb1f3c2288" />
<img width="1920" height="1080" alt="슬라이드15" src="https://github.com/user-attachments/assets/04ae9a71-074d-4eb3-91ab-7317de0af340" />
<img width="1920" height="1080" alt="슬라이드16" src="https://github.com/user-attachments/assets/abb378ea-279b-47e3-b587-fb5e91d51ab1" />
<img width="1920" height="1080" alt="슬라이드17" src="https://github.com/user-attachments/assets/4c3b9f05-fae3-4ff7-a858-854540868d6a" />
<img width="1920" height="1080" alt="슬라이드18" src="https://github.com/user-attachments/assets/cca19cdc-0004-4354-a469-8c43f939025f" />
<img width="1920" height="1080" alt="슬라이드19" src="https://github.com/user-attachments/assets/05c1d125-5a91-441e-bc2c-229f2fce3bff" />
<img width="1920" height="1080" alt="슬라이드20" src="https://github.com/user-attachments/assets/30e919f9-83e9-4e3c-bf66-af5fc2d01349" />









