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
