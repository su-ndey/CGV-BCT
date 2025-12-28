from DDA import *

def draw_rectangle(x1, y1, x2, y2):

    x3, y3 = x1, y2
    x4, y4 = x2, y1

    plotDDA(x1, y1, x3, y3)  # Left vertical
    plotDDA(x3, y3, x2, y2)  # Top horizontal
    plotDDA(x2, y2, x4, y4)  # Right vertical
    plotDDA(x4, y4, x1, y1)  # Bottom horizontal

    plt.title("Rectangle Using DDA Algorithm")
    plt.savefig("LAB2_qn1.png")

draw_rectangle(2, 3, 15, 9)
