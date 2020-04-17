import sys
sys.path.insert(0, '../MEA')

import math
import numpy as np
import matplotlib.pyplot as plt
from Igloo import electricalResistance, JNnoise

width=0.0005
diameters=np.array([45,60,90,150,200,300])
diameters=diameters/(10**4)

openings=np.array(range(2,25))

C_O1 = 8 * 10**(-10)

fig=plt.figure()
ax1=fig.add_subplot(211)
ax2=fig.add_subplot(212)

for d in diameters:
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for i in openings:
        j = electricalResistance(c_length=d,c_width=0.0005,openings=i)
        V = C_O1 * j
        V_n = JNnoise(j)
        SNR=V/V_n
        if (math.pi * d * 10**4)/i > 40:
            x1.append(i)
            y1.append(V)
            x3.append(i)
            y3.append(SNR)
        else:
            x2.append(i)
            y2.append(V)
            x4.append(i)
            y4.append(SNR)
    ax1.plot(x1,np.array(y1)*1000,label='Diameter '+str(int(d*10**4))+' um')
    ax1.scatter(x2,np.array(y2)*1000,marker='.')
    ax2.plot(x3,y3,label='Diameter '+str(int(d*10**4))+' um')
    ax2.scatter(x4,y4,marker='.')

ax1.set_xlabel('Openings (#)')
ax1.set_xticks(openings)
ax1.set_ylabel('R_igloo Voltage (mV)')
ax1.legend(prop={'size': 10})

ax2.set_xlabel('Openings (#)')
ax2.set_xticks(openings)
ax2.set_ylabel('R_igloo SNR (thermal)')
ax2.legend(prop={'size': 10})

fig.suptitle("Igloos (width = 5 um, bandwidth = 3500 Hz, 1st order approximation current = 0.8 nA)")

plt.show()

