# 👋 Introduction

본 발표는 **Deep Residual Learning for Image Recognition (He et al., 2015/2016)**, 일명 **ResNet**을 다룹니다.  
ResNet은 깊이가 늘어날수록 **훈련 오차조차 커지는 Degradation 문제**를 **Residual Learning**과 **Shortcut(Identity) Connection**으로 해결하여, “더 깊을수록 더 좋다”는 방향을 **현실화**한 모델입니다.

## ✨ TL;DR
- **핵심 아이디어**: 원하는 사상 \(H(x)\)를 직접 학습하는 대신, **잔차 \(F(x)=H(x)-x\)** 를 학습하고 **\(y = F(x) + x\)** 로 출력  
- **효과**: **정보·그래디언트가 shortcut을 통해 직접 흐름** → 깊은 네트워크의 **최적화 용이성**과 **일반화** 동시 확보  
- **아키텍처**:  
  - **Basic Block**(2×3×3 conv, BN+ReLU): ResNet-18/34  
  - **Bottleneck Block**(1×1 → 3×3 → 1×1): ResNet-50/101/152  
- **성능**: ImageNet에서 **50–152층**으로 SOTA 갱신, 검출/분할 등 다운스트림에서도 강력한 백본으로 자리매김  
  - **주의**: **1202층** 실험은 **CIFAR-10**에서의 결과이며, ImageNet은 152층까지 보고됨

## 🧩 어떻게 동작하나 (요지)
1. **Residual Block**: 하위 경로는 일반 conv, 상위 경로는 **identity(또는 1×1 projection)** 로 입력을 **직결**  
2. **차원/해상도 변경 시**: stride 2 및 **projection shortcut(1×1 conv)** 로 채널/공간 정합  
3. **학습 관점**:  
   - 최적화 난이도 ↓: **항등함수**가 쉬운 해로 존재 → 깊어져도 최소한의 성능 보존  
   - 표현력 ↑: 잔차 경로가 **필요한 변화만** 학습 → 안정적 수렴

## 🔍 설계 포인트
- **BatchNorm + ReLU**: 각 conv 뒤 정규화/활성화로 깊은 네트워크 안정화  
- **Bottleneck**: 1×1으로 채널 축소/확장 → **연산량 절감**과 **표현력 유지**  
- **Shortcut 종류**:  
  - **Identity**(차원 동일)  
  - **Projection (1×1 conv)**: 차원/해상도 불일치 시 사용

## ⚠️ 실무 메모
- **학습 스케줄**과 **정규화(BN 통계)** 가 성능에 민감  
- **Pre-activation ResNet(ResNet v2)** 는 BN/활성화를 블록 앞단으로 이동해 **깊은 네트워크의 학습 안정성**을 더 높임(후속 연구)

---

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드1" src="https://github.com/user-attachments/assets/708e213a-77d3-4bd4-a98d-272a2904a4a3" />
<img width="1920" height="1080" alt="슬라이드2" src="https://github.com/user-attachments/assets/6551abba-9303-43ea-b909-84d8ab84e3dd" />
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/54c386ff-ad9d-4eca-9d75-43ee67534f61" />
<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/790da960-c239-48ba-bffe-97edd48b1cb2" />
<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/4e5d9a74-d49e-4eed-b038-52ccce01a5e9" />
<img width="1920" height="1080" alt="슬라이드6" src="https://github.com/user-attachments/assets/14fca8b5-a525-4cac-8e84-76c245401090" />
<img width="1920" height="1080" alt="슬라이드7" src="https://github.com/user-attachments/assets/52e25d8f-ff49-4a73-9193-a1a1ef774412" />
<img width="1920" height="1080" alt="슬라이드8" src="https://github.com/user-attachments/assets/27e610c2-52a3-4ed0-8116-be37f112722c" />
<img width="1920" height="1080" alt="슬라이드9" src="https://github.com/user-attachments/assets/5b3b7d3a-b04a-4e38-ad5b-f9e58085a96a" />
<img width="1920" height="1080" alt="슬라이드10" src="https://github.com/user-attachments/assets/5301746a-6e35-4603-8caa-bdb5a1e61bf8" />
<img width="1920" height="1080" alt="슬라이드11" src="https://github.com/user-attachments/assets/bb3a6382-d89b-4cfe-aa9e-b8a03c99b63c" />
<img width="1920" height="1080" alt="슬라이드12" src="https://github.com/user-attachments/assets/891516ee-da6a-41fa-a91f-4058428b0493" />
<img width="1920" height="1080" alt="슬라이드13" src="https://github.com/user-attachments/assets/a288ec23-2a2e-4b65-a34f-842197fcf37e" />
<img width="1920" height="1080" alt="슬라이드14" src="https://github.com/user-attachments/assets/1c5c42f5-09db-411d-8021-8b4297259155" />
<img width="1920" height="1080" alt="슬라이드15" src="https://github.com/user-attachments/assets/9a0b286d-94ae-4392-be04-e318633bcc98" />
<img width="1920" height="1080" alt="슬라이드16" src="https://github.com/user-attachments/assets/5d89c375-c25e-45f5-86fe-9301c63c371a" />
<img width="1920" height="1080" alt="슬라이드17" src="https://github.com/user-attachments/assets/b12412e9-d7fb-49be-9937-7f78e782357f" />
<img width="1920" height="1080" alt="슬라이드18" src="https://github.com/user-attachments/assets/a2e6586e-d0cc-4687-a8c4-672c5c9c48ba" />
<img width="1920" height="1080" alt="슬라이드19" src="https://github.com/user-attachments/assets/08a740d1-9bdf-4bf3-a4ae-b8126de2af32" />
<img width="1920" height="1080" alt="슬라이드20" src="https://github.com/user-attachments/assets/021764ff-8885-45d6-9067-ce58ca8142f3" />
<img width="1920" height="1080" alt="슬라이드21" src="https://github.com/user-attachments/assets/7ed3dd31-e8fe-4947-8c79-bbd0153c8b4e" />
<img width="1920" height="1080" alt="슬라이드22" src="https://github.com/user-attachments/assets/50615cac-289a-4f54-8a37-760a45d1e564" />
<img width="1920" height="1080" alt="슬라이드23" src="https://github.com/user-attachments/assets/3189ca12-b742-468a-a00f-2774c144215b" />
<img width="1920" height="1080" alt="슬라이드24" src="https://github.com/user-attachments/assets/30aacc53-2ef9-4a30-9db2-9b1540a069f1" />
<img width="1920" height="1080" alt="슬라이드25" src="https://github.com/user-attachments/assets/592551c8-6839-4dd3-aae9-cde8165521ee" />

























