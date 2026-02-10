from qn1_a import liang_barsky
import matplotlib . pyplot as plt

def draw(original , clipped , xmin , ymin , xmax , ymax):
    plt . plot ([xmin, xmax, xmax, xmin, xmin],
                [ymin, ymin, ymax, ymax, ymin])
    x1 , y1 , x2 , y2 = original
    plt.plot([ x1 , x2 ] ,[ y1 , y2 ] ,"--")
    if clipped != None :
        cx1, cy1, cx2, cy2 = clipped
        plt.plot([ cx1 , cx2 ] ,[ cy1 , cy2 ])


xmin = 10
ymin = 10
xmax = 100
ymax = 100
original = (0 , 0 , 120 , 120)
clipped = liang_barsky (0 , 0 , 120 , 120 , xmin , ymin , xmax , ymax )
draw( original , clipped , xmin , ymin , xmax , ymax )

plt.axis("equal")
plt.grid(True)
plt.savefig("qn1(b)")