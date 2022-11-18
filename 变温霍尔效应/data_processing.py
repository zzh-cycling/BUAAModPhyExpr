from cProfile import label
from random import sample
import numpy as np
import matplotlib.pyplot as plt

path="E:\近代物理实验\BUAAModPhyExpr\变温霍尔效应\magnetic.txt"
data=np.genfromtxt(path)
path2="E:\近代物理实验\BUAAModPhyExpr\变温霍尔效应\potential_B.txt"
data2=np.genfromtxt(path2)

temp=[]
temp1=[]
sample_potential=[]
Hall_coefficient=[]
sample_current=[]
Hall_potential=[]
Magnetic_field=[]
stimulated_current=[]
sigma=[]

for i in range(1,len(data)):
    temp.append(data[i][1])
    temp1.append(1/data[i][1])
    sample_potential.append(data[i][2])
    sample_current.append(data[i][3])
    Hall_potential.append(data[i][4])
    Magnetic_field.append(data[i][5])
    stimulated_current.append(data[i][6])
    Hall_coefficient.append(data[i][4]*0.1/(data[i][3]*data[i][5]))
    sigma.append(data[i][3]/data[i][2])

B=[]
E_Hall=[]
R_H=[]
I=[]

for i in range(1,len(data2)):
    B.append(data2[i][5])
    E_Hall.append(data2[i][4])
    I.append(data2[i][3])
    R_H.append(data2[i][4]*0.1/(data2[i][3]*data2[i][5]))

# plt.plot(temp,sample_potential,label="Relation between temperature and sample_potential")
# plt.scatter(temp,Hall_potential,label="Relation between temperature and Hall_potential")
plt.scatter(temp1,sigma,label="Conductivity and temperature")
plt.xlabel(r'$\frac{1}{T} K^{-1}$')
plt.ylabel(r'Conductivity $S·cm^-1$')
# plt.scatter(B,R_H,label="Hall_coefficient and Magnetic field")
plt.legend()
plt.show()





