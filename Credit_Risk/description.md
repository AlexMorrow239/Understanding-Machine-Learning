# Optimizing Machine Learning Models for Credit Risk Prediction

## Project Goal and Business Context

The primary objective of this project is to develop and optimize machine learning models that can accurately predict whether a credit card holder will experience financial distress in the next two years. This prediction capability is crucial for banks and financial institutions to:

- Assess credit risk more accurately
- Make informed lending decisions
- Reduce potential financial losses
- Maintain a healthy loan portfolio

The challenge lies in finding the most effective model and optimizing it to handle real-world complexities like imbalanced data and the need for interpretable results.

## Understanding Our Dataset

The dataset is from <https://www.kaggle.com/c/GiveMeSomeCredit>

The GiveMeSomeCredit dataset contains 150,000 records of credit card holders with 11 features:

- SeriousDlqin2yrs: Target variable (1 = customer defaulted, 0 = customer in good standing)
- RevolvingUtilizationOfUnsecuredLines: Total balance on credit cards and personal lines of credit / total credit limits
- age: Age of borrower in years
- NumberOfTime30-59DaysPastDue: Number of times borrower has been 30-59 days past due
- DebtRatio: Monthly debt payments / monthly income
- MonthlyIncome: Monthly income in dollars
- NumberOfOpenCreditLinesAndLoans: Number of open loans and lines of credit
- NumberOfTimes90DaysLate: Number of times borrower has been 90+ days past due
- NumberRealEstateLoansOrLines: Number of mortgage and real estate loans
- NumberOfTime60-89DaysPastDue: Number of times borrower has been 60-89 days past due
- NumberOfDependents: Number of dependents in household (spouse, children etc.)

Class Distribution:

- 93.3% (139,974 samples) - Class 0 (No Default)
- 6.7% (10,026 samples) - Class 1 (Default)
This significant imbalance reflects real-world credit risk scenarios where defaults are relatively rare events.

## Understanding Our Models

### Logistic Regression: The Foundation

Logistic Regression serves as our baseline model, providing a simple yet powerful starting point for binary classification.

#### How Logistic Regression Works

1. At its core, logistic regression transforms a linear model into probability predictions using the logistic function:

   ```
   P(default) = 1 / (1 + e^(-z))
   where z = b0 + b1x1 + b2x2 + ... + bnxn
   ```

2. The model learns coefficients (b0, b1, ..., bn) that:
   - Indicate each feature's importance
   - Show whether a feature increases (positive coefficient) or decreases (negative coefficient) default probability
   - Can be interpreted as log-odds ratios

3. Advantages for Credit Risk:
   - Highly interpretable results
   - Provides probability scores
   - Computationally efficient
   - Less prone to overfitting

### Decision Trees: Adding Complexity

Decision Trees create a more sophisticated model by splitting data based on feature thresholds.

#### Tree Construction Process

1. Root Node Selection:
   - Evaluates all possible feature splits
   - Chooses split that maximizes information gain
   - Uses metrics like Gini impurity or entropy

2. Recursive Splitting:

   ```
   For each node:
   1. Calculate impurity measure
   2. Try all possible feature splits
   3. Select split that maximizes information gain
   4. Repeat until stopping criteria met
   ```

3. Key Parameters:
   - max_depth: Controls tree complexity
   - min_samples_split: Minimum samples needed to split
   - min_samples_leaf: Minimum samples in leaf nodes

4. Advantages for Credit Risk:
   - Handles non-linear relationships
   - Captures feature interactions
   - Provides clear decision rules
   - Handles missing values well

### Random Forest: Ensemble Power

Random Forest enhances decision trees through ensemble learning, creating a robust and powerful predictor.

#### Random Forest Architecture

1. Building the Forest:

   ```python
   for i in range(n_trees):
       1. Create bootstrap sample of training data
       2. Build decision tree with:
          - Random feature subset at each split
          - No pruning
       3. Store tree in ensemble
   ```

2. Making Predictions:
   - Each tree votes on the prediction
   - Final prediction is majority vote
   - Probability can be calculated from vote proportions

3. Feature Importance:
   - Calculated from decrease in impurity
   - Averaged across all trees
   - Provides robust importance rankings

4. Advantages for Credit Risk:
   - Reduces overfitting
   - Handles high-dimensional data
   - Provides feature importance
   - Robust to outliers

## Advanced Optimization: Grid Search

### Grid Search Methodology

Grid Search is a systematic approach to hyperparameter optimization that helps us find the best model configuration.

#### How Grid Search Works

1. Parameter Grid Definition:

   ```python
   param_grid = {
       'max_depth': [1, 10, 100],
       'min_samples_split': [2, 5, 10],
       'min_samples_leaf': [1, 5, 10],
       'max_features': ['sqrt', 'log2', None],
       'max_samples': [0.1, 0.5, 0.9]
   }
   ```

2. Cross-Validation Process:
   - Splits training data into k-folds
   - Tests each parameter combination on all folds
   - Averages performance metrics
   - Identifies best parameter set

3. Implementation Benefits:
   - Prevents overfitting to validation set
   - Provides robust performance estimates
   - Enables parallel processing
   - Systematic exploration of parameter space

### Handling Class Imbalance

Our dataset presents a significant class imbalance (93.3% non-default vs 6.7% default), requiring special handling:

1. Weighted Accuracy Metric:

   ```python
   def weighted_accuracy(confusion):
       M = confusion.copy().astype('float32')
       for k in range(0, M.shape[0]):
           M[k] /= M[k].sum() + 1e-8    
       acc = M.diagonal().sum() / M.sum()
       return acc
   ```

2. Class Weights:
   - Automatically adjusted based on class frequencies
   - Penalizes misclassification of minority class more heavily
   - Integrated into model training process

## Model Selection Results

After comprehensive testing and optimization:

1. Random Forest emerged as the best performer due to:
   - Better handling of non-linear relationships
   - Robust performance on imbalanced data
   - Strong resistance to overfitting
   - Valuable feature importance insights

2. Optimal Configuration Found:
   - Identified through Grid Search
   - Balanced complexity and performance
   - Validated through cross-validation
   - Tested on independent test set
