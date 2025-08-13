# 👋 Introduction

본 발표는 **AN IMAGE IS WORTH 16×16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE (Dosovitskiy et al., 2020)**, 일명 **Vision Transformer (ViT)** 를 다룹니다.  
ViT는 **Transformer를 순수 인코더(Encoder-only)** 형태로 비전 분류에 적용하여, **이미지를 패치 토큰으로 변환**해 처리합니다. 충분히 큰 데이터로 사전학습한 뒤 파인튜닝하면 **당시 SOTA CNN을 경쟁하거나 상회**하는 성능을 보고했습니다. 또한 이해를 돕기 위해 **원조 Transformer**(자기어텐션 기반, 포지션 인코딩, 잔차+LN 등)과의 **구성 비교**를 함께 첨부합니다.

## ✨ TL;DR
- **패치화**: 이미지를 **16×16**(또는 32×32 등) 크기의 패치로 나눠 **시퀀스 토큰**으로 간주  
- **Transformer 인코더**: 멀티헤드 자기어텐션 + MLP 블록(잔차·LayerNorm 포함)으로 전역 문맥을 학습  
- **클래스 토큰**: `[CLS]`에 해당하는 학습 가능한 토큰을 앞에 붙여 최종 분류에 사용  
- **스케일의 힘**: 대규모 사전학습(예: ImageNet-21k/JFT 등) → **ImageNet 등에서 파인튜닝 시 강력한 성능**

## 🧩 ViT가 동작하는 방식 (요지)
1. **Patchify**: $H\times W$ 이미지를 $P\times P$ 패치로 나눠 $N=\frac{HW}{P^2}$ 개 토큰을 생성  
2. **Linear Projection**: 각 패치를 **선형 임베딩**(채널 전개 후 프로젝션)하여 동일 차원의 토큰 시퀀스로 변환  
3. **Positional Embeddings**: 순서 정보를 위한 **학습형 포지션 임베딩**을 더함  
4. **[CLS] Token + Encoder**: `[CLS]`를 앞에 붙이고 **Transformer Encoder L층** 통과  
5. **Head**: `[CLS]`의 최종 표현을 **MLP Head**로 분류

## 🔍 CNN vs. ViT (핵심 비교)
- **수용 영역**: CNN은 지역(로컬)에서 전역으로 확장, **ViT는 초기부터 전역 어텐션**으로 장거리 상호작용 용이  
- **귀납적 편향**: CNN의 강한 편향(평행이동 불변성 등)이 적어 **ViT는 큰 데이터가 필요**하지만, **스케일에서 이점**  
- **복잡도**: 토큰 수 \(N\)에 대해 **어텐션 비용 \(O(N^2)\)** — **패치 크기**가 \(N\)을 좌우(작은 패치=세밀·비용↑)  
- **하이브리드 스템**: 초기 단계에 **CNN 스템(예: Conv stem)** 을 두어 로컬 패턴을 보완하는 변형도 존재

## 🛠️ 실무 메모
- **패치 크기**: `P=16`이 표준(ViT-B/16, L/16 등). 더 작은 패치는 세밀하지만 비용이 커짐  
- **정규화/증강**: 중·소규모 데이터에서는 **강한 증강/정규화**(Mixup/CutMix/DropPath 등)와 **장시간 학습**이 필요  
- **전이 전략**: **대규모 사전학습 → 다운스트림 파인튜닝**이 기본 레시피

## ⚠️ 유의점
- **데이터 의존성**: 충분한 사전학습 데이터가 없으면 **CNN 대비 열위**일 수 있음  
- **토큰 수 민감**: 입력 해상도·패치 크기에 따라 메모리/연산량이 크게 변동

---

# 🚀 Presentation


![Image](https://github.com/user-attachments/assets/60185547-bac1-4506-a3c8-9cfd4844d41b)

![Image](https://github.com/user-attachments/assets/f9b14bec-55e6-4529-9290-4677eed94eca)

![Image](https://github.com/user-attachments/assets/3a660241-f291-4d40-8dea-5a627b41bc7e)

![Image](https://github.com/user-attachments/assets/9921822b-bff1-47b6-9ad8-c8a9634c3d22)

![Image](https://github.com/user-attachments/assets/2c9b0d0e-c232-4b87-86a9-e60332abc448)

![Image](https://github.com/user-attachments/assets/683e6012-e203-46b6-ad86-84ab1be4fc36)

![Image](https://github.com/user-attachments/assets/f7554375-860c-42fd-b140-9740206099d0)

![Image](https://github.com/user-attachments/assets/53932aca-c519-40cb-9baf-49ed957ca5e7)

![Image](https://github.com/user-attachments/assets/6f625a50-ec18-4fde-83c4-8ee8b858a1eb)

![2025-06-26 18;33;22](https://github.com/user-attachments/assets/bc625493-d03f-46d5-8b83-671b386b4460)

![Image](https://github.com/user-attachments/assets/fa4b272d-fdf2-4f11-9c6e-630abcb33f29)

![Image](https://github.com/user-attachments/assets/160f091e-2d19-4942-a21a-da0ecf10fe86)

![Image](https://github.com/user-attachments/assets/e90ed581-d216-420b-9f1f-e9ace7e8febb)

![Image](https://github.com/user-attachments/assets/43a48828-1854-4a98-8a97-9e3adcbc1266)

![Image](https://github.com/user-attachments/assets/d19e09de-fc53-42e4-87ba-11fefe285a54)

![Image](https://github.com/user-attachments/assets/86c5392f-b009-4ff2-bb27-b0d3b7d9d054)

![Image](https://github.com/user-attachments/assets/e502035c-f53a-432c-81ce-52f2b044c69d)

![Image](https://github.com/user-attachments/assets/2900ae5c-20db-415f-8db5-ce997590b434)

![Image](https://github.com/user-attachments/assets/b7b0c92a-d439-4b75-b9d5-2d91c92792d5)

![Image](https://github.com/user-attachments/assets/851214c5-63d5-4eea-873f-20ae48e7ebba)

![Image](https://github.com/user-attachments/assets/0a45c860-f765-426b-a1b8-e70ca18cd0c4)

![Image](https://github.com/user-attachments/assets/43f5bc0f-f421-4791-9ba4-2abef1b3660c)
