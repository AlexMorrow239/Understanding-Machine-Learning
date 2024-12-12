# MNIST Digit Recognition: Combining K-means Clustering with KNN Classification

## Introduction

This project demonstrates how combining two different machine learning algorithms - K-means clustering and K-Nearest Neighbors (KNN) - can create an efficient solution for handwritten digit recognition. Using the MNIST dataset, we show how K-means clustering can be used for data reduction before applying KNN classification, resulting in a model that balances computational efficiency with classification accuracy.

## Understanding K-Nearest Neighbors (KNN)

Before diving into the implementation, it's crucial to understand KNN, as it's a fundamental component of our hybrid approach:

### What is KNN?

K-Nearest Neighbors is a supervised learning algorithm used for both classification and regression tasks. It works on a beautifully simple principle: an object is classified based on the majority vote of its neighbors. The object is assigned to the class most common among its K nearest neighbors, where K is a positive integer that we specify.

### How KNN Works

1. **Distance Calculation**: For each new data point we want to classify:
   - Calculate its distance to all points in our training set
   - Common distance metrics include Euclidean distance, Manhattan distance, or Hamming distance
   - In our project, we use Euclidean distance as it works well for image data

2. **Finding Neighbors**:
   - Sort all training points by their distance to the new point
   - Select the K closest points as neighbors

3. **Voting Process**:
   - Look at the classes of these K neighbors
   - Take a majority vote
   - Assign the most common class to our new point

### Key Characteristics of KNN

- **Non-parametric**: Makes no assumptions about the underlying data distribution
- **Instance-based learning**: No explicit training phase - it simply stores the training data
- **Lazy learning**: Computation happens only when we need to classify a new point
- **Memory-intensive**: Must store all training data to make predictions

### The K Parameter

The choice of K significantly impacts the model's behavior:

- Small K (like K=1): Very sensitive to local patterns, might be noisy
- Large K: Smoother decision boundaries, but might miss important patterns
- K is typically chosen to be odd (for classification) to avoid tied votes

## The MNIST Dataset

MNIST (Modified National Institute of Standards and Technology) is a widely-used dataset in machine learning and computer vision. It serves as a standard benchmark for testing image processing systems and machine learning algorithms.

### Dataset Composition

- **Training Set**: 60,000 handwritten digit images
- **Test Set**: 10,000 handwritten digit images
- **Image Size**: 28x28 pixels (784 total pixels per image)
- **Color Format**: Grayscale (0-255 pixel values)
- **Classes**: 10 (digits 0-9)

### Key Characteristics

1. **Image Format**:
   - Each image is normalized to fit into a 28x28 pixel box
   - Digits are centered in the image using center of mass
   - Images are grayscale with pixel values ranging from 0 (white) to 255 (black)

2. **Data Structure**:
   - Each image is represented as a 784-dimensional vector (28×28 = 784)
   - Each pixel value is a feature in this high-dimensional space
   - Labels are single digits from 0 to 9

3. **Dataset Properties**:
   - Clean and preprocessed
   - Relatively balanced class distribution
   - Variations in writing style, thickness, and tilt
   - No missing values or corrupted images

### Historical Significance

- Created by Yann LeCun, Corinna Cortes, and Christopher Burges
- Derived from NIST's original dataset
- Modified to be easier to use:
  - Normalized size and position
  - Anti-aliased to produce grayscale levels
  - Cleaned and preprocessed

### Why MNIST is Important

1. **Benchmark Standard**:
   - Used to compare different machine learning algorithms
   - Provides a consistent way to measure model performance
   - Extensive published results available for comparison

2. **Educational Value**:
   - Simple enough to understand
   - Complex enough to be interesting
   - Good size for experimentation
   - Real-world application

3. **Practical Benefits**:
   - Clean and preprocessed
   - No data cleaning required
   - Ready to use for machine learning
   - Well-documented

## The Problem: Scale and Speed

While KNN is an excellent classifier, it faces a significant challenge with large datasets like MNIST:

- 60,000 training images
- 10,000 test images
- Would require 600,000,000 image comparisons
- Computationally intensive and slow

## Our Solution: A Hybrid Approach

We solve this scaling problem by combining K-means clustering with KNN in a novel way:

1. **Data Reduction Using K-means**:
   - Split training data by digit (0-9)
   - Apply K-means clustering (K=9) to each digit group
   - Result: 90 representative images (9 clusters × 10 digits)
   - Reduces comparison requirements by 99.85%

2. **Classification Using KNN**:
   - Use cluster centers as our new training set
   - Compare new images against only 90 points
   - Fast classification while maintaining good accuracy

## Results Analysis

We assess our model's performance through multiple lenses:

1. **Training Data Assessment**:
   - Compare digit frequencies across datasets
   - Ensure representative sampling
   - Verify data distribution integrity

2. **Classification Performance**:
   - Measure prediction accuracy
   - Track classification time
   - Analyze error patterns

3. **Visual Analysis**:
   - K-means cluster visualization
   - Confusion matrix analysis
   - Sample classification results

## Running The Project

To run this project, either clone the repository:

```bash
git clone https://github.com/AlexMorrow239/CSC315.git
```

## Required Installations

Ensure you have Python 3.x installed. Install required libraries:

```bash
pip3 install matplotlib numpy pandas scipy
```

## Conclusion

This project demonstrates how combining algorithms can overcome limitations of individual approaches. By using K-means clustering for dimensionality reduction before applying KNN, we create a solution that is both computationally efficient and reasonably accurate. This hybrid approach shows how thoughtful algorithm combination can solve real-world machine learning challenges.
