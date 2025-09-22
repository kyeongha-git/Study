# 👋 Introduction  

본 발표는 **DINOv2 (Learning Robust Visual Features without Supervision, 2024)** 를 다룹니다.  

DINOv2는 **라벨 없는(self-supervised)** 방식으로 학습된 Vision Transformer 기반의 대규모 프리트레인 모델입니다.  
핵심은 **대규모 curated dataset(LVD-142M)** 과 **효율적 학습 레시피**를 결합해,  
텍스트 감독(CLIP류) 없이도 **범용적이고 강력한 비주얼 특징**을 제공합니다.  
특히 ImageNet, iNaturalist, ADE20k 등 **image-level + pixel-level** 다운스트림 과제에서  
기존 self-supervised는 물론, 일부 weakly-supervised(OpenCLIP 등) 모델보다 뛰어난 성능을 달성합니다. ✨  

---

## ✨ TL;DR
- **데이터**: 웹 크롤링 데이터에서 자동 필터링·클러스터링으로 만든 **LVD-142M (1.2B→142M)** curated 이미지  
- **학습**: DINO + iBOT loss, Sinkhorn-Knopp centering, KoLeo regularizer, high-res adaptation  
- **효율화**: FlashAttention 개선, Sequence Packing, Stochastic Depth 최적화, PyTorch FSDP  
- **스케일**: ViT-g (1.1B params)까지 학습, distillation으로 ViT-S/B/L 파생  
- **결과**: ImageNet Linear eval → **86.5% (ViT-g)**, Segmentation mIoU 53.0, Depth RMSE SOTA  
- **범용성**: Classification, Retrieval, Segmentation, Depth, Video Action Recognition 전반에서 강력한 전이  

---

## 🧩 How DINOv2 Works (한 장 요약)
1. **Data Pipeline**  
   - 웹 크롤링 uncurated 1.2B 이미지 → deduplication → retrieval 기반 curated **142M 이미지 (LVD-142M)**  
   - 다양한 domain을 커버하도록 자동 리밸런싱
2. **Self-Supervised Objectives**  
   - **DINO loss (image-level)** + **iBOT loss (patch-level MIM)**  
   - Teacher–student 구조 (EMA 업데이트)  
   - Sinkhorn-Knopp centering, KoLeo regularizer
3. **Efficient Training**  
   - FlashAttention 최적화, Sequence Packing, High Stochastic Depth, FSDP 병렬화  
   - Short high-resolution phase (224→518)로 pixel-level task 성능 향상
4. **Distillation**  
   - ViT-g로 학습 후, ViT-L/S/B 모델에 knowledge distillation  

---

## 🧪 Experiments & Results
- **ImageNet Linear Eval**: ViT-g/14 → 86.5%, ViT-L/14 → 86.3%  
- **Fine-grained Benchmarks**: Food101 94.7%, Cars 91.4%, CUB 91.6% → OpenCLIP과 유사 혹은 상회  
- **Domain Generalization**: ImageNet-A 75.9%, ImageNet-R 78.8, Sketch 62.5 → 기존 SSL 대비 +20%p 이상  
- **Instance Retrieval**: Landmark retrieval (Oxford/Paris)에서 OpenCLIP 대비 +34% mAP  
- **Semantic Segmentation (linear probe)**: ADE20k 49.0, CityScapes 71.3, Pascal VOC 83.0 (multiscale 시)  
- **Depth Estimation**: KITTI RMSE 2.11, SUN-RGBd transfer에서도 강한 일반화  
- **Video Understanding**: Kinetics-400 78.4%, SSv2 38.3% → OpenCLIP과 대등 혹은 우수  

---

## 🔍 강점 (Strengths)
- **범용성**: image-level + pixel-level 모두에서 강력한 성능  
- **Curated Data**: uncurated 대비 훨씬 나은 feature quality  
- **효율성**: 기존 iBOT 대비 2× 빠르고 3× 메모리 절감  
- **스케일 친화적**: 모델·데이터 크기 확장 시 성능 지속 상승  
- **라벨 불필요**: 텍스트 감독 없이도 weakly-supervised 모델에 근접/능가  

---

