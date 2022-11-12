from sympy.physics.qho_1d import psi_n
from sympy import var
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(-3, 3), ylim=(0, 1))
plt.ylabel('probability')
line, = ax.plot([], [],color='green', lw=2)
x = np.linspace(-3, 3, 500)

# initialization function: plot the background of each frame
def init():  # only required for blitting to give a clean slate.
    line.set_data([], [])
    return line,

def animate(i):
    omega=0.01
    psi_t=np.exp(-1j*omega*i/2)*(0.8*np.sqrt(2)*x*np.exp(-x**2/(2.))*np.exp(-1j*omega*i)/(np.pi**(1/4)) + 0.6*np.exp(-x**2/(2.))/(np.pi**(1/4)))
    y=np.abs(psi_t)**2
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=314, interval=30, blit=True)
anim.save('superposition.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#psi_t=np.exp(-1j*omega*i/2)(0.8*sqrt(2)*x*(m*omega)**(3/4)*np.exp(-m*omega*x**2/(2*hbar))*np.exp(-1j*omega*i)/(hbar**(3/4)*pi**(1/4)) + 0.6*(m*omega)**(1/4)*np.exp(-m*omega*x**2/(2*hbar))/(hbar**(1/4)*pi**(1/4)))

plt.show()
