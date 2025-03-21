import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the dataset (assuming you have 'readingSkills.csv' or equivalent)
try:
    reading_skills = pd.read_csv("readingSkills.csv") #replace with your file path if needed.
except FileNotFoundError:
    print("Error: readingSkills.csv not found. Please ensure the file is in the correct location.")
    exit()

# Select the first 105 rows
input_data = reading_skills.iloc[:105]

# Prepare the data for scikit-learn
X = input_data[["age", "shoeSize", "score"]]  # Features
y = input_data["nativeSpeaker"]  # Target variable

# Create the decision tree classifier
output_tree = DecisionTreeClassifier()

# Train the tree
output_tree.fit(X, y)

# Plot the tree
plt.figure(figsize=(12, 8))  # Adjust figure size as needed
plot_tree(output_tree, feature_names=["age", "shoeSize", "score"], class_names=sorted(input_data["nativeSpeaker"].unique()), filled=True)
plt.title("Decision Tree")
plt.savefig("decision_tree.png")
plt.show()