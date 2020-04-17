import sys
sys.path.insert(0, '../MEA')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from SpikeAnalysis import analyzeByDesign
from matplotlib import style
from matplotlib.ticker import FixedLocator, FixedFormatter

style.use('ggplot')

fig=plt.figure()
ax1=fig.add_subplot(331)
ax1_a=ax1.twinx()
ax2=fig.add_subplot(332)
ax2_a=ax2.twinx()
ax3=fig.add_subplot(333)

ax4=fig.add_subplot(334)
ax4_a=ax4.twinx()
ax5=fig.add_subplot(335)
ax5_a=ax5.twinx()
ax6=fig.add_subplot(336)

ax7=fig.add_subplot(337)
ax7_a=ax7.twinx()
ax8=fig.add_subplot(338)
ax8_a=ax8.twinx()
ax9=fig.add_subplot(339)


# 5DIV
pick2D_5DIV = 'DataframePickle/df2D16449_5DIV.pickle'
pick3D_5DIV = 'DataframePickle/df3D17316_5DIV.pickle'

# 7DIV
pick2D_7DIV = 'DataframePickle/df2D17326_7DIV.pickle'
pick3D_7DIV = 'DataframePickle/df3D17320_7DIV.pickle'

pd2D_5DIV=analyzeByDesign(pick2D_5DIV,"ExcelFiles/locations_final.xlsx",param='Name',skiprow=1)
pd3D_5DIV=analyzeByDesign(pick3D_5DIV,"ExcelFiles/locations_final.xlsx",param='Name',skiprow=1)

pd2D_7DIV=analyzeByDesign(pick2D_7DIV,"ExcelFiles/locations_final.xlsx",param='Name',skiprow=1)
pd3D_7DIV=analyzeByDesign(pick3D_7DIV,"ExcelFiles/locations_final.xlsx",param='Name',skiprow=1)

pd2D_5DIV.replace(0,np.NAN,inplace=True)
pd3D_5DIV.replace(0,np.NAN,inplace=True)
pd2D_7DIV.replace(0,np.NAN,inplace=True)
pd3D_7DIV.replace(0,np.NAN,inplace=True)

x=[10,20,30,40]
y=[0,50,100,150]
x_ticks=['5d   7d     5d   7d\n45', '5d   7d     5d   7d\n60', '5d   7d     5d   7d\n90', '5d   7d     5d   7d\n 150']
l=[('S2 W5'),('S2 W7,5'),('S3 W5'),('S3 W7,5'),('S6 W5'),('S6 W7,5')]

#start of 1

y1_2D_5DIV=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S2 W5' in i]]['Active Percent (%)'])
y1_2D_5DIV.append(y1_2D_5DIV[0])
y1_2D_5DIV.pop(0)

y1_2D_7DIV=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S2 W5' in i]]['Active Percent (%)'])
y1_2D_7DIV.append(y1_2D_7DIV[0])
y1_2D_7DIV.pop(0)

y1_3D_5DIV=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S2 W5' in i]]['Active Percent (%)'])
y1_3D_5DIV.append(y1_3D_5DIV[0])
y1_3D_5DIV.pop(0)

y1_3D_7DIV=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S2 W5' in i]]['Active Percent (%)'])
y1_3D_7DIV.append(y1_3D_7DIV[0])
y1_3D_7DIV.pop(0)

y1_2D_5DIV_a=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S2 W5' in i]]['Amplitude l (uV)'])
y1_2D_5DIV_a.append(y1_2D_5DIV_a[0])
y1_2D_5DIV_a.pop(0)

y1_2D_5DIV_sd=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S2 W5' in i]]['Amplitude l SD (uV)'])
y1_2D_5DIV_sd.append(y1_2D_5DIV_sd[0])
y1_2D_5DIV_sd.pop(0)

y1_2D_7DIV_a=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S2 W5' in i]]['Amplitude l (uV)'])
y1_2D_7DIV_a.append(y1_2D_7DIV_a[0])
y1_2D_7DIV_a.pop(0)

