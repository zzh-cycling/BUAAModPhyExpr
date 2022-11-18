from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

wavelength=[550,555,560,565,570,575,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,600,605,610,615,620]
d1=1.80
d2=1.27
dthick=[38,40,41,40,16,9,7,7,7,5,4,3,2,2,3,4,4,5,5,6,7,9,23,35,42,51,49]
dthin=[40,42,42,43,33,23,20,19,18,17,17,17,20,22,25,26,29,32,33,35,36,37,46,48,50,52,50]
coe=[]
for i in range(len(dthick)):
    coe.append((np.log(dthin[i])-np.log(dthick[i]))/(d1-d2))

# plt.plot(wavelength,dthick,label="thick glass")
# plt.plot(wavelength,dthin,label="thin glass")
# plt.xlabel("wavelength /nm")
# plt.legend()
# plt.savefig(r"E:\近代物理实验\BUAAModPhyExpr\absorption.png")

# plt.plot(wavelength,coe,label='coefficient of absorption')
# plt.savefig(r"E:\近代物理实验\BUAAModPhyExpr\absorptioncoeff.png")
# plt.show()
for i in range(len(dthin)):
    print(r'\hline',wavelength[i],'&',dthin[i],'&',wavelength[i],'&',dthick[i],'&',round(coe[i],6),r'\\')
