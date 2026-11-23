# Generative AI & LLMs — Worked Numericals

> NPTEL / SWAYAM GenAI · companion to exam-kept weeks (1, 2, 3, 5, 7, 9, 10, 11)  
> About **half the paper is numerical**. This pack is for **formulas + step-by-step solves**.

---

## Coverage check (your 5 sets)

| Your set | Course match | Exam weeks |
|----------|--------------|------------|
| **1. Optimizers** — SGD, AdaGrad | Yes (L03–L04). Also know momentum / RMSProp / Adam briefly | Week 1 |
| **2. Convolution** — feature map + size | Yes (L05). Also pooling size (L06) | Week 1 |
| **3. VAE** — μ, log-σ², reparam, recon, KL | Yes (L24). AE forward (L16) is the warm-up | Weeks 2–3 |
| **4. DDPM** — forward, closed-form, reverse, loss | Yes (L46–L47) | Week 7 |
| **5. Self-attention** — scores, scale, softmax, output | Yes (L56). PE numerical is also examinable (L57) | Weeks 10–11 |

**Verdict:** Your five sets are the **core exam numericals**. This PDF covers all five with worked numbers, plus three short extras that still appear in kept weeks: **AE forward**, **pooling size**, **positional encoding**.

**Not needed for the kept-week map** (dropped weeks 4 / 6 / 8 / 12): CVAE / β-VAE interpolation arithmetic, U-Net sinusoidal time-embedding demo ($T=100$, $d=8$), and similar deleted-week drills.

---

## How to use

1. Memorize the **cheat sheet** first (one page of formulas).  
2. For each set: read **formula → steps → worked example → exam lines**.  
3. Re-do every arithmetic block with a blank sheet until you can finish without looking.

---

# Formula cheat sheet (memorize)

### Optimizers


$$
W_{\text{new}} = W_{\text{old}} - \eta\, g_t
\quad\text{(SGD)}
$$



$$
\alpha_t = \alpha_{t-1} + g_t^2,\qquad
W_{\text{new}} = W_{\text{old}} - \frac{\eta}{\sqrt{\alpha_t+\varepsilon}}\, g_t
\quad\text{(AdaGrad)}
$$



$$
v_t = \beta\, v_{t-1} + (1-\beta)\, g_t,\qquad
W_{\text{new}} = W_{\text{old}} - \eta\, v_t
\quad\text{(momentum)}
$$



$$
s_t = \beta\, s_{t-1} + (1-\beta)\, g_t^2,\qquad
W_{\text{new}} = W_{\text{old}} - \frac{\eta}{\sqrt{s_t+\varepsilon}}\, g_t
\quad\text{(RMSProp)}
$$


Adam = **momentum** ($\beta_1$ on $g_t$) + **RMSProp** ($\beta_2$ on $g_t^2$).

### Convolution / pooling size


$$
\text{out} = \left\lfloor\frac{n+2p-f}{s}\right\rfloor + 1
$$


### VAE


$$
\sigma^2 = e^{\log\sigma^2},\quad
\sigma=\sqrt{\sigma^2},\quad
z=\mu+\sigma\,\varepsilon,\quad \varepsilon\sim\mathcal{N}(0,1)
$$



$$
L_{\text{recon}}=\mathrm{MSE}(x,\hat x),\qquad
D_{\mathrm{KL}}=\frac12\sum_j\bigl(\mu_j^2+\sigma_j^2-1-\log\sigma_j^2\bigr)
$$



$$
L = L_{\text{recon}} + D_{\mathrm{KL}}
$$


### DDPM


$$
\alpha_t=1-\beta_t,\qquad
\bar\alpha_t=\prod_{s=1}^{t}\alpha_s
$$



$$
x_t=\sqrt{\alpha_t}\,x_{t-1}+\sqrt{1-\alpha_t}\,\varepsilon_t
$$



$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon
\quad\text{(closed form)}
$$



