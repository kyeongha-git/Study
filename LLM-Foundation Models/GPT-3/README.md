# 👋 Introduction

본 발표는 **Language Models are Few-Shot Learners (Brown et al., 2020, NeurIPS)**, 일명 **GPT-3 리포트**를 다룹니다.  
GPT-3는 GPT-2의 제로샷(Zero-shot) 관찰을 확장하여, **모델·데이터·컨텍스트 스케일을 대폭 확대**하고 **제로샷·원샷·퓨샷(Zero/One/Few-shot)** 설정에서 **프롬프트만으로** 다양한 태스크를 수행할 수 있음을 체계적으로 입증했습니다.

> ✅ **중요 교정**  
> - GPT-2의 최대 파라미터는 **1.5B**(=1.5억 × 10)이며, GPT-3는 **175B**로 **약 117배** 큽니다.  
> - GPT-3는 **파인튜닝 없이** 프롬프트(맥락)만 바꿔 수행하는 **인컨텍스트 러닝**을 중심으로 평가했습니다.

## ✨ TL;DR
- **Decoder-only Transformer + Autoregressive LM**: 아키텍처는 GPT-2와 동일 계열(자기회귀 다음 토큰 예측)  
- **스케일 업**: 125M → 355M → 1.3B → 2.7B → 6.7B → 13B → **175B**까지 다중 크기 실험  
- **데이터 혼합**: 대규모 웹 코퍼스(필터링된 CommonCrawl 등) + WebText2 + Books + Wikipedia, **~300B 토큰** 규모  
- **컨텍스트 길이**: 최대 **2048 토큰**, 프롬프트 안의 예시(k-shot)가 곧 “학습 신호” 역할  
- **결과**: 다양한 벤치마크에서 **Zero/One/Few-shot 성능**이 **모델 크기와 함께 꾸준히 향상**, 일부 과제는 **SOTA**에 근접하거나 갱신

## 🧪 Zero / One / Few-shot 프로토콜
- **Zero-shot**: 태스크 지시문만 제공 → 모델의 사전지식으로 바로 답변  
- **One-shot**: 예시 1개 + 지시문 제공 → 패턴 유도  
- **Few-shot (k-shot)**: 예시 k개(보통 10~32) + 지시문 제공 → **명확한 성능 상승** 경향  
> 모든 설정에서 **파라미터 업데이트(파인튜닝)는 없음**. **프롬프트 구성**이 성능을 좌우합니다.

## 🆚 GPT-2와 뭐가 달라졌나?
- **평가 관점의 전환**: GPT-2는 주로 **제로샷**을 강조; GPT-3는 **Zero/One/Few-shot**를 **체계적으로 비교**  
- **스케일의 효과를 정량화**: 파라미터/데이터/컨텍스트 **스케일 증가 → 제로/퓨샷 성능 꾸준히 상승**  
- **범용성 강화**: 번역·질의응답·독해·상식추론·문법·장르변환 등 **다양한 태스크**에서 경쟁적 성능

## 🔍 관찰 포인트
- **Few-shot ≫ Zero-shot**(대체로): 프롬프트 내 예시가 **과제의 형식·패턴**을 모델에 암시  
- **프롬프트 민감도**: 지시문/예시 서술 방식에 따라 성능 변동 → **프롬프트 엔지니어링** 중요  
- **스케일 법칙의 단서**: 더 큰 모델·더 많은 데이터·더 긴 컨텍스트가 **일관된 개선**을 유도

## ⚠️ 한계와 유의
- **전용 파인튜닝 대비** 항상 우월하지는 않음(특정·전문화 과제는 미세조정이 유리)  
- **편향/지식 최신성**: 웹 데이터 특성상 **사회적 편향**과 **시계열 구식 정보**를 내포할 수 있음  
- **비용/자원 제약**: 175B 모델의 **학습·추론 비용**과 재현성 이슈

---

# 🚀 Presentation

![001](https://github.com/user-attachments/assets/d9d9ea4c-b14f-4b7f-8bdd-f287353af33d)

![002](https://github.com/user-attachments/assets/5b715f6d-24de-496f-8193-d93aac871013)

![003](https://github.com/user-attachments/assets/f76c6bb4-de71-463f-838a-4a86342aa2a1)

![004](https://github.com/user-attachments/assets/61846b59-0eb1-4ac2-9a05-740d5884216c)

![005](https://github.com/user-attachments/assets/1303640c-4c03-447e-a148-9aea94a58195)

![006](https://github.com/user-attachments/assets/7d726b1e-4988-4b5f-8199-534ae7ed1400)

![007](https://github.com/user-attachments/assets/904190a5-d484-47aa-8597-365ab7c5548a)

![008](https://github.com/user-attachments/assets/009eb3ba-75ac-4414-aa1a-305aaffa5f6c)

![009](https://github.com/user-attachments/assets/cb5139c2-8c63-4877-903b-e84545c609fb)

![010](https://github.com/user-attachments/assets/855828a2-8266-404a-b9c2-a97aa506fd59)

![011](https://github.com/user-attachments/assets/708f3dca-9635-4942-af83-49c02618d830)

![012](https://github.com/user-attachments/assets/c9dae16a-1533-49e1-b539-ca0fa45d001a)

![013](https://github.com/user-attachments/assets/0d5eedff-257f-4c31-aee3-dc580f0c696c)

![014](https://github.com/user-attachments/assets/63edff8b-f0db-4e57-94ed-71746c480be4)

![015](https://github.com/user-attachments/assets/2af2ea3f-f684-4dd2-8924-a5c81724240d)

![016](https://github.com/user-attachments/assets/2e13bbfd-82cb-4f0c-b461-b54d9e150cf6)

![017](https://github.com/user-attachments/assets/81a886c3-9b88-401b-9e75-a6a7d0f74338)

![018](https://github.com/user-attachments/assets/6a378937-f9ab-4e2f-9a86-f1bc65780659)

![019](https://github.com/user-attachments/assets/f0ced82e-5176-421a-8b23-0343dce22872)

![020](https://github.com/user-attachments/assets/94d427be-7bab-429f-b753-285d78b12c06)

![021](https://github.com/user-attachments/assets/d81966a7-1423-4745-8f10-f34caf9681c9)

![022](https://github.com/user-attachments/assets/7b44ad3d-6b55-449a-905d-3e64c21a23f7)

![023](https://github.com/user-attachments/assets/25d0ab77-ed92-4cc0-8588-d5bd56b072fa)

![024](https://github.com/user-attachments/assets/b5f1c89d-4b99-4b64-927d-c5e9f4c2dc12)




