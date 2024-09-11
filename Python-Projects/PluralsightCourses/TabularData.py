import pandas as pd
import tensorflow as tf
import autokeras as ak
from sklearn.model_selection import train_test_split

# Set logging level to hide warnings
tf.get_logger().setLevel('ERROR')

# Set folder path
file_path = "C:/Users/Frost/Documents/GitHub/Python-Projects/PluralsightCourses/Titanic.csv"

# Read the data into a data frame
data = pd.read_csv(file_path)

# Inspect the data
print(data.head())
print(len(data))

# Split data into test and training data 
train_x, test_x = train_test_split(
    data,
    test_size = 0.2)

# Inspect the size of the data sets
print("Training size is:", len(train_x))
print("Test size is:", len(test_x))

# Pop the last column off the data frame
train_y = train_x.pop("Survived")
test_y = test_x.pop("Survived")

# Inspect the teaining data set
print("X training data:", train_x.head())
print("Y training data:", train_y.head())

# Inspect the testing data set
print("X testing data:", test_x.head())
print("Y testing data:", test_y.head())

# Create a structured data classifier
classifier = ak.StructuredDataClassifier(
    max_trials = 5)

# Train the model
classifier.fit(
    x = train_x,
    y = train_y,
    epochs = 10)

score = classifier.evaluate(
    x = test_x,
    y = test_y)

print(score[1])