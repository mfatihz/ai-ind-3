# Plant Disease Classification

## Project Overview

The goal of this project is to find ways to help farmers detect plant diseases quickly and easily. The detection method used here is the classification of disease types through deep learning techniques.

## Introduction
### Background

The agricultural sector is currently grappling with challenges like climate change, pest infestations, and environmental stressors, necessitating innovative solutions for ensuring food security and sustainable crop production, especially for the upcoming challenges associated with quality food.

With the lack of agricultural experts and the vast geographical area of Indonesia, it is necessary to create an innovation that can help overcome the problems faced by farmers without the need to wait for assistance from experts. The innovation presented should be easy to operate and can be run anywhere.

### Objective

Build a deep learning model that can identify the type of disease in plants using a dataset that can describe the original conditions of plants in agricultural land.

### Scope

Exploring the accuracy of resnet50 and VGG19 models on existing datasets.

## Experiment

### 1. Data Collection & Preparation

Dataset: [PlantDoc](https://www.kaggle.com/datasets/abdulhasibuddin/plant-doc-dataset)

The dataset consists of 2 sets of training (2316 data) and testing (236 data) data.

From the observation, it is also known that there are some data that need to be ignored because they have invalid class data or too much noise.

For the next process, the training dataset is split with a ratio of 80/20 for training and validation. A data augmentation process is also performed to increase the variety of data. Each image is also resized to 224px x 224px.

### 2. Model Development

Model: Resnet50, Resnet152, VGG19

The model was modified by adding a dropout layer before the final layer to avoid overfitting.

### 3. Training & Optimization

In the training process, the model is run using several hyperparameter variants
Epoch: 30
Batch size = 32
Learning rate = 0.01, 0.001
Optimizer: SGD (Momentum: 0.0, 0.5, 0.9), Adam
Dropout: 0, 0.15

The metrics used are cross entropy loss (with or without weighting to handle imbalanced data) and accuracy.

The best training results for each model are summarized in the following table:

Model | Epoch | Optimizer | LR | Momentum | Dropout | Train lost | Train acc | Val lost | Val acc | Testing acc
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Resnet50 | 30 | SGD | 0.01 | 0 | 0 | 0.334 | 89.64 | 1.094 | 65.66 | 65.68
Resnet152 | 30 | SGD | 0.01 | 0.9 | 0 | 0.557 | 79.5 | 1.293 | 63.83 | 62.89
VGG | 50 | SGD | 0.001 | 0.9 | 0 | 0.829 | 72.10 | 1.273 | 64.15 | 59.32

## Deployment

The training result model can be accessed through [mfz-plant-disease](https://mfz-plant-disease.streamlit.app/)

The source code can be seen in [Github](https://github.com/mfatihz/streamlit-plant-disease)

## Conclusions and Suggestions

* The best accuracy is obtained by the resnet50 model with a value of 65.68%.
* There are quite a lot of data containing noise which causes the accuracy of model detection to be not too high.
* Although the accuracy is not too high, the model can still classify the disease quite well.
* The model should be retrained using more and better data.
* Conduct other deep learning experiments that are better able to separate data from surrounding objects, for example through object detection or segmentation.
