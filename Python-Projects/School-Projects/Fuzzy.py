import numpy as np
import skfuzzy as fuzz

# Accept user input 
user_input = input("Enter a value between 0 and 10: ")
input_value = float(user_input)

# Input variables 
x = np.arange(0, 11, 1) # Input range rom 0 to 10

# Define fuzzy sets for the input variable
low = fuzz.trimf(x, [0, 0, 5]) # Triangular fuzzy set for low values
medium = fuzz.trimf(x, [2, 5, 8]) # Triangular fuzzy set for medium values
high = fuzz.trimf(x, [5, 10, 10]) #Triangular fuzzy set for high values

# Get membership values for input_value
low_degree = fuzz.interp_membership(x, low, input_value)
medium_degree = fuzz.interp_membership(x, medium, input_value)
high_degree = fuzz.interp_membership(x, high, input_value)

# Define fuzzy rules
rule1 = np.fmax(low_degree, medium_degree) #Rule: if input is low or medium, then output is high
rule2 = np.fmin(medium_degree, high_degree) # Rule: if input is medium and high, then output is low

# Apply fuzzy rules to determine the fuzzy relation between input and output
relation = np.fmax(rule1, rule2)

# Aggregated = np.fmax(low, relation)
aggregated = np.fmax(low, relation)
activated = np.fmin(aggregated, medium)

# Defuzzify the relation toobtain a crisp output
output = fuzz.defuzz(x, activated, 'centroid')

print("Output:", output)