$$
\mu_\theta(x_t,t)=\frac{1}{\sqrt{\alpha_t}}\Bigl(x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\varepsilon_\theta(x_t,t)\Bigr)
$$



$$
L=\mathbb{E}\bigl\|\varepsilon-\varepsilon_\theta(x_t,t)\bigr\|^2
$$


### Self-attention + PE


$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\Bigl(\frac{QK^\top}{\sqrt{d_k}}\Bigr)V
$$



$$
\mathrm{PE}_{(\mathrm{pos},2i)}=\sin\!\Bigl(\frac{\mathrm{pos}}{10000^{2i/d}}\Bigr),\quad
\mathrm{PE}_{(\mathrm{pos},2i+1)}=\cos\!\Bigl(\frac{\mathrm{pos}}{10000^{2i/d}}\Bigr)
$$


---

# Set 1 — Optimizers (SGD + AdaGrad)

## What the question wants

Given $W_{\text{old}}$, $\eta$, and gradient(s), compute the **new weight**. For AdaGrad, also update the **squared-gradient accumulator**.

## Formulas

**SGD (plain):**


$$
W_{\text{new}} = W_{\text{old}} - \eta\, g_t
$$


Minus sign = move **opposite** the gradient (descent).

**AdaGrad:**

1. Accumulate squares: $\alpha_t=\alpha_{t-1}+g_t^2$ (often $\alpha_0=0$).  
2. Adaptive rate: $\eta_t=\eta/\sqrt{\alpha_t+\varepsilon}$.  
3. Update: $W_{\text{new}}=W_{\text{old}}-\eta_t\, g_t$.

Large past $|g|$ ⇒ large $\alpha$ ⇒ **smaller** step. Small past $|g|$ ⇒ **larger** step.

## Worked example A — SGD sign flip

**Given:** $W_{\text{old}}=5$, $\eta=0.1$.

| $g_t$ | Arithmetic | $W_{\text{new}}$ | Meaning |
|--------:|------------|-------------------:|---------|
| $-2$ | $5-0.1(-2)=5.2$ | **5.2** | negative grad → weight **up** |
| $+2$ | $5-0.1(2)=4.8$ | **4.8** | positive grad → weight **down** |

**Steps to repeat in the exam**

1. Write $W_{\text{new}}=W_{\text{old}}-\eta g$.  
2. Substitute numbers carefully with the sign of $g$.  
3. State whether $W$ increased or decreased.

## Worked example B — AdaGrad two steps

**Given:** $W_0=4$, $\eta=0.5$, $\varepsilon=0$ for hand calc, $\alpha_0=0$.  
Gradients: $g_1=2$, $g_2=1$.

**Step $t=1$**


$$
\alpha_1=0+2^2=4,\qquad
\eta_1=\frac{0.5}{\sqrt{4}}=0.25,\qquad
W_1=4-0.25\cdot 2=3.5
$$


**Step $t=2$**


$$
\alpha_2=4+1^2=5,\qquad
\eta_2=\frac{0.5}{\sqrt{5}}\approx 0.2236,\qquad
W_2=3.5-0.2236\cdot 1\approx 3.276
$$


Notice $\eta_2<\eta_1$: the accumulator grew, so AdaGrad **slowed** the step.

## Also know (same week) — momentum / RMSProp / Adam

**Momentum** ($\beta=0.9$, $v_0=0$):

| $t$ | $g_t$ | $v_t=0.9\,v_{t-1}+0.1\,g_t$ |
|------:|--------:|-------------------------------:|
| 1 | 5 | $0.1\cdot 5=0.5$ |
| 2 | 6 | $0.9\cdot 0.5+0.6=1.05$ |
| 3 | 7 | $0.9\cdot 1.05+0.7=1.645$ |

Same-direction grads ⇒ velocity **grows** ⇒ larger effective steps.  
If $g_4=-4$: $v_4=0.9\cdot 1.645+0.1(-4)\approx 1.08$ (damped, not a snap reverse).

