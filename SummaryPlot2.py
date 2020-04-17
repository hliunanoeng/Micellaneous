import sys
sys.path.insert(0, '../MEA')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
style.use('ggplot')



#MEA 17332

    #Spike Rate
# df_ByDiameter17332 = 'Excel/df_ByDiameter17332.csv'
# df_ByOpenings17332 = 'Excel/df_ByOpenings17332.csv'
# df_ByBranch17332 = 'Excel/df_ByBranch17332.csv'
#
# df1=pd.read_csv(df_ByDiameter17332,'\t',index_col=0)
# spikerate1=list(df1['Frequency (Hz)'])
# spikerate_SD1=list(df1['Frequency SD (Hz)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332,'\t',index_col=0)
# spikerate2=list(df2['Frequency (Hz)'])
# spikerate_SD2=list(df2['Frequency SD (Hz)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332,'\t',index_col=0)
# spikerate3=list(df3['Frequency (Hz)'])
# spikerate_SD3=list(df3['Frequency SD (Hz)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(spikerate1)+len(spikerate2)+len(spikerate3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(spikerate1)), spikerate1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)),spikerate1,yerr=spikerate_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1), spikerate2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1),spikerate2,yerr=spikerate_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2), spikerate3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2),spikerate3,yerr=spikerate_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,2)
# ax1.set_yticks([0,0.5,1,1.5,2.0])
# ax1.grid(b=None)
# ax1.set_ylabel("Spike Rate (Hz)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 7DIV')
# plt.show()

    #Signal Noise Ratio
# df_ByDiameter17332 = 'Excel/df_ByDiameter17332.csv'
# df_ByOpenings17332 = 'Excel/df_ByOpenings17332.csv'
# df_ByBranch17332 = 'Excel/df_ByBranch17332.csv'
#
# df1=pd.read_csv(df_ByDiameter17332,'\t',index_col=0)
# SNR1=list(df1['SNR'])
# SNR_SD1=list(df1['SNR SD'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332,'\t',index_col=0)
# SNR2=list(df2['SNR'])
# SNR_SD2=list(df2['SNR SD'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332,'\t',index_col=0)
# SNR3=list(df3['SNR'])
# SNR_SD3=list(df3['SNR SD'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(SNR1)+len(SNR2)+len(SNR3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(SNR1)), SNR1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(SNR1)),SNR1,yerr=SNR_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1), SNR2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1),SNR2,yerr=SNR_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2), SNR3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2),SNR3,yerr=SNR_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,10)
# ax1.set_yticks([0,1,2,3,4,5,6,7,8,9,10])
# ax1.grid(b=None)
# ax1.set_ylabel("Signal Noise Ratio")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 7DIV')
# plt.show()

    #Amplitude
# df_ByDiameter17332 = 'Excel/df_ByDiameter17332.csv'
# df_ByOpenings17332 = 'Excel/df_ByOpenings17332.csv'
# df_ByBranch17332 = 'Excel/df_ByBranch17332.csv'
#
# df1=pd.read_csv(df_ByDiameter17332,'\t',index_col=0)
# Amp1=list(df1['Amplitude l (uV)'])
# Amp_SD1=list(df1['Amplitude l SD (uV)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332,'\t',index_col=0)
# Amp2=list(df2['Amplitude l (uV)'])
# Amp_SD2=list(df2['Amplitude l SD (uV)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332,'\t',index_col=0)
# Amp3=list(df3['Amplitude l (uV)'])
# Amp_SD3=list(df3['Amplitude l SD (uV)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Amp1)+len(Amp2)+len(Amp3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Amp1)), Amp1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(Amp1)),Amp1,yerr=Amp_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1), Amp2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1),Amp2,yerr=Amp_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2), Amp3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2),Amp3,yerr=Amp_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,50)
# ax1.set_yticks([0,10,20,30,40,50])
# ax1.grid(b=None)
# ax1.set_ylabel("Amplitude ($\mu$V)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 7DIV')
# plt.show()

    #Activeness
# df_ByDiameter17332 = 'Excel/df_ByDiameter17332.csv'
# df_ByOpenings17332 = 'Excel/df_ByOpenings17332.csv'
# df_ByBranch17332 = 'Excel/df_ByBranch17332.csv'
#
# df1=pd.read_csv(df_ByDiameter17332,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332,'\t',index_col=0)
# Active2=list(df2['Active Percent (%)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332,'\t',index_col=0)
# Active3=list(df3['Active Percent (%)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)+len(Active2)+len(Active3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.bar(range(len(Active1)+1,len(Active1)+len(Active2)+1), Active2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.bar(range(len(Active1)+len(Active2)+2,len(Active1)+len(Active2)+len(Active3)+2), Active3, align='center',width=0.5,color='b',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1.grid(b=None)
# ax1.set_ylabel("Active Percent (%)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 7DIV')
# plt.show()

    #Activeness 2
# df_ByName17332 = 'Excel/df_ByName17332.csv'
#
# df1=pd.read_csv(df_ByName17332,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)
# x_label=x_label1
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
#
# ax1.set_ylabel("Active Percent (%)")
# plt.title('MEA 17332 7DIV')
# plt.show()

    #Impedance Correlation
