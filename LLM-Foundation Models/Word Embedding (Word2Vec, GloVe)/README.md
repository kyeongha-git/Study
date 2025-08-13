# 👋 Introduction

본 자료는 LLM의 전반적 워크플로우를 이해하기 위해 핵심 기반인 **Word Embedding**을 정리한 노트입니다.  
특히 **Word2Vec**과 **GloVe**의 개념·목표함수·학습 트릭·장단점을 **원 논문 맥락에 충실**하게 설명합니다.

## ✨ TL;DR
- **Distributional Hypothesis**: “같은 문맥에 등장하는 단어는 비슷한 의미를 갖는다.”
- **Word2Vec (예측 기반, local)**: 문맥에서 단어(또는 그 반대)를 **예측**하도록 학습 → **CBOW / Skip-gram**  
  - 효율적 학습: **Negative Sampling**, **Hierarchical Softmax**, **빈도 서브샘플링**
- **GloVe (카운트 기반, global)**: 전체 코퍼스 **공동출현(co-occurrence) 통계**를 맞추도록 회귀 → **전역적 구조 반영**
- 공통효과: 단어를 **밀집 벡터**로 표현하여 유의미한 **유사도/벡터 연산**(king − man + woman ≈ queen 등)을 가능하게 함

---

## 🧠 Word2Vec 한눈에 보기
- **목표**: 문맥 \(c\)가 주어졌을 때 중심 단어 \(w\) (CBOW) 또는 중심 단어가 주어졌을 때 문맥 단어(Skip-gram)를 **예측**  
- **Skip-gram + Negative Sampling(권장)** 의 전형적 목적함수(개략):
  $$
  \max\ \sum_{(w,c)\in D}\Big[\log \sigma(\mathbf{v}_w^\top \tilde{\mathbf{v}}_c)
  + \sum_{n\sim P_n}\log \sigma(-\mathbf{v}_w^\top \tilde{\mathbf{v}}_n)\Big]
  $$
  - \(\sigma\): 시그모이드, \(\mathbf{v},\tilde{\mathbf{v}}\): 입력/출력 임베딩, \(P_n\): 노이즈 분포(통상 \(U(w)^{0.75}\))
- **학습 트릭**
  - **서브샘플링**(빈도 높은 단어 버리기): \(P_{\text{discard}}(w)=1-\sqrt{t/f(w)}\), \(t\approx 10^{-5}\)
  - **윈도우 크기**: 5±2 등 랜덤 윈도우로 일반화 향상
- **장점**: 대규모 코퍼스에서 **빠르고 가볍게** 학습, 낮은 메모리  
- **한계**: **정적(static) 임베딩** → 다의어(polysemy) 표현 어려움, 전역 통계 반영 부족

---

## 📊 GloVe 한눈에 보기
- **아이디어**: 단어 \(i\)와 \(j\)의 **공동출현 횟수 \(X_{ij}\)** (윈도우 내 등장)를 이용해 **로그 카운트**를 근사하도록 학습
- **목적함수(가중 최소제곱 회귀)**:
  $$
  J=\sum_{i,j} f(X_{ij})\Big(\mathbf{w}_i^\top \tilde{\mathbf{w}}_j + b_i + \tilde b_j - \log X_{ij}\Big)^2
  $$
  - 가중함수 \(f(x)=\begin{cases}
  (x/x_{\max})^\alpha & x<x_{\max}\\
  1 & \text{otherwise}
  \end{cases}\), 보통 \(\alpha\approx 0.75,\ x_{\max}\approx 100\)
- **장점**: 전역 통계로 **안정적 의미 구조** 반영, 유사성/아날로지 성능 우수  
- **한계**: 대규모 **행렬 구성/메모리** 비용, 희소성 처리 필요

---

## 🔁 Word2Vec vs. GloVe (요약 비교)
- **학습 관점**: *예측(local)* vs. *카운트(global) 회귀*  
- **자원**: Word2Vec이 **훈련 빠름/메모리 절약**, GloVe는 **전역 구조** 반영 강점  
- **데이터 규모**: 코퍼스가 클수록 둘 다 향상. 전역 통계가 충분할 때 **GloVe 강세** 경향  
- **튜닝 포인트**: 차원(100–300 전통적), 윈도우/서브샘플링(Word2Vec), \(x_{\max},\alpha\)(GloVe)

---

## 🛠️ 실무 팁 & 현대적 맥락
- **OOV/형태소**: 희귀어 처리를 위해 **subword(fastText)** 고려  
- **바이어스**: 임베딩에는 **사회적 편향**이 내재될 수 있음 → 평가·완화 절차 필요  
- **현대 LLM**: BPE/SentencePiece 등 **서브워드 토큰** 임베딩을 **모델과 함께 end-to-end**로 학습(정적 임베딩 대체)  
- **전이 사용**: 고정(Freeze)+선형 분류기, 또는 다운스트림에서 **파인튜닝**

---

# 🚀 Presentation
![001](https://github.com/user-attachments/assets/82e7aa16-314e-42d7-ba6a-8c4c6990efcf)

![002](https://github.com/user-attachments/assets/e13f4bc5-4c0d-4ce3-af4c-4bd4c9b5ebe2)

![003](https://github.com/user-attachments/assets/58ce2632-8e9b-4320-90e3-770d7d7689e2)

![004](https://github.com/user-attachments/assets/1142b32d-fe34-470f-8ddd-14b739372412)

![005](https://github.com/user-attachments/assets/9ca4ffd0-2c5f-41a7-b27a-cde11a6061f6)

![006](https://github.com/user-attachments/assets/22826bc1-496c-465b-8557-ccef9b629c8b)

![007](https://github.com/user-attachments/assets/7421f81d-6078-4afd-b73b-4dd3abbdcf44)

![008](https://github.com/user-attachments/assets/6f3ec33f-f549-4ff3-a74f-29988ad0e6fb)

![009](https://github.com/user-attachments/assets/ebdbddee-a05c-4594-b930-f7cbbc5b5d00)

![010](https://github.com/user-attachments/assets/f18a05a7-2ad2-4a3e-b2e9-e0e2c9b81206)

![011](https://github.com/user-attachments/assets/ae651584-ebe0-4d02-b77a-7334cfe5eaf0)

![012](https://github.com/user-attachments/assets/cf6e90e2-6863-4e44-91b3-af8d49cf6c6a)

![013](https://github.com/user-attachments/assets/6bf41c04-5eee-481b-b785-f2c4d2d38b99)

![014](https://github.com/user-attachments/assets/b2759444-365d-429b-ba61-ecf9748cdff9)

![015](https://github.com/user-attachments/assets/0db25ef9-4f7f-4371-8807-229f1569d314)

![016](https://github.com/user-attachments/assets/c5404b14-9e42-4f2b-8cc6-98865009b4eb)

![017](https://github.com/user-attachments/assets/ffee2b5e-d95f-4fcf-8dd9-c0a6fb537b18)

![018](https://github.com/user-attachments/assets/83559832-a82b-4893-9387-1f122f121170)

![019](https://github.com/user-attachments/assets/3c6eec35-1002-4be6-acb7-9d72146d02b9)

![020](https://github.com/user-attachments/assets/a4ee409d-7efc-41bd-8b07-c5035f414a7b)

![021](https://github.com/user-attachments/assets/293e6686-d8ea-4142-8d5e-4f5321bc5b7f)

![022](https://github.com/user-attachments/assets/7b39fe6a-ee48-4687-b91a-d03efda0bee6)

