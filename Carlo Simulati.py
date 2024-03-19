import numpy as np
import matplotlib.pyplot as plt

# Define a function to integrate (e.g., circle quadrant)
def func(x, y):
    return x**2 + y**2 <= 1

# Number of random points
N = 1000

# Generate random points within a square [-1, 1] x [-1, 1]
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

# Count points inside the circle quadrant
inside_circle = func(x, y)
pi_estimate = 4 * np.sum(inside_circle) / N

# Plot the points and the circle quadrant
plt.scatter(x[inside_circle], y[inside_circle], color='blue', label='Inside circle')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', label='Outside circle')
circle = plt.Circle((0, 0), 1, color='green', fill=False, linestyle='--', label='Unit Circle')
plt.gca().add_patch(circle)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monte Carlo Simulation: Estimating Pi')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()

print("Estimated value of Pi:", pi_estimate)
