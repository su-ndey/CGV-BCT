from LAB8.Transform2D import *
import matplotlib .pyplot as plt
from LAB3.BLA import BLA

def apply_transform_to_line(x0, y0, x1, y1, *composite_matries):
    
    x_orignal, y_original = BLA(x0, y0, x1, y1)
    x_orignal = np.array(x_orignal)
    y_original = np.array(y_original)
    xes, yes = Transform2D.apply(x_orignal, y_original, *composite_matries)
    return xes, yes


def plot_difference(x_orig, y_orig, x_transformed, y_transformed):
    
    plt.figure(figsize =(8, 6))
    plt.plot(x_transformed, y_transformed, marker="o",
    color="red", linestyle ="--", label="Transformed Line ")
    plt.plot(x_orig, y_orig, marker="*", color="blue",
    linestyle ="-", label="Original Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    


if __name__ == "__main__":
    x0, y0= 0, 0
    x1, y1 = 100, 69
    
    x_transformed, y_transformed = apply_transform_to_line(x0, y0, x1, y1,
                                                        Transform2D.translate(x0,y0),
                                                        Transform2D.scale(1,.5),
                                                        Transform2D.translate(-x0,-y0))
    
    x_orig, y_orig = BLA(x0, y0, x1, y1)
    plot_difference(x_orig, y_orig, x_transformed, y_transformed)
    plt.show()


