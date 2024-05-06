# Theory
# https://www.youtube.com/watch?v=Lw7U9-VD6OQ&list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU&index=4
# Code
# https://www.youtube.com/watch?v=pQodbIyaBK0&list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU&index=5

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# VARIABLES
y0 = [0,0] # 0 G1, 0 G2 

# TIME
t = np.linspace(0,200,100)

# PARAMETERS
k1 = 0.5
gamma_1 = 0.1
k2 = 0.5
gamma_2 = 0.05
n = 5
c = 5

params = [k1, gamma_1, k2, gamma_2, c, n]

def sim(variables, t, params):

    G1 = variables[0]
    G2 = variables[1]

    k1 = params[0]
    gamma_1 = params[1]
    k2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    c =params[5]

    dG1dt = k1 - gamma_1 * G1
    dG2dt = (G1**n / (c**n + G1**n)) * k2 - gamma_2 * G2

    return ([dG1dt, dG2dt])

# SIMULATION

y = odeint(sim, y0, t, args=(params,))

# PLOTS
fig, ax = plt.subplots(1)

line1, = ax.plot(t,y[:,0], color="b", label="G1")
line2, = ax.plot(t,y[:,1], color="r", label="G2")

ax.set_ylabel("Number")
ax.set_xlabel("Time")
ax.legend(handles=[line1,line2])

plt.show()


