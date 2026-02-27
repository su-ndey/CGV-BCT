from LAB8.Transform2D import *
import matplotlib .pyplot as plt
from LAB3.BLA import BLA
from LAB8.qn1 import *

x0, y0= 0, 0
x1, y1 = 100, 69
x_mid = (x0 + x1)/2
y_mid = (y0 + y1)/2
x_transformed, y_transformed = apply_transform_to_line(x0, y0, x1, y1,
                                                    Transform2D.translate(x_mid,y_mid),
                                                    Transform2D.scale(1,.5),
                                                    Transform2D.translate(-x_mid,-y_mid))

x_orig, y_orig = BLA(x0, y0, x1, y1)
plot_difference(x_orig, y_orig, x_transformed, y_transformed)
plt.show()