**RMSProp:** replace AdaGrad’s sum $\alpha$ by EWMA of squares $s_t=\beta s_{t-1}+(1-\beta)g_t^2$ so the rate does not die forever.

**Adam:** momentum numerator + RMSProp denominator ($\beta_1,\beta_2$).

## Exam lines

- SGD: $W\leftarrow W-\eta g$; minus = descent.  
- AdaGrad: divide $\eta$ by $\sqrt{\sum g^2+\varepsilon}$; rate can **vanish** as the sum grows.  
- Momentum averages $g$; RMSProp averages $g^2$; Adam does **both**.

---

# Set 2 — Convolution (feature map + dimensions)

## What the question wants

1. Compute one feature-map **entry** (element-wise multiply + sum).  
2. Compute the **output height/width** from $n,f,p,s$.

## Formulas

**One entry:** place $f\times f$ kernel on a patch → multiply pairwise → **sum** → write that scalar into the map.

**Size (memorize this one):**


$$
\left\lfloor\frac{n+2p-f}{s}\right\rfloor + 1
$$


Special cases:

- No pad, stride 1: $n-f+1$.  
- “Same” size with $s=1$: choose $p$ so $n+2p-f+1=n$ ⇒ $p=(f-1)/2$ (e.g. $f=3\Rightarrow p=1$).

## Worked example A — size drills

| $n$ | $f$ | $p$ | $s$ | Calculation | Out |
|------:|------:|------:|------:|-------------|----:|
| 6 | 3 | 0 | 1 | $6-3+1$ | **4** |
| 6 | 3 | 1 | 1 | $6+2-3+1$ | **6** (same) |
| 7 | 3 | 0 | 1 | $(7-3)/1+1$ | **5** |
| 7 | 3 | 0 | 2 | $(7-3)/2+1=3$ | **3** |
| 5 | 3 | 0 | 2 | $\lfloor(5-3)/2\rfloor+1=\lfloor 1\rfloor+1$ | **2** |

## Worked example B — one convolution entry

**Patch** $3\times 3$ and **kernel** $3\times 3$:


$$
\text{patch}=
\begin{bmatrix}1&2&0\\2&1&1\\0&1&2\end{bmatrix},
\quad
\text{kernel}=
\begin{bmatrix}1&0&-1\\1&0&-1\\1&0&-1\end{bmatrix}
$$


**Step-by-step**

1. Element-wise products:  
   $1\cdot 1=1$, $2\cdot 0=0$, $0\cdot(-1)=0$,  
   $2\cdot 1=2$, $1\cdot 0=0$, $1\cdot(-1)=-1$,  
   $0\cdot 1=0$, $1\cdot 0=0$, $2\cdot(-1)=-2$.  
2. Sum: $1+0+0+2+0-1+0+0-2=\mathbf{0}$.  
3. Write **0** into that cell of the feature map.

Slide the kernel by stride $s$ and repeat. With $n=6$, $f=3$, $s=1$, $p=0$ you fill a **$4\times 4$** map (16 such multiply-and-sums).

## Worked example C — many kernels

Input $64\times 64\times 1$, **32** kernels of $3\times 3$, padding same, stride 1:

- Spatial size stays $64\times 64$.  
- Depth = number of kernels = **32**.  
- Output tensor: $64\times 64\times 32$.

## Exam lines

- Feature map entry = **multiply-and-sum** under the kernel.  
- Size $\lfloor(n+2p-f)/s\rfloor+1$; floor if not integer.  
- More kernels ⇒ more feature maps (depth), not a bigger spatial grid by itself.

---

# Set 3 — VAE (full forward + loss)

## What the question wants

Walk $x$ → encoder hidden → $\mu$, $\log\sigma^2$ → $\sigma$ → $z=\mu+\sigma\varepsilon$ → decoder → $\hat x$ → $L_{\text{recon}}+D_{\mathrm{KL}}$.

## Formulas / activation rules