# df_ByName17332 = 'Excel/df_ByName17332.csv'
#
# df1=pd.read_csv(df_ByName17332,'\t',index_col=0)
# Active=list(df1['Active Percent (%)'])
# SNR=list(df1['SNR'])
# SNR_SD=list(df1['SNR SD'])
# SpikeRate=list(df1['Frequency (Hz)'])
# SpikeRate_SD=list(df1['Frequency SD (Hz)'])
#
# x_label=list(df1.index)
#
# dic=dict()
# for i in range(len(x_label)):
#     dic[x_label[i]]=[Active[i]]+[SNR[i]]+[SNR_SD[i]]+[SpikeRate[i]]+[SpikeRate_SD[i]]
#
# Z_df = pd.read_excel('Excel/EffectiveAspectRatio.xlsx',sheet_name='V17.1')
# Z = np.array(Z_df['Effective Aspect Ratio (L/W)'])*0.2222
# Label=np.array(Z_df['Label'])
#
# Active=[]
# SNR=[]
# SNR_SD=[]
# SpikeRate=[]
# SpikeRate_SD=[]
# for i in Label:
#     Active.append(dic[i][0])
#     SNR.append(dic[i][1])
#     SNR_SD.append(dic[i][2])
#     SpikeRate.append(dic[i][3])
#     SpikeRate_SD.append(dic[i][4])
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# ax1_a=ax1.twinx()
# ax1_b=ax1.twinx()
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
# Z=np.array(['\n ('+str(round(i,2))+' M$\Omega$)' for i in Z])
# Label=Label+Z
#
# ax1.bar(range(len(Active)), Active, align='center',width=0.5,color='r',alpha=0.666)
# # ax1_a.plot(range(len(Z)),Z, label="$R_{igloo}$ (M$\Omega$)",color='b',alpha=0.35)
# ax1_a.set_ylim(0,10)
# SNR_lolims=(np.array(SNR)-np.array(SNR_SD))<0
# ax1_a.errorbar(range(len(SNR)),SNR,yerr=SNR_SD,color='g',alpha=0.8,marker='_',linewidth=1.5,lolims=SNR_lolims)
# ax1_a.set_ylabel('Signal to Noise Ratio')
# ax1_a.yaxis.set_label_coords(1.035,0.25)
#
# ax1_b.set_ylim(0,2.5)
# SpikeRate_lolims=(np.array(SpikeRate)-np.array(SpikeRate_SD))<0
# ax1_b.errorbar(range(len(SpikeRate)),SpikeRate,yerr=SpikeRate_SD,color='b',alpha=0.8,marker='_',linewidth=1.5,lolims=SpikeRate_lolims)
# ax1_b.spines['right'].set_position(('outward',50))
# ax1_b.set_ylabel('Spike Rate (Hz)')
# ax1_b.yaxis.set_label_coords(1.095,0.75)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(Label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1_a.set_ybound(0,20)
# ax1_a.set_yticks([0,2.5,5,7.5,10,20])
# ax1_a.set_yticklabels([0,2.5,5,7.5,10,''],color='g',alpha=0.88,size=6)
#
# ax1_b.set_ybound(-2.5,2.5)
# ax1_b.set_yticks([-2.5,0,0.5,1,1.5,2,2.5])
# ax1_b.set_yticklabels(['',0,0.5,1,1.5,2,2.5],color='b',alpha=0.88,size=6)
#
# ax1.set_ylabel("Active Percent (%)")
# # ax1.grid(False)
# ax1_a.grid(False)
# ax1_b.grid(False)
# plt.title('$R_{igloo}$ Correlation in MEA 17332 7DIV')
# plt.show()


# End of MEA 17332



#MEA 17336

    #Spike Rate
# df_ByDiameter17336 = 'Excel/df_ByDiameter17336.csv'
# df_ByOpenings17336 = 'Excel/df_ByOpenings17336.csv'
# df_ByBranch17336 = 'Excel/df_ByBranch17336.csv'
#
# df1=pd.read_csv(df_ByDiameter17336,'\t',index_col=0)
# spikerate1=list(df1['Frequency (Hz)'])
# spikerate_SD1=list(df1['Frequency SD (Hz)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336,'\t',index_col=0)
# spikerate2=list(df2['Frequency (Hz)'])
# spikerate_SD2=list(df2['Frequency SD (Hz)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336,'\t',index_col=0)
# spikerate3=list(df3['Frequency (Hz)'])
# spikerate_SD3=list(df3['Frequency SD (Hz)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(spikerate1)+len(spikerate2)+len(spikerate3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(spikerate1)), spikerate1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)),spikerate1,yerr=spikerate_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1), spikerate2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1),spikerate2,yerr=spikerate_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2), spikerate3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2),spikerate3,yerr=spikerate_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,2)
# ax1.set_yticks([0,0.5,1,1.5,2.0])
# ax1.grid(b=None)
# ax1.set_ylabel("Spike Rate (Hz)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 7DIV')
# plt.show()

    #Signal Noise Ratio
