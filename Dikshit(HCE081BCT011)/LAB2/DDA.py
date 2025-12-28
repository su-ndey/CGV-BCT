import matplotlib.pyplot as plt

def drawDDA(x1,y1,x2,y2):
    xes, yes = [], []
    dx = x2 -x1
    dy = y2- y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx/steps
    y_inc = dy/steps
    x = x1
    y = y1
    for _ in range(steps + 1):
        xes.append(round(x))
        yes.append(round(y))
        x+= x_inc
        y+= y_inc

    return xes, yes

def plotDDA(x1, y1, x2, y2):
    x,y = drawDDA(x1,y1,x2,y2)
    plt.plot(x, y,marker = "o")
    plt.grid(True)
