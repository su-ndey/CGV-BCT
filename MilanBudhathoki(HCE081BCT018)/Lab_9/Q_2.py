#2. Implement rotations about the X-axis and Y-axis and compare their effects with rotation about the Z-axis.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def make_cube():
    pts = np.array([
        [0,0,0,1], [1,0,0,1], [1,1,0,1], [0,1,0,1],
        [0,0,1,1], [1,0,1,1], [1,1,1,1], [0,1,1,1]
    ]).T
    return pts

def plot_cube(ax, pts, style='b-'):
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]
    xs, ys, zs = pts[0], pts[1], pts[2]
    for i,j in edges:
        ax.plot([xs[i],xs[j]],[ys[i],ys[j]],[zs[i],zs[j]],style)

def transform_points(pts, M):
    return M @ pts

theta = np.pi/6

Rx = np.array([
    [1,0,0,0],
    [0,np.cos(theta),-np.sin(theta),0],
    [0,np.sin(theta), np.cos(theta),0],
    [0,0,0,1]
])

Ry = np.array([
    [np.cos(theta),0,np.sin(theta),0],
    [0,1,0,0],
    [-np.sin(theta),0,np.cos(theta),0],
    [0,0,0,1]
])

Rz = np.array([
    [np.cos(theta),-np.sin(theta),0,0],
    [np.sin(theta), np.cos(theta),0,0],
    [0,0,1,0],
    [0,0,0,1]
])

cube = make_cube()

cube_x = transform_points(cube, Rx)
cube_y = transform_points(cube, Ry)
cube_z = transform_points(cube, Rz)

fig = plt.figure(figsize=(12,4))

ax1 = fig.add_subplot(131, projection='3d')
plot_cube(ax1, cube_x, 'r-')
ax1.set_title("Rotation about X-axis")

ax2 = fig.add_subplot(132, projection='3d')
plot_cube(ax2, cube_y, 'g-')
ax2.set_title("Rotation about Y-axis")

ax3 = fig.add_subplot(133, projection='3d')
plot_cube(ax3, cube_z, 'b-')
ax3.set_title("Rotation about Z-axis")

plt.show()
