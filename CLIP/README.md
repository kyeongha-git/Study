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
