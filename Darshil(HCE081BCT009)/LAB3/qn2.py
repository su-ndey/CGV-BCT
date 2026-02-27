import matplotlib.pyplot as plt

radii = [12, 18, 28, 36, 55]
colors = ['magenta', 'brown', 'black', 'red', 'green']

fig, ax = plt.subplots()

for r, c in zip(radii, colors):
    circle = plt.Circle((0, 0), r, color=c, fill=False, linewidth=2)
    ax.add_patch(circle)

ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-100, 70)
ax.set_ylim(-100, 70)

plt.grid(True)
plt.title("Concentric Circles")
plt.show()