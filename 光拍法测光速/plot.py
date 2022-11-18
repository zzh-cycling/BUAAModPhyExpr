from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

t=1
omega1=10
omega2=12
c=5
E=1
k1=omega1/c
k2=omega2/c
phi1=0
phi2=np.pi/4
x=np.linspace(1,10*np.pi,500)
E1=E*np.cos(omega1*t-k1*x+phi1)
E2=E=np.cos(omega2*t-k2*x+phi2)
E3=E1+E2
E4=2*E*np.cos((omega1-omega2)/2*(t-x/c)+(phi1-phi2)/2)
E5=np.cos((omega1+omega2)/2*(t-x/c)+(phi1+phi2)/2)

plt.subplot(311)
plt.plot(x,E1,label=r'$E1$')
plt.legend()
plt.ylabel(r'$E/m$')

plt.subplot(312)
plt.plot(x,E2,label=r'$E2$')
plt.legend()
plt.ylabel(r'$E/m$')

plt.subplot(313)
plt.plot(x,E3,label=r'$E_{total}$')
# plt.plot(x,E4)
# plt.plot(x,E5)
plt.legend()
plt.xlabel(r'$x/m$')
plt.ylabel(r'$E/m$')
plt.savefig('./beat.pdf')
plt.show()