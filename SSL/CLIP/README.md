# 👋 Introduction

본 발표는 **OpenAI의 CLIP (Learning Transferable Visual Models From Natural Language Supervision, 2021)** 를 다룹니다.

CLIP은 **자연어를 감독 신호**로 활용하여 이미지–텍스트 **공동 임베딩 공간**을 학습하고, **텍스트 프롬프트만으로 제로샷(Zero-shot)** 분류·검색 등 다양한 비전 과제를 수행합니다. 즉, “라벨을 많이 붙이지 않고도” **프롬프트 엔지니어링**만으로 새로운 태스크에 **즉시 전이**가 가능합니다. ✨

기존의 **Self-Supervised Pre-Training → (태스크별) Fine-Tuning** 패러다임은 전이력이 좋지만, 실제 태스크에 맞추려면 **추가 라벨**이 적지 않게 필요했고 **도메인 일반화**가 제한되는 경우가 많았습니다.  
CLIP은 **웹에서 수집한 대규모 이미지–텍스트 쌍(약 4억 쌍)** 을 이용해 **언어 기반 감독**으로 표현을 학습하고, 텍스트 프롬프트만 바꿔 **라벨 없이도 광범위한 전이**가 가능하도록 설계되었습니다.

> 결과적으로 CLIP은 여러 벤치마크에서 **제로샷 기준**으로 기존 supervised/unsupervised(SSL 포함) 모델과 **경쟁하거나 능가**하는 강한 **도메인 일반화** 성능을 보입니다.  
> 단, **태스크 전용 파인튜닝이 허용**될 때 항상 우월하다고 일반화할 수는 없고, CLIP의 본질적 강점은 **라벨 없이도 폭넓게 전이**된다는 점입니다. ✅

---

## ✨ TL;DR
- **2-타워(dual-encoder)** 구조: 이미지 인코더(ResNet/ViT) + 텍스트 인코더(Transformer)  
- **대규모 웹 데이터**: 인터넷에서 수집한 (이미지, 캡션) 쌍으로 **대칭적 대조학습(contrastive)**  
- **제로샷 분류**: 카테고리 이름을 문장 프롬프트로 만들고, 이미지–텍스트 **코사인 유사도**로 선택  
- **강한 일반화**: 라벨 없이도 다양한 데이터셋으로 전이 (분류/검색/로버스트니스 등)

---

## 🧩 How CLIP Works (한 장 요약)
1. **인코더 쌍**  
   - **Image Encoder**: ResNet/ViT로 이미지를 임베딩 \( \mathbf{v} \in \mathbb{R}^d \)  
   - **Text Encoder**: Transformer로 텍스트를 임베딩 \( \mathbf{t} \in \mathbb{R}^d \)
2. **정규화 & 유사도**  
   - 임베딩을 정규화 후 **코사인 유사도** \( s_{ij} = \frac{\mathbf{v}_i \cdot \mathbf{t}_j}{\|\mathbf{v}_i\|\|\mathbf{t}_j\|} \)
3. **대조학습(InfoNCE 유사)**  
   - 배치 내 정답 쌍 \((i=i)\)는 가깝게, 오답 \((i\neq j)\)는 멀어지게  
   - 대칭적 cross-entropy(이미지→텍스트, 텍스트→이미지)와 **온도 파라미터** \( \tau \) 사용
4. **제로샷 추론**  
   - 레이블 집합을 **프롬프트 문장**으로 변환(예: *“a photo of a {label}”*)  
   - 이미지 임베딩과 각 레이블 문장 임베딩의 코사인 유사도를 비교해 **가장 높은 것**을 예측

> **프롬프트 엔지니어링**: 템플릿을 다양화(ensembling)하면 성능이 더 좋아지는 경향이 있습니다.

---

## 🧪 Zero-shot Classification Recipe
1. 레이블 집합 \( \mathcal{Y} \) 준비  
2. 각 \( y \in \mathcal{Y} \)에 대해 프롬프트 템플릿 생성 (예: *“a photo of a {y}”*)  
3. 텍스트 인코더로 모든 문장 임베딩 사전 계산  
4. 테스트 이미지 임베딩과 **코사인 유사도**로 **argmax** 선택  
5. (선택) 여러 템플릿을 **평균/가중 결합**하여 안정화

---

## 🔍 강점(Strengths)
- **라벨 효율**: 대규모 웹 캡션만으로 강력한 전이 성능  
- **범용성**: 분류·검색·로버스트 평가 등 **태스크-불문** 사용 가능  
- **스케일 친화적**: 데이터·모델을 키울수록 전이력이 향상되는 경향