y1_2D_7DIV_sd=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S2 W5' in i]]['Amplitude l SD (uV)'])
y1_2D_7DIV_sd.append(y1_2D_7DIV_sd[0])
y1_2D_7DIV_sd.pop(0)

y1_3D_5DIV_a=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S2 W5' in i]]['Amplitude l (uV)'])
y1_3D_5DIV_a.append(y1_3D_5DIV_a[0])
y1_3D_5DIV_a.pop(0)

y1_3D_5DIV_sd=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S2 W5' in i]]['Amplitude l SD (uV)'])
y1_3D_5DIV_sd.append(y1_3D_5DIV_sd[0])
y1_3D_5DIV_sd.pop(0)

y1_3D_7DIV_a=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S2 W5' in i]]['Amplitude l (uV)'])
y1_3D_7DIV_a.append(y1_3D_7DIV_a[0])
y1_3D_7DIV_a.pop(0)

y1_3D_7DIV_sd=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S2 W5' in i]]['Amplitude l SD (uV)'])
y1_3D_7DIV_sd.append(y1_3D_7DIV_sd[0])
y1_3D_7DIV_sd.pop(0)

# end of 1

#start of 2

y2_2D_5DIV=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S2 W7,5' in i]]['Active Percent (%)'])
y2_2D_5DIV.append(y2_2D_5DIV[0])
y2_2D_5DIV.pop(0)

y2_2D_7DIV=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S2 W7,5' in i]]['Active Percent (%)'])
y2_2D_7DIV.append(y2_2D_7DIV[0])
y2_2D_7DIV.pop(0)

y2_3D_5DIV=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S2 W7,5' in i]]['Active Percent (%)'])
y2_3D_5DIV.append(y2_3D_5DIV[0])
y2_3D_5DIV.pop(0)

y2_3D_7DIV=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S2 W7,5' in i]]['Active Percent (%)'])
y2_3D_7DIV.append(y2_3D_7DIV[0])
y2_3D_7DIV.pop(0)

y2_2D_5DIV_a=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S2 W7,5' in i]]['Amplitude l (uV)'])
y2_2D_5DIV_a.append(y2_2D_5DIV_a[0])
y2_2D_5DIV_a.pop(0)

y2_2D_5DIV_sd=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S2 W7,5' in i]]['Amplitude l SD (uV)'])
y2_2D_5DIV_sd.append(y2_2D_5DIV_sd[0])
y2_2D_5DIV_sd.pop(0)

y2_2D_7DIV_a=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S2 W7,5' in i]]['Amplitude l (uV)'])
y2_2D_7DIV_a.append(y2_2D_7DIV_a[0])
y2_2D_7DIV_a.pop(0)

y2_2D_7DIV_sd=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S2 W7,5' in i]]['Amplitude l SD (uV)'])
y2_2D_7DIV_sd.append(y2_2D_7DIV_sd[0])
y2_2D_7DIV_sd.pop(0)

y2_3D_5DIV_a=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S2 W7,5' in i]]['Amplitude l (uV)'])
y2_3D_5DIV_a.append(y2_3D_5DIV_a[0])
y2_3D_5DIV_a.pop(0)

y2_3D_5DIV_sd=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S2 W7,5' in i]]['Amplitude l SD (uV)'])
y2_3D_5DIV_sd.append(y2_3D_5DIV_sd[0])
y2_3D_5DIV_sd.pop(0)

y2_3D_7DIV_a=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S2 W7,5' in i]]['Amplitude l (uV)'])
y2_3D_7DIV_a.append(y2_3D_7DIV_a[0])
y2_3D_7DIV_a.pop(0)

y2_3D_7DIV_sd=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S2 W7,5' in i]]['Amplitude l SD (uV)'])
y2_3D_7DIV_sd.append(y2_3D_7DIV_sd[0])
y2_3D_7DIV_sd.pop(0)
#end of 2

