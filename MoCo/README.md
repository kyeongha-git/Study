# 👋 Introduction

본 발표는 FAIR(Facebook AI Research)의 MoCo(Momentum Contrast for Unsupervised Visual Representation Learning)를 다룹니다.

MoCo는 대조학습(contrastive learning)에서 성능을 좌우하는 두 요소—큰 사전(dictionary)과 키 임베딩의 일관성(consistency)—을 동시에 달성하기 위해 FIFO 큐 + 모멘텀 인코더를 도입한 방법입니다. 🔧🧠

- 문제의식: 대조학습은 많은 Negative 샘플이 필요하지만, 일반적으로 미니배치 크기에 제약되어 사전이 작거나, 메모리뱅크를 쓰면 키 분포 불일치로 학습이 불안정해집니다.

- 핵심 아이디어:
    - Larger Dictionary → Queue: 학습 중 생성된 키 임베딩을 **큐에 적재/교체(FIFO)**하여 배치와 무관하게 매우 큰 사전을 유지합니다. 📚

    - Consistency → Momentum Encoder: 키 인코더를 모멘텀(지수이동평균) 업데이트로 천천히 갱신해, 큐에 쌓이는 키의 분포 변화를 완화합니다. 🔒

- 학습 방식(요지): 같은 이미지의 두 증강으로 **쿼리 𝑞**와 **양성 키 𝑘+**를 만들고, 큐의 다수 **음성 키 𝑘−**와 함께 InfoNCE 손실로 학습합니다.

결과적으로, MoCo는 라벨 없이 학습한 표현만으로 **선형 분류(linear eval)**와 검출/세그멘테이션 등 Downstream Transfer에서 경쟁적 혹은 상회하는 성능을 보이며, 대규모 배치 없이도 강력한 대조학습을 가능하게 합니다. 📈✨

# 🚀 Presentation

<img width="1920" height="1080" alt="001" src="https://github.com/user-attachments/assets/10714b00-3e27-4554-8f84-12fa821891de" />
<img width="1920" height="1080" alt="002" src="https://github.com/user-attachments/assets/37b1ab75-aa79-43ca-9d3e-70d592f91789" />
<img width="1920" height="1080" alt="003" src="https://github.com/user-attachments/assets/6457815b-a311-460a-bcbb-1cd81935a571" />
<img width="1920" height="1080" alt="004" src="https://github.com/user-attachments/assets/7192022d-e911-4855-bb9d-d8f56625e46c" />
<img width="1920" height="1080" alt="005" src="https://github.com/user-attachments/assets/3fe6d78c-3736-4a62-87da-c14043735f73" />
<img width="1920" height="1080" alt="006" src="https://github.com/user-attachments/assets/982f3b89-1888-4e74-b7da-3c46126ed531" />
<img width="1920" height="1080" alt="007" src="https://github.com/user-attachments/assets/9f4e7ca9-933c-4d6c-b345-bd8b396bf548" />
<img width="1920" height="1080" alt="008" src="https://github.com/user-attachments/assets/ca76a473-4883-4f35-bf6e-0af1cee268db" />
<img width="1920" height="1080" alt="009" src="https://github.com/user-attachments/assets/bd27d570-63f9-4135-a9fd-df31612ce61d" />
<img width="1920" height="1080" alt="010" src="https://github.com/user-attachments/assets/e9ff20e6-cf7e-4ab3-8756-8afd5dd3c983" />
<img width="1920" height="1080" alt="011" src="https://github.com/user-attachments/assets/dbb7a240-15aa-4bb7-851c-752eb5613db6" />
<img width="1920" height="1080" alt="012" src="https://github.com/user-attachments/assets/e397314f-b872-4ba8-888b-5b3e8634df85" />
<img width="1920" height="1080" alt="013" src="https://github.com/user-attachments/assets/cab9cf4c-925b-48ce-a280-4def72d4c80e" />
<img width="1920" height="1080" alt="014" src="https://github.com/user-attachments/assets/e4d837bf-ed53-4aa5-89ff-7febc33ca000" />
<img width="1920" height="1080" alt="015" src="https://github.com/user-attachments/assets/40889c6f-7089-4f83-819c-f09274a343b0" />
<img width="1920" height="1080" alt="016" src="https://github.com/user-attachments/assets/fa60854a-5315-47f4-8d32-60e8f430b70a" />
<img width="1920" height="1080" alt="017" src="https://github.com/user-attachments/assets/1eafd6c0-683a-4162-a956-5e4fe9b5e752" />
<img width="1920" height="1080" alt="018" src="https://github.com/user-attachments/assets/12cfadc1-c49b-4347-ba68-135f4dbbc366" />
<img width="1920" height="1080" alt="019" src="https://github.com/user-attachments/assets/93a7c58a-355d-40ea-badc-028d04b7d3f1" />
