import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data from CSV
data = pd.read_csv('Datasets\housing.csv')
X = data['RM'].values.reshape(-1, 1)  # Reshape for sklearn
y = data['PTRATIO'].values

# Using scikit-learn's LinearRegression
model = LinearRegression()
model.fit(X, y)

# Output the model parameters
print(f'Sklearn Intercept: {model.intercept_}')
print(f'Sklearn Slope: {model.coef_[0]}')

# Manually Implement Gradient Descent
learning_rate = 0.01
num_iterations = 1000
m = len(y)

# Initializing parameters (slope and intercept)
theta0 = 0  # Intercept
theta1 = 0  # Slope

# Gradient Descent
for _ in range(num_iterations):
    y_pred = theta0 + theta1 * X.flatten()
    
    d_theta0 = (1/m) * np.sum(y_pred - y)
    d_theta1 = (1/m) * np.sum((y_pred - y) * X.flatten())
    
    theta0 -= learning_rate * d_theta0
    theta1 -= learning_rate * d_theta1

# Print final parameters from Gradient Descent
print(f'Manual Gradient Descent Intercept: {theta0}')
print(f'Manual Gradient Descent Slope: {theta1}')

# Prediction for a new value using sklearn model
new_X = np.array([[6]])
predicted_y_sklearn = model.predict(new_X)
print(f'Prediction for X=6 using sklearn: y={predicted_y_sklearn[0]}')

# Prediction for a new value using manual gradient descent
predicted_y_manual = theta0 + theta1 * new_X.flatten()[0]
print(f'Prediction for X=6 using manual gradient descent: y={predicted_y_manual}')