#start of 4

y4_2D_5DIV=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S3 W5' in i]]['Active Percent (%)'])
y4_2D_5DIV.append(y4_2D_5DIV[0])
y4_2D_5DIV.pop(0)

y4_2D_7DIV=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S3 W5' in i]]['Active Percent (%)'])
y4_2D_7DIV.append(y4_2D_7DIV[0])
y4_2D_7DIV.pop(0)

y4_3D_5DIV=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S3 W5' in i]]['Active Percent (%)'])
y4_3D_5DIV.append(y4_3D_5DIV[0])
y4_3D_5DIV.pop(0)

y4_3D_7DIV=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S3 W5' in i]]['Active Percent (%)'])
y4_3D_7DIV.append(y4_3D_7DIV[0])
y4_3D_7DIV.pop(0)

y4_2D_5DIV_a=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S3 W5' in i]]['Amplitude l (uV)'])
y4_2D_5DIV_a.append(y4_2D_5DIV_a[0])
y4_2D_5DIV_a.pop(0)

y4_2D_5DIV_sd=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S3 W5' in i]]['Amplitude l SD (uV)'])
y4_2D_5DIV_sd.append(y4_2D_5DIV_sd[0])
y4_2D_5DIV_sd.pop(0)

y4_2D_7DIV_a=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S3 W5' in i]]['Amplitude l (uV)'])
y4_2D_7DIV_a.append(y4_2D_7DIV_a[0])
y4_2D_7DIV_a.pop(0)

y4_2D_7DIV_sd=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S3 W5' in i]]['Amplitude l SD (uV)'])
y4_2D_7DIV_sd.append(y4_2D_7DIV_sd[0])
y4_2D_7DIV_sd.pop(0)

y4_3D_5DIV_a=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S3 W5' in i]]['Amplitude l (uV)'])
y4_3D_5DIV_a.append(y4_3D_5DIV_a[0])
y4_3D_5DIV_a.pop(0)

y4_3D_5DIV_sd=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S3 W5' in i]]['Amplitude l SD (uV)'])
y4_3D_5DIV_sd.append(y4_3D_5DIV_sd[0])
y4_3D_5DIV_sd.pop(0)

y4_3D_7DIV_a=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S3 W5' in i]]['Amplitude l (uV)'])
y4_3D_7DIV_a.append(y4_3D_7DIV_a[0])
y4_3D_7DIV_a.pop(0)

y4_3D_7DIV_sd=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S3 W5' in i]]['Amplitude l SD (uV)'])
y4_3D_7DIV_sd.append(y4_3D_7DIV_sd[0])
y4_3D_7DIV_sd.pop(0)
#end of 4

#start of 5

y5_2D_5DIV=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S3 W7,5' in i]]['Active Percent (%)'])
y5_2D_5DIV.append(y5_2D_5DIV[0])
y5_2D_5DIV.pop(0)

y5_2D_7DIV=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S3 W7,5' in i]]['Active Percent (%)'])
y5_2D_7DIV.append(y5_2D_7DIV[0])
y5_2D_7DIV.pop(0)

y5_3D_5DIV=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S3 W7,5' in i]]['Active Percent (%)'])
y5_3D_5DIV.append(y5_3D_5DIV[0])
y5_3D_5DIV.pop(0)

y5_3D_7DIV=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S3 W7,5' in i]]['Active Percent (%)'])
y5_3D_7DIV.append(y5_3D_7DIV[0])
y5_3D_7DIV.pop(0)

y5_2D_5DIV_a=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S3 W7,5' in i]]['Amplitude l (uV)'])
y5_2D_5DIV_a.append(y5_2D_5DIV_a[0])
y5_2D_5DIV_a.pop(0)

y5_2D_5DIV_sd=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S3 W7,5' in i]]['Amplitude l SD (uV)'])
y5_2D_5DIV_sd.append(y5_2D_5DIV_sd[0])
y5_2D_5DIV_sd.pop(0)

