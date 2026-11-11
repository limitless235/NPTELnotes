# Volume 05 — Diffusion (L44–L53)

> Generative AI & LLMs · NPTEL · Generative AI / LLMs
> **notes-3** — concept exam notes (definitions & what things do). Breadth over lab depth.

---

## L44: Introduction to diffusion models

### Learning focus
- Place diffusion after autoencoders, VAEs, and GANs on the course timeline, including the **stability vs. quality** gap it was meant to close.
- Read a **probability landscape**: high-$p$ peaks = realistic images, low-$p$ valleys = noise, and why a model needs a **compass** (local next-step choices).
- Contrast a **fixed forward** noising chain with a **learned reverse** denoising chain, and sketch training vs. inference.
- State the **Markov** property used for both chains (snakes-and-ladders example).

### Exam lines
- Diffusion = many easy Markov steps instead of one intractable map from noise to data.
- Forward is **fixed** Gaussian corruption; reverse is the **learned** denoiser.
- High probability ↔ structure; low probability ↔ noise; generation is climbing with a local rule $p_t(x)$.
- The net is trained to predict **noise**, then used at inference to denoise $x_T\sim\mathcal{N}(0,I)$ down to an image.

### Concept tables
| Year (as taught) | Model | What it did | Limitation named here |
|------------------|-------|-------------|------------------------|
| **1987** | Autoencoder | Compress to a latent, **reconstruct** the input (zip / unzip a folder) | **Cannot** emit realistic **new** images; used for denoising, anomaly spotting, feature extraction, scratch restoration |
| **2013** | VAE | Latent is a **Gaussian** $(\mu,\sigma)$, not a single point | **Can** make variants (ship with different sky / water / hull color) but images are often **blurry**, not high-res |
| **2015** | GAN | High-quality fakes from **noise**; FaceApp (2017) and *This Person Does Not Exist* as GAN apps | **Mode collapse** (train on dogs/cats/horses/birds, emit only dogs) and **unstable** training |
| **2015** | Diffusion | Physics-style **diffusion** of probability | Designed to be **as stable as VAEs** and **as sharp as GANs** |
| Idea | Why it fails |
|------|----------------|
| Map **every image in the world** as a peak | Impossible |
| Memorize **known** rooms of “your house” | No help in an **unknown house** (new images) |


---

## L45: Mathematics of diffusion models

### Learning focus
- Write the **forward** kernel $q(x_t\mid x_{t-1})$ and the **reverse** kernel $p_\theta(x_{t-1}\mid x_t)$ as the lecture set them up.
- Explain the **noise variance schedule** $\beta_t$ and what goes wrong if destruction is too fast or too slow.
- Recall the **Gaussian** PDF, the **standard** Gaussian $\mathcal{N}(0,1)$, and why images need a **multivariate** Gaussian (covariance, not a scalar $\sigma^2$).
- Compute a $2\times2$ **covariance matrix** on the height–weight table (population $n$, not $n-1$).

### Exam lines
- $q$ noising is predefined Gaussian; $p_\theta$ denoising is the trainable Gaussian.
- $\beta_t$ is a **schedule**, not a constant, so $x_T$ is fully noise without making reverse learning impossible.
- Standard Gaussian = $\mathcal{N}(0,1)$; pixels need $\mathcal{N}(\mu,\Sigma)$.
- $\Sigma$’s diagonal is variance, off-diagonal is relationship; the $n=4$ height–weight example is the calculation you are expected to reproduce.

### Concept tables
| Symbol | Meaning |
|--------|---------|
| $x_0$ | original data (clean image / signal) |
| $x_t$ | noisy version at step $t$ |
| $T$ | total diffusion steps (can be **up to ~1000**, application-dependent) |
| $t\in\{1,\ldots,T\}$ | current step |
| | Forward | Reverse |
|--|---------|---------|
| Direction | clean → noise | noise → clean |
| Learning | none | $\theta$ |
| Typical letter | $q$ | $p_\theta$ |


---

## L46: DDPM — forward process

### Learning focus
- Identify **DDPM** as the 2020 Ho et al. (UC Berkeley) formulation of diffusion.
- Write the Markov forward kernel $q(x_t\mid x_{t-1})$ with mean $\sqrt{1-\beta_t}\,x_{t-1}$ and covariance $\beta_t I$.
- Show why the previous image must be **scaled** (unscaled variance **blows up**).
- Expand the recursion to the **closed-form** $q(x_t\mid x_0)$ and the **reparameterization** that samples any $t$ in one shot.

