import sys
sys.path.insert(0, '../MEA')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from SpikeAnalysis import analyzeByDesign
from matplotlib import style

style.use('ggplot')

fig=plt.figure()
ax1=fig.add_subplot(331)
ax2=fig.add_subplot(332)
ax3=fig.add_subplot(333)
ax4=fig.add_subplot(334)
ax5=fig.add_subplot(335)
ax6=fig.add_subplot(336)
ax7=fig.add_subplot(337)
ax8=fig.add_subplot(338)
ax9=fig.add_subplot(339)

# 5DIV
# pick2D = 'DataframePickle/df2D16449_5DIV.pickle'
# pick3D = 'DataframePickle/df3D17316_5DIV.pickle'

# 7DIV
pick2D = 'DataframePickle/df2D17326_7DIV.pickle'
pick3D = 'DataframePickle/df3D17320_7DIV.pickle'

pd2D=analyzeByDesign(pick2D,"ExcelFiles/locations_final.xlsx",param='Name',skiprow=1)
pd3D=analyzeByDesign(pick3D,"ExcelFiles/locations_final.xlsx",param='Name',skiprow=1)

x=[10,20,30,40]
x_ticks=['45', '60', '90', '150']
l=[('S2 W5'),('S2 W7,5'),('S3 W5'),('S3 W7,5'),('S6 W5'),('S6 W7,5')]

y1_2D=list(pd2D.loc[[i for i in pd2D.index if 'S2 W5' in i]]['Active Percent (%)'])
y1_2D.append(y1_2D[0])
y1_2D.pop(0)

y1_3D=list(pd3D.loc[[i for i in pd3D.index if 'S2 W5' in i]]['Active Percent (%)'])
y1_3D.append(y1_3D[0])
y1_3D.pop(0)

y2_2D=list(pd2D.loc[[i for i in pd2D.index if 'S2 W7,5' in i]]['Active Percent (%)'])
y2_2D.append(y2_2D[0])
y2_2D.pop(0)

y2_3D=list(pd3D.loc[[i for i in pd3D.index if 'S2 W7,5' in i]]['Active Percent (%)'])
y2_3D.append(y2_3D[0])
y2_3D.pop(0)

y4_2D=list(pd2D.loc[[i for i in pd2D.index if 'S3 W5' in i]]['Active Percent (%)'])
y4_2D.append(y4_2D[0])
y4_2D.pop(0)

y4_3D=list(pd3D.loc[[i for i in pd3D.index if 'S3 W5' in i]]['Active Percent (%)'])
y4_3D.append(y4_3D[0])
y4_3D.pop(0)

y5_2D=list(pd2D.loc[[i for i in pd2D.index if 'S3 W7,5' in i]]['Active Percent (%)'])
y5_2D.append(y5_2D[0])
y5_2D.pop(0)

y5_3D=list(pd3D.loc[[i for i in pd3D.index if 'S3 W7,5' in i]]['Active Percent (%)'])
y5_3D.append(y5_3D[0])
y5_3D.pop(0)

y7_2D=list(pd2D.loc[[i for i in pd2D.index if 'S6 W5' in i]]['Active Percent (%)'])
y7_2D.append(y7_2D[0])
y7_2D.pop(0)

y7_3D=list(pd3D.loc[[i for i in pd3D.index if 'S6 W5' in i]]['Active Percent (%)'])
y7_3D.append(y7_3D[0])
y7_3D.pop(0)

y8_2D=list(pd2D.loc[[i for i in pd2D.index if 'S6 W7,5' in i]]['Active Percent (%)'])
y8_2D.append(y8_2D[0])
y8_2D.pop(0)

y8_3D=list(pd3D.loc[[i for i in pd3D.index if 'S6 W7,5' in i]]['Active Percent (%)'])
y8_3D.append(y8_3D[0])
y8_3D.pop(0)

ax1.bar(np.array(x)-1,y1_2D,label='2D',width=3,align='center')
ax1.bar(np.array(x)+1,y1_3D,label='3D',width=3,align='center')
ax1.set_xticks([10,20,30,40])
ax1.set_xticklabels(x_ticks,size=4)
ax1.set_yticks([50,100])
ax1.set_yticklabels([50,100],size=4)
ax1.legend(fontsize=4,loc=1)
ax1.set_xlabel('Diameter (um)',size=5)
ax1.xaxis.set_label_coords(0.5, -0.05)
ax1.set_ylabel('Active (%)',size=5)
ax1.yaxis.set_label_coords(-0.05, 0.5)
ax1.set_title('W5 O2',size=5,y=0.90)

