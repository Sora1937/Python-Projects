import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # Ignores TensorFlow CPU instruction warning

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import random

# Define the number of samples and features
num_samples = 100
num_features = 5

# Generate random data for the dataset
data = {
    f'feature_{i+1}': [random.uniform(0, 1) for _ in range(num_samples)]
    for i in range(num_features)
}
data['species'] = [random.choice(['cat', 'dog']) for _ in range(num_samples)]

# Create a DataFrame from the data
dataset = pd.DataFrame(data)

# Save the dataset to a CSV file
dataset.to_csv('dataset_2.csv', index=False)

# Preprocess the data
X = dataset.drop(columns=['species']) # Remove the 'species' colimn as input features
y = dataset['species'] # Set the 'species' column as the target variable
le = LabelEncoder() # Initialize the label encoder
y = le.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(10, activation='relu'))
model.add(Dense(len(le.classes_), activation='softmax'))

# Compile and train the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train.values, y_train, epochs=10, batch_size=32)

_, accuracy = model.evaluate(X_test.values, y_test)
print(f'Accuracy: {accuracy}')