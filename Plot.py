import glob
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn-whitegrid')

l_measured_D150S2W5=['A15','D13','D04','E01','G10']
l_measured_D45S6W75=['B05','C12','D09','E06']
l_measured_uncovered=['B09','B08','C06','D10','F07','G05']

def MEAImpedanceSpectroscopyPlot_T(R_igloo,C_b=2.87*(10**-12),C_s=15.28*(10**-12),C_e=1.05*(10**-9),params=[10**(0),10**(6),10]):
    # assuming R_e >>> R_igloo, the amplitude of total impedance Z_total is not a function of R_e
    # C_e -> double layer capacitance, C_s -> capacitance formed by the conduction path and the electrolyte, C_b -> built-in capacitance from the SolarTron
    # R_igloo -> the electrolytic resistance of the igloo (or a bare spreading resistance)
    # a,b,c,d,e below are five parts of the final equation

    start=params[0]
    end=params[1]+1
    step=params[2]

    f=np.array(range(start-1,end+1,step))
    f[0]=1

    W=f*2*math.pi
    Z_total=[]

    for w in W:

        # a=(w**2)*(R_igloo**2)*(C_e**4)
        # b=C_e+C_s+C_b
        # c=((w**2)*(R_igloo**2)*(C_e**2))*(C_s+C_b)
        # d=(C_e+C_s+C_b)**2
        # e=((w**2)*(R_igloo**2)*(C_e**2))*((C_s+C_b)**2)
        # result=((a+((b+c)**2))/((w**2)*((d+e)**2)))**(1/2)
        # Z_total.append(result)

        Z_C_s = 1 / (w * C_s)
        Z_C_e = 1 / (w * C_e)
        Z_C_solartron = 1 / (w * C_b)
        Z_R_igloo = R_igloo

        # a = C_e & R_igloo in series
        a = Z_C_e + Z_R_igloo
        # b = C_s in parallel with "a"
        b = 1 / ((1 / Z_C_s) + (1 / a))
        # c = C_solartron in parallel with "b"
        c = 1 / ((1 / b) + (1 / Z_C_solartron))

        z_total = c
        Z_total.append(z_total)


    x_tick_start=int(math.log10(start))
    x_tick_end=int((math.log10(end)+1))
    x_tick=[]

    for i in range(x_tick_start,x_tick_end):
        x_tick.append(10**i)

    return (f,Z_total,x_tick)


def MEAImpedanceSpectroscopyPlot_E(measured,design,R_igloo,C_s=6*(10**-12),C_e=0.05*(10**-9),r=1,title='MEA Impedance Spectroscopy'):
    if design=='D150 S2 W5':
        R_design=1.66*(10**6)
    elif design=='D45 S6 W7.5':
        R_design=111111
    elif design=='Uncovered':
        R_design=11111
    l_filename=glob.glob('*/*/*.z')

    l_file=[]
    for i in l_filename:
        l=[j in i for j in measured]
        if any(l):
            l_file.append(i)

    l_file2=[]
    for i in l_file:
        if not "fitresult" in i.lower():
            l_file2.append(i)

    l_file=l_file2
    print(l_file)
    (f_t,Z_t,x_tick)=MEAImpedanceSpectroscopyPlot_T(R_design)
    (f_f,Z_f,x_tick)=MEAImpedanceSpectroscopyPlot_T(R_igloo, C_s=C_s, C_e=C_e)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.loglog(f_t,Z_t,color='r',linewidth=2,label="theoretical")
    ax1.loglog(f_f,Z_f,color='g',linewidth=2,label="fit")
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_xticks(x_tick)
    ax1.set_ylabel('Impedance (Ω)')
    ax1.set_title(title)

    for i in l_file:
        df=pd.read_csv(i,skiprows=124,delimiter='\t',header=0)
        df.drop([0], inplace=True)

        columns=df.columns.values
        columns=[i.strip() for i in columns]
        df=df.iloc[:,[0,4,5]]

        df.columns.values[0]='Frequency'
        df.columns.values[1]='Real'
        df.columns.values[2]='Imaginary'

        df['|Z|']=df.apply(lambda row: ((row.Real**2)+(row.Imaginary**2))**(1/2),axis=1)
        df['Frequency']=df['Frequency'].apply(lambda x: float(x))
        df=df.iloc[:,[0,3]]

        frequencyrange=df[df.Frequency>=r].index
        df=df.loc[frequencyrange]
        ax1.loglog(df['Frequency'],df['|Z|'],marker=',',color='#00FFFF',alpha=0.8,linewidth=0.66,label='_nolegend_')
        plt.legend()



#tweek-able parameters: R_igloo, C_s, C_e
MEAImpedanceSpectroscopyPlot_E(l_measured_D150S2W5,'D150 S2 W5',R_igloo=1.1*(10**6),title="MEA Impedance Spectroscopy (D150 S2 W5)")
MEAImpedanceSpectroscopyPlot_E(l_measured_D45S6W75,'D45 S6 W7.5',R_igloo=90000,title="MEA Impedance Spectroscopy (D45 S6 W7.5)")
MEAImpedanceSpectroscopyPlot_E(l_measured_uncovered,'Uncovered',R_igloo=30000,title="MEA Impedance Spectroscopy (Uncovered)")


plt.show()