import sys
sys.path.insert(0, '../MEA')

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from Igloo import electricalResistance
from Summary import y1_3D_7DIV, y4_3D_7DIV, y7_3D_7DIV

style.use('ggplot')

summary_dic = {'2':y1_3D_7DIV,'3':y4_3D_7DIV,'6':y7_3D_7DIV}

width=0.0005
diameters=np.array([45,60,90,150,200,300])
diameters=diameters/(10**4)

openings=np.array(range(2,25))

fig=plt.figure()
ax1=fig.add_subplot(111)
# ax2=fig.add_subplot(212)

#the spreading resistance of a 30 um diameter electrode is 11111 OHM
ax1.plot(openings,np.array([11111]*len(openings))/(10**6),'-.',color='gray',label='Diameter 30 um (uncovered)',alpha=0.5)

#the sealing resistance of igloo structures
for d in diameters:
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for i in openings:
        j = electricalResistance(c_length=d,c_width=0.0005,openings=i)
        if (math.pi * d * 10**4)/i > 40:
            x1.append(i)
            y1.append(j)
        else:
            x2.append(i)
            y2.append(j)
    ax1.plot(x1,np.array(y1)/(10**6),label='Diameter '+str(int(d*10**4))+' um')
    ax1.scatter(x2,np.array(y2)/(10**6),marker='.')


# (opening, diameter) pairs that showed activity in previous analysis (when w = 5 um)
detectable=[(2,60),(2,150),(3,90),(3,150),(6,150)]

dic_map={45:0,60:1,90:2,150:3}

for i in detectable:
    x3=i[0]
    y3=electricalResistance(c_length=i[1]/(10**4),c_width=0.0005,openings=i[0])

    alpha = summary_dic[str(x3)]
    index = dic_map[i[1]]
    alpha = alpha[index]/100

    # ax1.plot(x3, y3/(10**6), 'r*', alpha=alpha)
    ax1.plot(x3, y3/(10**6), 'r*')
    ax1.annotate(str(int(alpha*100))+'%',(x3,y3/(10**6)),size=8.8)

ax1.plot([],[],'r*',label='Active')

not_detectable=[(2,45),(2,90),(3,45),(3,60),(6,45),(6,60),(6,90)]

for i in not_detectable:
    x4=i[0]
    y4=electricalResistance(c_length=i[1]/(10**4),c_width=0.0005,openings=i[0])
    ax1.plot(x4, y4/(10**6), 'r*')
    ax1.annotate('0%',(x4,y4/(10**6)),size=8.8)

ax1.set_xlabel('Openings (#)')
ax1.set_xticks(openings)
ax1.set_ylabel('Seal Resistance (MΩ)')
# ax1.set_title("Igloo Electrolyte Resistance (width = 5 um)")
ax1.legend(loc=0,prop={'size': 10})

# ax2.get_xaxis().set_visible(False)
# ax2.get_yaxis().set_visible(False)
# circuit=mpimg.imread('PNG/circuit.png')
# ax2.imshow(circuit,interpolation='none')

plt.show()
