from Transform3D import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

cube_faces = [
    [0,1,2,3], # point 0, 1, 2, 3 indeces of x_cube, y_cube, z_cube (bottom face)
    [4,5,6,7], # point 4, 5, 6, 7 indeces of x_cube, y_cube, z_cube (top face)
    [0,1,5,4], # point 0, 1, 5, 4 indeces of x_cube, y_cube, z_cube (front face)
    [2,3,7,6], # point 2, 3, 7, 6 indeces of x_cube, y_cube, z_cube (back face)
    [1,2,6,5], # point 1, 2, 6, 5 indeces of x_cube, y_cube, z_cube (right face)
    [0,3,7,4]  # point 0, 3, 7, 4 indeces of x_cube, y_cube, z_cube (left face)
]

roof_faces = [
    [0,1,4],
    [1,2,4],
    [2,3,4],
    [3,0,4]
]

x_cube = [0, 1, 1, 0, 0, 1, 1, 0]
y_cube = [0, 0, 1, 1, 0, 0, 1, 1]
z_cube = [0, 0, 0, 0, 1, 1, 1, 1]

x_roof = [0,1,1,0, 0.5]
y_roof = [0,0,1,1, 0.5]
z_roof = [1,1,1,1, 1.8]

def house_points():

    cube_vertices = list(zip(x_cube, y_cube, z_cube))
    cube_polys = [[cube_vertices[i] for i in face] for face in cube_faces]
    
    roof_vertices = list(zip(x_roof, y_roof, z_roof))
    roof_polys = [[roof_vertices[i] for i in face] for face in roof_faces]
    
    return cube_polys, roof_polys

def transformed_house_points(*transform):
    x_cube_t, y_cube_t, z_cube_t = Transform3D.apply(x_cube, y_cube, z_cube, *transform)
    x_roof_t, y_roof_t, z_roof_t = Transform3D.apply(x_roof, y_roof, z_roof, *transform)
    
    cube_vertices_t = list(zip(x_cube_t, y_cube_t, z_cube_t))
    cube_polys_t = [[cube_vertices_t[i] for i in face] for face in cube_faces]
    
    roof_vertices_t = list(zip(x_roof_t, y_roof_t, z_roof_t))
    roof_polys_t = [[roof_vertices_t[i] for i in face] for face in roof_faces]
    
    return cube_polys_t, roof_polys_t





# Composite: Scale → Rotate Y → Rotate Z → Translate
transform = (
    Transform3D.translate(2,2,0),
    Transform3D.scale(2,2,2)
)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


cube_polys, roof_polys = house_points()
ax.add_collection3d(Poly3DCollection(cube_polys, alpha=0.5))
ax.add_collection3d(Poly3DCollection(roof_polys, alpha=0.7))

cube_polys_t, roof_polys_t = transformed_house_points(*transform)
ax.add_collection3d(Poly3DCollection(cube_polys_t, alpha=0.5))
ax.add_collection3d(Poly3DCollection(roof_polys_t, alpha=0.7))


ax.set_xlim(0,6)
ax.set_ylim(0,6)
ax.set_zlim(0,6)

plt.savefig("LAB9_qn1.png")
