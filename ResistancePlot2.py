import sys
sys.path.insert(0, '../MEA')

import math
import matplotlib.pyplot as plt
from matplotlib import style
from Igloo import electricalResistance

style.use('ggplot')

#assume width = 5 um, height = 3 um

openings=[2,3,4,6,8]
diameters=[45,60,90,150,200,300] #um, must be divided by 10^4 during resistance calculations
width=0.0005

dic={2:[],3:[],4:[],6:[],8:[]}

fig=plt.figure()
ax1=fig.add_subplot(111)

# backdrop
x_ticks=range(1,len(diameters)+1)

for i in openings:
    x1 = []
    x2 = []
    y = []
    for j in diameters:
        if (math.pi * j) / i > 40:
            x1.append(x_ticks[diameters.index(j)])
            dic[i].append(round(electricalResistance(c_length=j/(10**4),c_width=width,openings=i)/(10**6),2)) #MΩ resistance, 2 digits after decimal
        else:
            x2.append(x_ticks[diameters.index(j)])
            y.append(round(electricalResistance(c_length=j/(10**4),c_width=width,openings=i)/(10**6),2)) #MΩ resistance, 2 digits after decimal
    ax1.plot(x1,dic[i],label=str(i)+' Openings')
    ax1.scatter(x2,y,s=35,marker='.')

# print(dic)

# V17.0 Activeness
active={(150,2):'41%',(150,3):'28%',(150,6):'53%',(90,2):'0%',(90,3):'10%',(90,6):'0%',(60,2):'0%',(60,3):'0%',(45,2):'10%',(45,3):'0%'}

for i in active.keys():
    ax1.annotate(active[i],(x_ticks[diameters.index(i[0])],round(electricalResistance(c_length=i[0]/(10**4),c_width=width,openings=i[1])/(10**6),2)+0.05),color='k',size=6)
ax1.plot([],[],'k.',label='V17.0')

# V17.1 Designs
EAR_constant = 0.015*3*(10**(-4))
V17_1={'D300 S24 W5':(300,1.25),'D300 S24F6 W5':(300,1.98),'D300 S2 W5':(300,15),'D300 S12F3 W5':(300,4.1),'D300 S6 W5':(300,5),'D300 S12 W5':(300,2.5),'D200 S2 W5':(200,10),'D200 S6 W5':(200, 3.33),'D200 S12 W5':(200,1.67),'D200 S12 W5':(200,1.67)}

x=[]
y=[]
for i in V17_1.keys():
    value=V17_1[i]
    a=x_ticks[diameters.index(value[0])]
    b=value[1]/EAR_constant/(10**6)
    x.append(a)
    y.append(b)
    ax1.annotate(i, (a,b-0.066),size=6,color='gray')

ax1.scatter(x,y,s=8,marker='o',color='gray',label='V17.1')


ax1.set_xlabel('Diameter (um)')
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(diameters)
ax1.set_ylabel('Sealing Resistance (R igloo) (MΩ)')
ax1.set_title("Igloo Electrolyte Resistance (width = 5 um, height = 3 um)")
ax1.legend(prop={'size': 8})
plt.show()