# df_ByDiameter17336 = 'Excel/df_ByDiameter17336.csv'
# df_ByOpenings17336 = 'Excel/df_ByOpenings17336.csv'
# df_ByBranch17336 = 'Excel/df_ByBranch17336.csv'
#
# df1=pd.read_csv(df_ByDiameter17336,'\t',index_col=0)
# SNR1=list(df1['SNR'])
# SNR_SD1=list(df1['SNR SD'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336,'\t',index_col=0)
# SNR2=list(df2['SNR'])
# SNR_SD2=list(df2['SNR SD'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336,'\t',index_col=0)
# SNR3=list(df3['SNR'])
# SNR_SD3=list(df3['SNR SD'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(SNR1)+len(SNR2)+len(SNR3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(SNR1)), SNR1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(SNR1)),SNR1,yerr=SNR_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1), SNR2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1),SNR2,yerr=SNR_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2), SNR3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2),SNR3,yerr=SNR_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,10)
# ax1.set_yticks([0,1,2,3,4,5,6,7,8,9,10])
# ax1.grid(b=None)
# ax1.set_ylabel("Signal Noise Ratio")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 7DIV')
# plt.show()

    #Amplitude
# df_ByDiameter17336 = 'Excel/df_ByDiameter17336.csv'
# df_ByOpenings17336 = 'Excel/df_ByOpenings17336.csv'
# df_ByBranch17336 = 'Excel/df_ByBranch17336.csv'
#
# df1=pd.read_csv(df_ByDiameter17336,'\t',index_col=0)
# Amp1=list(df1['Amplitude l (uV)'])
# Amp_SD1=list(df1['Amplitude l SD (uV)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336,'\t',index_col=0)
# Amp2=list(df2['Amplitude l (uV)'])
# Amp_SD2=list(df2['Amplitude l SD (uV)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336,'\t',index_col=0)
# Amp3=list(df3['Amplitude l (uV)'])
# Amp_SD3=list(df3['Amplitude l SD (uV)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Amp1)+len(Amp2)+len(Amp3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Amp1)), Amp1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(Amp1)),Amp1,yerr=Amp_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1), Amp2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1),Amp2,yerr=Amp_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2), Amp3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2),Amp3,yerr=Amp_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,50)
# ax1.set_yticks([0,10,20,30,40,50])
# ax1.grid(b=None)
# ax1.set_ylabel("Amplitude ($\mu$V)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 7DIV')
# plt.show()

    #Activeness
# df_ByDiameter17336 = 'Excel/df_ByDiameter17336.csv'
# df_ByOpenings17336 = 'Excel/df_ByOpenings17336.csv'
# df_ByBranch17336 = 'Excel/df_ByBranch17336.csv'
#
# df1=pd.read_csv(df_ByDiameter17336,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336,'\t',index_col=0)
# Active2=list(df2['Active Percent (%)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336,'\t',index_col=0)
# Active3=list(df3['Active Percent (%)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)+len(Active2)+len(Active3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.bar(range(len(Active1)+1,len(Active1)+len(Active2)+1), Active2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.bar(range(len(Active1)+len(Active2)+2,len(Active1)+len(Active2)+len(Active3)+2), Active3, align='center',width=0.5,color='b',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1.grid(b=None)
# ax1.set_ylabel("Active Percent (%)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 7DIV')
# plt.show()

    #Activeness 2
# df_ByName17336 = 'Excel/df_ByName17336.csv'
#
# df1=pd.read_csv(df_ByName17336,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)
# x_label=x_label1
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
#
# ax1.set_ylabel("Active Percent (%)")
# plt.title('MEA 17336 7DIV')
# plt.show()

    #Impedance Correlation