## ⚠️ 한계(Caveats)
- **바이어스/편향**: 웹 데이터의 **사회적 편향**을 학습할 수 있음  
- **프롬프트 민감도**: 템플릿 문구·표현 변화에 성능이 출렁일 수 있음  
- **세밀 태스크**: 초정밀 로컬라이제이션/밀집 예측 등에서는 **전용 파인튜닝**이 유리할 수 있음

> 실무 적용 시 **안전성·윤리 검토**(bias/fairness), **프롬프트 관리**, **도메인 적합성 평가**를 권장합니다.

---

## 🧭 실무 팁(Quick Tips)
- **프롬프트 앙상블**: 다수 템플릿을 평균하면 제로샷 성능 상승  
- **클래스 이름 정제**: 애매한 레이블은 **설명 구문**(e.g., “a type of…” )을 추가  
- **라벨어 확장**: 동의어/언어 혼합(ko/en)로 도메인 민감도 보완  
- **후처리**: temperature scaling, class prior 보정 등도 고려

---

# 🚀 Presentation

<img width="1920" height="1080" alt="001" src="https://github.com/user-attachments/assets/42222f26-50d2-4ee8-9770-13e97bc8cd18" />
<img width="1920" height="1080" alt="002" src="https://github.com/user-attachments/assets/5aa3c533-7618-4575-b6f4-4675202f5342" />
<img width="1920" height="1080" alt="003" src="https://github.com/user-attachments/assets/73b1cd34-6b7d-4117-ba8d-87460b5276c4" />
<img width="1920" height="1080" alt="004" src="https://github.com/user-attachments/assets/ff7ca2e3-fd1e-4181-a73b-de55e53cff00" />
<img width="1920" height="1080" alt="005" src="https://github.com/user-attachments/assets/7f5e09ed-85e5-45bd-86d7-94d181191e91" />
<img width="1920" height="1080" alt="006" src="https://github.com/user-attachments/assets/3d43bc84-2360-440f-8707-f9e48c34f23f" />
<img width="1920" height="1080" alt="007" src="https://github.com/user-attachments/assets/2411f884-6f03-4d36-858c-605880c328df" />
<img width="1920" height="1080" alt="008" src="https://github.com/user-attachments/assets/c62d809b-3be6-488f-a2ee-3dd1126cca8d" />
<img width="1920" height="1080" alt="009" src="https://github.com/user-attachments/assets/2df088f3-75f1-4ad1-b237-74622c488ca5" />
<img width="1920" height="1080" alt="010" src="https://github.com/user-attachments/assets/b660680a-488a-4403-a80c-ca4e73515666" />
<img width="1920" height="1080" alt="011" src="https://github.com/user-attachments/assets/3dcbafb6-a211-4e84-9f57-8424d77e6a71" />
<img width="1920" height="1080" alt="012" src="https://github.com/user-attachments/assets/623fbda0-1f83-4ae0-8418-ca97a56c5e0f" />
<img width="1920" height="1080" alt="013" src="https://github.com/user-attachments/assets/94e98356-fb90-4e8c-a6d9-f771f1acda51" />
<img width="1920" height="1080" alt="014" src="https://github.com/user-attachments/assets/abf1b5dc-07b2-415f-a0ac-8a8994b388aa" />
<img width="1920" height="1080" alt="015" src="https://github.com/user-attachments/assets/bfeb908e-3bdf-4a19-a156-c197ca6a0e20" />
<img width="1920" height="1080" alt="016" src="https://github.com/user-attachments/assets/8c0ff932-1b31-496b-a44a-cea26673b16a" />
<img width="1920" height="1080" alt="017" src="https://github.com/user-attachments/assets/ad68fa9c-c1c8-4652-96b2-da22473155df" />
<img width="1920" height="1080" alt="018" src="https://github.com/user-attachments/assets/b496fb14-e9d7-432e-b2ed-756a65ec5bd3" />
<img width="1920" height="1080" alt="019" src="https://github.com/user-attachments/assets/2c7553cd-3fab-4727-b617-486bc1643bc8" />
<img width="1920" height="1080" alt="020" src="https://github.com/user-attachments/assets/518fc515-10f0-4410-8874-a4453c382002" />
<img width="1920" height="1080" alt="021" src="https://github.com/user-attachments/assets/acc08c20-6577-48c5-acf7-6675f11d99e5" />
<img width="1920" height="1080" alt="022" src="https://github.com/user-attachments/assets/5d59b418-9460-4426-b8b3-4837633d405f" />
<img width="1920" height="1080" alt="023" src="https://github.com/user-attachments/assets/6f7a082e-f227-49f8-aece-30a99a9073b0" />
<img width="1920" height="1080" alt="024" src="https://github.com/user-attachments/assets/287c4f33-8709-4853-b327-36e5afa7afb2" />
