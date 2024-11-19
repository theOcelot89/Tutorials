# Theory
# https://www.youtube.com/watch?v=pd1OFfxik_4&list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU&index=2
# Code
# https://www.youtube.com/watch?v=jVDcRqzJIJk&list=PLWVKUEZ25V94kdT2Lh97KqB9MoLV9ZzmU&index=3

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# VARIABLES
y0 = [0,0] # 0 mRNA & 0 protein

# TIME
t = np.linspace(0, 200, 100)

# PARAMETERS
k_m = 0.2 # mRNA synthesis rate
gamma_m = 0.05  # mRNA degradation rate
k_p = 0.4 # protein synthesis rate
gamma_p = 0.1 # mRNA degradation rate

params = [k_m, gamma_m, k_p, gamma_p]

def sim(variables, t, params):

    mRNA = variables[0]
    protein = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dmdt = k_m - gamma_m * mRNA
    dpdt = k_p * mRNA - gamma_p * protein

    return [dmdt, dpdt]

# ODEs
y = odeint(sim, y0, t , args=(params,))

# plot
fig, ax = plt.subplots(1)

line1, = ax.plot(t,y[:,0], color="b", label="mRNA")
line2, = ax.plot(t,y[:,1], color="r", label="protein")

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")
ax.legend(handles=[line1,line2])

plt.show()