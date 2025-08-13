# 👋 Introduction

본 발표는 **Attention Is All You Need (Vaswani et al., 2017)**, 최초의 **Transformer** 논문을 다룹니다.  
Transformer는 **자기어텐션(Self-Attention)** 기반의 **Encoder–Decoder** 구조로, **순환/합성곱 없이** 병렬 학습을 가능하게 하여 기계번역을 비롯한 시퀀스 과제에서 **표준 아키텍처**가 되었습니다.

## ✨ TL;DR
- **핵심 아이디어**: RNN/CNN 없이 **(스케일드) 닷프로덕트 어텐션**을 다중 헤드로 병렬화 → 장·단기 의존성 동시 포착  
- **구성**: 멀티헤드 어텐션 + 포지션 인코딩 + 위치별 FFN + **잔차/LayerNorm**  
- **효과**: 높은 **병렬성**과 **효율**로 학습 가속, 번역 등에서 SOTA 수준 성능

## 🧩 왜 중요한가?
- **Parallelism**: 어텐션은 모든 토큰 쌍을 **동시에** 처리 → 긴 문맥 처리와 학습 속도 이점  
- **모듈성**: Encoder/Decoder 스택과 어텐션 블록이 **타 도메인으로 손쉽게 이전** 가능 (NLP → 비전)

## 🔍 Vision Transformer(ViT)와 한 페이지 비교
- **입력 단위**: Transformer(원조)는 **토큰(단어/서브워드)**, **ViT**는 이미지를 **패치 토큰**으로 변환  
- **구조**: ViT는 **Encoder 전용**(클래스 토큰 + MLP 헤드)로 분류 수행, 디코더 없음(기본형)  
- **포지션 정보**: Transformer는 주로 **1D 포지션 인코딩**(사인/코사인 또는 학습형), ViT는 **패치 순서용** 포지션 임베딩  
- **데이터 스케일**: ViT는 대규모 사전학습(예: 수억 장 수준)에서 강점이 두드러지고, 소규모에서는 **규제·증강**이 중요

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
