# 👋 Introduction

본 발표는 OpenAI의 CLIP(Learning Transferable Visual Models From Natural Language Supervision)을 다룹니다.

CLIP은 자연어를 감독 신호로 활용해 이미지–텍스트 공동 표현 공간을 학습하고, 프롬프트(텍스트)만으로 다양한 비전 과제를 **제로샷(Zero-shot)**으로 수행합니다. ✨

기존 Self-Supervised Pre-Traning → Downstream Transfer (or Fine-Tuning) 패러다임은
특정 태스크에 맞추려면 추가 label(적지 않은 양)이 필요하고, 데이터셋 간 일반화가 제한되는 경우가 많았습니다.

CLIP은 웹에서 수집한 대규모 이미지–텍스트 쌍을 이용해 언어 기반 감독으로 표현을 학습하고,
텍스트 프롬프트만 바꿔 새로운 태스크로 즉시 Transfer할 수 있도록 설계되었습니다. 🧠➡️🖼️

결과적으로 CLIP은 여러 벤치마크에서 제로샷 기준으로 기존 Supervised/Unsupervised (including Self-Supervised) 모델과 경쟁하거나 능가하는 강한 도메인 일반화 성능을 보입니다.

(단, 태스크 전용 파인튜닝이 허용될 때 항상 우월하다고 일반화할 수는 없으며, CLIP의 강점은 라벨 없이도 광범위하게 전이된다는 점입니다.) ✅

# 🚀 Presentation
