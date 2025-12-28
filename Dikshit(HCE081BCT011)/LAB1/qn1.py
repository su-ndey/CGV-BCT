import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Calculate sine values
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Save the figure
plt.savefig("LAB1_qn1.png", dpi=300, bbox_inches="tight")
plt.close()

