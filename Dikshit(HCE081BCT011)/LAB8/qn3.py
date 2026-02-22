from LAB8.Transform2D import *
import matplotlib .pyplot as plt
from LAB3.BLA import BLA
from LAB8.qn1 import *

x0, y0= 0, 0
x1, y1 = 100, 69

x_transformed, y_transformed = apply_transform_to_line(x0, y0, x1, y1,
                                                    Transform2D.rotate(45),)

x_orig, y_orig = BLA(x0, y0, x1, y1)
plot_difference(x_orig, y_orig, x_transformed, y_transformed)
plt.show()