| Stage | Activation |
|-------|------------|
| Encoder / decoder hidden | **ReLU** $\max(0,h)$ |
| Mean head $\mu$ | **None** (negative mean is valid) |
| Log-variance head | **None** |
| Continuous $\hat x$ | **Linear** (identity) |
| Binary / $[0,1]$ $\hat x$ | **Sigmoid** |


$$
\sigma_j^2=e^{\log\sigma_j^2},\quad
\sigma_j=\sqrt{\sigma_j^2},\quad
z_j=\mu_j+\sigma_j\varepsilon_j
$$



$$
L_{\text{recon}}=\frac1d\sum_{i=1}^{d}(x_i-\hat x_i)^2
$$



$$
D_{\mathrm{KL}}=\frac12\sum_{j=1}^{k}\bigl(\mu_j^2+\sigma_j^2-1-\log\sigma_j^2\bigr)
$$



$$
L=L_{\text{recon}}+D_{\mathrm{KL}}
$$


## Worked example (lecture numbers — Iris-style $x$)

**Input:** $x=(5.1,\ 3.5,\ 1.4,\ 0.2)$. Latent dim $k=2$.

### Step 1 — encoder hidden (ReLU)

Spoken pre-activations after weighted sums: $h=(1.07,\ 1.93,\ 0.87)$. All positive ⇒


$$
a=(1.07,\ 1.93,\ 0.87)
$$


### Step 2 — mean head (no activation)


$$
\mu_1=1.07\cdot 0.5+1.93\cdot(-0.3)+0.87\cdot 0.1=0.043
$$



$$
\mu_2=1.07\cdot 0.2+1.93\cdot 0.4+0.87\cdot(-0.5)=0.551
$$



$$
\mu=(0.043,\ 0.551)
$$


### Step 3 — log-variance → σ


$$
\log\sigma_1^2=0.732,\quad\log\sigma_2^2=0.302
$$


| $j$ | $\log\sigma_j^2$ | $\sigma_j^2=e^{\cdot}$ | $\sigma_j$ |
|------:|-------------------:|--------------------------:|-------------:|
| 1 | 0.732 | $\approx 2.079$ | **1.442** |
| 2 | 0.302 | $\approx 1.353$ | $\approx 1.163$ |

### Step 4 — reparameterization

Given $\varepsilon=(0.5,\ -0.2)$:


$$
z_1=0.043+1.442\cdot 0.5=0.764
$$



$$
z_2=0.551+1.163\cdot(-0.2)\approx 0.318
$$



$$
z=(0.764,\ 0.318)
$$


Same $x$ (hence same $\mu,\sigma$), **new $\varepsilon$** ⇒ new $z$. That is the “many latents per $x$” claim.

### Step 5 — decoder hidden (ReLU)


$$
\begin{aligned}
h_1&=0.764\cdot 0.6+0.318\cdot 0.3+0.1=0.6538 &&\Rightarrow a_1=0.6538\\
h_2&=0.764\cdot(-0.4)+0.318\cdot 0.1+0.1=-0.1738 &&\Rightarrow a_2=0\\
h_3&=0.764\cdot 0.2+0.318\cdot(-0.5)+0.1=0.0938 &&\Rightarrow a_3=0.0938
\end{aligned}
$$


### Step 6 — reconstruction (linear)

One coordinate shown:


$$
\hat x_1=0.6538\cdot 0.2+0\cdot 0.1+0.0938\cdot(-0.3)=0.10262
$$


(Other $\hat x_i$ same pattern; lecture then uses the rounded $\hat x$ vector.)

### Step 7 — reconstruction loss


$$
L_{\text{recon}}=9.7111
$$


(MSE over the 4 coordinates with the slide’s $\hat x$.)

### Step 8 — KL (closed form)


$$
\begin{aligned}
\mu_1^2+\sigma_1^2-1-\log\sigma_1^2
&\approx 0.001849+2.079-1-0.732=0.3488\\
\mu_2^2+\sigma_2^2-1-\log\sigma_2^2
&\approx 0.3036+1.353-1-0.302=0.3546
\end{aligned}
$$