# df_ByName17336 = 'Excel/df_ByName17336.csv'
#
# df1=pd.read_csv(df_ByName17336,'\t',index_col=0)
# Active=list(df1['Active Percent (%)'])
# SNR=list(df1['SNR'])
# SNR_SD=list(df1['SNR SD'])
# SpikeRate=list(df1['Frequency (Hz)'])
# SpikeRate_SD=list(df1['Frequency SD (Hz)'])
#
# x_label=list(df1.index)
#
# dic=dict()
# for i in range(len(x_label)):
#     dic[x_label[i]]=[Active[i]]+[SNR[i]]+[SNR_SD[i]]+[SpikeRate[i]]+[SpikeRate_SD[i]]
#
# Z_df = pd.read_excel('Excel/EffectiveAspectRatio.xlsx',sheet_name='V17.1')
# Z = np.array(Z_df['Effective Aspect Ratio (L/W)'])*0.2222
# Label=np.array(Z_df['Label'])
#
# Active=[]
# SNR=[]
# SNR_SD=[]
# SpikeRate=[]
# SpikeRate_SD=[]
# for i in Label:
#     Active.append(dic[i][0])
#     SNR.append(dic[i][1])
#     SNR_SD.append(dic[i][2])
#     SpikeRate.append(dic[i][3])
#     SpikeRate_SD.append(dic[i][4])
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# ax1_a=ax1.twinx()
# ax1_b=ax1.twinx()
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
# Z=np.array(['\n ('+str(round(i,2))+' M$\Omega$)' for i in Z])
# Label=Label+Z
#
# ax1.bar(range(len(Active)), Active, align='center',width=0.5,color='r',alpha=0.666)
# # ax1_a.plot(range(len(Z)),Z, label="$R_{igloo}$ (M$\Omega$)",color='b',alpha=0.35)
# ax1_a.set_ylim(0,10)
# SNR_lolims=(np.array(SNR)-np.array(SNR_SD))<0
# ax1_a.errorbar(range(len(SNR)),SNR,yerr=SNR_SD,color='g',alpha=0.8,marker='_',linewidth=1.5,lolims=SNR_lolims)
# ax1_a.set_ylabel('Signal to Noise Ratio')
# ax1_a.yaxis.set_label_coords(1.035,0.25)
#
# ax1_b.set_ylim(0,2.5)
# SpikeRate_lolims=(np.array(SpikeRate)-np.array(SpikeRate_SD))<0
# ax1_b.errorbar(range(len(SpikeRate)),SpikeRate,yerr=SpikeRate_SD,color='b',alpha=0.8,marker='_',linewidth=1.5,lolims=SpikeRate_lolims)
# ax1_b.spines['right'].set_position(('outward',50))
# ax1_b.set_ylabel('Spike Rate (Hz)')
# ax1_b.yaxis.set_label_coords(1.095,0.75)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(Label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1_a.set_ybound(10,20)
# ax1_a.set_yticks([0,2.5,5,7.5,10,20])
# ax1_a.set_yticklabels([0,2.5,5,7.5,10,''],color='g',alpha=0.88,size=6)
#
# ax1_b.set_ybound(-3,3)
# ax1_b.set_yticks([-3,0,0.75,1.5,2.25,3])
# ax1_b.set_yticklabels(['',0,0.75,1.5,2.25,3],color='b',alpha=0.88,size=6)
#
# ax1.set_ylabel("Active Percent (%)")
# # ax1.grid(False)
# ax1_a.grid(False)
# ax1_b.grid(False)
# plt.title('$R_{igloo}$ Correlation in MEA 17336 7DIV')
# plt.show()

# End of MEA 17336




# MEA 17332B

    # Spike Rate
# df_ByDiameter17332B = 'Excel/df_ByDiameter17332B.csv'
# df_ByOpenings17332B = 'Excel/df_ByOpenings17332B.csv'
# df_ByBranch17332B = 'Excel/df_ByBranch17332B.csv'
#
# df1=pd.read_csv(df_ByDiameter17332B,'\t',index_col=0)
# spikerate1=list(df1['Frequency (Hz)'])
# spikerate_SD1=list(df1['Frequency SD (Hz)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332B,'\t',index_col=0)
# spikerate2=list(df2['Frequency (Hz)'])
# spikerate_SD2=list(df2['Frequency SD (Hz)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332B,'\t',index_col=0)
# spikerate3=list(df3['Frequency (Hz)'])
# spikerate_SD3=list(df3['Frequency SD (Hz)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(spikerate1)+len(spikerate2)+len(spikerate3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(spikerate1)), spikerate1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)),spikerate1,yerr=spikerate_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1), spikerate2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1),spikerate2,yerr=spikerate_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2), spikerate3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2),spikerate3,yerr=spikerate_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,8)
# ax1.set_yticks([0,1,2,3,4,5,6,7,8])
# ax1.grid(b=None)
# ax1.set_ylabel("Spike Rate (Hz)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 8DIV')
# plt.show()

    # Signal Noise Ratio
# df_ByDiameter17332B = 'Excel/df_ByDiameter17332B.csv'
# df_ByOpenings17332B = 'Excel/df_ByOpenings17332B.csv'
# df_ByBranch17332B = 'Excel/df_ByBranch17332B.csv'
#
# df1=pd.read_csv(df_ByDiameter17332B,'\t',index_col=0)
# SNR1=list(df1['SNR'])
# SNR_SD1=list(df1['SNR SD'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332B,'\t',index_col=0)
# SNR2=list(df2['SNR'])
# SNR_SD2=list(df2['SNR SD'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332B,'\t',index_col=0)
# SNR3=list(df3['SNR'])
# SNR_SD3=list(df3['SNR SD'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(SNR1)+len(SNR2)+len(SNR3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(SNR1)), SNR1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(SNR1)),SNR1,yerr=SNR_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1), SNR2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1),SNR2,yerr=SNR_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2), SNR3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2),SNR3,yerr=SNR_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,12)
# ax1.set_yticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
# ax1.grid(b=None)
# ax1.set_ylabel("Signal Noise Ratio")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 8DIV')
# plt.show()

    # Amplitude
# df_ByDiameter17332B = 'Excel/df_ByDiameter17332B.csv'
# df_ByOpenings17332B = 'Excel/df_ByOpenings17332B.csv'
# df_ByBranch17332B = 'Excel/df_ByBranch17332B.csv'
#
# df1=pd.read_csv(df_ByDiameter17332B,'\t',index_col=0)
# Amp1=list(df1['Amplitude l (uV)'])
# Amp_SD1=list(df1['Amplitude l SD (uV)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332B,'\t',index_col=0)
# Amp2=list(df2['Amplitude l (uV)'])
# Amp_SD2=list(df2['Amplitude l SD (uV)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332B,'\t',index_col=0)
# Amp3=list(df3['Amplitude l (uV)'])
# Amp_SD3=list(df3['Amplitude l SD (uV)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Amp1)+len(Amp2)+len(Amp3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Amp1)), Amp1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(Amp1)),Amp1,yerr=Amp_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1), Amp2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1),Amp2,yerr=Amp_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2), Amp3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2),Amp3,yerr=Amp_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,50)
# ax1.set_yticks([0,10,20,30,40,50])
# ax1.grid(b=None)
# ax1.set_ylabel("Amplitude ($\mu$V)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 8DIV')
# plt.show()

    # Activeness
