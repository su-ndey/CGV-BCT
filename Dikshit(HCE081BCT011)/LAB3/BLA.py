import matplotlib.pyplot as plt

def BLA(x1,y1,x2,y2):
    xes, yes = [], []
    
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    x_inc =  1 if x2 >= x1 else -1
    y_inc = 1 if y2 >= y1 else -1
    x, y = x1, y1

    if dx >= dy:
        p = 2*dy - dx
        for _ in range(dx+1):
            xes.append(x)
            yes.append(y)
            x +=x_inc
            if p >=0:
                y += y_inc
                p = p + 2 * dy - 2 * dx
            else:
                p = p + 2 * dy
    else:
        p = 2*dx - dy
        for _ in range(dy+1):
            xes.append(x)
            yes.append(y)
            y += y_inc
            if p >= 0:
                x += x_inc
                p = p + 2 * dx - 2 * dy
            else:
                p = p + 2 * dx
    
    return xes, yes

     
def plotBLA(x1, y1, x2, y2):
    xes, yes = BLA(x1, y1, x2, y2)
    plt.plot(xes, yes, marker="o")
    plt.grid(True)
