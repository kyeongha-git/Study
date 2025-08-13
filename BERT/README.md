# 👋 Introduction

해당 발표는 **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al., 2018)** 를 다룹니다.  
BERT는 **Transformer 인코더(Encoder-only)** 구조 위에서 **사전학습(Pre-training)** → **미세조정(Fine-tuning)** 파이프라인을 정립한 **언어 표현(Language Representation) 모델**입니다. 핵심 아이디어는 **양방향(Bidirectional) 문맥**을 직접 학습할 수 있도록 설계된 **마스크드 언어모델링(MLM)** 과 **다음문장 예측(NSP)** 을 결합해, 다양한 다운스트림 태스크(질문응답, 자연어추론, 문장 분류 등)에 강력히 전이한다는 점입니다.

## ✨ 한눈에 보기 (TL;DR)
- **양방향 컨텍스트**: 왼→오/오→왼 방향 제약 없이 **양방향 self-attention**으로 토큰 표현을 학습  
- **두 가지 사전학습 목표**  
  - **MLM**: 입력 토큰의 일부(약 15%)를 가려 놓고 해당 토큰을 맞히도록 학습  
  - **NSP**: 두 문장이 실제로 이어지는지(isNext) 여부를 예측
- **간단한 전이학습**: 태스크별 작은 헤드(분류/스팬 예측 등)만 얹어 **파라미터 전체를 미세조정**하면 SOTA에 근접하거나 갱신
- **대표 구성**  
  - **BERT-Base**: L=12, H=768, A=12, **~110M** params  
  - **BERT-Large**: L=24, H=1024, A=16, **~340M** params
- **효과**: GLUE, SQuAD, SWAG 등 **다양한 벤치마크에서 우수한 성능**

## 🧠 왜 중요한가?
기존 왼→오(left-to-right) 또는 오→왼(right-to-left) LM은 **완전한 양방향 문맥**을 활용하기 어려웠습니다. BERT는 **MLM으로 이 한계를 돌파**해 풍부한 문맥 표현을 획득하고, **간단한 헤드만 추가**해 태스크 전반에 **광범위한 전이(transfer)** 를 성립시켰습니다. 이는 이후 **RoBERTa/ALBERT/DeBERTa** 등 인코더 계열의 토대를 마련했습니다.

## 🧩 사전학습 디테일(요약)
- **토크나이저**: WordPiece  
- **MLM 마스킹 규칙(대표)**: 선택된 토큰의 **80%는 `[MASK]`**, **10%는 랜덤 토큰**으로 치환, **10%는 원형 유지**(모델의 과도한 마스크 의존 방지)  
- **NSP 데이터 구성**: 문장 쌍의 **50%는 실제 다음 문장**, **50%는 임의 문장**  
- **코퍼스(영어)**: BookCorpus + Wikipedia(대규모)

> ※ 후속 연구에서는 NSP의 필요성을 재검토하거나(예: RoBERTa), 마스킹·학습 스케줄을 확장해 성능을 더 끌어올렸습니다. 본 발표는 **원 논문의 설정과 공헌**에 집중합니다.

## 🧪 다운스트림 전이 방식(패턴)
1. **프롬프트가 아닌 헤드 부착**: 문장/토큰 단위 분류, 스팬 추출 등에 맞는 **작은 출력 헤드** 추가  
2. **엔드투엔드 미세조정**: 사전학습 가중치 전체를 **태스크 데이터로 업데이트**  
3. **간단한 입력 포맷**: `[CLS]` 문장표현, `[SEP]` 문장 경계 등 **포맷 일관화**로 구현 용이

## ⚠️ 한계와 유의점
- **생성(generation)에는 비적합**: 인코더 전용 구조라 **생성형 디코딩**에는 직접 쓰기 어려움  
- **긴 시퀀스 비용**: self-attention의 **O(n²)** 특성으로 **긴 문장 처리 비용**이 큼  
- **마스킹 불일치**: 학습 시 등장하는 `[MASK]` 토큰이 **추론 시에는 나타나지 않는 불일치** 존재(설계적 타협)

---

# 🚀 Presentation

![Image](https://github.com/user-attachments/assets/8122a175-2590-4207-83b4-9fac9539cdec)

![Image](https://github.com/user-attachments/assets/f4a2d3af-63e3-4a87-a0db-7c7f28490568)

![Image](https://github.com/user-attachments/assets/8987211b-0e5c-485c-abb0-adf02875edc7)

![Image](https://github.com/user-attachments/assets/5d7de313-398c-49b1-97a7-9e1b6fca4ea5)

![Image](https://github.com/user-attachments/assets/77405a69-114d-4f0c-9c9b-dfa85fc0f92c)

![Image](https://github.com/user-attachments/assets/614c3e7c-8f1e-4d13-86c5-7b96e263f9eb)

![Image](https://github.com/user-attachments/assets/29dec76a-d2c0-4ba4-b15b-ab6b44ae3fc4)

![Image](https://github.com/user-attachments/assets/9d98dd5f-6675-465d-b599-249d0abeb840)

![Image](https://github.com/user-attachments/assets/f2c7965f-42f4-454d-b8bd-51f5c00f9be3)

![Image](https://github.com/user-attachments/assets/015bac6b-2976-47b3-9a3b-921d01afb3b9)

![Image](https://github.com/user-attachments/assets/72eeb445-c348-45d9-8406-76591ed90c32)

![Image](https://github.com/user-attachments/assets/1369f975-dbd0-4c4f-a977-5a3642dea96e)

![Image](https://github.com/user-attachments/assets/280192b0-38bb-4362-b9e2-b738a6a4c94e)

![Image](https://github.com/user-attachments/assets/10e02b45-ca33-495e-aa87-476347bb3260)

![Image](https://github.com/user-attachments/assets/2ea00269-4b33-4291-a66a-bf4f0162bacf)

![Image](https://github.com/user-attachments/assets/15602335-7808-49e7-b236-5019e77036b3)

![Image](https://github.com/user-attachments/assets/222a5754-08f4-4d8f-a6c0-38053bb47714)

![Image](https://github.com/user-attachments/assets/1e8365ce-efb4-4530-8773-16f983266e0f)

![Image](https://github.com/user-attachments/assets/ecc0aa21-5a8e-44fe-b43a-eeb6d7045c84)

![Image](https://github.com/user-attachments/assets/6562031c-72c3-4085-aac6-ccdd90804c6d)

![Image](https://github.com/user-attachments/assets/f6f13df7-46d3-4a09-ab7f-cf7bd564f9eb)

![Image](https://github.com/user-attachments/assets/f89b2765-1810-4eb0-80f7-7895bfa96f11)

![Image](https://github.com/user-attachments/assets/3cd04a72-d397-4ca1-bab4-d3c001edb491)

![Image](https://github.com/user-attachments/assets/b0afffd9-95c9-4446-a38e-920aba733d65)