y5_2D_7DIV_a=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S3 W7,5' in i]]['Amplitude l (uV)'])
y5_2D_7DIV_a.append(y5_2D_7DIV_a[0])
y5_2D_7DIV_a.pop(0)

y5_2D_7DIV_sd=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S3 W7,5' in i]]['Amplitude l SD (uV)'])
y5_2D_7DIV_sd.append(y5_2D_7DIV_sd[0])
y5_2D_7DIV_sd.pop(0)

y5_3D_5DIV_a=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S3 W7,5' in i]]['Amplitude l (uV)'])
y5_3D_5DIV_a.append(y5_3D_5DIV_a[0])
y5_3D_5DIV_a.pop(0)

y5_3D_5DIV_sd=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S3 W7,5' in i]]['Amplitude l SD (uV)'])
y5_3D_5DIV_sd.append(y5_3D_5DIV_sd[0])
y5_3D_5DIV_sd.pop(0)

y5_3D_7DIV_a=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S3 W7,5' in i]]['Amplitude l (uV)'])
y5_3D_7DIV_a.append(y5_3D_7DIV_a[0])
y5_3D_7DIV_a.pop(0)

y5_3D_7DIV_sd=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S3 W7,5' in i]]['Amplitude l SD (uV)'])
y5_3D_7DIV_sd.append(y5_3D_7DIV_sd[0])
y5_3D_7DIV_sd.pop(0)

#end of 5

#start of 7

y7_2D_5DIV=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S6 W5' in i]]['Active Percent (%)'])
y7_2D_5DIV.append(y7_2D_5DIV[0])
y7_2D_5DIV.pop(0)

y7_2D_7DIV=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S6 W5' in i]]['Active Percent (%)'])
y7_2D_7DIV.append(y7_2D_7DIV[0])
y7_2D_7DIV.pop(0)

y7_3D_5DIV=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S6 W5' in i]]['Active Percent (%)'])
y7_3D_5DIV.append(y7_3D_5DIV[0])
y7_3D_5DIV.pop(0)

y7_3D_7DIV=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S6 W5' in i]]['Active Percent (%)'])
y7_3D_7DIV.append(y7_3D_7DIV[0])
y7_3D_7DIV.pop(0)

y7_2D_5DIV_a=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S6 W5' in i]]['Amplitude l (uV)'])
y7_2D_5DIV_a.append(y7_2D_5DIV_a[0])
y7_2D_5DIV_a.pop(0)

y7_2D_5DIV_sd=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S6 W5' in i]]['Amplitude l SD (uV)'])
y7_2D_5DIV_sd.append(y7_2D_5DIV_sd[0])
y7_2D_5DIV_sd.pop(0)

y7_2D_7DIV_a=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S6 W5' in i]]['Amplitude l (uV)'])
y7_2D_7DIV_a.append(y7_2D_7DIV_a[0])
y7_2D_7DIV_a.pop(0)

y7_2D_7DIV_sd=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S6 W5' in i]]['Amplitude l SD (uV)'])
y7_2D_7DIV_sd.append(y7_2D_7DIV_sd[0])
y7_2D_7DIV_sd.pop(0)

y7_3D_5DIV_a=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S6 W5' in i]]['Amplitude l (uV)'])
y7_3D_5DIV_a.append(y7_3D_5DIV_a[0])
y7_3D_5DIV_a.pop(0)

y7_3D_5DIV_sd=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S6 W5' in i]]['Amplitude l SD (uV)'])
y7_3D_5DIV_sd.append(y7_3D_5DIV_sd[0])
y7_3D_5DIV_sd.pop(0)

y7_3D_7DIV_a=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S6 W5' in i]]['Amplitude l (uV)'])
y7_3D_7DIV_a.append(y7_3D_7DIV_a[0])
y7_3D_7DIV_a.pop(0)

