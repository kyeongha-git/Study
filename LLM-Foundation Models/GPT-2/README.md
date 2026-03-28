# Introduction

본 발표는 **Language Models are Unsupervised Multitask Learners (Radford et al., 2019)**, 일명 **GPT-2 리포트**를 다룹니다.  
GPT-2는 **Transformer 디코더 전용(Decoder-only)** 구조에 **자기회귀(next-token prediction)** 목적함수를 사용해 **대규모 웹 코퍼스(WebText)** 로 사전학습된 **범용 언어 모델**입니다. 핵심 메시지는 다음과 같습니다.

## TL;DR
- **파인튜닝 없이도** 다양한 다운스트림 작업을 **제로샷(Zero-shot)** 으로 수행  
- **프롬프트(문맥)만 바꾸어** 번역·질의응답·독해·요약 등 여러 태스크에 적응  
- **스케일이 곧 성능**: 파라미터/데이터/컨텍스트 길이를 키울수록 제로샷 성능이 꾸준히 향상  
- **결과**: 당시 **여러 벤치마크에서 감독 학습 모델과 경쟁적이거나 근접한 성능**을 보고

## 왜 중요한가?
기존 **태스크별 파인튜닝** 패러다임은 특정 작업에는 강하지만 **일반화**가 제한되는 문제가 있었습니다. GPT-2는 **단일 사전학습 모델 + 프롬프트**만으로 다양한 작업을 수행할 수 있음을 보여 주며, **“프롬프트를 인터페이스로 한 제로샷 학습”** 시대를 여는 계기가 되었습니다.

## 모델과 학습 개요
- **아키텍처**: Transformer **Decoder-only** 스택(마스크드 self-attention)  
- **토크나이저**: **바이트 단위 BPE(byte-level BPE)**  
- **목표함수**: 다음 토큰 예측(언어모델링), **태스크별 헤드/라벨 불필요**  
- **데이터**: WebText (레딧 아웃바운드 링크 기반 수집, 중복·저품질 필터링)  
- **모델 크기(파라미터)**: **117M / 345M / 774M / 1.5B** (GPT-2-XL)

## 평가 방식(Zero-shot 프로토콜)
1) 태스크를 **텍스트 지시문** 형태로 기술(프롬프트 설계)  
2) 입력과 지시문을 연결한 시퀀스를 모델에 주고  
3) **우도/로그확률** 비교 또는 **생성 결과**로 정답을 선택  
→ 별도 파인튜닝 없이 **언어모델의 사전학습 지식**만으로 수행

## 관찰된 특징
- **범용성**: 번역·독해·질의응답·상식추론 등 **여러 작업에서 경쟁적 제로샷 성능**  
- **스케일 법칙**: 모델이 커질수록 **일관된 성능 향상**  
- **프롬프트 민감도**: 표현(어조/형식)에 따라 성능 변동 → **프롬프트 엔지니어링** 중요

## 한계와 주의
- **컨텍스트 길이 제약**: 당시 제한된 컨텍스트(예: 1024 토큰 내)  
- **지식 최신성/편향**: 웹 수집 데이터의 **시계열/사회적 편향**을 그대로 반영 가능  
- **완전한 우월 아님**: 태스크 전용 파인튜닝 모델이 여전히 더 강한 경우도 존재

---

# Presentation

![001](https://github.com/user-attachments/assets/f4d45f5b-893c-48df-8929-531dee85c346)

![002](https://github.com/user-attachments/assets/e43b6efc-6e8c-47b5-ae96-0699069b2864)

![003](https://github.com/user-attachments/assets/d7e796bd-6830-4e1a-b0f6-16af311de00a)

![004](https://github.com/user-attachments/assets/6666a0b4-ca55-4337-9df3-c2f63b2598a0)

![005](https://github.com/user-attachments/assets/042ae3fe-14b3-439d-93a2-2ad594ae9e2f)

![006](https://github.com/user-attachments/assets/32d6df30-6b46-4201-abbe-ea9d60cff080)

![007](https://github.com/user-attachments/assets/f4e1da1d-613c-478f-93fb-6ce34bd2fa5e)

![008](https://github.com/user-attachments/assets/8d953eaa-8b6a-43ec-b267-b6add377449d)

![009](https://github.com/user-attachments/assets/8386c579-6d18-43ba-b85e-b8b839d66ea7)

![010](https://github.com/user-attachments/assets/e96ee23f-70c5-489d-8dbc-20e0ee316800)

![011](https://github.com/user-attachments/assets/a6707bf1-9193-4d56-8aef-f03f634412ea)

![012](https://github.com/user-attachments/assets/e2ec9c4e-f0ec-44b9-b6cb-1165dd04ff97)

![013](https://github.com/user-attachments/assets/3e9aeb4f-cd7c-428d-a044-9c80f6f2fc23)

![014](https://github.com/user-attachments/assets/07d580b2-bdd5-4619-af9b-7c5bf414aa08)

![015](https://github.com/user-attachments/assets/6fc1e473-a9eb-4b7e-a100-edd20e92f9e8)

![016](https://github.com/user-attachments/assets/5eeaac15-f1d5-4da4-a468-1600eed3ee90)

![017](https://github.com/user-attachments/assets/0f5b83cf-8b60-458a-a595-56ddc85eab83)

![018](https://github.com/user-attachments/assets/06d5f7c2-7301-42b7-a3dc-c1c2a907fc5d)

![019](https://github.com/user-attachments/assets/34bb15ed-f764-487b-aa5b-913f72ee4586)

![020](https://github.com/user-attachments/assets/7d3bc810-9196-46d2-82fd-40e3b87dbe68)

![021](https://github.com/user-attachments/assets/d4d52764-03d3-49df-89c9-db8ef84be50e)

