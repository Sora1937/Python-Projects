import pandas as pd

# Load the dataset
df = pd.read_csv('School-Final-Assignments/Assignment_1/example_dataset.csv')

# Preprocessing and Feature Engineering
# Remove duplicates
df = df.drop_duplicates()

# Remove missing data
df = df.dropna()

# Calculating features
df['mean'] = (df['feature_1'] * df['feature_2'] * df['feature_3'] * df['feature_4'] * df['feature_5']) / 5
df['median'] = df.median(axis='columns')
df['sum'] = df['feature_1'] + df['feature_2'] + df['feature_3'] + df['feature_4'] + df['feature_5']
df['std'] = df[['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5']].std(axis=1)

# New features
average = df['mean']
median = df['median']
sum = df['sum']
std = df['std']

# Save the preprocessed dataset
df.to_csv('preprocessed_dataset.csv', index=False)