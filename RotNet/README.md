# 👋 Introduction

 해당 논문은 UNSUPERVISED REPRESENTATION LEARNING BY PREDICTING IMAGE ROTATIONS 입니다.
본 논문의 핵심은 Self-Supervised Learning입니다. Self-Supervised Learning이란, Supervised Learning의 장점인 Semantic Feature Learning, Generalization과 Unsupervised Learning의 장점인 Minimize Labeling Effort를 합친 방식입니다. Label을 데이터로부터 스스로 만들어내고, 이를 통해 Supervised Learning을 진행하여 사전 학습을 진행합니다. 이후, Labeled Data가 있는 Downstream Task에 Fine-Tuning하여 사용합니다.

 본 논문에서는 Self-Supervised Learning의 Pretext Task로 Rotation Prediction을 사용하였으며
기존의 SOTA Unsupervised Learning 모델과 다수의 벤치마크에서 동등하거나 우수한 성능을 보였습니다. 또한, Supervised Learning 모델과의 gap을 크게 줄였다는 점에서 의의가 있습니다.

# 🚀 Presentation
<img width="1920" height="1080" alt="슬라이드1" src="https://github.com/user-attachments/assets/8c5bc701-1279-4935-82c1-8793188efb8e" />
<img width="1920" height="1080" alt="슬라이드2" src="https://github.com/user-attachments/assets/88c7a99f-7de8-4529-bfde-2e517d14fc9b" />
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/b1c6c133-d040-4f19-8902-21c8acfde0a5" />
<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/480a561f-61af-477d-a37f-537bc107244f" />
<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/fa0d7739-0e60-4797-8307-2d7e937cb997" />
<img width="1920" height="1080" alt="슬라이드6" src="https://github.com/user-attachments/assets/c7757c44-40ad-4984-a690-9e32161e7488" />
<img width="1920" height="1080" alt="슬라이드7" src="https://github.com/user-attachments/assets/a694423c-fb23-413c-a526-d4531de15567" />
<img width="1920" height="1080" alt="슬라이드8" src="https://github.com/user-attachments/assets/ac74f891-98e4-4078-b9c7-155ef4cdc7e8" />
<img width="1920" height="1080" alt="슬라이드9" src="https://github.com/user-attachments/assets/009e094e-344c-4036-860f-e8c6afe56b77" />
<img width="1920" height="1080" alt="슬라이드10" src="https://github.com/user-attachments/assets/59b38f4d-0f2b-4921-a324-22426e0f3741" />
<img width="1920" height="1080" alt="슬라이드11" src="https://github.com/user-attachments/assets/43eb1671-f6ab-46a4-be25-532f3905cb57" />
<img width="1920" height="1080" alt="슬라이드12" src="https://github.com/user-attachments/assets/a7695152-4600-4d29-ae98-89af5ce826b5" />
<img width="1920" height="1080" alt="슬라이드13" src="https://github.com/user-attachments/assets/6ee4b69e-fd68-455e-8450-ee9ab3cc9188" />
<img width="1920" height="1080" alt="슬라이드14" src="https://github.com/user-attachments/assets/a3ebc0a2-59c3-4f45-8b60-973ec6e9c261" />
<img width="1920" height="1080" alt="슬라이드15" src="https://github.com/user-attachments/assets/9afda7e8-19dc-450e-9b2a-8c0816142c2f" />
<img width="1920" height="1080" alt="슬라이드16" src="https://github.com/user-attachments/assets/6ec62ec4-2a33-46ea-b70f-5a26dae71110" />
<img width="1920" height="1080" alt="슬라이드17" src="https://github.com/user-attachments/assets/1fb9efd1-5d8c-4a65-9c72-74cddc62badf" />
<img width="1920" height="1080" alt="슬라이드18" src="https://github.com/user-attachments/assets/d0b52c58-ca8c-47da-b44e-53335a8af454" />
<img width="1920" height="1080" alt="슬라이드19" src="https://github.com/user-attachments/assets/52d49f4a-3ef9-4550-b437-bfa3a1dcf1c3" />
<img width="1920" height="1080" alt="슬라이드20" src="https://github.com/user-attachments/assets/9a7070bb-aceb-4b3d-b43c-b1617fd53c93" />
