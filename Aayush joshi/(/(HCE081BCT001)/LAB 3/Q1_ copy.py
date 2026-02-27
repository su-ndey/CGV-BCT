#1. Implement Bresenham’s algorithm as shown.

import matplotlib.pyplot as plt
def bresenham(x0, y0, x1, y1):
    x_coords = []
    y_coords = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        x_coords.append(x)
        y_coords.append(y)
        if x == x1 and y == y1:
            break  
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return x_coords, y_coords
x0, y0, x1, y1 = 2, 2, 20, 10
x_bres, y_bres = bresenham(x0, y0, x1, y1)
plt.plot(x_bres, y_bres, 'bo-', label='Bresenham Line')
plt.title("Bresenham's Line")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()