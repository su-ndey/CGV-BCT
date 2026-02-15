#2. Draw lines for different octants and compare visually with DDA lines.

import matplotlib.pyplot as plt
def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x0, y0
    x_coords = [round(x)]
    y_coords = [round(y)]
    for _ in range(steps):
        x += x_inc
        y += y_inc
        x_coords.append(round(x))
        y_coords.append(round(y))
    return x_coords, y_coords
def bresenham(x0, y0, x1, y1):
    x_coords, y_coords = [], []
    dx, dy = abs(x1-x0), abs(y1-y0)
    sx, sy = (1 if x0<x1 else -1), (1 if y0<y1 else -1)
    err = dx - dy
    x, y = x0, y0
    while True:
        x_coords.append(x)
        y_coords.append(y)
        if x==x1 and y==y1:
            break
        e2 = 2*err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return x_coords, y_coords
lines = [
    (2, 2, 20, 10),   
    (2, 2, 10, 20),   
    (20, 10, 2, 2),   
    (10, 20, 2, 2),   
]
plt.figure(figsize=(10,8))
for i, (x0,y0,x1,y1) in enumerate(lines):
    x_dda, y_dda = dda(x0,y0,x1,y1)
    x_bres, y_bres = bresenham(x0,y0,x1,y1)
    plt.subplot(2,2,i+1)
    plt.plot(x_dda, y_dda, 'ro-', label='DDA')
    plt.plot(x_bres, y_bres, 'bo-', label='Bresenham')
    plt.title(f"Line {i+1} in Different Octant")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
plt.tight_layout()
plt.show()