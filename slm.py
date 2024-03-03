from sklearn.tree import DecisionTreeClassifier
import    numpy  as  np 
# Sample data (replace with your actual features and labels)
features = np.array([[1, 0], [2, 1], [3, 2], [4, 1], [5, 0]])
labels = np.array([1, 0, 1, 0, 1])

# Create and train the decision tree classifier
clf = DecisionTreeClassifier(criterion="gini", max_depth=3)  # Adjust parameters as needed
clf.fit(features, labels)

# Make predictions on new data
new_data = np.array([[6, 1]])
prediction = clf.predict(new_data)

# Print the prediction
print("Predicted class:", prediction[0])
