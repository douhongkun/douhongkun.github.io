# -*- coding: utf-8 -*-
"""Generate publication markdown with explicit sort priority.

Sort key (descending): year, first_author, venue_tier, title
Displayed order uses `date` as YYYY-MM-DD encoded from priority so
Jekyll `reversed` listing matches the intended academic ranking.
Venue year in citation remains accurate.
"""
from pathlib import Path

out = Path("_publications")
out.mkdir(exist_ok=True)
for p in out.glob("*.md"):
    p.unlink()

# venue_tier: higher = better (used within same year)
# first_author: 1 or 0
pubs = [
    # ===== 2026 =====
    dict(
        slug="2026-icml-plug-play-guidance",
        year=2026, month=7, day=1,
        first=1, tier=95,
        category="conferences",
        title="Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction",
        venue="International Conference on Machine Learning (ICML)",
        citation='**Dou, H.**, et al. (2026). &quot;Plug-and-Play Guidance for Discrete Diffusion Models via Gradient-Informed Logit Correction.&quot; <i>ICML</i>.',
        excerpt="Plug-and-play guidance for discrete diffusion models via gradient-informed logit correction. ICML 2026.",
    ),
    dict(
        slug="2026-tpami-multi-domain",
        year=2026, month=6, day=15,
        first=0, tier=100,
        category="manuscripts",
        title="Image Restoration via Multi-Domain Learning",
        venue="IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)",
        citation='Jiang, X., Gao, N., Zhang, X., **Dou, H.**, Fu, S., Zhong, X., Li, H., Deng, Y. (2026). &quot;Image Restoration via Multi-Domain Learning.&quot; <i>IEEE TPAMI</i>.',
        excerpt="Image restoration via multi-domain learning. IEEE TPAMI 2026.",
    ),
    dict(
        slug="2026-aaai-cps",
        year=2026, month=2, day=1,
        first=1, tier=80,
        category="conferences",
        title="Constrained Particle Seeking: Solving Diffusion Inverse Problems with Just Forward Passes",
        venue="AAAI Conference on Artificial Intelligence (AAAI)",
        citation='**Dou, H.**, et al. (2026). &quot;Constrained Particle Seeking: Solving Diffusion Inverse Problems with Just Forward Passes.&quot; <i>AAAI</i>.',
        excerpt="Solving diffusion inverse problems with forward passes only. AAAI 2026.",
    ),
    dict(
        slug="2026-tip-global-modeling",
        year=2026, month=1, day=1,
        first=0, tier=90,
        category="manuscripts",
        title="Global Modeling Matters: A Fast, Lightweight and Effective Baseline for Efficient Image Restoration",
        venue="IEEE Transactions on Image Processing (TIP)",
        citation='Jiang, X., Gao, N., **Dou, H.**, et al. (2026). &quot;Global Modeling Matters: A Fast, Lightweight and Effective Baseline for Efficient Image Restoration.&quot; <i>IEEE TIP</i>. (JCR Q1 Top, IF: 13.7)',
        excerpt="Fast lightweight baseline for efficient image restoration. IEEE TIP 2026 (IF: 13.7).",
    ),
    # ===== 2025 =====
    dict(
        slug="2025-tpami-yolo-step",
        year=2025, month=12, day=1,
        first=1, tier=100,
        category="manuscripts",
        title="You Only Look One Step: Accelerating Backpropagation in Diffusion Sampling with Gradient Shortcuts",
        venue="IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)",
        citation='**Dou, H.**, et al. (2025). &quot;You Only Look One Step: Accelerating Backpropagation in Diffusion Sampling with Gradient Shortcuts.&quot; <i>IEEE TPAMI</i>. (JCR Q1 Top, IF: 18.6)',
        excerpt="Accelerating backpropagation in diffusion sampling with gradient shortcuts. IEEE TPAMI 2025 (IF: 18.6).",
    ),
    dict(
        slug="2025-iccv-dposerx",
        year=2025, month=10, day=20,
        first=0, tier=92,
        category="conferences",
        title="DPoser-X: Diffusion Model as Robust 3D Whole-body Human Pose Prior",
        venue="International Conference on Computer Vision (ICCV) — Oral",
        citation='Lu, J., Lin, J., **Dou, H.**, et al. (2025). &quot;DPoser-X: Diffusion Model as Robust 3D Whole-body Human Pose Prior.&quot; <i>ICCV</i> (Oral).',
        excerpt="Diffusion model as robust 3D whole-body human pose prior. ICCV 2025 Oral.",
    ),
    dict(
        slug="2025-acmmm-underwater-gs",
        year=2025, month=10, day=15,
        first=0, tier=75,
        category="conferences",
        title="Spatiotemporal Degradation-Aware 3D Gaussian Splatting for Realistic Underwater Scene Reconstruction",
        venue="ACM Multimedia (ACM MM)",
        citation='Liu, S., Gao, N., Gu, Z., **Dou, H.**, et al. (2025). &quot;Spatiotemporal Degradation-Aware 3D Gaussian Splatting for Realistic Underwater Scene Reconstruction.&quot; <i>ACM MM</i>.',
        excerpt="Spatiotemporal degradation-aware 3DGS for underwater scenes. ACM MM 2025.",
    ),
    dict(
        slug="2025-tip-i2i-bfn",
        year=2025, month=9, day=1,
        first=1, tier=90,
        category="manuscripts",
        title="Image-to-Image Bayesian Flow Networks with Structurally Informative Priors",
        venue="IEEE Transactions on Image Processing (TIP)",
        citation='**Dou, H.**, et al. (2025). &quot;Image-to-Image Bayesian Flow Networks with Structurally Informative Priors.&quot; <i>IEEE TIP</i>. (JCR Q1 Top, IF: 13.7)',
        excerpt="I2I Bayesian Flow Networks with structurally informative priors. IEEE TIP 2025 (IF: 13.7).",
    ),
    dict(
        slug="2025-tnnls-score-np",
        year=2025, month=8, day=1,
        first=1, tier=88,
        category="manuscripts",
        title="Score-Based Neural Processes",
        venue="IEEE Transactions on Neural Networks and Learning Systems (TNNLS)",
        citation='**Dou, H.**, et al. (2025). &quot;Score-Based Neural Processes.&quot; <i>IEEE TNNLS</i>. (JCR Q1 Top, IF: 8.9)',
        excerpt="Score-based neural processes. IEEE TNNLS 2025 (IF: 8.9).",
    ),
    dict(
        slug="2025-nsr-bio-learning",
        year=2025, month=7, day=1,
        first=0, tier=98,
        category="manuscripts",
        title="Biologically inspired heterogeneous learning for accurate, efficient and low-latency neural network",
        venue="National Science Review",
        citation='Wang, B., Zhang, Y., Li, H., **Dou, H.**, et al. (2025). &quot;Biologically inspired heterogeneous learning for accurate, efficient and low-latency neural network.&quot; <i>National Science Review</i>. (JCR Q1 Top, IF: 17.1)',
        excerpt="Biologically inspired heterogeneous learning. National Science Review 2025 (IF: 17.1).",
    ),
    dict(
        slug="2025-iclr-hybrid-reg",
        year=2025, month=5, day=1,
        first=1, tier=95,
        category="conferences",
        title="Hybrid Regularization Improves Diffusion-based Inverse Problem Solving",
        venue="International Conference on Learning Representations (ICLR)",
        citation='**Dou, H.**, et al. (2025). &quot;Hybrid Regularization Improves Diffusion-based Inverse Problem Solving.&quot; <i>ICLR</i>.',
        excerpt="Hybrid regularization for diffusion-based inverse problem solving. ICLR 2025.",
    ),
    dict(
        slug="2025-iclr-physics-bridge",
        year=2025, month=4, day=25,
        first=0, tier=96,
        category="conferences",
        title="Physics-aligned field reconstruction with diffusion bridge",
        venue="International Conference on Learning Representations (ICLR) — Spotlight",
        citation='Li, Z., **Dou, H.**, et al. (2025). &quot;Physics-aligned field reconstruction with diffusion bridge.&quot; <i>ICLR</i> (Spotlight).',
        excerpt="Physics-aligned field reconstruction with diffusion bridge. ICLR 2025 Spotlight.",
    ),
    dict(
        slug="2025-iclr-value-aligned",
        year=2025, month=4, day=20,
        first=0, tier=94,
        category="conferences",
        title="Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization",
        venue="International Conference on Learning Representations (ICLR)",
        citation='Jiang, X., Gao, N., Zhang, X., **Dou, H.**, et al. (2025). &quot;Value-aligned Behavior Cloning for Offline Reinforcement Learning via Bi-level Optimization.&quot; <i>ICLR</i>.',
        excerpt="Value-aligned behavior cloning for offline RL. ICLR 2025.",
    ),
    dict(
        slug="2025-jctc-nqs",
        year=2025, month=3, day=15,
        first=0, tier=82,
        category="manuscripts",
        title="Expectation-Maximization-Based Optimization of Neural Quantum States for Ab Initio Quantum Chemistry",
        venue="Journal of Chemical Theory and Computation (JCTC)",
        citation='Fang, S., **Dou, H.**, et al. (2025). &quot;Expectation-Maximization-Based Optimization of Neural Quantum States for Ab Initio Quantum Chemistry.&quot; <i>JCTC</i>. (JCR Q1 Top, IF: 5.5)',
        excerpt="EM-based optimization of neural quantum states for ab initio quantum chemistry. JCTC 2025 (IF: 5.5).",
    ),
    dict(
        slug="2025-tai-hyperopt",
        year=2025, month=3, day=10,
        first=1, tier=78,
        category="manuscripts",
        title="High-dimensional Hyperparameter Optimization via Adjoint Differentiation",
        venue="IEEE Transactions on Artificial Intelligence (TAI)",
        citation='**Dou, H.**, et al. (2025). &quot;High-dimensional Hyperparameter Optimization via Adjoint Differentiation.&quot; <i>IEEE TAI</i>.',
        excerpt="High-dimensional hyperparameter optimization via adjoint differentiation. IEEE TAI 2025.",
    ),
    dict(
        slug="2025-tai-consistency",
        year=2025, month=3, day=5,
        first=1, tier=78,
        category="manuscripts",
        title="Towards a Unified Framework for Consistency Generative Modeling",
        venue="IEEE Transactions on Artificial Intelligence (TAI)",
        citation='**Dou, H.**, et al. (2025). &quot;Towards a Unified Framework for Consistency Generative Modeling.&quot; <i>IEEE TAI</i>.',
        excerpt="A unified framework for consistency generative modeling. IEEE TAI 2025.",
    ),
    # ===== 2024 =====
    dict(
        slug="2024-neurips-world-model",
        year=2024, month=12, day=1,
        first=0, tier=95,
        category="conferences",
        title="Task-aware world model learning with meta weighting via bi-level optimization",
        venue="Neural Information Processing Systems (NeurIPS)",
        citation='Yuan, H., **Dou, H.**, et al. (2024). &quot;Task-aware world model learning with meta weighting via bi-level optimization.&quot; <i>NeurIPS</i>.',
        excerpt="Task-aware world model learning with meta weighting. NeurIPS 2024.",
    ),
    dict(
        slug="2024-tip-segsid",
        year=2024, month=6, day=1,
        first=0, tier=90,
        category="manuscripts",
        title="SEGSID: A Semantic-Guided Framework for Sonar Image Despeckling",
        venue="IEEE Transactions on Image Processing (TIP)",
        citation='Liu, S., Lu, J., **Dou, H.**, et al. (2024). &quot;SEGSID: A Semantic-Guided Framework for Sonar Image Despeckling.&quot; <i>IEEE TIP</i>. (JCR Q1 Top, IF: 13.7)',
        excerpt="Semantic-guided sonar image despeckling. IEEE TIP 2024 (IF: 13.7).",
    ),
    # ===== 2023 =====
    dict(
        slug="2023-jstars-scoreseg",
        year=2023, month=6, day=1,
        first=0, tier=70,
        category="manuscripts",
        title="ScoreSeg: Leveraging score-based generative model for self-supervised semantic segmentation of remote sensing",
        venue="IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing (JSTARS)",
        citation='Lu, J., He, G., **Dou, H.**, et al. (2023). &quot;ScoreSeg: Leveraging score-based generative model for self-supervised semantic segmentation of remote sensing.&quot; <i>IEEE JSTARS</i>. (IF: 5.3)',
        excerpt="Score-based self-supervised semantic segmentation for remote sensing. IEEE JSTARS 2023 (IF: 5.3).",
    ),
    # ===== 2022 =====
    dict(
        slug="2022-eccv-dehazing",
        year=2022, month=10, day=1,
        first=0, tier=88,
        category="conferences",
        title="Boosting supervised dehazing methods via bi-level patch reweighting",
        venue="European Conference on Computer Vision (ECCV)",
        citation='Jiang, X., **Dou, H.**, et al. (2022). &quot;Boosting supervised dehazing methods via bi-level patch reweighting.&quot; <i>ECCV</i>.',
        excerpt="Boosting supervised dehazing via bi-level patch reweighting. ECCV 2022.",
    ),
    # ===== 2020 =====
    dict(
        slug="2020-ol-residual-d2nn",
        year=2020, month=1, day=1,
        first=1, tier=60,
        category="manuscripts",
        title="Residual D2NN: training diffractive deep neural networks via learnable light shortcuts",
        venue="Optics Letters",
        citation='**Dou, H.**, et al. (2020). &quot;Residual D2NN: training diffractive deep neural networks via learnable light shortcuts.&quot; <i>Optics Letters</i>. (IF: 3.3)',
        excerpt="Residual D2NN with learnable light shortcuts. Optics Letters 2020 (IF: 3.3).",
    ),
]