$$
D_{\mathrm{KL}}=\frac12(0.3488+0.3546)\approx 0.3517\to\mathbf{0.352}
$$


### Step 9 — total loss


$$
L=9.7111+0.352=\mathbf{10.0631}
$$


High because weights were **random**. Training would now backprop and update every weight/bias.

## Exam lines

- Emit **log-variance**, then $e^{(\cdot)}$ for $\sigma^2$.  
- Always $z=\mu+\sigma\varepsilon$ (reparam) — do **not** sample $z\sim\mathcal{N}(\mu,\sigma^2)$ as a black box for backprop.  
- No ReLU on $\mu$ / log-σ².  
- $L=\mathrm{MSE}+\mathrm{KL}$ for continuous data in this course.

---

# Set 4 — DDPM (forward, closed form, reverse, loss)

## What the question wants

Translate between $\beta_t$, $\alpha_t$, $\bar\alpha_t$; write one-step and closed-form $x_t$; write reverse mean using $\varepsilon_\theta$; state the training loss.

## Formulas


$$
\alpha_t=1-\beta_t,\qquad
\bar\alpha_t=\prod_{s=1}^{t}\alpha_s
$$


**One-step forward:**


$$
q(x_t\mid x_{t-1})=\mathcal{N}\bigl(\sqrt{\alpha_t}\,x_{t-1},\,(1-\alpha_t)I\bigr)
$$



$$
x_t=\sqrt{\alpha_t}\,x_{t-1}+\sqrt{1-\alpha_t}\,\varepsilon_t,\quad\varepsilon_t\sim\mathcal{N}(0,I)
$$


**Closed form (memorize):**


$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\varepsilon
$$


**Why $\sqrt{\alpha_t}$ on the signal?** Without it, variance **accumulates** every step and the law blows up.

**Reverse mean (no $x_0$ at generation time):**


$$
\mu_\theta(x_t,t)=\frac{1}{\sqrt{\alpha_t}}\left(
x_t-\frac{\beta_t}{\sqrt{1-\bar\alpha_t}}\,\varepsilon_\theta(x_t,t)
\right)
$$



$$
x_{t-1}=\mu_\theta(x_t,t)+\sigma_t z,\quad z\sim\mathcal{N}(0,I)
$$


**Training loss (noise prediction):**


$$
L=\mathbb{E}_{x_0,\varepsilon,t}\bigl\|\varepsilon-\varepsilon_\theta(x_t,t)\bigr\|^2
$$


## Worked example A — schedule numbers

Suppose $\beta_1=0.1$, $\beta_2=0.2$.


$$
\alpha_1=0.9,\quad\alpha_2=0.8,\quad
\bar\alpha_1=0.9,\quad
\bar\alpha_2=0.9\cdot 0.8=0.72
$$


Closed-form coefficients at $t=2$:


$$
\sqrt{\bar\alpha_2}=\sqrt{0.72}\approx 0.849,\qquad
\sqrt{1-\bar\alpha_2}=\sqrt{0.28}\approx 0.529
$$


So


$$
x_2\approx 0.849\,x_0+0.529\,\varepsilon
$$


## Worked example B — one-shot vs walk

To get $x_{99}$ you do **not** need 99 Markov steps in training if you know $x_0$ and $\bar\alpha_{99}$:


$$
x_{99}=\sqrt{\bar\alpha_{99}}\,x_0+\sqrt{1-\bar\alpha_{99}}\,\varepsilon
$$


That is why DDPM training is cheap: sample $t$, build $x_t$ in **one shot**, predict noise.

## Worked example C — reverse / loss story (exam narrative)

1. Forward $q$ is **fixed** (known $\beta$ schedule).  
2. Ideal reverse posterior mean $\tilde\mu_t$ needs **$x_0$** — unavailable at generation.  
3. Invert $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\varepsilon$ for $x_0$, substitute, replace $\varepsilon$ by network $\varepsilon_\theta$.  
4. Train with MSE between true $\varepsilon$ and $\varepsilon_\theta(x_t,t)$.