# df_ByDiameter17332B = 'Excel/df_ByDiameter17332B.csv'
# df_ByOpenings17332B = 'Excel/df_ByOpenings17332B.csv'
# df_ByBranch17332B = 'Excel/df_ByBranch17332B.csv'
#
# df1=pd.read_csv(df_ByDiameter17332B,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17332B,'\t',index_col=0)
# Active2=list(df2['Active Percent (%)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17332B,'\t',index_col=0)
# Active3=list(df3['Active Percent (%)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)+len(Active2)+len(Active3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.bar(range(len(Active1)+1,len(Active1)+len(Active2)+1), Active2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.bar(range(len(Active1)+len(Active2)+2,len(Active1)+len(Active2)+len(Active3)+2), Active3, align='center',width=0.5,color='b',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1.grid(b=None)
# ax1.set_ylabel("Active Percent (%)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17332 8DIV')
# plt.show()

    # Activeness 2
# df_ByName17332B = 'Excel/df_ByName17332B.csv'
#
# df1=pd.read_csv(df_ByName17332B,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)
# x_label=x_label1
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
#
# ax1.set_ylabel("Active Percent (%)")
# plt.title('MEA 17332 8DIV')
# plt.show()

    #Impedance Correlation 1
# df_ByName17332B = 'Excel/df_ByName17332B.csv'
#
# df1=pd.read_csv(df_ByName17332B,'\t',index_col=0)
# Active=list(df1['Active Percent (%)'])
# SNR=list(df1['SNR'])
# SNR_SD=list(df1['SNR SD'])
# SpikeRate=list(df1['Frequency (Hz)'])
# SpikeRate_SD=list(df1['Frequency SD (Hz)'])
#
# x_label=list(df1.index)
#
# dic=dict()
# for i in range(len(x_label)):
#     dic[x_label[i]]=[Active[i]]+[SNR[i]]+[SNR_SD[i]]+[SpikeRate[i]]+[SpikeRate_SD[i]]
#
# Z_df = pd.read_excel('Excel/EffectiveAspectRatio.xlsx',sheet_name='V17.1')
# Z = np.array(Z_df['Effective Aspect Ratio (L/W)'])*0.2222
# Label=np.array(Z_df['Label'])
#
# Active=[]
# SNR=[]
# SNR_SD=[]
# SpikeRate=[]
# SpikeRate_SD=[]
# for i in Label:
#     Active.append(dic[i][0])
#     SNR.append(dic[i][1])
#     SNR_SD.append(dic[i][2])
#     SpikeRate.append(dic[i][3])
#     SpikeRate_SD.append(dic[i][4])
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# ax1_a=ax1.twinx()
# ax1_b=ax1.twinx()
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
# Z=np.array(['\n ('+str(round(i,2))+' M$\Omega$)' for i in Z])
# Label=Label+Z
#
# ax1.bar(range(len(Active)), Active, align='center',width=0.5,color='r',alpha=0.666)
# # ax1_a.plot(range(len(Z)),Z, label="$R_{igloo}$ (M$\Omega$)",color='b',alpha=0.35)
# ax1_a.set_ylim(0,10)
# SNR_lolims=(np.array(SNR)-np.array(SNR_SD))<0
# ax1_a.errorbar(range(len(SNR)),SNR,yerr=SNR_SD,color='g',alpha=0.8,marker='_',linewidth=1.5,lolims=SNR_lolims)
# ax1_a.set_ylabel('Signal to Noise Ratio')
# ax1_a.yaxis.set_label_coords(1.035,0.25)
#
# ax1_b.set_ylim(0,2.5)
# SpikeRate_lolims=(np.array(SpikeRate)-np.array(SpikeRate_SD))<0
# ax1_b.errorbar(range(len(SpikeRate)),SpikeRate,yerr=SpikeRate_SD,color='b',alpha=0.8,marker='_',linewidth=1.5,lolims=SpikeRate_lolims)
# ax1_b.spines['right'].set_position(('outward',50))
# ax1_b.set_ylabel('Spike Rate (Hz)')
# ax1_b.yaxis.set_label_coords(1.095,0.75)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(Label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1_a.set_ybound(20,40)
# ax1_a.set_yticks([0,5,10,15,20,40])
# ax1_a.set_yticklabels([0,5,10,15,20,''],color='g',alpha=0.88,size=6)
#
# ax1_b.set_ybound(-8,8)
# ax1_b.set_yticks([-8,0,2,4,6,8])
# ax1_b.set_yticklabels(['',0,2,4,6,8],color='b',alpha=0.88,size=6)
#
# ax1.set_ylabel("Active Percent (%)")
# # ax1.grid(False)
# ax1_a.grid(False)
# ax1_b.grid(False)
# plt.title('$R_{igloo}$ Correlation in MEA 17332 8DIV')
# plt.show()

    # Impedance Correlation 2
