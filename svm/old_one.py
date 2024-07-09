import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt

# Load original points from file
original_points = np.loadtxt("/Users/akshatkarnwal/Desktop/svm /output/original_points.txt")

# Load labels from file or generate random labels
labels = np.random.randint(2, size=len(original_points))

# Get the values of n, k, d, and epsilon
n = len(original_points)
d = original_points.shape[1]  # Number of dimensions
epsilon = 0.1  # Placeholder value for epsilon
k_min = int(24 * np.log(n) / (3 * (epsilon ** 2) - 2 * (epsilon ** 3)))

print(f"n (number of points): {n}")
print(f"d (number of dimensions): {d}")
print(f"epsilon: {epsilon}")
print(f"k_min (minimum value of k): {k_min}")

# Create SVM classifier for original points
clf_original = svm.SVC(kernel='linear')
clf_original.fit(original_points, labels)

# Get the coefficients of the hyperplane
coefficients = clf_original.coef_[0]

# Get the intercept of the hyperplane
intercept = clf_original.intercept_[0]

# Print the equation of the hyperplane
print("\nEquation of the hyperplane:")
print(" + ".join([f"({coefficients[i]:.2f} * x{i+1})" for i in range(len(coefficients))]) + f" + {intercept:.2f} = 0")

# Predict labels for original points
predicted_labels_original = clf_original.predict(original_points)

# Transform original points (example: using JL lemma)
transformed_points = np.loadtxt("/Users/akshatkarnwal/Desktop/svm /output/transformed_points.txt") # Placeholder for transformation

# Create SVM classifier for transformed points
clf_transformed = svm.SVC(kernel='linear')
clf_transformed.fit(transformed_points, labels)

# Predict labels for transformed points
predicted_labels_transformed = clf_transformed.predict(transformed_points)

# Count points that switched sides after transformation
switched_points_indices = np.where(predicted_labels_original != predicted_labels_transformed)[0]
switched_points_count = len(switched_points_indices)

print("\nNumber of points that switched sides after transformation:", switched_points_count)

# Get the indices of points that changed sides
changed_to_red_indices = switched_points_indices[predicted_labels_transformed[switched_points_indices] == 0]
changed_to_blue_indices = switched_points_indices[predicted_labels_transformed[switched_points_indices] == 1]

# Plot original points
plt.figure(figsize=(15, 5))

# Plot original points
plt.subplot(1, 3, 1)
plt.scatter(original_points[:, 0], original_points[:, 1], c=labels, cmap='coolwarm')
plt.title('Original Points')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Plot transformed points
plt.subplot(1, 3, 2)
plt.scatter(transformed_points[:, 0], transformed_points[:, 1], c=labels, cmap='coolwarm')
plt.title('Transformed Points')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Highlight points that changed sides after transformation
plt.scatter(transformed_points[switched_points_indices, 0], transformed_points[switched_points_indices, 1],
            marker='x', color='black', label='Changed Sides')
plt.legend()

# Plot points that changed to another side
plt.subplot(1, 3, 3)
plt.scatter(transformed_points[changed_to_red_indices, 0], transformed_points[changed_to_red_indices, 1],
            color='red', label='Changed to Red')
plt.scatter(transformed_points[changed_to_blue_indices, 0], transformed_points[changed_to_blue_indices, 1],
            color='blue', label='Changed to Blue')
plt.title('Points That Changed Sides')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

plt.tight_layout()
plt.show()
