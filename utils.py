import matplotlib.pyplot as plt

def labelon(X, Y, xx, yy, size, color, weight):
    n = len(X)
    for i in range (n):
        number = '{:,}'.format(int(Y[i])).replace(',', '.')
        plt.annotate(
            number, xy=(X[i], Y[i]),
            xytext =(0 + xx, 0 + yy),
            textcoords="offset points",
            ha ='center', va='bottom', 
            color  = color, size = size, 
            weight = weight)