# df_ByName17332B = 'Excel/df_ByName17332B.csv'
#
# df1=pd.read_csv(df_ByName17332B,'\t',index_col=0)
# Active=list(df1['Active Percent (%)'])
# SNR=list(df1['SNR'])
# SNR_SD=list(df1['SNR SD'])
# SpikeRate=list(df1['Frequency (Hz)'])
# SpikeRate_SD=list(df1['Frequency SD (Hz)'])
#
# x_label=list(df1.index)
#
# dic=dict()
# for i in range(len(x_label)):
#     dic[x_label[i]]=[Active[i]]+[SNR[i]]+[SNR_SD[i]]+[SpikeRate[i]]+[SpikeRate_SD[i]]
#
# Z_df = pd.read_excel('Excel/EffectiveAspectRatio.xlsx',sheet_name='V17.1')
# Z = np.array(Z_df['Effective Aspect Ratio (L/W)'])*0.2222
# Label=np.array(Z_df['Label'])
#
# Active=[]
# SNR=[]
# SNR_SD=[]
# SpikeRate=[]
# SpikeRate_SD=[]
# for i in Label:
#     Active.append(dic[i][0])
#     SNR.append(dic[i][1])
#     SNR_SD.append(dic[i][2])
#     SpikeRate.append(dic[i][3])
#     SpikeRate_SD.append(dic[i][4])
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# ax1_a=ax1.twinx()
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
# Z=np.array(['\n ('+str(round(i,2))+' M$\Omega$)' for i in Z])
# Label=Label+Z
#
# ax1.bar(range(len(Active)), Active, align='center',width=0.5,color='r',alpha=0.666)
# ax1_a.set_ylim(0,10)
# SNR_lolims=(np.array(SNR)-np.array(SNR_SD))<0
# ax1_a.errorbar(range(len(SNR)),SNR,yerr=SNR_SD,color='g',alpha=0.8,marker='_',linewidth=1.5,lolims=SNR_lolims)
# ax1_a.set_ylabel('Signal to Noise Ratio')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(Label,size=8.8)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1_a.set_yticks([0,5,10,15,20])
#
# ax1.set_ylabel("Active Percent (%)")
# ax1_a.grid(False)
# plt.show()
# End of MEA 17332B



# MEA 17336B

    # Spike Rate
# df_ByDiameter17336B = 'Excel/df_ByDiameter17336B.csv'
# df_ByOpenings17336B = 'Excel/df_ByOpenings17336B.csv'
# df_ByBranch17336B = 'Excel/df_ByBranch17336B.csv'
#
# df1=pd.read_csv(df_ByDiameter17336B,'\t',index_col=0)
# spikerate1=list(df1['Frequency (Hz)'])
# spikerate_SD1=list(df1['Frequency SD (Hz)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336B,'\t',index_col=0)
# spikerate2=list(df2['Frequency (Hz)'])
# spikerate_SD2=list(df2['Frequency SD (Hz)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336B,'\t',index_col=0)
# spikerate3=list(df3['Frequency (Hz)'])
# spikerate_SD3=list(df3['Frequency SD (Hz)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(spikerate1)+len(spikerate2)+len(spikerate3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(spikerate1)), spikerate1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)),spikerate1,yerr=spikerate_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1), spikerate2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+1,len(spikerate1)+len(spikerate2)+1),spikerate2,yerr=spikerate_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2), spikerate3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(spikerate1)+len(spikerate2)+2,len(spikerate1)+len(spikerate2)+len(spikerate3)+2),spikerate3,yerr=spikerate_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,8)
# ax1.set_yticks([0,1,2,3,4,5,6,7,8])
# ax1.grid(b=None)
# ax1.set_ylabel("Spike Rate (Hz)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 8DIV')
# plt.show()

    # Signal Noise Ratio
# df_ByDiameter17336B = 'Excel/df_ByDiameter17336B.csv'
# df_ByOpenings17336B = 'Excel/df_ByOpenings17336B.csv'
# df_ByBranch17336B = 'Excel/df_ByBranch17336B.csv'
#
# df1=pd.read_csv(df_ByDiameter17336B,'\t',index_col=0)
# SNR1=list(df1['SNR'])
# SNR_SD1=list(df1['SNR SD'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336B,'\t',index_col=0)
# SNR2=list(df2['SNR'])
# SNR_SD2=list(df2['SNR SD'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336B,'\t',index_col=0)
# SNR3=list(df3['SNR'])
# SNR_SD3=list(df3['SNR SD'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(SNR1)+len(SNR2)+len(SNR3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(SNR1)), SNR1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(SNR1)),SNR1,yerr=SNR_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1), SNR2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+1,len(SNR1)+len(SNR2)+1),SNR2,yerr=SNR_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2), SNR3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(SNR1)+len(SNR2)+2,len(SNR1)+len(SNR2)+len(SNR3)+2),SNR3,yerr=SNR_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,16)
# ax1.set_yticks([0,2,4,6,8,10,12,14,16])
# ax1.grid(b=None)
# ax1.set_ylabel("Signal Noise Ratio")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 8DIV')
# plt.show()

    # Amplitude
