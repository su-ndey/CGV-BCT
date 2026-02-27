from qn1 import *
# Implement rotations about the X-axis and Y-axis and compare their effects with
# rotation about the Z-axis.


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


cube_polys, roof_polys = house_points()
ax.add_collection3d(Poly3DCollection(cube_polys, alpha=0.5))
ax.add_collection3d(Poly3DCollection(roof_polys, alpha=0.7))


# Rotate about x-axis  BLUE
transform = (
    Transform3D.translate(2,2,0),
    Transform3D.rotate_about_x(45),
)
cube_polys_t, roof_polys_t = transformed_house_points(*transform)
ax.add_collection3d(Poly3DCollection(cube_polys_t, alpha=0.5, shade=True, facecolors='blue', edgecolors='black'))
ax.add_collection3d(Poly3DCollection(roof_polys_t, alpha=0.7, shade=True, facecolors='blue', edgecolors='black'))

# Rotate about y-axis  RED
transform = (
    Transform3D.translate(0,4,2),
    Transform3D.rotate_about_y(45),
)
cube_polys_t, roof_polys_t = transformed_house_points(*transform)
ax.add_collection3d(Poly3DCollection(cube_polys_t, alpha=0.5, shade=True, facecolors='red', edgecolors='black'))
ax.add_collection3d(Poly3DCollection(roof_polys_t, alpha=0.7, shade=True, facecolors='red', edgecolors='black'))

# Rotate about z-axis  GREEN
transform = (
    Transform3D.translate(2, 0, 2),
    Transform3D.rotate_about_z(45),
)
cube_polys_t, roof_polys_t = transformed_house_points(*transform)
ax.add_collection3d(Poly3DCollection(cube_polys_t, alpha=0.5, shade=True, facecolors='green', edgecolors='black'))
ax.add_collection3d(Poly3DCollection(roof_polys_t, alpha=0.7, shade=True, facecolors='green', edgecolors='black'))


ax.set_xlim(0,6)
ax.set_ylim(0,6)
ax.set_zlim(0,6)

plt.savefig("LAB9_qn2.png")