ax2.bar(np.array(x)-1,y2_2D,label='2D',width=3,align='center')
ax2.bar(np.array(x)+1,y2_3D,label='3D',width=3,align='center')
ax2.set_xticks([10,20,30,40])
ax2.set_xticklabels(x_ticks,size=4)
ax2.set_yticks([50,100])
ax2.set_yticklabels([50,100],size=4)
ax2.legend(fontsize=4,loc=1)
ax2.set_xlabel('Diameter (um)',size=5)
ax2.xaxis.set_label_coords(0.5, -0.05)
ax2.set_ylabel('Active (%)',size=5)
ax2.yaxis.set_label_coords(-0.05, 0.5)
ax2.set_title('W7.5 O2',size=5,y=0.90)

ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
opening2=mpimg.imread('PNGFiles/2.png')
ax3.imshow(opening2)

ax4.bar(np.array(x)-1,y4_2D,label='2D',width=3,align='center')
ax4.bar(np.array(x)+1,y4_3D,label='3D',width=3,align='center')
ax4.set_xticks([10,20,30,40])
ax4.set_xticklabels(x_ticks,size=4)
ax4.set_yticks([50,100])
ax4.set_yticklabels([50,100],size=4)
ax4.legend(fontsize=4,loc=1)
ax4.set_xlabel('Diameter (um)',size=5)
ax4.xaxis.set_label_coords(0.5, -0.05)
ax4.set_ylabel('Active (%)',size=5)
ax4.yaxis.set_label_coords(-0.05, 0.5)
ax4.set_title('W5 O3',size=5,y=0.90)

ax5.bar(np.array(x)-1,y5_2D,label='2D',width=3,align='center')
ax5.bar(np.array(x)+1,y5_3D,label='3D',width=3,align='center')
ax5.set_xticks([10,20,30,40])
ax5.set_xticklabels(x_ticks,size=4)
ax5.set_yticks([50,100])
ax5.set_yticklabels([50,100],size=4)
ax5.legend(fontsize=4,loc=1)
ax5.set_xlabel('Diameter (um)',size=5)
ax5.xaxis.set_label_coords(0.5, -0.05)
ax5.set_ylabel('Active (%)',size=5)
ax5.yaxis.set_label_coords(-0.05, 0.5)
ax5.set_title('W7.5 O3',size=5,y=0.90)

ax6.get_xaxis().set_visible(False)
ax6.get_yaxis().set_visible(False)
opening3=mpimg.imread('PNGFiles/3.png')
ax6.imshow(opening3)

ax7.bar(np.array(x)-1,y7_2D,label='2D',width=3,align='center')
ax7.bar(np.array(x)+1,y7_3D,label='3D',width=3,align='center')
ax7.set_xticks([10,20,30,40])
ax7.set_xticklabels(x_ticks,size=4)
ax7.set_yticks([50,100])
ax7.set_yticklabels([50,100],size=4)
ax7.legend(fontsize=4,loc=1)
ax7.set_xlabel('Diameter (um)',size=5)
ax7.xaxis.set_label_coords(0.5, -0.05)
ax7.set_ylabel('Active (%)',size=5)
ax7.yaxis.set_label_coords(-0.05, 0.5)
ax7.set_title('W5 O6',size=5,y=0.90)

ax8.bar(np.array(x)-1,y8_2D,label='2D',width=3,align='center')
ax8.bar(np.array(x)+1,y8_3D,label='3D',width=3,align='center')
ax8.set_xticks([10,20,30,40])
ax8.set_xticklabels(x_ticks,size=4)
ax8.set_yticks([50,100])
ax8.set_yticklabels([50,100],size=4)
ax8.legend(fontsize=4,loc=1)
ax8.set_xlabel('Diameter (um)',size=5)
ax8.xaxis.set_label_coords(0.5, -0.05)
ax8.set_ylabel('Active (%)',size=5)
ax8.yaxis.set_label_coords(-0.05, 0.5)
ax8.set_title('W7.5 O6',size=5,y=0.90)

ax9.get_xaxis().set_visible(False)
ax9.get_yaxis().set_visible(False)
opening6=mpimg.imread('PNGFiles/6.png')
ax9.imshow(opening6)

plt.annotate('Width (um)',(-1.8,-0.4),size=12,xycoords="axes fraction")
plt.annotate('5',(-2.42,-0.2),size=10,xycoords="axes fraction")
plt.annotate('7.5',(-1.0,-0.2),size=10,xycoords="axes fraction")
plt.annotate('Openings (#)',(-3.6,1.65),size=12,xycoords="axes fraction")
plt.annotate('2',(-3.15,2.86),size=10,xycoords="axes fraction")
plt.annotate('3',(-3.15,1.65),size=10,xycoords="axes fraction")
plt.annotate('6',(-3.15,0.44),size=10,xycoords="axes fraction")

fig.suptitle('2D vs. 3D Igloo Electrodes Comparison 5DIV',size=15)
# fig.suptitle('2D vs. 3D Igloo Electrodes Comparison 7DIV',size=15)

plt.show()