## ⚠️ 한계 (Caveats)
- **고비용 학습**: ViT-g/14 (1.1B) 규모는 여전히 큰 자원 필요  
- **특수 태스크 한계**: 초정밀 dense prediction에서는 full finetuning 유리  
- **데이터 의존성**: curated pipeline 품질에 성능이 민감  

---

## 🧭 실무 팁 (Quick Tips)
- **중·대형 모델**: ViT-L 이상일 때 DINOv2의 강점이 뚜렷  
- **멀티 크롭 + 하이레졸루션 적응** → dense task 성능 강화  
- **Distillation 활용**: 작은 모델은 ViT-g distill 버전 권장  
- **k-NN 평가**로 빠르게 feature 품질 점검 가능  

---

# 🚀 Presentation  
<img width="1920" height="1080" alt="슬라이드1" src="https://github.com/user-attachments/assets/cb05f8f3-d74b-459d-8f6c-1bebfbb272fb" />
<img width="1920" height="1080" alt="슬라이드2" src="https://github.com/user-attachments/assets/e8123e73-35f7-4c76-9861-6ba5297fdfc9" />
<img width="1920" height="1080" alt="슬라이드3" src="https://github.com/user-attachments/assets/70bdf47d-2832-429e-b177-32b54193eb00" />
<img width="1920" height="1080" alt="슬라이드4" src="https://github.com/user-attachments/assets/c91f8a11-9aa9-4da0-a518-4994b150bf0b" />
<img width="1920" height="1080" alt="슬라이드5" src="https://github.com/user-attachments/assets/7aa83499-70c7-415d-9018-1cac34a29deb" />
<img width="1920" height="1080" alt="슬라이드6" src="https://github.com/user-attachments/assets/be22d6b0-e829-4d3f-b12b-2c01638e4ec6" />
<img width="1920" height="1080" alt="슬라이드7" src="https://github.com/user-attachments/assets/0e64862c-5c0a-4e8d-b762-c27e751a0b3c" />
<img width="1920" height="1080" alt="슬라이드8" src="https://github.com/user-attachments/assets/a56e2146-774f-43ff-a3e4-a2fce253b89f" />
<img width="1920" height="1080" alt="슬라이드9" src="https://github.com/user-attachments/assets/fa85c9f5-382e-4702-8db0-369098b2162b" />
<img width="1920" height="1080" alt="슬라이드10" src="https://github.com/user-attachments/assets/5ad1d7da-a3cb-4484-8a35-464e5ed75034" />
<img width="1920" height="1080" alt="슬라이드11" src="https://github.com/user-attachments/assets/40c4b3a8-ce18-45b0-aaf5-67ec34d07cfb" />
<img width="1920" height="1080" alt="슬라이드12" src="https://github.com/user-attachments/assets/7338b6f5-8fb3-4401-8d38-edad8ff8b2af" />
<img width="1920" height="1080" alt="슬라이드13" src="https://github.com/user-attachments/assets/9ad0d43e-b6a5-481d-a5de-45cdb75d1912" />
<img width="1920" height="1080" alt="슬라이드14" src="https://github.com/user-attachments/assets/2ab5cd95-7b1f-4321-86d3-494550815505" />
<img width="1920" height="1080" alt="슬라이드15" src="https://github.com/user-attachments/assets/373634a4-cbcc-404b-a23f-15efcdd1a669" />
<img width="1920" height="1080" alt="슬라이드16" src="https://github.com/user-attachments/assets/0c152e9b-bde9-4ec8-92b4-a549d1028d45" />
<img width="1920" height="1080" alt="슬라이드17" src="https://github.com/user-attachments/assets/484a0328-52c4-40a7-9d40-d13c6542ca01" />
<img width="1920" height="1080" alt="슬라이드18" src="https://github.com/user-attachments/assets/f13e099a-cb16-4040-8535-da6fe27eeb62" />
<img width="1920" height="1080" alt="슬라이드19" src="https://github.com/user-attachments/assets/5a0f1b1e-7be5-412e-a668-9068e606439d" />
<img width="1920" height="1080" alt="슬라이드20" src="https://github.com/user-attachments/assets/096cbdb3-b411-4ab0-9e8f-cbf645400f04" />
