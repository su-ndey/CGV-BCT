#3. Compare the number of integer additions and multiplications used by DDA andBresenham.

import matplotlib.pyplot as plt
def dda_count_ops(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps
    additions = multiplications = 0
    x, y = x0, y0
    for _ in range(steps):
        x += x_inc
        y += y_inc
        additions += 2
        multiplications += 2
    return additions, multiplications
def bresenham_count_ops(x0, y0, x1, y1):
    additions = multiplications = 0
    dx, dy = abs(x1-x0), abs(y1-y0)
    sx, sy = (1 if x0<x1 else -1), (1 if y0<y1 else -1)
    err = dx - dy
    x, y = x0, y0
    while True:
        if x == x1 and y == y1:
            break
        e2 = 2*err
        multiplications += 1
        additions += 1
        if e2 > -dy:
            err -= dy
            x += sx
            additions += 2
        if e2 < dx:
            err += dx
            y += sy
            additions += 2
    return additions, multiplications
x0, y0, x1, y1 = 2, 2, 20, 10
dda_add, dda_mul = dda_count_ops(x0, y0, x1, y1)
bres_add, bres_mul = bresenham_count_ops(x0, y0, x1, y1)
labels = ['Additions', 'Multiplications']
dda_ops = [dda_add, dda_mul]
bres_ops = [bres_add, bres_mul]
x = range(len(labels))
plt.figure(figsize=(8,5))
plt.bar([p-0.15 for p in x], dda_ops, width=0.3, label='DDA', color='red')
plt.bar([p+0.15 for p in x], bres_ops, width=0.3, label='Bresenham', color='blue')
plt.xticks(x, labels)
plt.ylabel('Number of Operations')
plt.title('Comparison of DDA vs Bresenham Operations')
plt.legend()
plt.grid(axis='y')
plt.show()