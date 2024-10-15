import numpy as np
import matplotlib.pylab as plt

def gen_data(): # generates sin data with noise
    x = np.linspace(0, 10 * np.pi, num=600)
    y = 100 * np.sin(x)  + np.random.normal(scale=30, size=x.size)
    return x,y

x,y = gen_data()
plt.plot(x, y)
low_passes = [y[0]]
alpha = 0.9

def low_pass(new_value, prev_avg, alpha):
    global y
    avg = alpha * prev_avg + (1-alpha) * new_value # formula for a low pass
    return avg


for i in range(1, x.size):
    low_passes.append(low_pass(y[i], low_passes[i-1], alpha))
plt.plot(x, low_passes)
plt.show()