### Exam lines
- DDPM forward is a **fixed** Markov Gaussian: $q(x_t\mid x_{t-1})=\mathcal{N}(\sqrt{1-\beta_t}\,x_{t-1},\,\beta_t I)$.
- $\alpha_t=1-\beta_t$; samples $x_t=\sqrt{\alpha_t}\,x_{t-1}+\sqrt{1-\alpha_t}\,\varepsilon_t$.
- Skipping the $\sqrt{\alpha_t}$ scale makes variance **accumulate** until the law blows up.
- $\bar{\alpha}_t=\prod_s\alpha_s$ yields $q(x_t\mid x_0)=\mathcal{N}(\sqrt{\bar{\alpha}_t}\,x_0,\,(1-\bar{\alpha}_t)I)$ and the one-shot $x_t=\sqrt{\bar{\alpha}_t}\,x_0+\sqrt{1-\bar{\alpha}_t}\,\varepsilon$.

### Concept tables
| Forward | Reverse |
|---------|---------|
| Clean image → almost pure noise, step by step | Almost pure noise → clean image |
| **No learning**; predefined Gaussian | Learning lives here (next lecture) |
| Symbol | Meaning |
|--------|---------|
| $x_t$ | image at step $t$ |
| $x_{t-1}$ | image at step $t-1$ |
| $\beta_t$ | how much noise is added at $t$ (magnitude) |
| $I$ | identity matrix |


---

## L47: DDPM — reverse process

### Learning focus
- Write the reverse **Markov** joint $p_\theta(x_{0:T})$ from a Gaussian **prior** $x_T$.
- State the **forward posterior** $q(x_{t-1}\mid x_t,x_0)$ (mean $\tilde{\mu}_t$ depends on $x_0$ — unusable at generation).
- Eliminate $x_0$ using the forward reparameterization, replace $\varepsilon$ by $\varepsilon_\theta$, and sample $x_{t-1}$.
- Quote the **MSE noise-prediction** loss used to train DDPM.

### Exam lines
- Reverse joint = prior $x_T\sim\mathcal{N}(0,I)$ times Markov conditionals $p_\theta(x_{t-1}\mid x_t)$.
- $q(x_{t-1}\mid x_t,x_0)$ is Gaussian, but $\tilde{\mu}_t$ needs the **unknown** $x_0$ at sampling time.
- $\mu_\theta(x_t,t)=\frac{1}{\sqrt{\alpha_t}}\bigl(x_t-\frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\varepsilon_\theta(x_t,t)\bigr)$.
- $x_{t-1}=\mu_\theta+\sigma_t z$; train $\varepsilon_\theta$ with MSE vs true $\varepsilon$.

### Concept tables
| Factor | Meaning |
|--------|---------|
| $p_\theta(x_{0:T})$ | joint of the **entire reverse trajectory** |
| $p(x_T)$ | **prior** at the start of generation |
| $\prod p_\theta(x_{t-1}\mid x_t)$ | all reverse conditionals |
| $\theta$ | trainable weights |
| Term | Lecture meaning |
|------|-----------------|
| **Prior** | what you assume **before** extra evidence |
| **Posterior** | the law **after** observing more information |


---

## L48: Hands-on — forward diffusion process

### Learning focus
- Implement the DDPM **forward** kernel, $\alpha_t$, $\bar{\alpha}_t$, and **closed-form** $x_t$ from $x_0$.
- Compare **linear** vs **cosine** $\beta$-schedules ($T=1000$) on remaining signal and **SNR**.
- Show that **iterative Markov** noising and **one-shot** $q(x_t\mid x_0)$ match in **mean and std** (Monte Carlo).
- Train a small **time-conditioned CNN** on MNIST to predict $\varepsilon$, then reconstruct by **subtracting** predicted noise — and list what a full DDPM still needs.

### Exam lines
- Code $x_t=\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\varepsilon$ and the Markov one-step kernel; they match in Monte Carlo.
- $T=1000$; cosine $\beta$ beats linear on uniform signal decay and final SNR.
- Astronaut viz: linear is “done” by ~500; cosine fades evenly.
- MNIST CNN (~124k params, 12k/2k split) can drop $L_{\text{simple}}$ and roughly undo noise in one subtract — that is **not** yet a DDPM sampler.

### Concept tables
| Process | Path | Who learns |
|---------|------|------------|
| **Forward** | $x_0\to x_1\to\cdots\to x_T$ | nobody — add small Gaussians until noise |
| **Reverse** | $x_T\sim\mathcal{N}(0,I)$ toward $x_0$ | **neural net** |
| Schedule | Shape on the plot | Remaining signal $\bar{\alpha}_t$ |
|----------|-------------------|-------------------------------------|
| **Linear** | essentially **flat** $\beta_t \approx 1/1000$ | signal decays **slowly at first**, then **drops** |
| **Cosine** | $\beta_t$ **small at the start**, then **rises** | **more uniform** decline of original signal |