y7_3D_7DIV_sd=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S6 W5' in i]]['Amplitude l SD (uV)'])
y7_3D_7DIV_sd.append(y7_3D_7DIV_sd[0])
y7_3D_7DIV_sd.pop(0)

#end of 7

#start of 8

y8_2D_5DIV=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S6 W7,5' in i]]['Active Percent (%)'])
y8_2D_5DIV.append(y8_2D_5DIV[0])
y8_2D_5DIV.pop(0)

y8_2D_7DIV=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S6 W7,5' in i]]['Active Percent (%)'])
y8_2D_7DIV.append(y8_2D_7DIV[0])
y8_2D_7DIV.pop(0)

y8_3D_5DIV=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S6 W7,5' in i]]['Active Percent (%)'])
y8_3D_5DIV.append(y8_3D_5DIV[0])
y8_3D_5DIV.pop(0)

y8_3D_7DIV=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S6 W7,5' in i]]['Active Percent (%)'])
y8_3D_7DIV.append(y8_3D_7DIV[0])
y8_3D_7DIV.pop(0)

y8_2D_5DIV_a=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S6 W7,5' in i]]['Amplitude l (uV)'])
y8_2D_5DIV_a.append(y8_2D_5DIV_a[0])
y8_2D_5DIV_a.pop(0)
y8_2D_5DIV_sd=list(pd2D_5DIV.loc[[i for i in pd2D_5DIV.index if 'S6 W7,5' in i]]['Amplitude l SD (uV)'])
y8_2D_5DIV_sd.append(y8_2D_5DIV_sd[0])
y8_2D_5DIV_sd.pop(0)

y8_2D_7DIV_a=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S6 W7,5' in i]]['Amplitude l (uV)'])
y8_2D_7DIV_a.append(y8_2D_7DIV_a[0])
y8_2D_7DIV_a.pop(0)

y8_2D_7DIV_sd=list(pd2D_7DIV.loc[[i for i in pd2D_7DIV.index if 'S6 W7,5' in i]]['Amplitude l SD (uV)'])
y8_2D_7DIV_sd.append(y8_2D_7DIV_sd[0])
y8_2D_7DIV_sd.pop(0)

y8_3D_5DIV_a=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S6 W7,5' in i]]['Amplitude l (uV)'])
y8_3D_5DIV_a.append(y8_3D_5DIV_a[0])
y8_3D_5DIV_a.pop(0)

y8_3D_5DIV_sd=list(pd3D_5DIV.loc[[i for i in pd3D_5DIV.index if 'S6 W7,5' in i]]['Amplitude l SD (uV)'])
y8_3D_5DIV_sd.append(y8_3D_5DIV_sd[0])
y8_3D_5DIV_sd.pop(0)

y8_3D_7DIV_a=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S6 W7,5' in i]]['Amplitude l (uV)'])
y8_3D_7DIV_a.append(y8_3D_7DIV_a[0])
y8_3D_7DIV_a.pop(0)

y8_3D_7DIV_sd=list(pd3D_7DIV.loc[[i for i in pd3D_7DIV.index if 'S6 W7,5' in i]]['Amplitude l SD (uV)'])
y8_3D_7DIV_sd.append(y8_3D_7DIV_sd[0])
y8_3D_7DIV_sd.pop(0)

#end of 8

