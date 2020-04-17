import sys
sys.path.insert(0, '../MEA')

from Util import readExcel, selectTimeSequence
from SpikeAnalysis import analyzeRecordings, analyzeByDesign
from SpikeVisualization import plotDeviceData, violinByDesign
from SpikeTest import T_table




#Igloo MEA specific functions below

def electricalResistance(c_length=None,c_width=None,c_height=0.0003,conductance=0.015,openings=None,d_uncovered=None):
    # the electrolytic resistance for each electrode from the MEA device
    # all channel parameters in 'cm'

    if openings is None:
        d_uncovered=0.003
        r_uncovered=d_uncovered/2
        R_s=(1/conductance)/(4*r_uncovered)
        return R_s
    else:
        # the length for each resistor segment is half the diameter, aka the channel length
        c_length = c_length / 2
        R_seg = (1/conductance)*(c_length/(c_width*c_height))
        R_eq = R_seg/openings
        return R_eq

def JNnoise(R,T=310.15,f=3500):
    #returns the Johnston noise

    k_B = 1.3806 * (10**(-23))
    V_n = (4*k_B*T*R*f)**(1/2)
    return V_n

def ImpedanceMeasurementAidSheet(table1,table2='ExcelFiles/locations_final.xlsx'):
    # table1 variable refers to the excel file which links the spring contact to its corresponding electrode label
    # table2 variable refers to the excel file which links the electrode label to its corresponding design

    dic1=readExcel(path=table2,param="Name",skiprow=1)
    for i in dic1.keys():
        j=i.replace(',','.')
        if j !=i:
            dic1[j]=dic1[i]
            del dic1[i]

    i=[]
    for v in dic1.values():
        i.extend(v)

    dic2={}

    dic={}
    dic['Spring Contact']=[None]*len(i)
    dic['Electrode Label']=i
    dic['Device Type'] = [None] * len(i)
    dic['R_theoretical (MΩ)'] = [None] * len(i)
    dic['R_measured (MΩ)'] = [None] * len(i)

    df=pd.DataFrame(data=dic)

    for i in dic1.keys():
        for j in dic1[i]:
            dic2[j]=i

    df_s2e = pd.read_excel(table1, sheet_name="Sheet1", index_col='Spring Contact')
    df_s2e.sort_index(inplace=True)

    j2i={'J10':'I10','J11':'I11','J12':'I12','J13':'I13','J14':'I14','J15':'I15','J16':'I16','R01':'R14'}
    counter=0
    for i in df_s2e['Electrode Label']:
        if len(i.strip())<3:
            df_s2e.at[counter+1,'Electrode Label']=i[0]+'0'+i[1]
        counter+=1

    counter=0
    for i in df_s2e['Electrode Label']:
        if i in j2i.keys():
            df_s2e.at[counter + 1, 'Electrode Label'] = j2i[i]
        counter+=1

    # print(df_s2e.sort_values(by=['Electrode Label']))

    counter=0
    for i in df['Electrode Label']:
        df.at[counter,'Device Type']=dic2[i]
        # print(i)
        df.at[counter, 'Spring Contact'] = df_s2e.index[df_s2e['Electrode Label'] == i].tolist()[0]
        if dic2[i] != 'Uncovered':
            l=dic2[i].split(' ')
            c_length=float(l[0][1:])
            openings=float(l[1][1:])
            c_width=float(l[2][1:])
            R=electricalResistance(c_length=c_length/(10**4),c_width=c_width/(10**4),openings=openings)
            df.at[counter,'R_theoretical (MΩ)']=round(R/(10**6),4)
        else:
            R=11111
            df.at[counter, 'R_theoretical (MΩ)'] = round(R/(10**6),4)


        counter+=1

    df.set_index('Spring Contact',inplace=True)
    df.sort_index(inplace=True)

    print(df)
    df.to_csv('Excel/ImpedanceMeasurementAidSheet.csv')
    return None

