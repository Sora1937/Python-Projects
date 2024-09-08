import pandas as pd
import tensorflow as tf
from keras import layers, models
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the csv file
df = pd.read_csv('Datasets/Dataset_1.csv')

# Dropping empty cells
df = df.dropna()

# Convert categorical variables to one-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Define features (X) and target (y)
X = df.iloc[:, :-1].values  # Features (everything except the last column)
y = df.iloc[:, -1].values   # Target (last column)

# Standardize the feature data (only X, not y)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Get the number of features in the dataset
input_shape = X_train.shape[1]  # Number of features

# 1. Define the model
model = models.Sequential()

# Input layer matching the feature count
model.add(layers.InputLayer(input_shape=(input_shape,)))

# 2. Add a dense layer with 5 neurons and ReLU activation
model.add(layers.Dense(5, activation='relu'))

# 3. Add output layer for binary classification
model.add(layers.Dense(1, activation='sigmoid'))

# 4. Compile the model
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])

# 5. Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy:.2f}")
