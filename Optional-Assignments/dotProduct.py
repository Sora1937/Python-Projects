def dot_product(x, y):
    # Ensure vectors are the same length
    if len(x) != len(y):
        raise ValueError("Vectors must be of the same length")
    
    # Calculate the dot product
    return sum(v1 * v2 for v1, v2 in zip(x, y))

vec1 = [1, 2 ,3]
vec2 = [4, 5, 6]

result = dot_product(vec1, vec2)
print("Dot Product:", result)