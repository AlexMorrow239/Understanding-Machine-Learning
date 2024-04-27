# Banknote Authentication Analysis

## Introduction

This Python-based project focuses on the classification of banknotes as real or counterfeit using the Banknote Authentication dataset. It showcases data analysis and visualization techniques, including the use of matplotlib, numpy, pandas, and scipy libraries to understand and predict the authenticity of banknotes.

## Data

The Banknote Authentication dataset contains attributes like variance, skewness, kurtosis, and entropy of banknote images, along with their authenticity labels. This project analyzes these features to classify the banknotes.

## Features

- **Data Visualization:** Utilizes matplotlib to generate scatter plots, highlighting the distinctions between real and counterfeit banknotes.
- **Centroid Calculation:** Employs numpy and pandas to calculate centroids for both real and counterfeit banknotes, aiding in visualization and classification.
- **Euclidean Distance Classifier:** Implements a basic classifier based on the Euclidean distance to centroids for an initial guess of authenticity.
- **Gaussian Probability Density Classifier:** (Extra Credit) Enhances classification accuracy using a Gaussian probability density function to predict banknote authenticity.

## Code Overview

### Data Loading and Preparation:

Utilizes pandas to load the Banknote Authentication dataset and preprocess it for analysis.

### Scatter Plot Visualization:

Uses matplotlib to create scatter plots of the data, differentiating real and counterfeit banknotes with color codes. This visual representation is crucial for understanding the data distribution and the challenge of classification.

### Centroid Calculation:

Implements numpy to calculate the centroids of real and counterfeit banknotes, which are later used to classify a banknote based on its proximity to these centroids.

### Authenticity Prediction

This is where the two versions of the code differ. Utilizing the data, each python file predicts the authenticity of each banknote utilizing different methods.

**`EuclideanDist.py`**

basic.py utilizes euclidean distance from the centroids to determine authenticity. This means that for each banknote, the program will calculate the euclidean distance from the 'real' centroid and the 'counterfeit' centroid. The program will then determine authenticity by comparing these 2 distances.

- If real_distance > counterfeit_distance, then banknote is counterfeit. Else, banknote is real.

**`Gaussian.py`**

The extra credit portion of the project involves utilizing a Gaussian probability density function (PDF) to enhance the classification accuracy of the banknote authentication analysis. This method provides a probabilistic approach to determining whether a banknote is real or counterfeit, based on its feature measurements.

**Overview**

The Gaussian PDF is used to model the likelihood that a given banknote, characterized by certain features like variance, skewness, kurtosis, and entropy, belongs to either the real or counterfeit distribution. The essence of this approach is to calculate the probability of a banknote being drawn from either distribution, based on its features.

**Calculation**

The process involves defining the standard deviations for the real and counterfeit samples for each feature. The probability of a banknote \(x\) being real or counterfeit is computed as follows:

1. _Feature Independence:_ Assuming the independence of the banknote's features (variance, skewness, kurtosis, entropy), the total probability of a banknote \(x\) being real or counterfeit is the product of the probabilities for each feature.
2. _Probability Calculation:_ For a single feature, the probability is calculated using the Gaussian PDF formula. This involves the mean and standard deviation of the feature for both real and counterfeit banknotes.
3. _Overall Probability:_ The overall probability of \(x\) being real or counterfeit is obtained by multiplying the probabilities calculated for each feature.

**Classification Decision**

After calculating p(real, x) and p(fake, x) for a banknote x, the classification decision is made by comparing these probabilities. The banknote is classified as:

- _Real:_ If p(real, x) > p(fake, x)
- _Counterfeit:_ If p(fake, x) > p(real,x)

This probabilistic approach provides a nuanced mechanism for classification, leveraging the statistical properties of the banknote features to make informed predictions about their authenticity.

## Key Components

- _matplotlib, numpy, pandas:_ These libraries form the backbone of the project, enabling data manipulation, analysis, and visualization.
- _Scipy (Gaussian.py):_ Utilized for statistical analysis, specifically for implementing the Gaussian classifier.

- _Data Analysis Techniques:_ Both scripts demonstrate essential data analysis techniques, from basic statistical calculations to more complex probabilistic models.
- _Classifier Design:_ The project illustrates two different approaches to classification, providing insight into machine learning methodologies at a fundamental level.

## Running The Project

- Basic Classification using Euclidian Distance:

```bash
python EuclideanDist.py
```

- Classification using Gaussian Probability:

```bash
python Gaussian.py
```

## Required Installations

Ensure you have Python 3.x installed. Install the required libraries using:

```bash
pip3 install matplotlib numpy pandas scipy
```
