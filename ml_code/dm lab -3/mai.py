
import numpy as np # 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load the IRIS dataset and select the specific attributes
iris = load_iris()
X = iris.data[:, [0, 3]]  # Select Sepal Length and Petal Width

# (a) Find all the principal components
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)

# (b) Scatter plot of mean-centered data
X_centered = X - np.mean(X, axis=0)
plt.scatter(X_centered[:, 0], X_centered[:, 1], label='Mean Centered Data')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')

# (c) Show all the principal components on the same plot
for i, (length, vector) in enumerate(zip(pca.explained_variance_, pca.components_)):
    v = vector * 3 * np.sqrt(length)
    plt.quiver(*np.mean(X, axis=0), v[0], v[1], color='r', scale=1, scale_units='xy', angles='xy', label=f'PC{i+1}')

plt.legend()
plt.show()

# (d) Project samples onto the first principal component
X_proj = X_pca[:, 0]  # First principal component
plt.scatter(X_proj, np.zeros_like(X_proj), label='Projected Samples')
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.3, label='Original PCA Data')
plt.xlabel('1st Principal Component')
plt.legend()
plt.show()

# (e) Function to compute number of PCs required to capture p% variance
def required_pcs(p):
    cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
    num_pcs = np.argmax(cumulative_variance >= p / 100) + 1
    return num_pcs

# Example: Find the number of PCs for 96% variance
p = 96
num_pcs = required_pcs(p)
print(f'Number of PCs required to capture {p}% variance: {num_pcs}')

p = 97
num_pcs = required_pcs(p)
print(f'Number of PCs required to capture {p}% variance: {num_pcs}')

p = 98
num_pcs = required_pcs(p)
print(f'Number of PCs required to capture {p}% variance: {num_pcs}')
