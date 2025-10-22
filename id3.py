from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
import numpy as np
import pandas as pd

dataset = pd.read_csv("/content/diabetes.csv")
dataset.head()
dataset.shape
features = dataset.drop(["Outcome"], axis=1)
X = np.array(features)
y = np.array(dataset["Outcome"])

X_train, X_val, y_train, y_val = train_test_split(X, y, random_state=0, test_size=0.20)
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
tree.tree_.max_depth
validation_prediction = tree.predict(X_val)
training_prediction = tree.predict(X_train)

print('Accuracy training set: ', accuracy_score(y_true=y_train, y_pred=training_prediction))
print('Accuracy validation set: ', accuracy_score(y_true=y_val, y_pred=validation_prediction))
from sklearn.tree import export_graphviz

import graphviz
feature_names = features.columns
dot_data = export_graphviz(tree, out_file=None,
                        feature_names=feature_names,
                         class_names=True,
                         filled=True, rounded=True,
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph