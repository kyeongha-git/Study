# 👋 Introduction

본 발표는 **Scaling Laws for Neural Language Models (Kaplan et al., 2020, OpenAI)** 를 다룹니다.  
핵심 질문은 “**언어 모델의 성능(손실)**이 **모델 크기 \(N\)**, **데이터 토큰 수 \(D\)**, **학습 연산량 \(C\)** 에 어떻게 의존하는가?”입니다. 저자들은 광범위한 규모 실험을 통해 **손실이 단순한 거듭제곱(Power-law)** 으로 감소한다는 **경험 법칙**을 제시합니다.

## ✨ TL;DR
- **Power-law 감소**: 테스트 손실 \(L\)은 대략  
  $L(N,D)\approx L_\infty + a\,N^{-\alpha_N} + b\,D^{-\alpha_D}$꼴로 줄어듭니다. 즉, **모델을 키우거나 데이터를 늘리면 꾸준히 좋아지되 점점 수익 체감**이 발생합니다.
- **Compute-optimal 트레이드오프**: 대략 \(C \propto N\times D\) (토큰당 비용이 매개변수 수에 비례)로 볼 수 있어, **고정 연산량**에서 \(N\)만 키우거나 \(D\)만 늘리면 비효율적이며, **둘을 함께 스케일**해야 최적입니다.
- **실무 지침**: 주어진 연산/시간 예산에서 **적정 \(N\)–\(D\) 균형**을 잡고, 과도한 파라미터에 **짧은 학습**이나, 작은 모델에 **과도한 토큰**처럼 **한쪽 편향**을 피하라는 메시지.

## 🧠 무엇을, 왜 밝혔나?
1. **모델 크기 의존성**  
   \[
   L(N,\infty)\approx L_\infty + a\,N^{-\alpha_N}
   \]
   모델 파라미터가 커질수록 손실이 **예측 가능하게** 감소합니다.
2. **데이터 규모 의존성**  
   \[
   L(\infty,D)\approx L_\infty + b\,D^{-\alpha_D}
   \]
   학습 토큰을 늘리면 비슷한 **기댓손실 감소율**을 따릅니다.
3. **결합 모델**  
   \[
   L(N,D)\approx L_\infty + a\,N^{-\alpha_N}+b\,D^{-\alpha_D}
   \]
   → 두 축 모두에서 **매끄러운 스케일링 곡선**을 확인.
4. **연산량 제약 하 최적화**  
   총 학습 연산을 \(C\approx k\,N D\)로 놓고 \(L(N,D)\)를 최소화하면,  
   **주어진 \(C\)** 에 대해 **\(N\)과 \(D\)를 함께 키우는 해**가 존재(= *compute-optimal frontier*).  
   실무적으로는 “**모델·데이터를 균형 있게 확장**”이 핵심입니다.

> 요지: **규모를 늘리면 좋아진다**는 명제가 **정량식**으로 주어졌고, **얼마나 늘려야 효율적인지**에 대한 **스케일링 전략**이 제안됩니다.

## 🛠️ 실무 체크리스트
- **예산 먼저**: 가용 **연산량/시간/메모리**를 산정하고, 그 범위에서 \(N\)–\(D\) 균형을 맞춥니다.
- **토큰 예산 배분**: 너무 큰 모델에 **짧은 학습**(undertraining) 혹은 작은 모델에 **과도한 토큰**(data-overprovision) 모두 비효율.
- **데이터 품질**: 동일 \(D\)라도 **노이즈/중복**이 많으면 **유효 토큰**이 줄어듭니다(파워로만 설명 불가).
- **조기 종료/스케줄**: 목표 손실 구간에 도달하면 **학습 종료**가 연산 효율적일 수 있음.
- **지속 모니터링**: 손실이 **예상된 기울기**(log–log 직선)에서 벗어나면 병목을 점검(학습률, 배치, 정규화, 데이터 중복 등).

## ⚠️ 한계와 주의
- **유효 범위**: 파워로우는 **관측된 스케일 범위** 내에서 잘 맞습니다. 너무 작은 모델·데이터, 혹은 극단적으로 큰 설정에서는 **편차**가 생길 수 있습니다.
- **다운스트림 전이 ≠ 언어모델 손실**: LM 손실이 낮아도 **태스크 성능**이 항상 선형적으로 오르지는 않습니다(프롬프트·평가 프로토콜 영향).
- **후속 연구와의 관계**: 이후 연구(예: 더 큰 데이터/모델, 다른 훈련 레시피)는 **데이터–파라미터 비율**에 대한 **구체적 권장치**를 갱신/보완했습니다. 본 발표는 **원 논문의 일반 법칙**에 초점을 둡니다.

