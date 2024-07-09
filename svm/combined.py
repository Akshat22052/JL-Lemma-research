import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Function to generate random points
def generate_random_points(n, d):
    np.random.seed(0)
    return np.random.randn(n, d)

# Generate random points
n = int(input("Enter the number of points (n): "))
d = int(input("Enter the number of dimensions (d): "))
original_points = generate_random_points(n, d)

# Generate random labels for the original points
labels = np.random.randint(2, size=len(original_points))

# Create SVM classifier
clf = svm.SVC(kernel='linear')

# Train SVM model on original points
clf.fit(original_points, labels)

# Predict classes for original points
predicted_labels = clf.predict(original_points)

# Apply Johnson-Lindenstrauss Lemma transformation
epsilon = float(input("Enter the value of epsilon (between 0 and 1): "))
k = int(input("Enter the number of dimensions after transformation (k): "))

# Calculate minimum number of dimensions
k_min = int(24 * np.log(n) / (3 * epsilon**2 - 2 * epsilon**3))
print("Minimum value of k:", k_min)

# Transform original points using random projection matrix
projection_matrix = np.random.randn(d, k) / np.sqrt(d)  # Correct dimensions
transformed_points = np.dot(original_points, projection_matrix)

# Predict classes for transformed points using the same hyperplane
transformed_classes = clf.predict(transformed_points)

# Find points whose classification changed after transformation
changed_points = np.sum(predicted_labels != transformed_classes)

print("Number of points whose classification changed after transformation:", changed_points)

# Plot original points with different colors based on predicted labels
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(original_points[:, 0], original_points[:, 1], c=predicted_labels, cmap=plt.cm.Paired)
plt.title('Original Points')
plt.xlabel('X1')
plt.ylabel('X2')

# Plot transformed points with different colors based on predicted classes
plt.subplot(1, 2, 2)
plt.scatter(transformed_points[:, 0], transformed_points[:, 1], c=transformed_classes, cmap=plt.cm.Paired)
plt.title('Transformed Points')
plt.xlabel('X1')
plt.ylabel('X2')

plt.tight_layout()
plt.show()
