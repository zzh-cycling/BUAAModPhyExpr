from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
pc=np.linspace(0,2.5,200)
E_1=pc**2*0.5/0.511
E_2=np.sqrt(pc**2+0.511**2)-0.511
pcdiscrete=[1.142,1.332,1.523,1.713,1.903]
E_3=[0.749,0.9007,1.109,1.2986,1.485]
plt.plot(pc,E_1,label="classical")
plt.plot(pc,E_2,label="relativity")
plt.scatter(pcdiscrete,E_3,label='experiment')
plt.xlabel("momentum pc/MeV")
plt.ylabel("energy /MeV")
plt.legend()
plt.savefig(r"E:\近代物理实验\BUAAModPhyExpr\betaray.png")
plt.show()