---
title: "Lec 07 Introduction to Google Colab"
video_id: ukII_nwzPsI
index: 07
duration: 16:21
language: English (auto-generated)
playlist: https://www.youtube.com/playlist?list=PLgMDNELGJ1Ca_DduFvH6qfI1eapL48xOr
---

# Lec 07 Introduction to Google Colab

| | |
|---|---|
| **Lecture** | 07 / 63 + intro |
| **Duration** | 16:21 |
| **Captions** | English (auto-generated) |
| **Words** | 2,782 |
| **Video** | [ukII_nwzPsI](https://www.youtube.com/watch?v=ukII_nwzPsI) |
| **Playlist** | [Fundamentals of Generative AI and LLMs](https://www.youtube.com/playlist?list=PLgMDNELGJ1Ca_DduFvH6qfI1eapL48xOr) |

Auto-generated YouTube captions, lightly cleaned (removed `[music]` tags, grouped into paragraphs). These are **verbatim lecture captions**, not edited notes.

## Transcript

**[00:00]** Hello everyone. Welcome to the first hands-on session of this course. In this session, I want to give introduction about the Google Colab. Why we are going for Google Colab is it is a free cloud environment where we can able to run the Python code by using Jupyter Notebook as an interface. So, without wasting any time, let us enter into the Google Colab. Click on Chrome and type here Google Colab. So, you can get a page like this.

**[00:35]** So, in this, the very first one, you just click here, welcome to Colab. So, you will get a window like this. So, here you can able to find new notebook. So, click on the new notebook. So, it will take some time for loading of this page. So, you'll get a page like this. So, in this, you can able to find untitled five.ipynb. So, untitled five, you can able to replace it with your project name. So, I'm just giving it as project four.

**[01:11]** And dot ipynb, it is nothing but I stands for interactive, py stands for Python, and nb stands for notebook. So, it is a interactive Python notebook. So, after giving the project name, so, right side, you can able to find out top connect. So, click on this connect. And meanwhile, I think you can able to see the menu at the left side where it is where you are going to have file, edit, view, insert, runtime, tools, and help. So, this is the menu which you are going to have under this Google Colab.

**[01:49]** And next, here you can able at the right side, you can able to find out the drop down here. So, click on the drop down. And here, you can able to find sign change run time. So, click on this change run time. So, in the change run time, we have got three options. One is a run time type, hardware accelerator, run time version. So, what is this run time type is here you have got one more drop down here. So, please click on that. You can find Python 3, R, and Julia. That is, if you are writing the code in Python, then you have to click on Python 3. If you are doing R programming, click here like R.

**[02:25]** So, here you can find hardware accelerator. So, it is CPU, GPU, and TPU. CPU, you all know that it is a central processing unit. So, by default, it will be selected as CPU only. Here, you are having GPU. That is, graphical processing unit. So, why we go for GPU is that suppose if you are running a code in by using CPU, it is taking some 10 to 12 hours of time. But, by using GPU, it will take only 1 to 2 hours of time.

**[02:52]** And next, you are going TPU. That is, tensor processing unit. So, this we go for generally when you are having a very large data sets or for NLP programming, we go for TPU. So, before you run the code, you have to select this hardware accelerator. So, for time being, I'm just selecting only the CPU. Next, third one is run time version. So, here you have got many versions of the run time, but always recommend use the latest one. Now, click on save.

**[03:20]** And if you see here, you can find the RAM and the disk. So, it is going to say that how much space is allotted for this particular program. for a particular program. Next, here you have got the tabs called code and text. So, if you want to write the any of the code, so click on this code. If you want to enter any of the text, for example, just I'm clicking on this text. So, here I'll just give you one simple example.

**[03:50]** Suppose if I'm writing a code for multiplying of two numbers, then mul tiplication of two numbers I'm giving. So now, you have to press shift plus enter. So then it is going to give a text here. The display will be like this. Next, now we start entering the code. X equal to five, Y equal to eight, Z equal to X into Y. Enter. Enter. Print Z. So in order to run the code, you can use the button which is present inside this particular cell or simply you can also press shift plus enter.

**[04:42]** So click here. So got the answer it as 40. That is 5 into 8 is 40. So this is a simple Python program. So I just give an example. But generally if you go for your Google Colab, you're going you're using this Google Colab for your machine learning and deep learning models. So where you're going to deal with your data sets. So if you go That is where you can able to find the data sets. You will be having many data resources to get these data data sets. For example, Kaggle, GitHub, UCI. You can find many resources like this. What will be the form of your data set? For the data set, it will be in the form of CSV file, images, or videos.

**[05:23]** Now go for the another tab. I'm opening other tab here where I'm going to write it as Kaggle. First we go with the first resource, that is Kaggle. So you're going to enter into the Kaggle. So if you are a new user for the Kaggle, it will be asking for the sign up or register. Since I am already registered in this one, it is showing as my name here. Now whatever the data set you want to search here, you can able to give in the search button, like lung cancer.

**[05:55]** So, here I can find 5,191 results were there. That is these many projects were there on this lung cancer. So, here I can able to see the very first one. It is a lung cancer.csv. That is this person, he has done this project by taking the CSV file. So, please click on this one. And you can able to see at the right side top download. So, please click here. You can get download.ipynb. So, if you're clicking on this, then your file will be downloaded. Now, your file will be downloaded where? Into your system.

**[06:33]** Similarly, if you want image data set image data set, then you can able to give any any of the data set I can able to give. Suppose, Alzheimer's data set I'm giving. So, here I can able to find Alzheimer's data set. Similarly, click here. So, you can able to find the download. So, before that you can able to see that they have given some description about what are the data sets they have taken, what are the table of the contents, and what are the libraries is they have used, everything. So, similarly, if you click here the download, you can find out that zip file. So, in that zip file, again you'll be having the separate folders where you'll be having the test data set separately, train data

**[07:15]** separately, and validation data set separately. So, download all those folders into your system. So, once if you're downloading all those data sets into your system, the very next step what you have to do is you have to upload in your Google Drive. So, once if you're uploading all the data sets in your Google Drive, now how you're going to integrate the data sets with your code? So, I think here at the left side you can able to see a folder.

**[07:42]** And in this folder, you can able to see that one folder having the drive icon inside. Now, click on this drive icon inside. It is going to ask connect to Google Drive. So, when you give connect to Google Drive here, it is going to connect with your Google Drive. So, now it was go it was only a sample of data set folder. Now, if you look at it is mounting the data Google Drive. So, here you can find the drive. Click on this and here my drive is there.

**[08:10]** So, click on this my drive. So, whatever the information is there in your Google Drive, that will be displayed here. So, if you look at here that in the very first one, I have downloaded all that is already have download the test data, train data, and also I'm having this lung cancer CSV file also is there. Now, how to see that is what are the your CSV file? You can just open the CSV file and you can see what is the features of your data. But here, how we can able to see now let us see. So, then just go for some coding here.

**[08:45]** Importing the packages. Import pandas as pd. import numpy as np I'm giving lung is equal to Now, I'm going to read this CSV file. Read so CSV file. Give the brackets. Single double quotes. Now, I have to give the path of the CSV file. For this, what I have to do? So, go for this folder that is CSV file. Give a right click. You can find copy path here. Just paste the path here. And next, if I want to see what are the features present in this CSV file, I just give lung.head.

**[09:46]** And I'm going to run the code. Now you can see here the CSV file it was displayed here with few few persons' information. Now what are the features of this CSV file? Name, surname, age, smokes, area, alcohol, result. So result is nothing but here whether they are having the lung cancer or not. It is a binary classification. So these are the features it is having. So this is your CSV file how we can able to integrate with your code. Next, in the same way, how we can able to integrate your test data and the train data. So here also you're going to have test click on click right click on test you're going to have the copy path.

**[10:26]** So here the copy path also can be written. So test data, so it is your test. Give the path is equal to So this is my test data I'm going to have. Similarly, train data also I can give like this. That is just I'm giving the path of the test folder and the train folder. So click on the train, right click on the train, copy the path, and here you can give train data. So like this you can able to integrate your test and the train data in your coding.

**[11:03]** Next, this is your Kaggle. So generally Kaggle what people think is it is only the data set, but it is not only the data set. You can also create a notebook here. So if you find here, please click on the create. And you'll get a notebook here. So a notebook will be opened like this. So here you can able to write the coding. Here, see code, you can click on this code and you can start writing the code. So, Kaggle, it is not only the data set, you can also write the code, and you can also execute here.

**[11:38]** Suppose, if you want to share this Kaggle code, or that is the Kaggle project, whatever you have done here, you can also share with anyone. So, to share that anyone, so please click here the share, and you can make it a private, that is, if you want to share it with a particular persons, then you can go for private, or you can also make it publicly available just by giving the link. Similarly, how you are that is uh it is similar to that of how you are going to share the documents or the folders which are present in your Google Drive to someone, it is the same process. You can able to share.

**[12:11]** So, this is about the Kaggle. Now, let us go for the next one, next data resource, which is nothing but your GitHub. So, if you go for your GitHub, so you're getting a page display like this. So, if you are a new user, definitely it will ask for the register or your sign up. So, already I have signed in into the GitHub. So, that's why my page is like this. So, here also, you can able to in the search button, you can type lung cancer.

**[12:38]** So, give enter, then you can see here 11.6k results were there. So, these many projects are there. Now, each and every project, they will be describing about what they have done in each and every project. Now, click on the first one. You can see what is a lung cancer project is about, and what is how they have built the CNN, the training model, and next what is the testing data, and what is the confusion matrix they got, and everything. That is, the entire project was uploaded in this GitHub. So, you can use the GitHub for uploading your project also, entire project you can able to upload. At the same time, whatever the data sets they have used for the project, you can also download. So, the downloading process is

**[13:18]** similar, that is, download to your system, and then upload into your drive. This process is same. Suppose, if you want to upload your own project in your GitHub, then here you can find new repositories will be there. So, click on new repositories and keep give your repository name. Suppose it is your lung two. Lung two. Now, choose visibility. It is your public. Next, add read me. You have to give it as on so that you can able to edit something so that you can write something explanation for your project.

**[13:55]** Now, create a repository. Now, a repository was created where I can able to write the description of my project or I can able to enter the code. Whatever I want, I can able to do here. So, to write that, you have got an icon here edit file. So, click on that edit file and write whatever the code you want, you can write here. And whatever the code you have written, next click on this commit changes. And here also you click on commit changes. Now, your repository repository was created.

**[14:27]** So, if you look at the repository, that is the lung two which you have created and you have written these things in that your lung two. So, this is about your GitHub. Similarly, if you you can able to share the link. For example, on the top you are having this link. You can share directly this link to anyone whom you would like to or you can also make this link as a public also. So, this is about your GitHub. Next, the other one is UCI data sets.

**[14:54]** If you go for your UCI data set, it is your University of California. So, where it is going to have the data sets. So, here you can find many data sets are available. For example, if you click on this uh heart disease data set, you can have download option here. So, where you can able to download to your system and then upload into your Google Drive and that Google Drive you can give a link to your Google Colab. So, the procedure is same, but these are all the different resources. Suppose if you want to contribute any of the data set to this UCI, you can click see here, contribute data set, donate a new, or you can also give in a form of a link.

**[15:29]** So, this can be given for your UCI. So, these are the various data set resources we are having. Apart from this, you're also having many other, but many most of the people they are going to use the Kaggle, GitHub, and sometimes they are also taking from UCI. So, after doing coding and everything here, here you have got under the file option, you have got a save save option. So, save you can give a save of copy into drive, or save a copy into GitHub. Directly, you can do that.

**[15:59]** So, with this, I think you have got enough idea about how to integrate your images or your CSV file to your program, and how to download the data sets from the different data resources. Thank you, one and all.