---

# 🚀 Presentation
<img width="1920" height="1080" alt="001" src="https://github.com/user-attachments/assets/54ffcf94-8ade-42f1-9589-f75a805d3d8e" />
<img width="1920" height="1080" alt="002" src="https://github.com/user-attachments/assets/5767014e-f4ed-43b7-a769-7018311e53e8" />
<img width="1920" height="1080" alt="003" src="https://github.com/user-attachments/assets/5921479c-c3eb-49b9-9355-4b9b0537a42e" />
<img width="1920" height="1080" alt="004" src="https://github.com/user-attachments/assets/5b2d3f62-c63e-4530-977f-8348308dca84" />
<img width="1920" height="1080" alt="005" src="https://github.com/user-attachments/assets/3329c165-4039-4727-b75b-a3615f0dda07" />
<img width="1920" height="1080" alt="006" src="https://github.com/user-attachments/assets/94eccdc5-cee8-44c4-a95f-3d3ac8054ae6" />
<img width="1920" height="1080" alt="007" src="https://github.com/user-attachments/assets/6a08c64a-b468-4877-baf0-a2832878f587" /> 
<img width="1920" height="1080" alt="008" src="https://github.com/user-attachments/assets/8604222a-2197-4fbe-9719-cc79f4551748" />
<img width="1920" height="1080" alt="009" src="https://github.com/user-attachments/assets/743a8a3c-4255-4811-9391-08e2c9eb3761" />
<img width="1920" height="1080" alt="010" src="https://github.com/user-attachments/assets/9f30f875-0d9f-4c3a-b701-215ed69f1995" />
<img width="1920" height="1080" alt="011" src="https://github.com/user-attachments/assets/64f7d441-f953-4810-8670-1ec11a84d427" />
<img width="1920" height="1080" alt="012" src="https://github.com/user-attachments/assets/c68f8849-4bf4-4559-9240-d2927de641d6" />
<img width="1920" height="1080" alt="013" src="https://github.com/user-attachments/assets/04c62d18-4e12-45ed-95af-10aa6ef336a8" />
<img width="1920" height="1080" alt="014" src="https://github.com/user-attachments/assets/406f10d7-045c-421d-823d-fddee2a6ed34" />
<img width="1920" height="1080" alt="015" src="https://github.com/user-attachments/assets/ac4a8caf-3f5c-493a-975f-9fdd7cb89c9e" />
<img width="1920" height="1080" alt="016" src="https://github.com/user-attachments/assets/20d82e15-dced-46ac-8d02-4d42685624fe" />
<img width="1920" height="1080" alt="017" src="https://github.com/user-attachments/assets/6dc623b7-5fc7-4cd7-9d18-8c04d34821c1" />
<img width="1920" height="1080" alt="018" src="https://github.com/user-attachments/assets/6077f938-6295-420f-be0f-0d8d96811945" />
<img width="1920" height="1080" alt="019" src="https://github.com/user-attachments/assets/ac8bf70f-e60a-4fef-9ca3-f7d8163c3b25" />
<img width="1920" height="1080" alt="020" src="https://github.com/user-attachments/assets/2b8a6bb3-f33a-4f94-b713-1365bf944d2b" />
<img width="1920" height="1080" alt="021" src="https://github.com/user-attachments/assets/5fc6a064-cc86-4460-afb3-535bdd972243" />
<img width="1920" height="1080" alt="022" src="https://github.com/user-attachments/assets/0af9bad0-6c80-4fa8-8aec-14a87fb352ae" />
<img width="1920" height="1080" alt="023" src="https://github.com/user-attachments/assets/ed8a3704-6e7a-4dc0-a0f5-7a659317768b" />
<img width="1920" height="1080" alt="024" src="https://github.com/user-attachments/assets/e792670b-406d-4ea1-a486-3f7b3fb6d330" />
<img width="1920" height="1080" alt="025" src="https://github.com/user-attachments/assets/9371ebfb-4b73-4e99-930f-6fdc20462073" />
<img width="1920" height="1080" alt="026" src="https://github.com/user-attachments/assets/b93696f0-27c6-41d9-accb-57fa40e0b45a" />