def MEAImpedanceSpectrocopyPlot(R_igloo,C_b=2.87*(10**-12),C_s=15.28*(10**-12),C_e=1.05*(10**-9),params=[10**(0),10**(6),10],title="MEA Impedance Spectroscopy"):
    # assuming R_e >>> R_igloo, the amplitude of total impedance Z_total is not a function of R_e
    # C_e -> double layer capacitance, C_s -> capacitance formed by the conduction path and the electrolyte, C_b -> built-in capacitance from the SolarTron
    # R_igloo -> the electrolytic resistance of the igloo (or a bare spreading resistance)
    # a,b,c,d,e below are five parts of the final derived equation

    style.use('seaborn-whitegrid')

    start=params[0]
    end=params[1]+1
    step=params[2]

    f=np.array(range(start-1,end+1,step))
    f[0]=1

    W=f*2*math.pi
    Z_total=[]

    for w in W:

        a=(w**2)*(R_igloo**2)*(C_e**4)
        b=C_e+C_s+C_b
        c=((w**2)*(R_igloo**2)*(C_e**2))*(C_s+C_b)
        d=(C_e+C_s+C_b)**2
        e=((w**2)*(R_igloo**2)*(C_e**2))*((C_s+C_b)**2)
        result=((a+((b+c)**2))/((w**2)*((d+e)**2)))**(1/2)
        Z_total.append(result)

        # Z_C_s = 1 / (w * C_s)
        # Z_C_e = 1 / (w * C_e)
        # Z_C_solartron = 1 / (w * C_b)
        # Z_R_igloo = R_igloo
        #
        # # a = C_e & R_igloo in series
        # a = Z_C_e + Z_R_igloo
        # # b = C_s in parallel with "a"
        # b = 1 / ((1 / Z_C_s) + (1 / a))
        # # c = C_solartron in parallel with "b"
        # c = 1 / ((1 / b) + (1 / Z_C_solartron))
        #
        # z_total = c
        # Z_total.append(z_total)


    x_tick_start=int(math.log10(start))
    x_tick_end=int((math.log10(end)+1))
    x_tick=[]

    for i in range(x_tick_start,x_tick_end):
        x_tick.append(10**i)

    fig = plt.figure()
    global ax1
    ax1 = fig.add_subplot(111)
    ax1.loglog(f,Z_total)
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_xticks(x_tick)
    ax1.set_ylabel('Impedance (Ω)')
    ax1.set_title(title)
    plt.show()

def electricalResistanceTable(path,skiprow=1):
    designDict=readExcel(path,param="Name",skiprow=1)
    RDic=dict()
    for i in designDict.keys():
        if i == 'Uncovered':
            RDic[i]=electricalResistance()
        else:
            [d, o, w] = i.split(' ')
            c_length = int(d[1:]) / (10 ** 4)
            openings = int(o[1:])
            c_width = float(w.replace(',', '.')[1:]) / (10 ** 4)
            RDic[i]=electricalResistance(c_length=c_length,c_width=c_width,openings=openings)

    print(RDic)

    deviceDict=dict()
    for i,resistance in RDic.items():
        for j in designDict[i]:
            deviceDict[j]=resistance

    output=pd.DataFrame.from_dict(deviceDict, orient='index')
    output.sort_index(inplace=True)
    output.rename(columns={0: "Resistance (Ohm)"},inplace=True)
    output=output.astype(int)
    # output.round(0)

    path = 'Excel/Resistance.csv'
    output.to_csv(path, sep='\t', encoding="utf-8")

    return output








#Demo

ExcelPath='ExcelFiles/V17.1/Location17336.xlsx'
path17336_8DIV='../../../../../../Volumes/HLiuUSB/HippoH5/V17.1/Hippo_10kperuL_new igloo_8DIV_17336_test.h5'

# selectTimeSequence(path17336_8DIV,300)

# print(readExcel(ExcelPath,param="Name",skiprow=0))

# plotDeviceData(path17336_8DIV,'C02',300)

# print(analyzeRecordings(path17336_8DIV,300))

pick17336_8DIV='DataframePickle/df3D17336_8DIV.pickle'

# print(analyzeByDesign(pick17336_8DIV,ExcelPath,param='Name',skiprow=0))

# violinByDesign("SNR",pick17336_8DIV,ExcelPath,'Name', skiprow=0,title='MEA 17336 8DIV \n ')

# print(T_table(pick17336_8DIV,ExcelPath,'ptable'))