---
title: "Lec 35 Introduction to DCGAN"
video_id: XSSaV-FHW2E
index: 35
duration: 10:49
language: English (auto-generated)
playlist: https://www.youtube.com/playlist?list=PLgMDNELGJ1Ca_DduFvH6qfI1eapL48xOr
---

# Lec 35 Introduction to DCGAN

| | |
|---|---|
| **Lecture** | 35 / 63 + intro |
| **Duration** | 10:49 |
| **Captions** | English (auto-generated) |
| **Words** | 1,797 |
| **Video** | [XSSaV-FHW2E](https://www.youtube.com/watch?v=XSSaV-FHW2E) |
| **Playlist** | [Fundamentals of Generative AI and LLMs](https://www.youtube.com/playlist?list=PLgMDNELGJ1Ca_DduFvH6qfI1eapL48xOr) |

Auto-generated YouTube captions, lightly cleaned (removed `[music]` tags, grouped into paragraphs). These are **verbatim lecture captions**, not edited notes.

## Transcript

**[00:00]** Hello everyone. Welcome to the last of theory session of the week five. In the week five, we are dealing with the generative adversarial network foundations. So in week five till now, I think we have seen the limitations of variation autoencoders, which has given motivation for the GANs. And we have also seen what is adversarial learning, GAN architecture, what are the objectives of GAN, and we have also calculated what are the loss functions for the GAN.

**[00:30]** And in this session, we are going to study about the introduction to deep convolution GAN. In short form, we can call it as DCGAN. So in today's session, we are going to see about the limitations of GAN and introduction to deep convolution GANs. Before going to DCGAN, let us have the overview of the GAN. So GAN has got two neural networks. One is the generator, other one is a discriminator. If you look at the block diagram which is here, the generator is going to generate the images. So how the generator is generating the images? It is getting the input from the latent space, which is nothing but the noise.

**[01:10]** So generator is going to generate the images, and discriminator is other neural network, which is having the input from the generator as well as from the real images. So what does the discriminator will do is it is going to distinguish between the real images and the generated images. So what is the job of the generator is that it has to generate the images in such a way that the discriminator thinks that it is the real image only.

**[01:38]** So what are the duty of the discriminator is that it has to distinguish in a better way between the generated images and the real images. So both these neural networks, it has got opposite objective function. So I think if you look, that is generator gets better at fooling the discriminator and discriminator gets better at catching of generator. And if you look at this equation, which is going to say about the opposite objectives between these two neural networks. That is the min-max relationship between the generator and the discriminator.

**[02:16]** So, I think you have seen this equation in the previous session. So, the first term in this equation, which is going to say about the discriminator, which is dealing with the real data. And the second term, the discriminator, it is dealing with the generated data. So, since it is dealing the first term is dealing with the real data, the probability must be maximum of maximum. And in the second one, since the discriminator is dealing with the generated image, it has to be minimum. So, that's why it is the min-max relationship between the generator and the discriminator.

**[02:52]** So, I think with this knowledge, let us continue. Let us see what are the limitations of the GANs. So, the very first one is no convergence guarantee. Since it is a min-max game and because two networks have got the competitive objectives, it is very difficult to reach a stable of equilibrium state during the training. So, there can be no guarantee for the convergence. That is the first limitation of the GAN. And second one, mode collapse.

**[03:25]** So, in mode collapse, I'll just explain you with the example. Suppose if my real data images is having the animals images like cat, dog, horse, and elephant. Now, what does the generator must do? The generator should able to generate the images related to cat, dog, horse, and elephant. So, what is the generator now it's going to do is it is going to generate the cat image. So, it has generated a very realistic image of cat and it has sent to the discriminator. So, now the discriminator will think that it is a real image and it has given the output as real.

**[04:01]** So, now what this generator is going to think is that okay, the realistic image was accepted by the discriminator. So, let me generate one more cat image. Let me generate one more cat image. So, it is going on generating only the cat images. It is not generating the other animal images like horse, elephant, and dog. So, that is there is a possibility of mode collapsing. That is the other modes were not generated. Only the mode which were accepted by the discriminator, only that particular mode images it is generating. The other modes it is not generating. So, this will lead further mode collapse also.

**[04:36]** And the third limitation is the vanishing gradients. When the discriminator will get trained in the that is well trained in the early training only or it becomes in the early stages or if it becomes too accurate, then the gradient there will be no gradient input to the generator. When there is no gradient input to the generator, then the generator cannot able to improve itself. So, this will lead further So, this is called as the vanishing gradients.

**[05:10]** Next, hyperparameter sensitivity. So, hyperparameter sensitivity is that So, when you are going to train any of the model, hyperparameter should be done before the training of the model. But, in between the training, you should not go further tuning of the parameters like changing the learning rates or changing the batch sizes. That can be done. So, if you are doing such kind of changes, then the model the model doesn't work properly.

**[05:41]** Sometimes it may it may lead also for the entire failure of the model. So, these are the some of the limitations of the GAN. So, to uh reduce these limitations, we are going for the deep convolution GAN, and we are going to call it as the stable deep convolution GAN, because we are going to reach the stability for this. So, how we are going to reach the stability is we are doing few changes in the architecture. For example, in the discriminator, since the normal GAN or the vanilla GAN, it is uh dealing with the fully connected layers, that is the dense layers, pooling was used there, but here we are going to use the strided convolution in the discriminator. And in generator, we are going to use the transposed

**[06:25]** convolutions, or we can call it as a deconvolution, or fraction strided convolutions. And we are using the batch normalization in the generator and the discriminator, where in normal GANs, we are not using the batch normalization. And the third one is we are going to remove the fully connected layers for the deeper architectures. And in generator, we are going to use the ReLU as activation function, except at the output layer, we are going to use the tanH in the generator.

**[06:56]** Next, coming to the discriminator, we are using leaky ReLU activation function, and in the last layer, we are going to use the sigmoid activation function, because it is going to should say only two outputs, that is zero or one, that is real or fake. Now, let us go into the deeper of the generator, that is no, the generator is going to have the input as a noise, and the image as an output. So, first, if you look at latent vector Z, that is the noise, which has got the 100 dimensions, that is random noise from the normal distribution.

**[07:32]** We are going to reshape that 100 dimensions to 4 cross 4 into 1024 by using this reshape. And next, we are applying the upsampling, which is done by using transpose convolution plus batch normalization and using ReLU as an activation function. So, if you look at the 4 cross 4 spatial dimensions, they're changed to 8 cross 8. That means it is doubled. Whereas the channels, 1024 channels, it got into half. That is 512.

**[08:00]** So, like this we go for the upsampling of the process, where the spatial dimensions every time it is going to get double, and at last it has reached the dimensions of 64 into 64. Whereas the channels from 1024 to 512, 512 to 256, 256 to 128, and at last it has come to up to three. What are those three channels? RGB. So, the which is going to say about my image. So, this is the generator inside architecture. Next, if you go for your discriminator, so what is the input for the discriminator? It is the image generated by the generator. So, the real generated image or the real image will be of the size of 64 into 64 into three.

**[08:38]** So, next we are going for the downsampling, where you're going to use a strided convolution plus leaky ReLU as your activation function and batch normalization, also. So, 64 cross 64 into three, in the first step, when you downsample, it gets converted to 32 into 32 into 64. And in next time, when you do downsampling again, it gets converted to 16 into 16 into 128. So, here the spatial dimensions are getting into half, whereas the channels are going to get double. So, at last you're going to get 4 cross 4 into 512.

**[09:11]** And the last layer is nothing but your sigmoid layer, where it has to give the probability either zero or one, which is going to say about the real versus fake or the real image or the fake image. So, this is the architecture of the discriminator. So, DC GANs, by you by using DC GANs, I think most of the limitations they have reduced. But still, other types of GANs were also developed, like StyleGAN, BigGAN, WGAN. But for all the later GANs, whatever they were developed, DCGAN is the foundation for all of this.

**[09:44]** So, just for the DCGAN foundation, they have used some additional features on the top, and they have given them different names. So, for example, if you take StyleGAN. So, the StyleGAN means it has taken better noise injection and the style control. So, that's why they have given the name as StyleGAN. So, the architecture is same as the DCGAN, but only some additional features were added. So, next next the BigGAN. So, which is going to say that attention for long-range dependencies.

**[10:13]** So, like that many GANs were developed, but DCGAN core design remains constant. So, with all these, I think you have got the idea about what is the deep convolution GANs, and what are the advantages of that, and what is the architecture process, and what are the different GANs that were developed by considering DCGAN as the basic foundation. So, in the next session, we are going to see about the implementation of the basic GAN and implementation of the DCGAN hands-on session.

**[10:42]** Thank you all.
