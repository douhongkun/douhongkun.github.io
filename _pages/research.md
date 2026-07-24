---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

Overview
======
My work centers on making deep generative models **more controllable, efficient, and scientifically useful**—from guided diffusion sampling and inverse problems, to post-training and enhancement of **diffusion large language models**, weather field reconstruction, and biological sequence design.

Research Themes
======
- Controllable generation & alignment for diffusion / flow models
- Post-training, guidance, and capability enhancement for diffusion LLMs
- Generative AI for Science (meteorology, DNA / protein design)

Projects
======

### Controllable Generation of Masked Diffusion Models
**May 2025 – Present**

Addresses non-differentiability and inefficiency in controlled generation for discrete data with a general masked-diffusion control framework.

- **Innovation:** A logit-correction algorithm derived from variational inference that embeds guidance signals into discrete sampling.
- **Results:** ~19% higher DNA enhancer activity and ~23% higher protein inverse-folding efficiency vs. RL fine-tuning schemes.

### Meteorological Field Reconstruction & Prediction
**Feb 2025 – Present** · Collaboration with Huawei 2012 Labs (Central Research Institute)

Generative AI for high-precision meteorological reconstruction and forecasting.

- **Approach:** Compress spatiotemporal weather fields into low-dimensional tokens (Sora-style); model atmospheric dynamics with spatiotemporal DiT; spherical Gaussian constraints for adaptive-step sampling.
- **Impact:** ~20× inference speedup, ~90% VRAM reduction; integrated into the **Pangu** weather large model for provincial power and solar forecasting.

### Control & Reward Alignment for Text-to-Image/Video Models
**Feb 2025 – Aug 2025**

Reduces the gradient-backpropagation cost of controllable T2I/T2V generation via **SDO**, a high-performance low-overhead algorithm.

- **Innovation:** Gradient shortcuts from implicit differentiation and fixed-point iteration, with theoretical guarantees—no full reverse-mode through the sampling path.
- **Results:** Text-guided editing, aesthetic enhancement, and human preference alignment with ~90% speedup and 35% VRAM savings; mitigates gradient explosion on long sampling paths.

### Multi-object Referring & Localization for Multimodal LLMs
**Aug 2024 – Feb 2025**

Pixel-level multi-object referring and localization for MLLMs.

- **Architecture:** Channel expansion and hybrid adapters for simultaneous free-form multi-region perception; large-scale multi-object referring/segmentation benchmark.
- **Results:** +14.4% on multi-target exhaustive description; +13.0 cIoU on multi-referring segmentation.

### Diffusion-based Inverse Problem Solving
**May 2023 – Aug 2024**

Hybrid regularization to mitigate mode collapse and diversity loss from inaccurate gradients in diffusion inverse solvers.

- Introduces consistency distillation into the regularization framework for accuracy and stability.
- SOTA-level results on inpainting, super-resolution, data assimilation, and black-hole imaging with lower runtime and memory.

### Image-to-Image Bayesian Flow Networks (I2I-BFNs)
**Aug 2022 – May 2024**

Brings Bayesian Flow Networks to image-to-image translation with structurally informative deterministic priors from the condition image.

- Competitive few-step generation across low-quality images, edges, normal maps, and related control settings.
- Lower resource cost and improved interpretability vs. noise-driven diffusion I2I pipelines.
