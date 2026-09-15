# Lecture Index — Fundamentals of Generative AI and LLMs

**36 lectures** · 3 per week × 12 weeks · aligned with NPTEL `noc26_cs95`

Weeks 1–9 map to approximately **58 official NPTEL video lectures**. This index consolidates that video content into 27 lectures (L01–L27) and extends weeks 10–12 as L28–L36. Official NPTEL week themes and video titles are noted where available.

---

## Week 1 — Fundamentals of Deep Learning for Generative AI

*NPTEL videos: ~7 lectures · Official week theme: Generative AI overview, neural network revision, CNNs (LeNet, VGG, ResNet)*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L01** | [Introduction to Generative AI and Course Overview](notes/vol-01.md#l01-introduction-to-generative-ai-and-course-overview) | *Fundamentals of Generative AI and Large Language Models: Theory and Practice (Intro)* |
| **L02** | [Neural Network Fundamentals for Generative Models](notes/vol-01.md#l02-neural-network-fundamentals-for-generative-models) | Neural network revision; backpropagation |
| **L03** | [Convolutional Neural Networks: LeNet, VGG, ResNet](notes/vol-01.md#l03-convolutional-neural-networks-lenet-vgg-resnet) | CNN architectures for representation learning |

---

## Week 2 — Autoencoders

*NPTEL videos: ~6 lectures · Official week theme: Encoder-decoder architecture, bottleneck representation, denoising autoencoders*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L04** | [Encoder-Decoder Architecture and Bottleneck Representations](notes/vol-01.md#l04-encoder-decoder-architecture-and-bottleneck-representations) | Autoencoder architecture |
| **L05** | [Training Autoencoders and Reconstruction Loss](notes/vol-01.md#l05-training-autoencoders-and-reconstruction-loss) | Loss functions and latent spaces |
| **L06** | [Denoising and Sparse Autoencoders](notes/vol-01.md#l06-denoising-and-sparse-autoencoders) | Denoising autoencoders |

---

## Week 3 — Variational Autoencoders (VAEs)

*NPTEL videos: ~7 lectures · Official week theme: Latent variable models, reparameterization trick, ELBO*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L07** | [Latent Variable Models and the Probabilistic Perspective](notes/vol-01.md#l07-latent-variable-models-and-the-probabilistic-perspective) | Generative modeling as density estimation |
| **L08** | [Variational Autoencoders and the Reparameterization Trick](notes/vol-01.md#l08-variational-autoencoders-and-the-reparameterization-trick) | VAE architecture |
| **L09** | [Evidence Lower Bound (ELBO) Derivation](notes/vol-01.md#l09-evidence-lower-bound-elbo-derivation) | ELBO optimization |

---

## Week 4 — Advanced VAEs

*NPTEL videos: ~6 lectures · Official week theme: Conditional VAE, Beta-VAE, disentanglement, latent interpolation*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L10** | [Conditional VAE (CVAE)](notes/vol-02.md#l10-conditional-vae-cvae) | Conditional generation |
| **L11** | [Beta-VAE and Disentangled Representations](notes/vol-02.md#l11-beta-vae-and-disentangled-representations) | β-VAE objective |
| **L12** | [Latent Space Interpolation and VAE Limitations](notes/vol-02.md#l12-latent-space-interpolation-and-vae-limitations) | Latent traversal |

---

## Week 5 — Generative Adversarial Networks (GANs)

*NPTEL videos: ~7 lectures · Official week theme: Generator-discriminator, minimax objective, DCGAN*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L13** | [Generative Adversarial Networks: Minimax Formulation](notes/vol-02.md#l13-generative-adversarial-networks-minimax-formulation) | GAN introduction |
| **L14** | [GAN Training Dynamics and Mode Collapse](notes/vol-02.md#l14-gan-training-dynamics-and-mode-collapse) | Training challenges |
| **L15** | [DCGAN Architecture and Design Principles](notes/vol-02.md#l15-dcgan-architecture-and-design-principles) | Deep convolutional GANs |

---

## Week 6 — Advanced GAN Variants

*NPTEL videos: ~7 lectures · Official week theme: cGAN, CycleGAN, Pix2Pix, StyleGAN/StyleGAN2, evaluation metrics*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L16** | [Conditional GAN and Pix2Pix](notes/vol-02.md#l16-conditional-gan-and-pix2pix) | Supervised image translation |
| **L17** | [CycleGAN and Unpaired Image Translation](notes/vol-02.md#l17-cyclegan-and-unpaired-image-translation) | Cycle consistency |
| **L18** | [StyleGAN and GAN Evaluation Metrics](notes/vol-02.md#l18-stylegan-and-gan-evaluation-metrics) | FID, IS, precision/recall |

---

## Week 7 — Diffusion Models

*NPTEL videos: ~6 lectures · Official week theme: Forward diffusion process, variance schedules, noise prediction*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L19** | [Forward Diffusion Process and Noise Schedules](notes/vol-03.md#l19-forward-diffusion-process-and-noise-schedules) | Forward process |
| **L20** | [Score-Based Models and Denoising Objectives](notes/vol-03.md#l20-score-based-models-and-denoising-objectives) | Score matching |
| **L21** | [DDPM: Reverse Diffusion Formulation](notes/vol-03.md#l21-ddpm-reverse-diffusion-formulation) | DDPM derivation |

---

## Week 8 — Reverse Diffusion, U-Net, and Training

*NPTEL videos: ~6 lectures · Official week theme: DDPM pipeline, classifier guidance*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L22** | [U-Net Architecture for Diffusion Models](notes/vol-03.md#l22-u-net-architecture-for-diffusion-models) | U-Net for denoising |
| **L23** | [DDPM Training Pipeline](notes/vol-03.md#l23-ddpm-training-pipeline) | Training and sampling |
| **L24** | [Classifier Guidance and Conditional Diffusion](notes/vol-03.md#l24-classifier-guidance-and-conditional-diffusion) | Guided generation |

---

## Week 9 — Sequence Models, NLP, and LSTMs

*NPTEL videos: ~6 lectures · Official week theme: RNNs, LSTMs, motivation for Transformers*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L25** | [Sequence Models, RNNs, and Backpropagation Through Time](notes/vol-03.md#l25-sequence-models-rnns-and-backpropagation-through-time) | RNN fundamentals |
| **L26** | [LSTMs, GRUs, and Sequence-to-Sequence](notes/vol-03.md#l26-lstms-grus-and-sequence-to-sequence) | Long-range dependencies |
| **L27** | [Motivation for Transformers and Attention Mechanisms](notes/vol-03.md#l27-motivation-for-transformers-and-attention-mechanisms) | Attention preview |

---

## Week 10 — Foundations of LLMs and Prompt Engineering

*Proposed lectures L28–L30 · Official week theme: Transformer architecture, self-attention, tokenization*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L28** | [Transformer Architecture and Self-Attention](notes/vol-04.md#l28-transformer-architecture-and-self-attention) | Transformer blocks |
| **L29** | [Tokenization, Embeddings, and Positional Encoding](notes/vol-04.md#l29-tokenization-embeddings-and-positional-encoding) | Input representation |
| **L30** | [Prompt Engineering and In-Context Learning](notes/vol-04.md#l30-prompt-engineering-and-in-context-learning) | Prompting strategies |

---

## Week 11 — Retrieval-Augmented Generation (RAG)

*Proposed lectures L31–L33 · Official week theme: Retrieval and generation, in-context learning, LoRA*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L31** | [Retrieval-Augmented Generation Architecture](notes/vol-04.md#l31-retrieval-augmented-generation-architecture) | RAG pipeline |
| **L32** | [Vector Databases and Document Chunking](notes/vol-04.md#l32-vector-databases-and-document-chunking) | Retrieval infrastructure |
| **L33** | [Fine-Tuning with LoRA and Parameter-Efficient Methods](notes/vol-04.md#l33-fine-tuning-with-lora-and-parameter-efficient-methods) | PEFT / LoRA |

---

## Week 12 — LLM Capabilities, Multimodal AI, and Ethics

*Proposed lectures L34–L36 · Official week theme: Bias, fairness, hallucinations, safety, evaluation*

| Lecture | Title | NPTEL alignment |
|---------|-------|-----------------|
| **L34** | [Multimodal AI: Vision-Language Models](notes/vol-04.md#l34-multimodal-ai-vision-language-models) | CLIP, multimodal LLMs |
| **L35** | [LLM Evaluation, Hallucinations, and Safety](notes/vol-04.md#l35-llm-evaluation-hallucinations-and-safety) | Evaluation benchmarks |
| **L36** | [Bias, Fairness, and Ethics in Generative AI](notes/vol-04.md#l36-bias-fairness-and-ethics-in-generative-ai) | Responsible AI |

---

## Volume cross-reference

| Volume | Lectures | File |
|--------|----------|------|
| Vol. 01 | L01–L09 | [notes/vol-01.md](notes/vol-01.md) |
| Vol. 02 | L10–L18 | [notes/vol-02.md](notes/vol-02.md) |
| Vol. 03 | L19–L27 | [notes/vol-03.md](notes/vol-03.md) |
| Vol. 04 | L28–L36 | [notes/vol-04.md](notes/vol-04.md) |