#start of 1
ax1.bar(np.array(x)-2,y1_2D_5DIV,label='2D',width=1.5,align='center')
ax1.bar(np.array(x)-1,y1_2D_7DIV,width=1.5,align='center',color='r')
ax1.bar(np.array(x)+1,y1_3D_5DIV,label='3D',width=1.5,align='center')
ax1.bar(np.array(x)+2,y1_3D_7DIV,width=1.5,align='center',color='b')
ax1_a.errorbar(np.array(x)-2,y1_2D_5DIV_a,yerr=y1_2D_5DIV_sd,color='c',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax1_a.errorbar(np.array(x)-1,y1_2D_7DIV_a,yerr=y1_2D_7DIV_sd,color='c',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax1_a.errorbar(np.array(x)+1,y1_3D_5DIV_a,yerr=y1_3D_5DIV_sd,color='g',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax1_a.errorbar(np.array(x)+2,y1_3D_7DIV_a,yerr=y1_3D_7DIV_sd,color='g',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax1.set_xticks([10,20,30,40])
ax1.set_xticklabels(x_ticks,size=4)
ax1.set_yticks([50,100])
ax1.set_yticklabels([50,100],size=4)
ax1.legend(fontsize=4,loc=2)
ax1.set_xlabel('Diameter (um)',size=5)
ax1.xaxis.set_label_coords(0.5, -0.1)
ax1.set_ylabel('Active (%)',size=5)
ax1.yaxis.set_label_coords(-0.05, 0.5)
ax1.set_title('W5 O2',size=5,y=0.90)
ax1.grid(b=None)
ax1_a.set_yticks(y)
ax1_a.set_yticklabels(y,size=4)
ax1_a.set_ylabel('Amplitude (uV)',size=5)
ax1_a.grid(b=None)

#end of 1

#start of 2

ax2.bar(np.array(x)-2,y2_2D_5DIV,label='2D',width=1.5,align='center')
ax2.bar(np.array(x)-1,y2_2D_7DIV,width=1.5,align='center',color='r')
ax2.bar(np.array(x)+1,y2_3D_5DIV,label='3D',width=1.5,align='center')
ax2.bar(np.array(x)+2,y2_3D_7DIV,width=1.5,align='center',color='b')
ax2_a.errorbar(np.array(x)-2,y2_2D_5DIV_a,yerr=y2_2D_5DIV_sd,color='c',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax2_a.errorbar(np.array(x)-1,y2_2D_7DIV_a,yerr=y2_2D_7DIV_sd,color='c',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax2_a.errorbar(np.array(x)+1,y2_3D_5DIV_a,yerr=y2_3D_5DIV_sd,color='g',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax2_a.errorbar(np.array(x)+2,y2_3D_7DIV_a,yerr=y2_3D_7DIV_sd,color='g',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax2.set_xticks([10,20,30,40])
ax2.set_xticklabels(x_ticks,size=4)
ax2.set_yticks([50,100])
ax2.set_yticklabels([50,100],size=4)
ax2.legend(fontsize=4,loc=2)
ax2.set_xlabel('Diameter (um)',size=5)
ax2.xaxis.set_label_coords(0.5, -0.1)
ax2.set_ylabel('Active (%)',size=5)
ax2.yaxis.set_label_coords(-0.05, 0.5)
ax2.set_title('W7.5 O2',size=5,y=0.90)
ax2.grid(b=None)
ax2_a.set_ybound(0,150)
ax2_a.set_yticks(y)
ax2_a.set_yticklabels(y,size=4)
ax2_a.set_ylabel('Amplitude (uV)',size=5)
ax2_a.grid(b=None)

#end of 2

#start of 3

ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
opening2=mpimg.imread('PNGFiles/2.png')
ax3.imshow(opening2)

#end of 3

#start of 4

ax4.bar(np.array(x)-2,y4_2D_5DIV,label='2D',width=1.5,align='center')
ax4.bar(np.array(x)-1,y4_2D_7DIV,width=1.5,align='center',color='r')
ax4.bar(np.array(x)+2,y4_3D_5DIV,label='3D',width=1.5,align='center')
ax4.bar(np.array(x)+2,y4_3D_7DIV,width=1.5,align='center',color='b')
ax4_a.errorbar(np.array(x)-2,y4_2D_5DIV_a,yerr=y4_2D_5DIV_sd,color='c',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax4_a.errorbar(np.array(x)-1,y4_2D_7DIV_a,yerr=y4_2D_7DIV_sd,color='c',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax4_a.errorbar(np.array(x)+1,y4_3D_5DIV_a,yerr=y4_3D_5DIV_sd,color='g',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax4_a.errorbar(np.array(x)+2,y4_3D_7DIV_a,yerr=y4_3D_7DIV_sd,color='g',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax4.set_xticks([10,20,30,40])
ax4.set_xticklabels(x_ticks,size=4)
ax4.set_yticks([50,100])
ax4.set_yticklabels([50,100],size=4)
ax4.legend(fontsize=4,loc=2)
ax4.set_xlabel('Diameter (um)',size=5)
ax4.xaxis.set_label_coords(0.5, -0.1)
ax4.set_ylabel('Active (%)',size=5)
ax4.yaxis.set_label_coords(-0.05, 0.5)
ax4.set_title('W5 O3',size=5,y=0.90)
ax4.grid(b=None)
ax4_a.set_ybound(0,150)
ax4_a.set_yticks(y)
ax4_a.set_yticklabels(y,size=4)
ax4_a.set_ylabel('Amplitude (uV)',size=5)
ax4_a.grid(b=None)

#end of 4

#start of 5

ax5.bar(np.array(x)-2,y5_2D_5DIV,label='2D',width=1.5,align='center')
ax5.bar(np.array(x)-1,y5_2D_7DIV,width=1.5,align='center',color='r')
ax5.bar(np.array(x)+1,y5_3D_5DIV,label='3D',width=1.5,align='center')
ax5.bar(np.array(x)+2,y5_3D_7DIV,width=1.5,align='center',color='b')
ax5_a.errorbar(np.array(x)-2,y5_2D_5DIV_a,yerr=y5_2D_5DIV_sd,color='c',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax5_a.errorbar(np.array(x)-1,y5_2D_7DIV_a,yerr=y5_2D_7DIV_sd,color='c',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax5_a.errorbar(np.array(x)+1,y5_3D_5DIV_a,yerr=y5_3D_5DIV_sd,color='g',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax5_a.errorbar(np.array(x)+2,y5_3D_7DIV_a,yerr=y5_3D_7DIV_sd,color='g',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax5.set_xticks([10,20,30,40])
ax5.set_xticklabels(x_ticks,size=4)
ax5.set_yticks([50,100])
ax5.set_yticklabels([50,100],size=4)
ax5.legend(fontsize=4,loc=2)
ax5.set_xlabel('Diameter (um)',size=5)
ax5.xaxis.set_label_coords(0.5, -0.1)
ax5.set_ylabel('Active (%)',size=5)
ax5.yaxis.set_label_coords(-0.05, 0.5)
ax5.set_title('W7.5 O3',size=5,y=0.90)
ax5.grid(b=None)
ax5_a.set_ybound(0,150)
ax5_a.set_yticks(y)
ax5_a.set_yticklabels(y,size=4)
ax5_a.set_ylabel('Amplitude (uV)',size=5)
ax5_a.grid(b=None)

#end of 5

#start of 6

ax6.get_xaxis().set_visible(False)
ax6.get_yaxis().set_visible(False)
opening3=mpimg.imread('PNGFiles/3.png')
ax6.imshow(opening3)

#end of 6

#start of 7

ax7.bar(np.array(x)-2,y7_2D_5DIV,label='2D',width=1.5,align='center')
ax7.bar(np.array(x)-1,y7_2D_7DIV,width=1.5,align='center',color='r')
ax7.bar(np.array(x)+1,y7_3D_5DIV,label='3D',width=1.5,align='center')
ax7.bar(np.array(x)+2,y7_3D_7DIV,width=1.5,align='center',color='b')
ax7_a.errorbar(np.array(x)-2,y7_2D_5DIV_a,yerr=y7_2D_5DIV_sd,color='c',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax7_a.errorbar(np.array(x)-1,y7_2D_7DIV_a,yerr=y7_2D_7DIV_sd,color='c',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax7_a.errorbar(np.array(x)+1,y7_3D_5DIV_a,yerr=y7_3D_5DIV_sd,color='g',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax7_a.errorbar(np.array(x)+2,y7_3D_7DIV_a,yerr=y7_3D_7DIV_sd,color='g',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax7.set_xticks([10,20,30,40])
ax7.set_xticklabels(x_ticks,size=4)
ax7.set_yticks([50,100])
ax7.set_yticklabels([50,100],size=4)
ax7.legend(fontsize=4,loc=2)
ax7.set_xlabel('Diameter (um)',size=5)
ax7.xaxis.set_label_coords(0.5, -0.1)
ax7.set_ylabel('Active (%)',size=5)
ax7.yaxis.set_label_coords(-0.05, 0.5)
ax7.set_title('W5 O6',size=5,y=0.90)
ax7.grid(b=None)
ax7_a.set_ybound(0,150)
ax7_a.set_yticks(y)
ax7_a.set_yticklabels(y,size=4)
ax7_a.set_ylabel('Amplitude (uV)',size=5)
ax7_a.grid(b=None)

#end of 7

#start of 8

ax8.bar(np.array(x)-2,y8_2D_5DIV,label='2D',width=1.5,align='center')
ax8.bar(np.array(x)-1,y8_2D_7DIV,width=1.5,align='center',color='r')
ax8.bar(np.array(x)+1,y8_3D_5DIV,label='3D',width=1.5,align='center')
ax8.bar(np.array(x)+2,y8_3D_7DIV,width=1.5,align='center',color='b')
ax8_a.errorbar(np.array(x)-2,y8_2D_5DIV_a,yerr=y8_2D_5DIV_sd,color='c',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax8_a.errorbar(np.array(x)-1,y8_2D_7DIV_a,yerr=y8_2D_7DIV_sd,color='c',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax8_a.errorbar(np.array(x)+1,y8_3D_5DIV_a,yerr=y8_3D_5DIV_sd,color='g',alpha=0.66,marker='_',linestyle='None',linewidth=0.8)
ax8_a.errorbar(np.array(x)+2,y8_3D_7DIV_a,yerr=y8_3D_7DIV_sd,color='g',alpha=1,marker='_',linestyle='None',linewidth=0.8)
ax8.set_xticks([10,20,30,40])
ax8.set_xticklabels(x_ticks,size=4)
ax8.set_yticks([50,100])
ax8.set_yticklabels([50,100],size=4)
ax8.legend(fontsize=4,loc=2)
ax8.set_xlabel('Diameter (um)',size=5)
ax8.xaxis.set_label_coords(0.5, -0.1)
ax8.set_ylabel('Active (%)',size=5)
ax8.yaxis.set_label_coords(-0.05, 0.5)
ax8.set_title('W7.5 O6',size=5,y=0.90)
ax8.grid(b=None)
ax8_a.set_ybound(0,150)
ax8_a.set_yticks(y)
ax8_a.set_yticklabels(y,size=4)
ax8_a.set_ylabel('Amplitude (uV)',size=5)
ax8_a.grid(b=None)

#end of 8

#start of 9

ax9.get_xaxis().set_visible(False)
ax9.get_yaxis().set_visible(False)
opening6=mpimg.imread('PNGFiles/6.png')
ax9.imshow(opening6)

#end of 9

plt.annotate('Width (um)',(-1.8,-0.4),size=12,xycoords="axes fraction")
plt.annotate('5',(-2.42,-0.25),size=10,xycoords="axes fraction")
plt.annotate('7.5',(-1.0,-0.25),size=10,xycoords="axes fraction")
plt.annotate('Openings (#)',(-3.6,1.65),size=12,xycoords="axes fraction")
plt.annotate('2',(-3.15,2.86),size=10,xycoords="axes fraction")
plt.annotate('3',(-3.15,1.65),size=10,xycoords="axes fraction")
plt.annotate('6',(-3.15,0.44),size=10,xycoords="axes fraction")

fig.suptitle('2D vs. 3D Igloo Electrodes Comparison',size=15)

plt.show()
