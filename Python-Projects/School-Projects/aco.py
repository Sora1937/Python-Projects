import numpy as np

# Define the distance matrix
distance_matrix = np.array([
    [4, 7, 9, 2, 3],
    [1, 0, 6, 0, 8],
    [4, 2, 0, 7, 3],
    [1, 7, 6, 0, 9],
    [2, 5, 7, 9, 0]
])

# Number of cities
num_cities = distance_matrix.shape[0]

# Number of ants 
num_ants = 25

def ant_colony_optimization(num_iterations):
    # Initialize pheromone level matrix
    pheromone_level = np.ones((num_cities, num_cities))

    # Initialize heuristic information matrix
    heuristic_info = 1 / (distance_matrix + np.finfo(float).eps) # Avoid division by zero

    # Alpha and beta parameters
    alpha = 1.0 # Pheromone importance
    beta = 2.0 # Heuristic importance

    # Initialize best path and distance
    best_distance = float('inf')
    best_path = []
    best_iteration = -1 # Initialist the best _interation variable

    for iteration in range(num_iterations):
        # Initialize any paths and distances
        ant_paths = np.zeros((num_ants, num_cities), dtype=int)
        ant_distances = np.zeros(num_ants)

        for ant in range(num_ants):
            # Choose the starting city randomly
            current_city = np.random.randint(num_cities)
            visited = [current_city]

            # Construct the path
            for _ in range(num_cities - 1):
                # Calculate the selection probabilites
                selection_probs = (pheromone_level[current_city] ** alpha) * (heuristic_info[current_city] ** beta)
                selection_probs[np.array(visited)] = 0 # Set selection probabilites of visited cities to 0

                # Choose the nest city based on the selection probabilites
                next_city = np.random.choice(np.arange(num_cities), p=(selection_probs / np.sum(selection_probs)))

                # Update the path and visited list
                ant_paths[ant, _+1] = next_city
                visited.append(next_city)

                ant_distances[ant] += distance_matrix[current_city, next_city]

                # Update the current city
                current_city = next_city

            # Update the distance to return to the starting city
            ant_distances[ant] += distance_matrix[current_city, ant_paths[ant, 0]]

        # Update the pheromone level based on the ant paths
        pheromone_level *= 0.5 # Evaporation
        for ant in range(num_ants):
            for city in range(num_cities - 1):
                pheromone_level[ant_paths[ant, city], ant_paths[ant, city+1]] += 1 / ant_distances[ant]
            pheromone_level[ant_paths[ant, -1], ant_paths[ant, 0]] += 1 / ant_distances[ant]

        # Update the best path and distance if a better solution is found
        min_distance_idx = np.argmin(ant_distances)
        if ant_distances[min_distance_idx] < best_distance:
            best_distance = ant_distances[min_distance_idx]
            best_path = ant_paths[min_distance_idx]
            best_iteration = iteration # Update the best_iteration
    
    return best_path, best_distance, best_iteration

# Run the Ant Colony Optimization algorithm
num_iterations = 250 # Number of iterations
best_path, best_distance, best_iteration = ant_colony_optimization(num_iterations)

# Display the best path and distance
print("Here is the best path:", best_path)
print("Here is the best iteration:", best_iteration)