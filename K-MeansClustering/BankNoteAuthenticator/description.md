# Beyond K-means: Exploring Classification Methods with Banknote Authentication

In our previous exploration of K-means clustering, we saw how unsupervised learning can help us discover patterns in housing data and compress images. Now, let's dive into a different type of machine learning problem: classification. We'll use a real-world example of banknote authentication to explore two classification approaches that build upon the concepts we learned with K-means.

## The Problem: Authenticating Banknotes

Counterfeit currency is a serious problem that affects economies worldwide. Banks and financial institutions need reliable methods to distinguish genuine banknotes from counterfeits. While modern banknotes contain sophisticated security features, we can also use machine learning to analyze various characteristics of banknotes to determine their authenticity.

## Dataset Analysis

The Banknote Authentication dataset contains measurements of images taken from genuine and forged banknotes. Each banknote is described by 5 features:

### Feature Description

1. **Variance of Wavelet Transformed Image** (variance)
   - Range: -4.4779 to 6.8248
   - Distribution: Roughly normal, centered around 2.0
   - Indicates the variation in pixel intensities after wavelet transformation

2. **Skewness of Wavelet Transformed Image** (skewness)
   - Range: -13.7731 to 11.9625
   - Distribution: Bimodal, showing distinct patterns for real and fake notes
   - Measures asymmetry in the pixel intensity distribution

3. **Kurtosis of Wavelet Transformed Image** (kurtosis)
   - Range: -5.2861 to 17.9274
   - Distribution: Right-skewed
   - Quantifies the "tailedness" of the pixel intensity distribution

4. **Entropy of Image** (entropy)
   - Range: -8.5482 to 2.4495
   - Distribution: Left-skewed
   - Measures the randomness in the image textures

5. **Class Label** (counterfeit)
   - Binary: 0 (genuine) or 1 (counterfeit)
   - Well-balanced dataset: approximately equal numbers of genuine and counterfeit notes

### Statistical Analysis

Key observations from the dataset:

1. **Feature Correlations**
   - Strong negative correlation between skewness and kurtosis (-0.82)
   - Moderate correlation between variance and entropy (0.43)
   - Other features show relatively weak correlations

2. **Separability Analysis**
   - Genuine notes tend to have:
     - Higher variance values
     - More positive skewness
     - Lower kurtosis values
     - Higher entropy values

   - Counterfeit notes typically show:
     - Lower variance values
     - More negative skewness
     - Higher kurtosis values
     - Lower entropy values

3. **Class Distribution**
   - Real banknotes: 762 samples
   - Counterfeit banknotes: 610 samples
   - Total dataset size: 1,372 samples

### Data Quality

The dataset demonstrates several positive characteristics:

1. **Completeness**
   - No missing values
   - All features are numerical
   - Well-defined value ranges

2. **Balance**
   - Near-equal distribution of classes
   - Good representation of both genuine and counterfeit notes

3. **Feature Engineering**
   - Features are derived from wavelet transformation
   - Captures both statistical and textural properties of the images

4. **Dimensionality**
   - Low dimensional (4 features + 1 label)
   - Makes it suitable for visualization and analysis
   - Reduces computational complexity

This dataset is particularly interesting because it represents a real-world application of machine learning in financial security. The features are derived from wavelet transformation of banknote images, which is a sophisticated method for capturing image characteristics at different scales.

## From K-means to Classification

While K-means is great for discovering natural groupings in data, our banknote problem is different because:

1. We know exactly how many groups we have (2: real and counterfeit)
2. We have labeled training data
3. We want to classify new banknotes based on these labels

Let's explore two methods that build upon the centroid concept we learned with K-means.

## Method 1: Euclidean Distance Classification

Our first approach is conceptually similar to K-means, but simpler since we already know our groups:

1. Calculate centroids for real and counterfeit banknotes
2. For each new banknote, measure its distance to both centroids
3. Classify it based on which centroid it's closer to

### Implementation Insights

```python
def calc_euclidean_distance(real_centroid, counterfeit_centroid, features, row):
    distance_to_real = np.sqrt(np.sum((features - real_centroid) ** 2))
    distance_to_counterfeit = np.sqrt(np.sum((features - counterfeit_centroid) ** 2))
    
    actual_status = 'Real' if row['counterfeit'] == 0 else 'Counterfeit'
    predicted_status = 'Real' if distance_to_real < distance_to_counterfeit else 'Counterfeit'
    return (actual_status, predicted_status)
```

