# Project 1: Face Recognition

## Overview
The Face Recognition project carried out here is in the form of gender classification. Gender classification applications can be utilized in various fields, for example, security or consumerism.

## Datasets
The data used for model training consists of 5000 unique image data, with dimensions HxW=218x178. Each data has attributes -1 (female) and 1 (male) in the Male column.

## Experiments
This gender classification experiment was conducted using 3 architectures:
1. VGG (VGG19)
2. GoogLeNet (inception V1)
3. ResNet (ResNet50)

For each architectural design, transfer learning, fine-tuning, and hyperparameter tuning were performed to achieve the targeted accuracy level (>90%).
For transfer learning, all pre-trained weights data comes from the Pytorch library.

## Result
From the experiments conducted, it was found that the three architectures above can exceed the target accuracy value (>90%), with the Resnet obtaining the highest result among the three architectures used.

Considering the accuracy achieved, training time, and hardware requirements, our group recommends using the ResNet architecture.

## Improvements
Although the accuracy result has exceeded the target, the fine-tuning and hyperparameter tuning process performed in this experiment are still minimum. Therefore, to improve the prediction performance, further exploration can be done on both processes, especially on the data augmentation process.

## Deployment
Demo: [Streamlit](https://mfz-gender-prediction.streamlit.app/)

Source code: [Github](https://github.com/mfatihz/streamlit-gender-prediction)
