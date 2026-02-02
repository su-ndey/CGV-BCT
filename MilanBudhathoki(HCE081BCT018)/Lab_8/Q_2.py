# Change the fixed point to the midpoint of the line and implement

import numpy as np
import matplotlib.pyplot as plt
def bresenham_line(x0, y0, x1, y1):
    xes, yes = [], []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x1 >= x0 else -1
    sy = 1 if y1 >= y0 else -1
    x, y = x0, y0
    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            xes.append(x)
            yes.append(y)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            xes.append(x)
            yes.append(y)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx
    return np.array(xes), np.array(yes)
def apply_2d_transformation(x_coords, y_coords, matrix):
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])
    transformed = matrix @ points
    return transformed[0], transformed[1]
def plot_line(x0, y0, x1, y1):
    x_orig, y_orig = bresenham_line(x0, y0, x1, y1)
    xm = (x0 + x1) / 2
    ym = (y0 + y1) / 2   
    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]
    ])
    T_to_mid = np.array([
        [1, 0, -xm],
        [0, 1, -ym],
        [0, 0, 1]
    ])
    T_back_mid = np.array([
        [1, 0, xm],
        [0, 1, ym],
        [0, 0, 1]
    ])
    composite_matrix = T_back_mid @ scaling_matrix @ T_to_mid
    x_scaled, y_scaled = apply_2d_transformation(x_orig, y_orig, composite_matrix)
    plt.plot(x_orig, y_orig, 'b*-', label="Original Line")
    plt.plot(x_scaled, y_scaled, 'ro--', label="Scaled about Midpoint")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.title("Fixed Point Scaling about Midpoint")
    plt.show()
plot_line(2, 3, 10, 8)