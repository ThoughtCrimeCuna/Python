#Levi Peachstone

import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Polygon


# ★
# Define the matrix dimensions and colors
tall = int(input("how tall?"))
wide = int(input("how wide?"))
symbols = ['⌂', '⚘', '↟', '◮']  # Symbols for each hexagon
matrix = np.random.randint(0, len(symbols), size=(tall, wide))
colors = ['aqua', 'green', 'orange', 'red']
hex_size = (tall+wide)/60  # Size of each hexagon

# Function to generate the vertices of a hexagon
def hexagon(center_x, center_y, size):
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]
    return [(center_x + size * np.cos(angle), center_y + size * np.sin(angle)) for angle in angles]

# Create a plot
fig, ax = plt.subplots(figsize=(15, 15))
ax.axis('off')  # Hide axes

# Draw hexagons and symbols
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        # Determine center positions with offset for interlocking hexagons
        x = j * (1.5 * hex_size)  # Horizontal spacing for interlocking
        y = i * (np.sqrt(3) * hex_size) + (0.5 * np.sqrt(3) * hex_size if j % 2 else 0)

        # Create hexagon and add it to plot
        hex_coords = hexagon(x, y, hex_size)
        color = random.choice(colors)  # Randomly select a color from the limited list

        # Create the hexagon patch
        hexagon_patch = Polygon(hex_coords, closed=True, edgecolor='black', fill=True, facecolor=color, linewidth=2)
        ax.add_patch(hexagon_patch)

        # Print the color for debugging purposes
        # print(f"Hexagon at ({i}, {j}) has color: {color}")  # Debug output to show colors being assigned

        # Place the symbol inside the hexagon
        ax.text(x, y, symbols[matrix[i, j]], color='black', fontsize=20, ha='center', va='center')

# Set plot limits to fit all hexagons
ax.set_xlim(-1, matrix.shape[1] * 1.5 * hex_size)
ax.set_ylim(-1, matrix.shape[0] * np.sqrt(3) * hex_size)
plt.gca().set_aspect('equal', adjustable='box')  # Keep hexagons proportionate
plt.show()
