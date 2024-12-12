# Understanding K-means Clustering Through Real-World Python Projects

K-means clustering is one of the most widely used unsupervised machine learning algorithms, known for its simplicity and effectiveness. In this blog post, we'll explore two fascinating applications of K-means clustering: analyzing California housing patterns and compressing images. Through these practical examples, you'll gain a deep understanding of how K-means works and how it can be applied to solve real-world problems.

## What is K-means Clustering?

Before diving into our projects, let's understand what K-means clustering is and how it works.

K-means clustering is an unsupervised learning algorithm that helps us identify patterns in data by grouping similar data points together. The algorithm works by:

1. Choosing K initial cluster centers (centroids) randomly
2. Assigning each data point to the nearest centroid
3. Recalculating the centroids based on the mean of all points assigned to each cluster
4. Repeating steps 2-3 until convergence (when centroids no longer move significantly)

The "K" in K-means represents the number of clusters we want to find in our data. This is a hyperparameter that we need to choose based on our understanding of the problem and experimentation.

## Project 1: Analyzing California Housing Patterns

Our first project uses K-means clustering to analyze housing patterns in California. This project demonstrates how clustering can reveal geographic and economic patterns in real estate data.

### The Dataset

The California housing dataset contains information about housing blocks in California, including:

- Geographic coordinates (latitude and longitude)
- Median house values
- Median income
- Population
- Ocean proximity
- Other housing-related features

### Preprocessing Decisions and Their Impact

1. **Data Loading and Exploration**:
   - We first examine the data distribution using histograms, which reveals significant skewness in features like median_income and median_house_value
   - This skewness influences our decision to use MinMaxScaler rather than StandardScaler, as we want to preserve the relative relationships between extreme values

2. **Handling Categorical Data**:
   - The 'ocean_proximity' feature is converted using one-hot encoding instead of label encoding
   - This decision is crucial because:
     - Label encoding would imply an ordinal relationship between categories
     - One-hot encoding preserves the true categorical nature of the data
     - It allows the algorithm to treat each ocean proximity category independently

3. **Feature Selection for Different Analyses**:
   - For location-based clustering:
     - We include longitude, latitude, and ocean_proximity
     - Ocean proximity is included because it provides additional context about location that pure coordinates might miss
     - This combination helps identify natural geographic regions while accounting for coastal influence

   - For wealth-based clustering:
     - We include longitude, latitude, median_income, median_house_value, and population
     - Geographic features are retained because wealth patterns often have spatial correlation
     - Population is included to weight the importance of different areas

### Experimental Results and Analysis

#### Location-Based Clustering (K=3)

The choice of K=3 for location clustering was based on California's natural geographic divisions:

1. **Cluster Analysis**:
   - Coastal North: Characterized by high ocean_proximity values and moderate latitudes
   - Coastal South: Similar ocean_proximity but lower latitudes
   - Inland: Distinctly different ocean_proximity values and varied latitudes

2. **Distribution Analysis**:
   - The histogram of cluster labels shows uneven cluster sizes
   - This is expected and valid because California's population is not evenly distributed geographically
   - Coastal clusters are smaller but denser, reflecting real population patterns

#### Wealth-Based Clustering (K=6)

The decision to use K=6 for wealth clustering was made to capture finer gradations in economic patterns:

1. **Cluster Characteristics**:
   - High-Wealth Clusters:
     - Concentrated in coastal areas and urban centers
     - Show strong correlation between income and house values
     - Typically smaller in size but high in density

   - Middle-Wealth Clusters:
     - More evenly distributed geographically
     - Show moderate correlation between income and house values
     - Represent the largest segments by population

   - Low-Wealth Clusters:
     - Often found in rural and inland areas
     - Show weaker correlation between income and house values
     - Cover large geographic areas but lower population density

2. **Interesting Anomalies**:
   - Some clusters show high house values but lower incomes, particularly in certain coastal areas
   - This suggests the presence of historically wealthy areas now inhabited by lower-income residents
   - Could indicate areas with high proportions of retirees or inherited properties

3. **Geographic Distribution Patterns**:
   - Wealth clusters show strong spatial correlation
   - Coastal proximity generally correlates with higher wealth
   - Urban centers form distinct wealth clusters regardless of coastal proximity

## Project 2: Image Compression with K-means

### Implementation Decisions and Their Impact

1. **Color Space Representation**:
   - We use RGB color space rather than alternatives like HSV or LAB
   - Reasoning:
     - RGB is the native format of the image
     - The Euclidean distance in RGB space, while not perceptually uniform, works well enough for most images
     - Simpler implementation and faster computation

2. **Data Type Considerations**:
   - Convert to float32 instead of using uint8
   - Benefits:
     - Better numerical precision during clustering
     - Avoids potential issues with integer overflow
     - More stable centroid calculations

3. **Choice of K Values**:
   - Experiment uses K=5 for color reduction
   - This choice balances:
     - Visual quality (higher K = better quality)
     - Compression ratio (lower K = better compression)
     - Computational efficiency

### Compression Results Analysis

1. **Visual Quality vs. Compression Trade-off**:
   - Original image: Uses full 24-bit color (16.7 million colors)
   - Compressed image (K=5): Uses only 5 colors
   - Quality retention:
     - Large uniform areas maintain good quality
     - Gradients show more noticeable banding
     - Fine details may be lost or simplified

2. **File Size Analysis**:
   - Raw file size comparison:
     - Original and compressed BMP files are similar in size
     - This is because BMP format doesn't utilize color redundancy

   - Compressed file size comparison:
     - Zipped compressed image is significantly smaller
     - Reason: Higher color redundancy allows better zip compression
     - Additional compression possible with optimized color indexing

3. **Performance Considerations**:
   - Computation time increases with:
     - Image size (number of pixels)
     - Number of clusters (K)
     - Number of iterations until convergence
   - Memory usage is primarily affected by image size

## Advanced Implementation Considerations

1. **Initialization Strategy**:
   - Default sklearn K-means uses k-means++ initialization
   - Benefits over random initialization:
     - More stable results
     - Faster convergence
     - Better final clustering

2. **Convergence Criteria**:
   - Algorithm stops when:
     - Maximum iterations reached
     - Centroid positions stabilize
   - Trade-off between accuracy and computation time

3. **Scaling Considerations**:
   - Housing data: MinMaxScaler used to preserve relative differences
   - Image data: Already normalized (0-1 range)
   - Impact on cluster quality and interpretation

## Conclusion

These experiments demonstrate how K-means clustering can be effectively applied to very different types of data analysis problems. The key to success lies in understanding:

1. The nature of your data and how it should be preprocessed
2. The impact of parameter choices on results
3. The trade-offs involved in different implementation decisions
4. How to interpret and validate the results in the context of your specific problem

Whether you're analyzing geographic patterns or compressing images, careful consideration of these factors will help you achieve better results with K-means clustering.

Remember that while K-means is relatively simple to implement, getting good results requires careful consideration of feature selection, preprocessing, and parameter tuning. The projects we've explored here provide a foundation for understanding these considerations in practice.
