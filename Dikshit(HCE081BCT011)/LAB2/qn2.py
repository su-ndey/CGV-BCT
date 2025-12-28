from DDA import *

def draw_axes(length=20):
    plt.figure(figsize=(6, 6))
    
    # X-axis (horizontal)
    plotDDA(-length, 0, length, 0)
    # Y-axis (vertical)
    plotDDA(0, -length, 0, length)
    
    plt.title("Simple Coordinate System using DDA")
    plt.axis('equal')
    plt.savefig("LAB2_qn2.png", dpi=300, bbox_inches='tight')
    plt.close()

draw_axes(20) # axis of length 20
