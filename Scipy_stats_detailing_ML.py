import numpy as np
import scipy.stats as stats
import pandas as pd

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Descriptive Statistics
print("Descriptive Statistics:")
print(f"Mean: {stats.describe(data).mean}")
print(f"Variance: {stats.describe(data).variance}")

print('---------------------------------------------------------------------------------------------------------')
# 2. Distribution Testing
print("\nDistribution Testing:")
# Shapiro-Wilk test for normality
shapiro_test = stats.shapiro(data)
print(f"Shapiro-Wilk Test: statistic={shapiro_test.statistic}, p-value={shapiro_test.pvalue}")

print('---------------------------------------------------------------------------------------------------------')
# 3. Correlation Methods
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
print("\nCorrelation Methods:")
# Pearson correlation
pearson_corr = stats.pearsonr(x, y)
print(f"Pearson Correlation: coefficient={pearson_corr.statistic}, p-value={pearson_corr.pvalue}")

# Spearman rank correlation
spearman_corr = stats.spearmanr(x, y)
print(f"Spearman Correlation: coefficient={spearman_corr.statistic}, p-value={spearman_corr.pvalue}")

print('---------------------------------------------------------------------------------------------------------')
# 4. Hypothesis Testing
print("\nHypothesis Testing:")
# T-test (independent samples)
group1 = [1, 2, 3, 4, 5]
group2 = [2, 4, 6, 8, 10]
t_test = stats.ttest_ind(group1, group2)
print(f"T-Test: statistic={t_test.statistic}, p-value={t_test.pvalue}")

print('---------------------------------------------------------------------------------------------------------')
# 5. Probability Distributions
print("\nProbability Distributions:")
# Normal distribution
norm_dist = stats.norm(loc=0, scale=1)
print(f"Normal Distribution PDF at x=0: {norm_dist.pdf(0)}")
print(f"Normal Distribution CDF at x=1: {norm_dist.cdf(1)}")

print('---------------------------------------------------------------------------------------------------------')
# 6. Sampling and Random Generation
print("\nRandom Number Generation:")
# Generate random samples from distributions
normal_samples = stats.norm.rvs(loc=0, scale=1, size=5)
print("Normal Distribution Samples:", normal_samples)

print('---------------------------------------------------------------------------------------------------------')
# 7. Outlier Detection
print("\nOutlier Detection:")
# Z-score based outlier detection
z_scores = np.abs(stats.zscore(data))
outliers = np.where(z_scores > 2)
print("Outlier Indices:", outliers)