# df_ByDiameter17336B = 'Excel/df_ByDiameter17336B.csv'
# df_ByOpenings17336B = 'Excel/df_ByOpenings17336B.csv'
# df_ByBranch17336B = 'Excel/df_ByBranch17336B.csv'
#
# df1=pd.read_csv(df_ByDiameter17336B,'\t',index_col=0)
# Amp1=list(df1['Amplitude l (uV)'])
# Amp_SD1=list(df1['Amplitude l SD (uV)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336B,'\t',index_col=0)
# Amp2=list(df2['Amplitude l (uV)'])
# Amp_SD2=list(df2['Amplitude l SD (uV)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336B,'\t',index_col=0)
# Amp3=list(df3['Amplitude l (uV)'])
# Amp_SD3=list(df3['Amplitude l SD (uV)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Amp1)+len(Amp2)+len(Amp3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Amp1)), Amp1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.errorbar(range(len(Amp1)),Amp1,yerr=Amp_SD1,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1), Amp2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+1,len(Amp1)+len(Amp2)+1),Amp2,yerr=Amp_SD2,color='gray',marker='_',linestyle='None')
#
# ax1.bar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2), Amp3, align='center',width=0.5,color='b',alpha=0.666)
# ax1.errorbar(range(len(Amp1)+len(Amp2)+2,len(Amp1)+len(Amp2)+len(Amp3)+2),Amp3,yerr=Amp_SD3,color='gray',marker='_',linestyle='None')
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,60)
# ax1.set_yticks([0,15,30,45,60])
# ax1.grid(b=None)
# ax1.set_ylabel("Amplitude ($\mu$V)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 8DIV')
# plt.show()

    # Activeness
# df_ByDiameter17336B = 'Excel/df_ByDiameter17336B.csv'
# df_ByOpenings17336B = 'Excel/df_ByOpenings17336B.csv'
# df_ByBranch17336B = 'Excel/df_ByBranch17336B.csv'
#
# df1=pd.read_csv(df_ByDiameter17336B,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# df2=pd.read_csv(df_ByOpenings17336B,'\t',index_col=0)
# Active2=list(df2['Active Percent (%)'])
# x_label2=list(df2.index)
#
# df3=pd.read_csv(df_ByBranch17336B,'\t',index_col=0)
# Active3=list(df3['Active Percent (%)'])
# x_label3=list(df3.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)+len(Active2)+len(Active3)+2
# x_label=x_label1+x_label2+x_label3
# x_ticks=[0,1,3,4,5,6,8,9,10]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
# ax1.bar(range(len(Active1)+1,len(Active1)+len(Active2)+1), Active2, align='center',width=0.5,color='g',alpha=0.666)
# ax1.bar(range(len(Active1)+len(Active2)+2,len(Active1)+len(Active2)+len(Active3)+2), Active3, align='center',width=0.5,color='b',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1.grid(b=None)
# ax1.set_ylabel("Active Percent (%)")
# plt.annotate('Igloo Diameter ($\mu$m)',(0.033,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Number of Openings (#)',(0.36,-0.1),size=6,xycoords="axes fraction")
# plt.annotate('Branch Level (#)',(0.78,-0.1),size=6,xycoords="axes fraction")
# plt.title('MEA 17336 8DIV')
# plt.show()

    # Activeness 2
# df_ByName17336B = 'Excel/df_ByName17336B.csv'
#
# df1=pd.read_csv(df_ByName17336B,'\t',index_col=0)
# Active1=list(df1['Active Percent (%)'])
# x_label1=list(df1.index)
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# x_length=len(Active1)
# x_label=x_label1
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
#
# ax1.bar(range(len(Active1)), Active1, align='center',width=0.5,color='r',alpha=0.666)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(x_label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
#
# ax1.set_ylabel("Active Percent (%)")
# plt.title('MEA 17336 8DIV')
# plt.show()

    # Impedance Correlation 1
