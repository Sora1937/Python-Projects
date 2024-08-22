import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('School-Final-Assignments/Assignment_2/exampledataset1.csv')

# Split the dataset into features (X) and target (y)
X = df.drop('Target', axis=1)
y = df['Target']

# Split the data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=16)

# TODO: Write code to initialize the logistic regression mode
lrm = LogisticRegression(random_state=16)

# Train the Model
# TODO: Write code to make predictions on the testing set using the trained model
lrm.fit(X_train, y_train)

y_pred = lrm.predict(X_test)

# Evaluate the model's performance
# TODO: Write code to calculate and print the accuracy score of the model's predictions
result = accuracy_score(y_test, y_pred)
print(result)