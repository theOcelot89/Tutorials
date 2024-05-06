import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# theory https://www.youtube.com/watch?v=Zg9k9ijiYPA&list=PLWVKUEZ25V97W2qS7faggHrv5gdhPcgjq&index=2
# https://www.youtube.com/watch?v=2f5aRTBmm10&list=PLWVKUEZ25V97W2qS7faggHrv5gdhPcgjq&index=2

# Parameters
t = np.linspace(0,50, num=1000) #(start, end, fractions)
alpha = 1.1
beta = 0.4
gamma = 0.4
delta = 0.1

# Initial Conditions (put whichever on the odeint)
y0=[10,1] #[fish,bears]
steady_state_y0 = [gamma/delta, alpha/beta]


params = [alpha,beta,gamma,delta]

def sim(variables, t, params):

    x = variables[0] # fish population
    y = variables[1] # bear population

    alpha, beta, gamma, delta = params # unpacking params

    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y

    return dxdt, dydt

# solve
y = odeint(sim, steady_state_y0, t, args=(params,))


# plot population dynamics
fig, (ax1,ax2) = plt.subplots(2)
ax1.plot(t,y[:,0], color="b")
# ax1.plot(t,y[:,1], color="g")
ax2.plot(t,y[:,1], color="r")

ax1.set_ylabel('Fish')
ax2.set_ylabel('Bears')
ax2.set_xlabel("Time")


# plot relationship between populations
fig, axs =plt.subplots(2)
axs[0].plot(y[:,0],y[:,1])
axs[0].set_xlabel("Fish")
axs[0].set_ylabel('Bears')
plt.show()