## Exam lines

- $\alpha=1-\beta$, $\bar\alpha=$ product of $\alpha$s.  
- Closed form: $x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\varepsilon$.  
- Learn **noise** $\varepsilon_\theta$; loss is $\|\varepsilon-\varepsilon_\theta\|^2$.  
- Generation starts from $x_T\sim\mathcal{N}(0,I)$ and steps down with $\mu_\theta$.

---

# Set 5 — Self-attention (scores → softmax → output)

## What the question wants

From $Q,K,V$: compute scores $QK^\top$, **scale** by $\sqrt{d_k}$, **softmax** row-wise, multiply by $V$.

## Formulas


$$
Q=XW_Q,\quad K=XW_K,\quad V=XW_V
$$



$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$



$$
\mathrm{softmax}(z)_i=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$


Masked / causal: set future scores to $-\infty$ so $e^{-\infty}=0$.

## Worked example — tiny 2-token attention

**Given** ($d_k=2$):


$$
Q=\begin{bmatrix}1&0\\0&1\end{bmatrix},
\quad
K=\begin{bmatrix}1&0\\1&1\end{bmatrix},
\quad
V=\begin{bmatrix}1&2\\3&4\end{bmatrix}
$$


### Step 1 — raw scores $QK^\top$


$$
K^\top=\begin{bmatrix}1&1\\0&1\end{bmatrix},
\quad
QK^\top=\begin{bmatrix}1&1\\0&1\end{bmatrix}
$$


(Row 1: token 1 vs both keys → $[1,1]$. Row 2: token 2 → $[0,1]$.)

### Step 2 — scale by $\sqrt{d_k}=\sqrt{2}\approx 1.414$


$$
\frac{QK^\top}{\sqrt{2}}
\approx
\begin{bmatrix}0.707&0.707\\0&0.707\end{bmatrix}
$$


### Step 3 — softmax per row

**Row 1:** $e^{0.707}\approx 2.028$ for both → weights $[0.5,\ 0.5]$.

**Row 2:** $e^{0}=1$, $e^{0.707}\approx 2.028$ → sum $3.028$ → weights


$$
\bigl[\tfrac{1}{3.028},\ \tfrac{2.028}{3.028}\bigr]\approx [0.330,\ 0.670]
$$


Attention weight matrix:


$$
A\approx\begin{bmatrix}0.500&0.500\\0.330&0.670\end{bmatrix}
$$


### Step 4 — multiply by $V$


$$
AV\approx
\begin{bmatrix}
0.5\cdot 1+0.5\cdot 3 & 0.5\cdot 2+0.5\cdot 4\\
0.330\cdot 1+0.670\cdot 3 & 0.330\cdot 2+0.670\cdot 4
\end{bmatrix}
=
\begin{bmatrix}2.00&3.00\\2.34&3.34\end{bmatrix}
$$


That matrix is the **attention output** (one row per query token).

## Multi-head (conceptual numerical)

Heads run the same four steps with **different** $W_Q,W_K,W_V$, then **concat** head outputs and apply a final linear layer.

## Exam lines

- Must scale by $\sqrt{d_k}$ before softmax.  
- Softmax is **row-wise** (each query distributes mass over keys).  
- Mask: future → $-\infty$ → weight $0$.  
- Output = weighted sum of **values**.

---

# Extra A — Autoencoder forward (Week 2 warm-up)

Same multiply–add–ReLU pattern as VAE encoder, but latent is a **deterministic** code (no $\mu/\sigma/\varepsilon$).

**Architecture:** $5\to 4\to 3\to 4\to 5$.  
**Input:** $x=(0.8,\ 0.4,\ 0.6,\ 0.2,\ 0.5)$.  
Hidden: **ReLU**. Output: **linear** + **MSE**.

