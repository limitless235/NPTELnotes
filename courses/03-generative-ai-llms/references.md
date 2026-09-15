# References — Fundamentals of Generative AI and LLMs

## Primary textbooks

1. **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press.  
   [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)  
   Chapters 2 (linear algebra), 3 (probability), 5–9 (deep learning fundamentals), 13 (linear factor models), 20 (deep generative models).

2. **Zhang, A., Lipton, Z. C., Li, M., & Smola, A. J.** (2023). *Dive into Deep Learning* (2nd ed.).  
   [https://d2l.ai/](https://d2l.ai/)  
   Chapters on preliminaries, CNNs, RNNs, attention, transformers, and optimization.

3. **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer.  
   Chapters 1–2 (probability), 8 (graphical models), 9 (mixture models), 10 (variational inference).

4. **Murphy, K. P.** (2022). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.  
   Chapters on VAEs, GANs, diffusion models, and sequence models.

## Generative models — seminal papers

| Topic | Paper | Year |
|-------|-------|------|
| Autoencoders | Hinton, G. E., & Salakhutdinov, R. *Reducing the Dimensionality of Data with Neural Networks.* Science. | 2006 |
| VAE | Kingma, D. P., & Welling, M. *Auto-Encoding Variational Bayes.* ICLR. | 2014 |
| β-VAE | Higgins, I., et al. *β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework.* ICLR. | 2017 |
| GAN | Goodfellow, I., et al. *Generative Adversarial Nets.* NeurIPS. | 2014 |
| DCGAN | Radford, A., Metz, L., & Chintala, S. *Unsupervised Representation Learning with Deep Convolutional GANs.* ICLR. | 2016 |
| CycleGAN | Zhu, J.-Y., et al. *Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.* ICCV. | 2017 |
| StyleGAN | Karras, T., et al. *A Style-Based Generator Architecture for GANs.* CVPR. | 2019 |
| DDPM | Ho, J., Jain, A., & Abbeel, P. *Denoising Diffusion Probabilistic Models.* NeurIPS. | 2020 |
| Score-based | Song, Y., & Ermon, S. *Generative Modeling by Estimating Gradients of the Data Distribution.* NeurIPS. | 2019 |
| Transformer | Vaswani, A., et al. *Attention Is All You Need.* NeurIPS. | 2017 |
| BERT | Devlin, J., et al. *BERT: Pre-training of Deep Bidirectional Transformers.* NAACL. | 2019 |
| GPT-3 | Brown, T., et al. *Language Models are Few-Shot Learners.* NeurIPS. | 2020 |
| RAG | Lewis, P., et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS. | 2020 |
| LoRA | Hu, E. J., et al. *LoRA: Low-Rank Adaptation of Large Language Models.* ICLR. | 2022 |
| CLIP | Radford, A., et al. *Learning Transferable Visual Models From Natural Language Supervision.* ICML. | 2021 |

## Large language models

5. **Jurafsky, D., & Martin, J. H.** (2025). *Speech and Language Processing* (3rd ed. draft).  
   [https://web.stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/)  
   Chapters on neural networks, RNNs, transformers, and pre-trained models.

6. **Raschka, S., Liu, Y., & Mirjalili, V.** (2022). *Machine Learning with PyTorch and Scikit-Learn*. Packt.  
   Practical implementations of CNNs, RNNs, and transformers.

## Ethics and safety

7. **Bender, E. M., et al.** (2021). *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* FAccT.

8. **Weidinger, L., et al.** (2022). *Taxonomy of Risks posed by Language Models.* FAccT.

9. **NIST AI Risk Management Framework** (2023).  
   [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)

## Online resources

- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — line-by-line transformer walkthrough
- [Lil'Log: The Transformer Family](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/)
- [Hugging Face Course](https://huggingface.co/learn/nlp-course) — practical NLP and transformers
- [Diffusion Models: A Comprehensive Survey](https://arxiv.org/abs/2209.00796) — Yang et al., 2023

## Mathematical supplements

- **Cover, T. M., & Thomas, J. A.** *Elements of Information Theory.* — entropy, KL divergence, rate-distortion.
- **Boyd, S., & Vandenberghe, L.** *Convex Optimization.* — for understanding ELBO optimization and GAN dynamics.