# df_ByName17336B = 'Excel/df_ByName17336B.csv'
#
# df1=pd.read_csv(df_ByName17336B,'\t',index_col=0)
# Active=list(df1['Active Percent (%)'])
# SNR=list(df1['SNR'])
# SNR_SD=list(df1['SNR SD'])
# SpikeRate=list(df1['Frequency (Hz)'])
# SpikeRate_SD=list(df1['Frequency SD (Hz)'])
#
# x_label=list(df1.index)
#
# dic=dict()
# for i in range(len(x_label)):
#     dic[x_label[i]]=[Active[i]]+[SNR[i]]+[SNR_SD[i]]+[SpikeRate[i]]+[SpikeRate_SD[i]]
#
# Z_df = pd.read_excel('Excel/EffectiveAspectRatio.xlsx',sheet_name='V17.1')
# Z = np.array(Z_df['Effective Aspect Ratio (L/W)'])*0.2222
# Label=np.array(Z_df['Label'])
#
# Active=[]
# SNR=[]
# SNR_SD=[]
# SpikeRate=[]
# SpikeRate_SD=[]
# for i in Label:
#     Active.append(dic[i][0])
#     SNR.append(dic[i][1])
#     SNR_SD.append(dic[i][2])
#     SpikeRate.append(dic[i][3])
#     SpikeRate_SD.append(dic[i][4])
#
# fig=plt.figure()
# ax1=fig.add_subplot(111)
# ax1_a=ax1.twinx()
# ax1_b=ax1.twinx()
# x_ticks=[0,1,2,3,4,5,6,7,8,9]
#
# Z=np.array(['\n ('+str(round(i,2))+' M$\Omega$)' for i in Z])
# Label=Label+Z
#
# ax1.bar(range(len(Active)), Active, align='center',width=0.5,color='r',alpha=0.666)
# # ax1_a.plot(range(len(Z)),Z, label="$R_{igloo}$ (M$\Omega$)",color='b',alpha=0.35)
# ax1_a.set_ylim(0,10)
# SNR_lolims=(np.array(SNR)-np.array(SNR_SD))<0
# ax1_a.errorbar(range(len(SNR)),SNR,yerr=SNR_SD,color='g',alpha=0.8,marker='_',linewidth=1.5,lolims=SNR_lolims)
# ax1_a.set_ylabel('Signal to Noise Ratio',size=6)
# ax1_a.yaxis.set_label_coords(1.035,0.25)
#
# ax1_b.set_ylim(0,2.5)
# SpikeRate_lolims=(np.array(SpikeRate)-np.array(SpikeRate_SD))<0
# ax1_b.errorbar(range(len(SpikeRate)),SpikeRate,yerr=SpikeRate_SD,color='b',alpha=0.8,marker='_',linewidth=1.5,lolims=SpikeRate_lolims)
# ax1_b.spines['right'].set_position(('outward',50))
# ax1_b.set_ylabel('Spike Rate (Hz)',size=6)
# ax1_b.yaxis.set_label_coords(1.095,0.75)
#
# ax1.set_xticks(x_ticks)
# ax1.set_xticklabels(Label,size=5)
# ax1.set_ybound(0,100)
# ax1.set_yticks([0,20,40,60,80,100])
# ax1_a.set_ybound(0,40)
# ax1_a.set_yticks([0,5,10,15,20,40])
# ax1_a.set_yticklabels([0,5,10,15,20,''],color='g',alpha=0.88,size=6)
#
# ax1_b.set_ybound(-8,8)
# ax1_b.set_yticks([-8,0,2,4,6,8])
# ax1_b.set_yticklabels(['',0,2,4,6,8],color='b',alpha=0.88,size=6)
#
# ax1.set_ylabel("Active Percent (%)")
# # ax1.grid(False)
# ax1_a.grid(False)
# ax1_b.grid(False)
# plt.title('$R_{igloo}$ Correlation in MEA 17336 8DIV')
# plt.show()

    # Impedance Correlation2
df_ByName17336B = 'ExcelFiles/df_ByName17336B.csv'

df1=pd.read_csv(df_ByName17336B,'\t',index_col=0)
Active=list(df1['Active Percent (%)'])
SNR=list(df1['SNR'])
SNR_SD=list(df1['SNR SD'])
SpikeRate=list(df1['Frequency (Hz)'])
SpikeRate_SD=list(df1['Frequency SD (Hz)'])

x_label=list(df1.index)

dic=dict()
for i in range(len(x_label)):
    dic[x_label[i]]=[Active[i]]+[SNR[i]]+[SNR_SD[i]]+[SpikeRate[i]]+[SpikeRate_SD[i]]

Z_df = pd.read_excel('ExcelFiles/EffectiveAspectRatio.xlsx',sheet_name='V17.1')
Z = np.array(Z_df['Effective Aspect Ratio (L/W)'])*0.2222
Label=np.array(Z_df['Label'])

Active=[]
SNR=[]
SNR_SD=[]
SpikeRate=[]
SpikeRate_SD=[]
for i in Label:
    Active.append(dic[i][0])
    SNR.append(dic[i][1])
    SNR_SD.append(dic[i][2])
    SpikeRate.append(dic[i][3])
    SpikeRate_SD.append(dic[i][4])

fig=plt.figure()
ax1=fig.add_subplot(111)
ax1_a=ax1.twinx()
x_ticks=[0,1,2,3,4,5,6,7,8,9]

Z=np.array(['\n ('+str(round(i,2))+' M$\Omega$)' for i in Z])
Label=Label+Z

ax1.bar(range(len(Active)), Active, align='center',width=0.5,color='r',alpha=0.666)
SNR_lolims=(np.array(SNR)-np.array(SNR_SD))<0
ax1_a.errorbar(range(len(SNR)),SNR,yerr=SNR_SD,color='g',alpha=0.8,marker='_',linewidth=1.5,lolims=SNR_lolims)
ax1_a.set_ylabel('Signal to Noise Ratio')

ax1.set_xticks(x_ticks)
ax1.set_xticklabels(Label,size=8.8)
ax1.set_ybound(0,100)
ax1.set_yticks([0,20,40,60,80,100])
ax1_a.set_yticks([0,5,10,15,20])

ax1.set_ylabel("Active Percent (%)")
ax1_a.grid(False)

plt.show()
# End of MEA 17336B