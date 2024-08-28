import matplotlib.pyplot as plt

# Sample data points
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Create a line plot
plt.plot(x, y)

# Add title and labels
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()