First encoder neuron (weights $0.2,0.5,0.4,0.3,0.1$, bias $0.01$):


$$
\begin{aligned}
z_1&=0.8\cdot 0.2+0.4\cdot 0.5+0.6\cdot 0.4+0.2\cdot 0.3+0.5\cdot 0.1+0.01\\
&=0.16+0.20+0.24+0.06+0.05+0.01=0.72
\end{aligned}
$$



$$
a_1=\max(0,0.72)=0.72
$$


After four hidden units the lecture has $(0.72,\ 0.65,\ 0.66,\ 0.77)$. Continue the same way to the 3-D latent, then decode to $\hat x$, then MSE.

**Exam line:** AE = reconstruct with MSE; VAE adds **stochastic $z$** + **KL**.

---

# Extra B — Pooling output size (Week 1)

Same size idea as conv:


$$
\left(\frac{n_H-F}{S}+1\right)\times(\text{same for }W)\times D
$$


Example: $5\times 5\times 1$ map, pool window $3\times 3$, stride $1$:


$$
\frac{5-3}{1}+1=3\to 3\times 3\times 1
$$


Max-pool $2\times 2$, stride $2$ on $7\times 7$ → $4\times 4$ (lecture: diagonal feature still visible).

---

# Extra C — Positional encoding (Week 10)


$$
\mathrm{PE}_{(\mathrm{pos},2i)}=\sin\!\Bigl(\frac{\mathrm{pos}}{10000^{2i/d_{\mathrm{model}}}}\Bigr),\quad
\mathrm{PE}_{(\mathrm{pos},2i+1)}=\cos\!\Bigl(\frac{\mathrm{pos}}{10000^{2i/d_{\mathrm{model}}}}\Bigr)
$$


**Toy:** sentence *the cat sat on the mat*, $d_{\mathrm{model}}=4$, token *sat* at $\mathrm{pos}=2$.

| Dim | Formula | Value |
|----:|---------|------:|
| 0 (even, $i=0$) | $\sin(2/10000^0)=\sin 2$ | **0.9093** |
| 1 (odd, $i=0$) | $\cos 2$ | **−0.4161** |
| 2 (even, $i=1$) | $\sin(2/100)=\sin 0.02$ | **0.0200** |
| 3 (odd, $i=1$) | $\cos 0.02$ | **0.9998** |

Final input embedding = **token embedding + PE** (element-wise add).

---

# Quick self-test (cover answers)

1. $W=3$, $\eta=0.2$, $g=-4$. New $W$?  
2. $n=8$, $f=3$, $p=1$, $s=2$. Feature-map side length?  
3. $\mu=0.2$, $\sigma=0.5$, $\varepsilon=-1$. What is $z$?  
4. $\beta=0.3$. What is $\alpha$? If also $\alpha_1=0.9$, what is $\bar\alpha_2$?  
5. Why divide attention scores by $\sqrt{d_k}$?  
6. PE for even dim uses **sin** or **cos**?

**Answers:**  
1. $3-0.2(-4)=3.8$.  
2. $\lfloor(8+2-3)/2\rfloor+1=\lfloor 3.5\rfloor+1=4$.  
3. $z=0.2+0.5(-1)=-0.3$.  
4. $\alpha=0.7$; $\bar\alpha_2=0.9\cdot 0.7=0.63$.  
5. Keeps softmax from saturating when dot products grow with dimension.  
6. **Sin** on even ($2i$); **cos** on odd ($2i+1$).

---

# One-page exam drill order

1. Write the formula **before** plugging numbers.  
2. Track signs (SGD minus; VAE ReLU zeros; attention mask $-\infty$).  
3. For VAE/DDPM, name **each intermediate** ($\mu,\log\sigma^2,\sigma,z$ / $\alpha,\bar\alpha,x_t,\varepsilon_\theta$).  
4. Box the final numeric answer.

Good luck — if you can redo Sets 1–5 cold, you have the numerical half of the GenAI paper.
