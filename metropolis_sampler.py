import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import random

def target(x):
    return 0.3*np.exp(-(x+3)**2) + np.exp(-(x-2)**2/0.5)

x = np.linspace(-6,6,1000)

##MCMC
n = 100000
pos = 0
samples = []
burn_in = 100
step_size = 1.2


for i in range(n):
    new = pos+ np.random.normal(0,step_size)
    if target(new) > target(pos):
        pos = new
    else:
        prob = target(new)/target(pos)
        if(random.random()<=prob):
            pos = new
    
    if(i>burn_in):
        samples.append(pos)

y = target(x)
y = y / np.trapezoid(y, x)
plt.plot(x, y, label="target")
plt.hist(samples, bins=100, density=True, alpha=0.5, label="Markov Chain Monte Carlo sim")
plt.legend()
plt.show()