# Sort globally for printing, then assign dates per category so section lists sort correctly
pubs.sort(key=lambda p: (p["year"], p["first"], p["tier"]), reverse=True)

from collections import defaultdict

by_cat = defaultdict(list)
for p in pubs:
    by_cat[p["category"]].append(p)

seen = set()
for category, items in by_cat.items():
    # already globally sorted; preserve that relative order within category
    for j, p in enumerate(items):
        year = p["year"]
        # denser packing: top items get later months
        month = max(1, 12 - j)
        day = 28 - (j % 10)
        d = f"{year:04d}-{month:02d}-{day:02d}"
        while d in seen:
            day -= 1
            if day < 1:
                month -= 1
                day = 28
                if month < 1:
                    year -= 1
                    month = 12
            d = f"{year:04d}-{month:02d}-{day:02d}"
        seen.add(d)
        p["date"] = d

for p in pubs:
    content = "\n".join(
        [
            "---",
            f'title: "{p["title"]}"',
            "collection: publications",
            f'category: {p["category"]}',
            f'permalink: /publication/{p["slug"]}',
            f"excerpt: '{p['excerpt']}'",
            f'date: {p["date"]}',
            f"venue: '{p['venue']}'",
            f"citation: '{p['citation']}'",
            f"author_profile: true",
            "---",
            "",
            p["excerpt"],
            "",
        ]
    )
    path = out / f"{p['date']}-{p['slug']}.md"
    path.write_text(content, encoding="utf-8")
    fa = "1st" if p["first"] else "co"
    print(f"{p['date']}  [{fa}|{p['tier']:3d}]  {p['title'][:70]}")

print("total", len(pubs))