---

## L49: U-Net for denoising

### Learning focus
- Place **U-Net** in DDPM: input $(x_t,t)$ → predicted noise $\varepsilon_\theta(x_t,t)$.
- Contrast **Ronneberger** segmentation U-Net with the DDPM stack: **time embeddings**, **residual blocks**, **self-attention**.
- Compute a **sinusoidal** time embedding (the $T=100$, $d=8$ numerical example).
- Walk **encoder / bottleneck / decoder**, the residual-block algebra (GroupNorm, **SiLU**, time projection), and **QKV** attention.

### Exam lines
- U-Net is the DDPM denoiser: global structure + skips for fine detail.
- $\mathrm{TE}(t)$ uses $\sin/\cos$ of $t/10000^{2i/d}$; the $t=100$, $d=8$ vector is the exam-style drill.
- Residual path: GroupNorm → SiLU → conv → **add $W_t\mathrm{TE}(t)$** → GroupNorm → SiLU → conv → **$H+F(H)$**.
- Attention: $Q,K,V$ projections, softmax$(QK^\top/\sqrt{d})$, then $AV$, so far-apart structure (two eyes) can interact.

### Concept tables
| Part | Job |
|------|-----|
| **Encoder** (contracting) | downsample; spatial size shrinks; keep important information |
| **Bottleneck** | most **compressed** summary |
| **Decoder** (expanding) | upsample / reconstruct |
| **Skips** | **crop and concatenate** encoder features onto the matching decoder level so fine detail survives |
| Example $t$ | Typical look (as taught) |
|-------------|---------------------------|
| 50 | slightly noisy |
| 500 | moderately noisy |
| 900 | heavily noised |


---

## L50: Classifier-guided diffusion model

### Learning focus
- Explain why an unconditional DDPM cannot choose a class (dog vs cat vs flower).
- Describe the **artist + critic** pair: a denoising U-Net plus a **noisy-image classifier**.
- Reconstruct the Bayes / score derivation that turns a classifier gradient into a **guided noise** $\hat{\varepsilon}$.
- State the **guidance scale** $s$ trade-off (class precision vs diversity) and the sampling replacement rule.
- List the pipeline limitations that motivate classifier-free guidance in the next lecture.

### Exam lines
- Unconditional DDPM generates realistic images with **no class knob**.
- Classifier guidance adds a noisy-image critic; $\nabla_{x_t}\log p_\phi(y\mid x_t)$ steers denoising toward $y$.
- Bayes splits the conditional score into a **realism** term (U-Net $\varepsilon_\theta$) and a **class** term (classifier).
- Guided noise $\hat{\varepsilon}$ replaces $\varepsilon_\theta$ in the reverse update; $s$ trades **precision vs diversity**.
- Cost: a second network, noisy-label training, per-step gradients, and adversarial artifacts. Next lecture: **classifier-free** guidance.

### Concept tables
| Role | What it is | What it does |
|------|------------|--------------|
| **Artist** | Ordinary **unconditional** DDPM / U-Net | Denoises a noisy image toward something realistic. It does **not** know which class to emit. |
| **Critic** | A **classifier**, itself a pretrained network | Looks at the *noisy* image $x_t$ and predicts $p_\phi(y \mid x_t)$ over classes (cats, dogs, trees, houses, …). |
| $s$ | Class recognizability | Sample diversity |
|-----|------------------------|------------------|
| Small | Weak conditioning; images may not look like the target class | Higher diversity |
| Large | Strong, precise class (very “dog-like”) | Diversity **drops** |


---

## L51: Classifier-free diffusion models

### Learning focus
- Restate why classifier-guided diffusion is heavy (extra noisy classifier, no off-the-shelf ResNet).
- Explain **classifier-free guidance (CFG)**: one U-Net trained for **both** conditional and unconditional denoising.
- Write the CFG noise combination with guidance scale $s$.
- Contrast sampling cost: U-Net **+ classifier** vs **two U-Net passes**.

### Exam lines
- CFG exists to **delete the noisy classifier** while keeping class control.
- One U-Net, **joint** training: keep $y$ or replace it by null $\phi$ with fixed dropout probability.
- The old classifier gradient is rewritten as **conditional minus unconditional** diffusion scores.
- $\hat{\varepsilon}=(1+s)\varepsilon_\theta(x_t,t,y)-s\varepsilon_\theta(x_t,t,\phi)$; larger $s$ (paper demo $s=3$) sharpens class at some cost (saturation / diversity).
- Sampling trades classifier cost for **two U-Net evaluations**. Next lecture: **Stable Diffusion**.

