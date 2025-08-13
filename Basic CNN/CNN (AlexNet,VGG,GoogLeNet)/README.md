# 👋 Introduction

본 리포지토리는 **CNN의 기초를 ‘세 개의 대표 모델’(AlexNet · VGG · GoogLeNet)로 압축**해 학습하는 스터디 자료입니다.  
각 모델의 **아키텍처 구성, 핵심 아이디어, 설계 선택의 트레이드오프**를 논문을 바탕으로 정리하여, 이미지 분류용 CNN의 **설계 철학과 진화 과정**을 한눈에 연결해 이해하는 것을 목표로 합니다.

## ✨ TL;DR
- **목표**: 논문을 기반으로 아키텍처를 읽고 → 재구성하고 → 비교하여 **CNN의 기본기를 탄탄히** 다지기
- **범위**: 이미지 분류 중심의 **구조(레이어 스택), 하이퍼파라미터(커널/스트라이드/패딩), 정규화·정규화기법, 연산량·파라미터 규모** 등
- **원칙**: 원 논문의 표현과 실험 맥락을 **최대한 충실히 반영**하되, 이해에 필요한 **보충 설명**을 덧붙임

## 📚 Coverage (핵심 포인트만)
- **AlexNet (2012)**: ReLU 도입, **GPU 병렬 학습**, 데이터 증강, Dropout, LRN 등으로 깊은 모델 학습을 현실화  
- **VGG (2014)**: **3×3 컨볼루션의 반복 스택**으로 깊이를 확장하고 단순·규칙적인 구조로 표현력을 강화(리셉티브 필드 누적의 효과)  
- **GoogLeNet / Inception (2014)**: **멀티-스케일 분기(Inception 모듈)** + **1×1 병목**으로 연산 효율·표현력 동시 추구, 보조 분류기(auxiliary classifier) 활용

## 🧠 What you’ll learn
- 3×3 스택 vs. 큰 커널(5×5, 7×7)의 **Receptive Filed 등가성**과 **표현·연산 트레이드오프**
- **1×1 컨볼루션**의 역할(채널 혼합·차원 축소·비선형성 삽입)과 연산량 절감 효과
- **Pooling 선택**(Max vs. Avg), **Padding/Stride 설계**, **정규화·규제 기법**(Dropout 등)이 성능과 안정성에 미치는 영향
- **파라미터 수·FLOPs·메모리** 관점에서의 구조적 선택과 실제 구현 시 고려사항

> ※ 본 자료는 **논문 서술을 우선**으로 하며, 슬라이드에는 이해를 돕는 **도식·주석**을 덧붙였습니다.

---

# 🚀 Presentation
<img width="1920" height="1080" alt="001" src="https://github.com/user-attachments/assets/a178b52b-c431-4a2e-8229-ab8430544884" />
<img width="1920" height="1080" alt="002" src="https://github.com/user-attachments/assets/568553fc-6a91-412f-aeb9-1a8a9a4fb289" />
<img width="1920" height="1080" alt="003" src="https://github.com/user-attachments/assets/3b3c9288-0516-4a17-b1fc-408657b65b30" />
<img width="1920" height="1080" alt="004" src="https://github.com/user-attachments/assets/da1db3e4-e4f2-453f-81a9-4c7734260020" />
<img width="1920" height="1080" alt="005" src="https://github.com/user-attachments/assets/31631a13-e20e-47c7-89e1-b743d9462bd7" />
<img width="1920" height="1080" alt="006" src="https://github.com/user-attachments/assets/10821992-da19-47dc-81e5-f1a8a6139600" />
<img width="1920" height="1080" alt="007" src="https://github.com/user-attachments/assets/29a5a626-784b-4a40-8600-63edceeb57ea" />
<img width="1920" height="1080" alt="008" src="https://github.com/user-attachments/assets/a763f351-e5a5-4bb3-849f-d7834d14679d" />
<img width="1920" height="1080" alt="009" src="https://github.com/user-attachments/assets/18939656-5c0d-413e-b279-277b3549f4e0" />
<img width="1920" height="1080" alt="010" src="https://github.com/user-attachments/assets/68f0f03e-2bd7-4429-9bdd-18e082b9155d" />
<img width="1920" height="1080" alt="011" src="https://github.com/user-attachments/assets/20c0f722-b770-4e70-a96c-55b8c623ba27" />
<img width="1920" height="1080" alt="012" src="https://github.com/user-attachments/assets/62278719-0a69-487b-b8d0-f461c953b3ab" />
<img width="1920" height="1080" alt="013" src="https://github.com/user-attachments/assets/8658baae-687a-4390-881b-3c2d289d1851" />
<img width="1920" height="1080" alt="014" src="https://github.com/user-attachments/assets/a88deba3-7e62-450f-aad9-f7cd0c241cf6" />
<img width="1920" height="1080" alt="015" src="https://github.com/user-attachments/assets/531d03b8-7d32-4e53-a775-4250dc010640" />
<img width="1920" height="1080" alt="016" src="https://github.com/user-attachments/assets/e0b23a3f-a83e-4dd9-9f9c-89772dd6df4e" />
<img width="1920" height="1080" alt="017" src="https://github.com/user-attachments/assets/fa31dc5d-abe5-4e0f-b535-879b3ed2efca" />
<img width="1920" height="1080" alt="018" src="https://github.com/user-attachments/assets/73b556fc-3134-4ba6-b334-1d47e667e2e0" />
<img width="1920" height="1080" alt="019" src="https://github.com/user-attachments/assets/2cebaafb-77eb-43ba-9c48-1ac2a8db8261" />
<img width="1920" height="1080" alt="020" src="https://github.com/user-attachments/assets/9222d96c-0d6b-4326-acc6-b631afd9bc1f" />
<img width="1920" height="1080" alt="021" src="https://github.com/user-attachments/assets/48af304d-1dd1-4ae3-b878-b0bc565892f6" />
<img width="1920" height="1080" alt="022" src="https://github.com/user-attachments/assets/f0f6637d-0793-42da-afc3-3ba3b506f8ae" />
<img width="1920" height="1080" alt="023" src="https://github.com/user-attachments/assets/9e7abc01-17ca-49a7-a2eb-5df2e5df153b" />
<img width="1920" height="1080" alt="024" src="https://github.com/user-attachments/assets/ae575cda-9295-4905-a70c-5eae690579f4" />
<img width="1920" height="1080" alt="025" src="https://github.com/user-attachments/assets/5e7c6f8f-1af1-4680-8418-132b1dc79ff0" />
<img width="1920" height="1080" alt="026" src="https://github.com/user-attachments/assets/db8f353d-3c85-4c8a-8aa3-b9dfdf367ae0" />
<img width="1920" height="1080" alt="034" src="https://github.com/user-attachments/assets/424be04f-0a14-408c-a073-fac63cef366e" />
<img width="1920" height="1080" alt="035" src="https://github.com/user-attachments/assets/9d69a2a5-8d43-4abf-9741-e243042e82c2" />















