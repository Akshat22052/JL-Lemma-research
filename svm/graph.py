import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Load original and transformed points
original_points = np.loadtxt('original_points.txt')
transformed_points = np.loadtxt('transformed_points.txt')


# Generate random labels for original points
num_samples = original_points.shape[0]
labels = np.random.choice([0, 1], size=num_samples)

# Classify original points into two categories using SVM
clf = svm.SVC(kernel='linear')
clf.fit(original_points[:, :2], labels)  # Considering only the first two dimensions for classification

# Predict categories for transformed points
transformed_categories = clf.predict(transformed_points[:, :2])  # Considering only the first two dimensions for prediction

# Plot original and transformed points
plt.figure(figsize=(12, 6))

# Plot original points
plt.subplot(1, 2, 1)
plt.scatter(original_points[:, 0], original_points[:, 1], c=labels, cmap=plt.cm.Paired, label='Original Points')
plt.title('Original Points')
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(label='Category')

# Plot transformed points
plt.subplot(1, 2, 2)
plt.scatter(transformed_points[:, 0], transformed_points[:, 1], c=transformed_categories, cmap=plt.cm.Paired, label='Transformed Points')
plt.title('Transformed Points')
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(label='Category')

plt.tight_layout()
plt.show()


# # import numpy as np
# # from sklearn import svm
# # import matplotlib.pyplot as plt

# # print("fucku")
# # # Load original and transformed points from files
# # original_points = np.loadtxt("original_points.txt")
# # transformed_points = np.loadtxt("transformed_points.txt")
# # print("hello ")

# # # Generate random labels for the original points
# # # This is just for demonstration purposes since you don't have the actual labels
# # labels = np.random.randint(2, size=len(original_points))
# # print("fuck2")
# # # Create SVM classifier
# # clf = svm.SVC(kernel='linear')

# # # Train the classifier on original points
# # clf.fit(original_points, labels)
# # print("fuck3")

# # # Predict labels for transformed points
# # transformed_labels = clf.predict(transformed_points)
# # print("fuck4")

# # # Separate points based on predicted labels
# # class_0_indices = np.where(transformed_labels == 0)[0]
# # class_1_indices = np.where(transformed_labels == 1)[0]
# # print("fuck5")

# # # Plot original and transformed points with different colors based on predicted labels
# # plt.figure(figsize=(12, 6))

# # # Plot original points
# # plt.subplot(1, 2, 1)
# # plt.scatter(original_points[:, 0], original_points[:, 1], c=labels, cmap=plt.cm.Paired, label='Original Points')
# # plt.title('Original Points Classified using SVM')
# # plt.xlabel('X1')
# # plt.ylabel('X2')
# # plt.colorbar(label='Category')

# # # Plot transformed points
# # plt.subplot(1, 2, 2)
# # plt.scatter(transformed_points[:, 0], transformed_points[:, 1], c=transformed_labels, cmap=plt.cm.Paired, label='Transformed Points')
# # plt.title('Transformed Points Classified using SVM')
# # plt.xlabel('X1')
# # plt.ylabel('X2')
# # plt.colorbar(label='Category')

# # plt.tight_layout()
# # plt.show()
# # print("done :)")

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import svm

# # Load original and transformed points
# original_points = np.loadtxt('/Users/akshatkarnwal/Desktop/svm /output/original_points.txt')
# transformed_points = np.loadtxt('/Users/akshatkarnwal/Desktop/svm /output/transformed_points.txt')

# # Create an SVM classifier
# clf = svm.SVC(kernel='linear')

# # Fit SVM model on original points to classify them into two categories
# clf.fit(original_points, np.random.choice([0, 1], size=len(original_points)))

# # Predict classes for original points
# original_classes = clf.predict(original_points)

# # Predict classes for transformed points using the same hyperplane
# transformed_classes = clf.predict(transformed_points)

# # Plot original and transformed points
# plt.figure(figsize=(12, 6))

# # Plot original points
# plt.subplot(1, 2, 1)
# plt.scatter(original_points[:, 0], original_points[:, 1], c=original_classes, cmap=plt.cm.Paired)
# plt.title('Original Points')
# plt.xlabel('X1')
# plt.ylabel('X2')

# # Plot transformed points
# plt.subplot(1, 2, 2)
# plt.scatter(transformed_points[:, 0], transformed_points[:, 1], c=transformed_classes, cmap=plt.cm.Paired)
# plt.title('Transformed Points')
# plt.xlabel('X1')
# plt.ylabel('X2')

# plt.tight_layout()
# plt.show()