### Concept tables
| Problem | Why it hurts |
|---------|----------------|
| Extra classifier | Must be trained **on noisy images** $x_t$ to supply $\nabla_{x_t}\log p(y\mid x_t)$ |
| No ImageNet ResNet | Off-the-shelf nets saw **clean** pixels, not $x_t$ |
| Two trainings | Unconditional DDPM **and** the classifier → slower, more complex pipeline |
| | **Classifier-guided** (Lec 50) | **Classifier-free (CFG)** |
|--|-------------------------------|---------------------------|
| Separate classifier | Yes | **No** (main advantage) |
| Noisy-classifier training | Yes | Not required |
| Where the guidance signal comes from | Classifier gradient $\nabla_{x_t}\log p_\phi(y\mid x_t)$ | **Difference** of conditional vs unconditional scores |
| Sampling-time cost | U-Net **plus** classifier, both run while generating | **Two U-Net passes** (conditional and unconditional) per step |


---

## L52: Stable Diffusion model

### Learning focus
- Motivate **latent** diffusion: why pixel-space DDPM on $512\times 512\times 3$ is too expensive.
- Separate **latent diffusion (LDM)** (the algorithm) from **Stable Diffusion** (text-to-image implementation).
- Trace the frozen autoencoder → noisy latent → U-Net → decoder pipeline and the latent-space MSE objective.
- Write **cross-attention** with $Q$ from U-Net maps and $K,V$ from a **CLIP** text encoder.
- Choose **concatenation vs cross-attention** from whether the condition has spatial structure.

### Exam lines
- LDM moves DDPM from pixels into a **frozen autoencoder’s latent** ($64\times 64\times 4$ vs $512\times 512\times 3$).
- Stable Diffusion **is** that algorithm plus **CLIP text embeddings** and **cross-attention** into the U-Net.
- Loss is DDPM’s noise MSE on **$z_t$**, not $x_t$.
- $Q$ from U-Net maps, $K$ and $V$ from $\tau_\theta(y)$; concat is for **spatial** conditions.
- Next in the playlist is the **reverse-diffusion lab**; the instructor also flags the coming shift to **NLP / transformers / LLMs**.

### Concept tables
| Name | What it is |
|------|------------|
| **Latent diffusion model (LDM)** | The **algorithm** in that paper |
| **Stable Diffusion** | A **practical** LDM implementation for **text-to-image**, with extra **conditioning** |
| Symbol | Meaning |
|--------|---------|
| $\varepsilon$ | Gaussian noise added in the **forward** process |
| $z_t$ | **Noisy latent** at time $t$ |
| $\varepsilon_\theta(z_t, t)$ | U-Net prediction — depends on **$z_t$ and $t$**, **not** on pixel $x_t$ |


---

## L53: Hands-on reverse diffusion process

### Learning focus
- Implement reverse DDPM sampling from $\mathcal{N}(0,I)$ with a **small class-conditional U-Net** on **MNIST**.
- Train with **$L_{\mathrm{simple}}$** (MSE on Gaussian noise) and **null-class dropout** for classifier-free guidance.
- Compare **guidance scales** and a tiny **quality classifier** on generated digits.
- Contrast diffusion vs **GAN** vs **VAE** using the lecture’s table (tendencies, not universal laws).

### Exam lines
- Reverse diffusion repeatedly maps noise toward data; a U-Net mixes global structure with skip-connection detail.
- Train by predicting known Gaussian noise with **MSE**; condition on **$t$** (noise level) and optionally **$y$**.
- Null-class dropout + $\varepsilon_{\mathrm{uncond}}+s(\varepsilon_{\mathrm{cond}}-\varepsilon_{\mathrm{uncond}})$ is **classifier-free** guidance. Moderate $s$ helps class adherence; excessive $s$ hurts diversity / adds artifacts.
- This classroom model **demonstrates the mechanism**; scale data, $T$, channels, and epochs to get convincing digits. That closes the diffusion hands-on pair (forward + reverse).

### Concept tables
| Setting | Value in the notebook |
|---------|------------------------|
| Time steps $T$ | **100** (`fast_mode=True`; set `False` to increase $T$) |
| $\beta$ schedule | **Linear**, $\beta$ from **0** to **0.02** |
| $\alpha_t$ | $1-\beta_t$ |
| Also computed | $\bar{\alpha}_t$, posterior variance |
| Split | Size |
|-------|------|
| Train | **12,000** |
| Validation | **2,000** |


---
