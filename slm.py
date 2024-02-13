from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target variable (species)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier with maximum depth of 3
model = DecisionTreeClassifier(max_depth=3)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance (accuracy)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree (optional)
from sklearn.tree import plot_tree
plot_tree(model, feature_names=iris.feature_names)





from transformers import pipeline

# Create a pipeline using the "question-answering" task and the desired model
question_answering = pipeline(task="question-answering", model="sasha1keshten/finetune-BERT-squad")

# Prepare the context and question
context = "France is a country in Western Europe. Its capital is Paris."
question = "What is the capital of France?"

# Pass the context and question to the pipeline for analysis
answer = question_answering(question=question, context=context)

# Print the answer and its score
print(f"Answer: {answer['answer']}")
print(f"Score: {answer['score']}")