This method achieves 70.70% accuracy. While better than random guessing, there's room for improvement.

### Visualization Analysis

Our visualizations show some interesting patterns:

- Clear separation between real and counterfeit notes in some feature pairs
- Significant overlap in others, explaining classification errors
- Centroid positions provide insights into typical characteristics of each class

## Method 2: Gaussian Probability Density

Building on the limitations of the Euclidean distance approach, we implement a more sophisticated method using Gaussian probability distributions. This method considers not just the distance to centroids, but the overall distribution of features.

### The Math Behind It

For each feature, we:

1. Calculate the mean (μ) and standard deviation (σ) for both real and counterfeit notes
2. Use the Gaussian probability density function:
   P(x) = (1 / (σ√(2π))) * e^(-(x-μ)²/(2σ²))

### Implementation Details

```python
def calculate_gaussian_probabilities(data, feature, mean_real, std_real, mean_fake, std_fake):
    prob_real = norm.pdf(data[feature], mean_real, std_real)
    prob_fake = norm.pdf(data[feature], mean_fake, std_fake)
    return prob_real, prob_fake
```

The final classification combines probabilities across all features:

```python
probabilities_real = np.ones(len(data))
probabilities_fake = np.ones(len(data))

for feature in ['variance', 'skewness', 'kurtosis', 'entropy']:
    prob_real, prob_fake = calculate_gaussian_probabilities(...)
    probabilities_real *= prob_real
    probabilities_fake *= prob_fake
```

### Results and Analysis

The Gaussian method achieves 84.77% accuracy, a significant improvement over the Euclidean distance approach. This improvement comes from:

1. **Better Handling of Feature Distributions**
   - Accounts for the spread of data, not just central tendency
   - More robust to outliers
   - Considers the shape of the feature distributions

2. **Feature Independence Assumption**
   - Treats each feature as independent
   - Multiplies individual feature probabilities
   - Works well when features are relatively uncorrelated

3. **Probabilistic Decision Boundary**
   - Creates more nuanced decision boundaries than simple distance
   - Better handles overlapping classes
   - Provides confidence levels for classifications

## Visualization and Color Coding

Both implementations use a clever color coding scheme to show classification results:

- Dark Blue: Correctly identified real notes
- Light Blue: Real notes misclassified as counterfeit
- Dark Red: Correctly identified counterfeit notes
- Light Red: Counterfeit notes misclassified as real

This visualization helps us:

1. Identify regions where classification is most reliable
2. Spot patterns in misclassifications
3. Understand the strengths and limitations of each method

## Key Learnings and Insights

1. **Feature Relationships Matter**
   - Some feature pairs (like variance-entropy) show better separation
   - Other pairs have significant overlap, making classification harder
   - Multiple features together provide better classification than any single feature

2. **Distribution Shapes**
   - Real and counterfeit notes often have different distributions
   - Gaussian assumption works well but isn't perfect
   - Some features show skewed or multi-modal distributions

3. **Model Complexity Trade-offs**
   - Euclidean distance: Simple but less accurate
   - Gaussian method: More complex but better performance
   - Each method has its use cases depending on needs

## Next Steps and Improvements

Several potential enhancements could improve classification:

1. **Feature Engineering**
   - Create new features from combinations of existing ones
   - Transform features to make distributions more Gaussian
   - Remove or combine highly correlated features

2. **Advanced Methods**
   - Try kernel density estimation for non-Gaussian distributions
   - Implement support vector machines for better boundary detection
   - Explore deep learning for automatic feature extraction

3. **Validation and Testing**
   - Use cross-validation for more robust accuracy estimates
   - Test with different subsets of features
   - Evaluate on new, unseen data

## Conclusion

This project shows how we can build upon the centroid concept from K-means to create increasingly sophisticated classification methods. While the Euclidean distance method provides a simple baseline, the Gaussian probability approach demonstrates how incorporating statistical properties of the data can significantly improve classification accuracy.

The visual tools we've developed help us understand both the power and limitations of these methods, providing insights that can guide further improvements in banknote authentication and similar classification problems.
