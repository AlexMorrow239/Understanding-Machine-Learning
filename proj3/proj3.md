# MNIST Digit Recognition

## Introduction

This project applies machine learning techniques to recognize handwritten digits from the MNIST dataset. The project employs K-Means clustering for data reduction and K-Nearest Neighbors (KNN) for classification, followed by various visualizations to interpret the model's performance and the data's characteristics.

## Table of Contents

1. [MNIST Digit Recognition](#mnist-digit-recognition)
2. [Introduction](#introduction)
3. [Table of Contents](#table-of-contents)
4. [Data Processing](#data-processing)
   - [Too Many Comparisons](#too-many-comparisons)
   - [Comparison Reduction](#comparison-reduction)
5. [Assessing the Training Data](#assessing-the-training-data)
6. [Classifying the Test Data](#classifying-the-test-data)
   - [K-Nearest Neighbors](#k-nearest-neighbors)
   - [Prediction Time](#prediction-time)
7. [Analyzing Results of Classification](#analyzing-results-of-classification)
   - [Confusion Matrix](#confusion-matrix)
   - [Visualizing the K-Means Clusters](#visualizing-the-k-means-clusters)
   - [Visualizing the Classifications](#visualizing-the-classifications)
8. [Conclusion](#conclusion)
9. [Running The Project](#running-the-project)
10. [Required Installations](#required-installations)

## Data Processing

### Too Many Comparisons

K-Nearest Neighbors (KNN) is an accurate classifier, but it is just too slow. The MNIST handwritten digits have 60,000 training images, and 10,000 test images. A KNN classifier would need to compare each of 10,000 images against each of 60,000 images to find the K nearest neigbhbors. That’s 600,000,000 image comparisons! This is simply too slow

### Comparison Reduction

To speed up KNN I approximate the MNIST training data using K-means clustering. I split the MNIST training dataset into groups based on it’s label digit “0-9”. Then, I ran K-means with K=9 separately on each group. The result is an
Approximate Training Set with only 90 images

## Assessing the Training Data

Before I proceeded, I needed to verify that the training data was representative of the total populaton, so I compared the frequencies of each digit in each data set to ensure they were relatively similar. This servered as a simple sanity check since this is a reputable public dataset.

## Classifying the Test Data

### K-Nearest Neighbors

To classify the data, I used K-nearest neighbors which works as follows:

- K-Nearest Neighbors (KNN) is a classification algorithm that predicts the class of a data point based on the classes of its nearest neighbors.

- It is a non-parametric algorithm, meaning it does not make any assumptions about the underlying data distribution.

- KNN calculates the distance between the new data point and all other data points in the training set.

- The "K" in KNN refers to the number of nearest neighbors to consider when making predictions.

- The class of the majority of the K nearest neighbors is assigned to the new data point.

In this problem, I label the testing data based on its singular nearest neighbor in the approximated training data set of clusters.

### Prediction Time

I also calculate the amount of time it took to classify the testing data as an additional sanity check

## Analyzing Results of Classification

I assess the results of this model through a series of Visualizations.

### Confusion Matrix

Confusion matrices are a common diagnostic metric in machine learning models.

- They provide a way to visualize the performance of a classification model.

- A confusion matrix is a square matrix that displays the counts of true
  positive, true negative, false positive, and false negative predictions.

- The rows of the matrix represent the actual classes, while the columns represent the predicted classes.

- The diagonal elements of the matrix represent the correct predictions, while the off-diagonal elements represent the incorrect predictions.

- The confusion matrix allows us to calculate various evaluation metrics such as accuracy, precision, recall, and F1 score.

- It helps in understanding the types of errors made by the model and identifying areas for improvement.

- By analyzing the confusion matrix, we can gain insights into the model's performance for different classes and make informed decisions about adjusting the classification threshold or improving the model's training.

In addition, I also calculate the prediction accuracy and display the prediction time.

### Visualizing the K-Means Clusters

This section displays each digit's 9 clusters in a clean and digestible format. Another sanity check.

### Visualizing the Classifications

This section Uses the first 20 testing observations to get an idea for how the model is preforming.

In the left column, the testing observation and label is displayed. In the right column, the cluster used to classify the corresponding testing observation is displayed.

## Conclusion

For this data, K-Means Clustering provides a satisfactory representation of the total testing dataset. this allowed me too utilize the precision of K-Nearest Neighbors on an approximated dataset to create an efficient Machine Learning Classification Model.

## Running The Project

To run this project, you can either clone this entire repository:

```bash
git clone https://github.com/AlexMorrow239/CSC315.git
```

## Required Installations

Ensure you have Python 3.x installed. Install the required libraries to your python kernel using:

```bash
pip3 install matplotlib numpy pandas scipy
```
