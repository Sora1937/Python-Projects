import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import scipy.sparse

# Load dataset
df = pd.read_csv('School-Final-Assignments/Assignment_4/exampledataset2.csv')

# Split data into features and labels
X = df['text']
y = df['sentiment']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text data
count_vect = CountVectorizer(lowercase=False, stop_words='english')
X_train = count_vect.fit_transform(X_train)
X_test = count_vect.transform(X_test)

# Train and predict with SVM
clf = SVC(kernel='linear').fit(X_train, y_train)

# Predict results
y_pred = clf.predict(X_test)

# Measure accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
