import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math
import seaborn
from scipy.stats import norm
import scipy.optimize as opt

#input optimal and original CV model tracks from Knigge et al. 2011
m2_optimal = np.loadtxt('Knigge11/knigge11_optimal.dat',dtype=float,usecols = [0],skiprows=4)
P_optimal = np.loadtxt('Knigge11/knigge11_optimal.dat',dtype=float,usecols = [1],skiprows=4)
m2_standard = np.loadtxt('Knigge11/knigge11_standard.dat',dtype=float,usecols = [1],skiprows=4)
P_standard = np.loadtxt('Knigge11/knigge11_standard.dat',dtype=float,usecols = [2],skiprows=4)

P_k11_ds = np.loadtxt('Knigge11/knigge11_don_seq.dat',dtype=float,usecols = [0],skiprows=3)
m2_k11_ds = np.loadtxt('Knigge11/knigge11_don_seq.dat',dtype=float,usecols = [1],skiprows=3)
r2_k11_ds = np.loadtxt('Knigge11/knigge11_don_seq.dat',dtype=float,usecols = [2],skiprows=3)

#input BD donor track from Kolb & Baraffe 1999
m2_BD_1 = np.loadtxt('KolbBaraffe99/KolbBaraffe99_BD.dat',dtype=float,usecols = [2])
P_BD_1 = np.loadtxt('KolbBaraffe99/KolbBaraffe99_BD.dat',dtype=float,usecols = [18])

#input BD donor tracks from Baraffe (Priv. comm)
m2_BD_2 = np.loadtxt('Baraffe/Baraffe_t2gyr.dat',dtype=float,usecols = [2])
P_BD_2 = np.loadtxt('Baraffe/Baraffe_t2gyr.dat',dtype=float,usecols = [18])
m2_BD_3 = np.loadtxt('Baraffe/Baraffe_t1gyr.dat',dtype=float,usecols = [2])
P_BD_3 = np.loadtxt('Baraffe/Baraffe_t1gyr.dat',dtype=float,usecols = [18])
m2_BD_4 = np.loadtxt('Baraffe/Baraffe_t600myr.dat',dtype=float,usecols = [2])
P_BD_4 = np.loadtxt('Baraffe/Baraffe_t600myr.dat',dtype=float,usecols = [18])

#input evolved donor tracks from thorstensen et al. 2002
m2_evol_12 = np.loadtxt('Thorstensen02/thorstensen02_evol1.2.dat',dtype=float,usecols = [1])
P_evol_12 = np.loadtxt('Thorstensen02/thorstensen02_evol1.2.dat',dtype=float,usecols = [0])
m2_evol_15 = np.loadtxt('Thorstensen02/thorstensen02_evol1.5.dat',dtype=float,usecols = [1])
P_evol_15 = np.loadtxt('Thorstensen02/thorstensen02_evol1.5.dat',dtype=float,usecols = [0])

#produce plot

seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

#plt.rcParams['xtick.major.pad']='15'
#plt.rcParams['ytick.major.pad']='10'

#plt.axis([1.1,1.70001,0.03,0.12001])
#plt.axis([1.1,2.5001,0.0,0.25001])
#plt.axis([1.0,3.001,0.02,0.401])
#plt.axis([1.1,1.6,0.03,0.11])
#plt.tick_params(top='on',right='on')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([1.0, 7.5])
ax.set_xticks([1,2,3,4,5,6,7])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_yscale('log')
ax.set_ylim([0.02, 0.9])
ax.set_yticks([0.02,0.04,0.06,0.08,0.1,0.2,0.4,0.6,0.8])
ax.get_yaxis().set_major_formatter(ScalarFormatter())
ax.minorticks_off()


############ PHL 1445 paper ##############


#plt.scatter(0.0529848884*24,0.064,marker='o',color='k',s=10)
#plt.errorbar(0.0529848884*24,0.064,yerr=0.006,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0529848884*24,0.063,'  PHL 1445',color='k',size=12)


############ DONE (with GPs) ##############


plt.scatter(0.0529848884*24,0.071,marker='o',color='g',s=10)
plt.errorbar(0.0529848884*24,0.071,yerr=[[0.005],[0.009]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0529848884*24,0.071,'  PHL 1445 (10 ecl)',color='g',size=12)

#plt.scatter(0.0529848884*24,0.061,marker='o',color='g',s=10)
#plt.errorbar(0.0529848884*24,0.061,yerr=[[0.008],[0.005]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0529848884*24,0.061,'  PHL 1445 (6 ecl)',color='g',size=12)

plt.scatter(0.060310649*24,0.109,marker='o',color='g',s=10)
plt.errorbar(0.060310649*24,0.109,yerr=[[0.013],[0.012]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.060310649*24,0.109,'  ASASSN-14ag',color='g',size=12)

plt.scatter(0.0739089282*24,0.141,marker='o',color='g',s=10)
plt.errorbar(0.0739089282*24,0.141,yerr=[[0.007],[0.007]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0739089282*24,0.141,'  IY UMa',color='g',size=12)

plt.scatter(0.0744992631*24,0.152,marker='o',color='g',s=10)
plt.errorbar(0.0744992631*24,0.152,yerr=[[0.005],[0.006]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0744992631*24,0.152,'  Z Cha',color='g',size=12)

plt.scatter(0.059578970*24,0.081,marker='o',color='g',s=10)
plt.errorbar(0.059578970*24,0.081,yerr=[[0.005],[0.005]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.059578970*24,0.081,'  CSS080623',color='g',size=12)

plt.scatter(0.0778805320*24,0.138,marker='o',color='g',s=10)
plt.errorbar(0.0778805320*24,0.138,yerr=[[0.007],[0.007]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0778805320*24,0.138,'  SDSS 0901',color='g',size=12)

plt.scatter(0.0858526521*24,0.187,marker='o',color='g',s=10)
plt.errorbar(0.0858526521*24,0.187,yerr=[[0.012],[0.003]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0858526521*24,0.187,'  DV UMa',color='g',size=12)

plt.scatter(0.088940717*24,0.166,marker='o',color='g',s=10)
plt.errorbar(0.088940717*24,0.166,yerr=[[0.003],[0.006]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.088940717*24,0.166,'  CTCV 1300',color='g',size=12)

plt.scatter(0.0631209221*24,0.093,marker='o',color='g',s=10)
plt.errorbar(0.0631209221*24,0.093,yerr=[[0.001],[0.003]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0631209221*24,0.093,'  OY Car',color='g',size=12)

plt.scatter(0.065769292*24,0.140,marker='o',color='g',s=10)
plt.errorbar(0.065769292*24,0.140,yerr=[[0.008],[0.012]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.065769292*24,0.140,'  SSS130413',color='g',size=12)

plt.scatter(0.0660508707*24,0.105,marker='o',color='g',s=10)
plt.errorbar(0.0660508707*24,0.105,yerr=[[0.006],[0.008]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0660508707*24,0.105,'  CSS110113',color='g',size=12)

plt.scatter(0.0587045*24,0.083,marker='o',color='g',s=10)
plt.errorbar(0.0587045*24,0.083,yerr=[[0.004],[0.006]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0587045*24,0.083,'  SSS100615',color='g',size=12)

plt.scatter(0.0677497026*24,0.094,marker='o',color='g',s=10)
plt.errorbar(0.0677497026*24,0.094,yerr=[[0.009],[0.016]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0677497026*24,0.094,'  SDSS 1152',color='g',size=12)

plt.scatter(0.0627919557*24,0.0436,marker='o',color='g',s=10)
plt.errorbar(0.0627919557*24,0.0436,yerr=[[0.0017],[0.0025]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0627919557*24,0.0436,'  SDSS1057',color='g',size=12)

plt.scatter(0.185912957*24,0.37,marker='o',color='g',s=10)
plt.errorbar(0.185912957*24,0.37,yerr=[[0.06],[0.06]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.185912957*24,0.37,'  SDSS 1006',color='g',size=12)

plt.scatter(0.1754424023*24,0.394,marker='o',color='g',s=10)
plt.errorbar(0.1754424023*24,0.394,yerr=[[0.022],[0.016]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.1754424023*24,0.394,'  GY Cnc',color='g',size=12)

plt.scatter(0.0854185080*24,0.176,marker='o',color='g',s=10)
plt.errorbar(0.0854185080*24,0.176,yerr=[[0.018],[0.007]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0854185080*24,0.176,'  V713 Cep',color='g',size=12)

plt.scatter(0.0568412623*24,0.061,marker='o',color='g',s=10)
plt.errorbar(0.0568412623*24,0.061,yerr=[[0.003],[0.004]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0568412623*24,0.061,'  SDSS 1501',color='g',size=12)


######### IN LITERATURE ################


# HIGH_TIME RESOLUTION ECLIPSE MODELLING (circles)

'''
# Systems from Savoury 11 that have been revisited

#plt.scatter(0.059578970*24,0.098,marker='o',color='k',s=10,alpha=0.25)
#plt.errorbar(0.059578970*24,0.098,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1,alpha=0.25)
#plt.text(0.059578970*24,0.095,'  CSS080623',color='k',size=12,alpha=0.25)

#plt.scatter(0.0778805320*24,0.161,marker='o',color='k',s=10,alpha=0.25)
#plt.errorbar(0.0778805320*24,0.161,yerr=0.007,ls='none',color='k',capsize=None,linewidth=1,alpha=0.25)
#plt.text(0.0778805320*24,0.162,'  SDSS 0901',color='k',size=12,alpha=0.25)

#plt.scatter(0.088940717*24,0.177,marker='o',color='k',s=10)
#plt.errorbar(0.088940717*24,0.177,yerr=0.021,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.088940717*24,0.177,'  CTCV J1300-3052',color='k',size=12)

#plt.scatter(0.0677497026*24,0.087,marker='o',color='k',s=10)
#plt.errorbar(0.0677497026*24,0.087,yerr=0.006,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0677497026*24,0.087,'  SDSS 1152',color='k',size=12)

#plt.scatter(0.0858526521*24,0.196,marker='o',color='k',s=10)
#plt.errorbar(0.0858526521*24,0.196,yerr=0.005,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0858526521*24,0.196,'  DV UMa',color='k',size=12)

#plt.scatter(0.0568412623*24,0.077,marker='o',color='k',s=10)
#plt.errorbar(0.0568412623*24,0.077,yerr=0.010,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0568412623*24,0.074,'  SDSS 1501',color='k',size=12)
'''

# Systems from Savoury 11

plt.scatter(0.054240679*24,0.0571,marker='o',color='k',s=10)
plt.errorbar(0.054240679*24,0.0571,yerr=0.0007,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.054240679*24,0.0571,'  SDSS 1433',color='k',size=12)

plt.scatter(0.04625828*24,0.0575,marker='o',color='k',s=10)
plt.errorbar(0.04625828*24,0.0575,yerr=0.002,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.04625828*24,0.0551,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0570067*24,0.0475,marker='o',color='k',s=10)
plt.errorbar(0.0570067*24,0.0475,yerr=0.0012,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0570067*24,0.0457,'  SDSS 1035',color='k',size=12)

plt.scatter(0.065550270*24,0.101,marker='o',color='k',s=10)
plt.errorbar(0.065550270*24,0.101,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.065550270*24,0.103,' CTCV J2354-4700',color='k',size=12)

plt.scatter(0.059073543*24,0.099,marker='o',color='k',s=10)
plt.errorbar(0.059073543*24,0.099,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.059073543*24,0.098,'  SDSS 0903',color='k',size=12)

plt.scatter(0.062959041*24,0.0889,marker='o',color='k',s=10)
plt.errorbar(0.062959041*24,0.0889,yerr=0.0025,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.062959041*24,0.0889,'  SDSS 1227',color='k',size=12)

plt.scatter(0.061159491*24,0.091,marker='o',color='k',s=10)
plt.errorbar(0.061159491*24,0.091,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.061159491*24,0.092,'  XZ Eri',color='k',size=12)

plt.scatter(0.05890961*24,0.0781,marker='o',color='k',s=10)
plt.errorbar(0.05890961*24,0.0781,yerr=0.0008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.05890961*24,0.0781,'  SDSS 1502',color='k',size=12)

plt.scatter(0.072706113*24,0.1157,marker='o',color='k',s=10)
plt.errorbar(0.072706113*24,0.1157,yerr=0.0022,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.072706113*24,0.1157,'  OU Vir',color='k',size=12)

plt.scatter(0.10008215*24,0.223,marker='o',color='k',s=10)
plt.errorbar(0.10008215*24,0.223,yerr=0.010,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.10008215*24,0.223,'  SDSS 1702',color='k',size=12)

'''
# Systems from other sources that have been revisited

# From Southworth09
#plt.scatter(0.185912957*24,0.40,marker='o',color='b',s=10,alpha=0.3)
#plt.errorbar(0.185912957*24,0.40,yerr=0.10,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.185912957*24,0.40,'  SDSS 1006_S09',color='b',size=12,alpha=0.3)
'''

# Other systems

#From Shafter03
plt.scatter(0.209937*24,0.53,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.209937*24,0.53,yerr=0.01,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.209937*24,0.53,'  EX Dra_S03',color='b',size=12,alpha=0.3)

#From Littlefair14 (UCAM data)
plt.scatter(0.1653077*24,0.39,marker='o',color='k',s=10)
plt.errorbar(0.1653077*24,0.39,yerr=0.04,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.1653077*24,0.39,'  KIS J1927_L14',color='k',size=12)

#From Copperwheat10 (UCAM data)
plt.scatter(0.1582061029*24,0.55,marker='o',color='k',s=10)
plt.errorbar(0.1582061029*24,0.55,yerr=0.02,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.1582061029*24,0.55,'  IP Peg_C10',color='k',size=12)

#From Miszalski16 (Mass overestimated due to bug in code)
plt.scatter(0.120971374*24,0.28,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.120971374*24,0.28,yerr=[[0.03],[0.03]],ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.120971374*24,0.28,'  CSS111003_M16',color='b',size=12,alpha=0.3)

#From Rodriguez-Gil15 (eclipse modelling)
plt.scatter(0.14920775*24,0.47,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.14920775*24,0.47,yerr=0.05,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.14920775*24,0.47,'  HS 0220+0603_RG15',color='b',size=12,alpha=0.3)

#From Hernandez17 (eclipse modelling) (in agreement with RV study of echevarria)
plt.scatter(0.26937431*24,0.58,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.26937431*24,0.58,yerr=0.06,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.26937431*24,0.58,'  1RXS J064434.5+334451_H17',color='b',size=12,alpha=0.3)

#From Tovmassian14 (eclipse modelling) (no errors included -- 20% errors used)
plt.scatter(0.1369745*24,0.28,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.1369745*24,0.28,yerr=0.05,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.1369745*24,0.28,'  SDSS0756+0858_T14',color='b',size=12,alpha=0.3)


# CONTACT PHASE TIMING (squares)

'''
# Systems that have been revisited

#From Steeghs03 (timing)
#plt.scatter(0.0739089282*24,0.10,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0739089282*24,0.10,yerr=0.01,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0739089282*24,0.10,'  IY UMa_S03',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.083,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.083,yerr=0.003,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0744992631*24,0.083,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Littlefair08 (Revised from Wood & Horne 1990)
#plt.scatter(0.0631209221*24,0.086,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.086,yerr=0.005,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0631209221*24,0.086,'  OY Car_L08',color='b',size=12,alpha=0.3)

#From Wood&Horne90 (timing)
#plt.scatter(0.0631209221*24,0.082,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.082,yerr=0.004,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0631209221*24,0.082,'  OY Car_WH90',color='b',size=12,alpha=0.3)
'''

#From Horne91 (timing)
plt.scatter(0.0736471745*24,0.09,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0736471745*24,0.09,yerr=0.02,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0736471745*24,0.09,' HT Cas_H91 ',color='b',size=12,alpha=0.3)

#From Baptista98 (timing)
plt.scatter(0.06242785751*24,0.15,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.06242785751*24,0.15,yerr=0.03,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.06242785751*24,0.15,'  V2051 Oph_B98',color='b',size=12,alpha=0.3)

#From Borges&Baptista05 (timing)
plt.scatter(0.0614296779*24,0.092,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0614296779*24,0.092,yerr=0.016,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0614296779*24,0.092,'  V4140 Sgr_BB05',color='b',size=12,alpha=0.3)

#From Baptista00 (timing) (More accurate mass from Shafter03)
#plt.scatter(0.209937*24,0.54,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.209937*24,0.54,yerr=0.10,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.209937*24,0.54,'  EX Dra_B00',color='b',size=12,alpha=0.3)

#From Araujo-Betancour03 & Patterson05 (timing & q from epsilon)
plt.scatter(0.136606499*24,0.21,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.136606499*24,0.21,yerr=0.03,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.136606499*24,0.21,'  DW UMa_AB03',color='b',size=12,alpha=0.3)

#From Baptista94 (timing)
plt.scatter(0.1638049430*24,0.20,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.1638049430*24,0.20,yerr=0.07,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.1638049430*24,0.20,'  UU Aqr_B94',color='b',size=12,alpha=0.3)


# RADIAL VELOCITY (triangles)

'''
# Systems that have been revisited

#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.198,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.088940717*24,0.198,yerr=[[0.029],[0.029]],ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.088940717*24,0.198,'  CTCV 1300_S12',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
#plt.scatter(0.0744992631*24,0.125,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.125,yerr=0.014,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0744992631*24,0.125,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.1754424023*24,0.33,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.1754424023*24,0.33,yerr=0.07,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.1754424023*24,0.33,'  GY Cnc_T00',color='b',size=12,alpha=0.3)
'''

#From Echevarria16 (RV)
plt.scatter(0.068233843*24,0.10,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.068233843*24,0.10,yerr=0.02,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.068233843*24,0.10,'  EX Hya_E16',color='b',size=12,alpha=0.3)

#From HernandezSantisteban17 (RV) (seems an outlier as other studies favour Hernandez17) 
#plt.scatter(0.26937431*24,0.78,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.26937431*24,0.78,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.26937431*24,0.78,'  1RXS J064434.5+334451_HS17',color='b',size=12,alpha=0.3)

#From Echevarria07 (RV)
plt.scatter(0.17690617*24,0.42,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.17690617*24,0.42,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.17690617*24,0.42,'  U Gem_E07',color='b',size=12,alpha=0.3)

#From Horne93 (RV)
plt.scatter(0.193620897*24,0.40,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.193620897*24,0.40,yerr=0.05,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.193620897*24,0.40,'  DQ Her_H93',color='b',size=12,alpha=0.3)

#From Thoroughgood05 (RV)
plt.scatter(0.231936060*24,0.52,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.231936060*24,0.52,yerr=0.06,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.231936060*24,0.52,'  V347 Pup_T05',color='b',size=12,alpha=0.3)

#From Arenas00 (RV)
plt.scatter(0.13820103*24,0.29,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.13820103*24,0.29,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.13820103*24,0.29,'  V603 Aql_A00',color='b',size=12,alpha=0.3)

#From Rodriguez-Gil01 (RV)
plt.scatter(0.101838931*24,0.20,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.101838931*24,0.20,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.101838931*24,0.20,'  V348 Pup_RG01,color='b',size=12,alpha=0.3)

#From Steeghs01+07 (wd mass from gravitational redshift (S07) & q from RV (S01))
plt.scatter(0.0566878460*24,0.049,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.0566878460*24,0.049,yerr=0.015,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0566878460*24,0.049,'  WZ Sge_S01/07',color='b',size=12,alpha=0.3)

#From Echevarria08 (RV) -- Not included as expected to have evolved secondary and P > 0.8
#plt.scatter(0.4116554800*24,0.37,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.4116554800*24,0.37,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.4116554800*24,0.37,'  AE Aqr_E08',color='b',size=12,alpha=0.3)

#Welsh07 (RV)
plt.scatter(0.290909*24,0.77,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.290909*24,0.77,yerr=0.08,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.290909*24,0.77,'  EM Cyg_W07',color='b',size=12,alpha=0.3)

#From Thoroughgood04 (RV)
plt.scatter(0.30047747*24,0.77,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.30047747*24,0.77,yerr=0.05,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.30047747*24,0.77,'  AC Cnc_T04',color='b',size=12,alpha=0.3)



# SUPERHUMPER WORK


mwd_k11 = 0.75
# Values from MwdvsP_curr.py
mwd_new = 0.812
mwd_new_err = 0.020
mwd_int_dis = 0.133

ep_q_intercept_k06 = 0.114
ep_q_intercept_k06_err = 0.005
ep_q_gradient_k06 = 3.97
ep_q_gradient_k06_err = 0.41
# Values from epsilon-q_relation.py
ep_q_intercept_b = 0.118
#ep_q_intercept_b = 0.114
ep_q_intercept_b_err = 0.003
ep_q_gradient_b = 4.45
ep_q_gradient_b_err = 0.28
ep_q_int_dis_b = 0.012
ep_q_intercept_c = 0.135
#ep_q_intercept_c = 0.114
ep_q_intercept_c_err = 0.004
ep_q_gradient_c = 5.0
ep_q_gradient_c_err = 0.7
ep_q_int_dis_c = 0.012

#apply a shift to m2 values from P05+Knigge06 (method 1)
p_orb = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [0])
m2_sh = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [1])
m2_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [2])
r2_sh = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [3])
r2_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [4])
ep_sh = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [5])
ep_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [6])
mwd_pat = np.loadtxt('Superhumpers/superhumpers_p05_curr.dat',dtype=float,usecols = [7])

m2_sh_shift = mwd_new*((m2_sh/mwd_k11)+(ep_q_intercept_b-ep_q_intercept_k06))
#m2_sh_shift = mwd_new*((m2_sh/mwd_k11)+(ep_q_intercept_c-ep_q_intercept_k06))
#m2_optimal_shift = mwd_new*((m2_optimal/mwd_k11)+(ep_q_intercept_new-ep_q_intercept_k06))

#calculate new q from just porb and psh from Kato papers (method 2)
p_orb_b = np.loadtxt('Superhumpers/superhumpers_kato_b.dat',dtype=float,usecols = [0])
p_orb_b_err = np.loadtxt('Superhumpers/superhumpers_kato_b.dat',dtype=float,usecols = [1])
p_sh_b = np.loadtxt('Superhumpers/superhumpers_kato_b.dat',dtype=float,usecols = [2])
p_sh_b_err = np.loadtxt('Superhumpers/superhumpers_kato_b.dat',dtype=float,usecols = [3])

p_orb_c = np.loadtxt('Superhumpers/superhumpers_kato_c.dat',dtype=float,usecols = [0])
p_orb_c_err = np.loadtxt('Superhumpers/superhumpers_kato_c.dat',dtype=float,usecols = [1])
p_sh_c = np.loadtxt('Superhumpers/superhumpers_kato_c.dat',dtype=float,usecols = [2])
p_sh_c_err = np.loadtxt('Superhumpers/superhumpers_kato_c.dat',dtype=float,usecols = [3])

ep_b = (p_sh_b - p_orb_b)/p_orb_b 
ep_b_err = ep_b*np.sqrt((np.sqrt(p_sh_b_err**2.0+p_orb_b_err**2.0)/(p_sh_b-p_orb_b))**2.0+(p_orb_b_err/p_orb_b)**2.0)
ep_c = (p_sh_c - p_orb_c)/p_orb_c 
ep_c_err = ep_c*np.sqrt((np.sqrt(p_sh_c_err**2.0+p_orb_c_err**2.0)/(p_sh_c-p_orb_c))**2.0+(p_orb_c_err/p_orb_c)**2.0)

q_b = ep_q_intercept_b+(ep_q_gradient_b*(ep_b-0.025))
q_c = ep_q_intercept_c+(ep_q_gradient_c*(ep_c-0.025))
#q_pat = ep_q_intercept_k06+(ep_q_gradient_k06*(ep_sh-0.025))
q_pat = ep_q_intercept_b+(ep_q_gradient_b*(ep_sh-0.025))

#q_b_err = np.sqrt((ep_q_intercept_b_err**2.0)+((ep_q_gradient_b*(ep_b-0.025))**2.0)*((ep_q_gradient_b_err/ep_q_gradient_b)**2.0+(ep_b_err/(ep_b-0.025))**2.0))
#q_c_err = np.sqrt((ep_q_intercept_c_err**2.0)+((ep_q_gradient_c*(ep_c-0.025))**2.0)*((ep_q_gradient_c_err/ep_q_gradient_c)**2.0+(ep_c_err/(ep_c-0.025))**2.0))
# Intrinsic dispersion error used in place of intercept error
# Check this at some point
q_b_err = np.sqrt((ep_q_int_dis_b**2.0)+((ep_q_gradient_b*(ep_b-0.025))**2.0)*((ep_q_gradient_b_err/ep_q_gradient_b)**2.0+(ep_b_err/(ep_b-0.025))**2.0))
q_c_err = np.sqrt((ep_q_int_dis_c**2.0)+((ep_q_gradient_c*(ep_c-0.025))**2.0)*((ep_q_gradient_c_err/ep_q_gradient_c)**2.0+(ep_c_err/(ep_c-0.025))**2.0))
#q_pat_err = np.sqrt((ep_q_intercept_k06_err**2.0)+((ep_q_gradient_k06*(ep_sh-0.025))**2.0)*((ep_q_gradient_k06_err/ep_q_gradient_k06)**2.0+(ep_err_sh/(ep_sh-0.025))**2.0))
q_pat_err = np.sqrt((ep_q_int_dis_b**2.0)+((ep_q_gradient_b*(ep_sh-0.025))**2.0)*((ep_q_gradient_b_err/ep_q_gradient_b)**2.0+(ep_err_sh/(ep_sh-0.025))**2.0))

m2_b = mwd_new*q_b
m2_c = mwd_new*q_c
m2_pat = mwd_pat*q_pat

m2_b_err = m2_b*np.sqrt((q_b_err/q_b)**2.0+(mwd_int_dis/mwd_new)**2.0)
m2_c_err = m2_c*np.sqrt((q_c_err/q_c)**2.0+(mwd_int_dis/mwd_new)**2.0)
m2_pat_err = m2_pat*np.sqrt((q_pat_err/q_pat)**2.0+(mwd_int_dis/mwd_pat)**2.0)

for i in range(len(p_orb)):
    #plt.scatter(p_orb[i],m2_sh_shift[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(p_orb[i],m2_sh_shift[i],yerr=m2_err_sh[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)
    #plt.scatter(p_orb[i],m2_new[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(p_orb[i],m2_new[i],yerr=m2_err_sh[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)
   
    plt.scatter(p_orb[i],m2_pat[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(p_orb[i],m2_pat[i],yerr=m2_pat_err[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)

for i in range(len(p_orb_b)):   
    plt.scatter(p_orb_b[i]*24,m2_b[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(p_orb_b[i]*24,m2_b[i],yerr=m2_b_err[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)
    
for i in range(len(p_orb_c)):  
    plt.scatter(p_orb_c[i]*24,m2_c[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(p_orb_c[i]*24,m2_c[i],yerr=m2_c_err[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)


#plt.plot(P_optimal*1.064,m2_optimal*1.1,c='r',linewidth=1) # m=0.22
#plt.plot(P_optimal*1.048,m2_optimal*1.075,c='r',linewidth=1) # m=0.215
#plt.plot(P_optimal*1.035,m2_optimal*1.05,c='r',linewidth=1) # m=0.21
#plt.plot(P_standard*1.035,m2_standard*1.05,c='k',linewidth=1) # m=0.21
#plt.plot(P_optimal*1.016,m2_optimal*1.025,c='r',linewidth=1) # m=0.205
#plt.plot(P_standard*1.016,m2_standard*1.025,c='k',linewidth=1) # m=0.205
#plt.plot(P_optimal*0.983,m2_optimal*0.975,c='r',linewidth=1) # m=0.195
#plt.plot(P_standard*0.983,m2_standard*0.975,c='k',linewidth=1) # m=0.195
#plt.plot(P_optimal*0.982,m2_optimal*1.07,c='r',linewidth=1)
plt.plot(P_optimal,m2_optimal,c='r',linewidth=1,alpha=0.8)#,linestyle='dashed',alpha=0.5)
#plt.plot(P_standard+(0.3/P_standard**5),m2_standard,c='k',linewidth=1,linestyle='dashed')
plt.plot(P_standard,m2_standard,c='k',linewidth=1,alpha=0.8)
#plt.plot(P_BD_1,m2_BD_1,c='b',linewidth=1)
#plt.plot(P_BD_2,m2_BD_2,c='b',linestyle='--',linewidth=1)
#plt.plot(P_BD_3,m2_BD_3,c='b',linestyle='-.',linewidth=1)
#plt.plot(P_BD_4,m2_BD_4,c='b',linestyle=':',linewidth=1)
#plt.plot(P_evol_12,m2_evol_12,c='g',linewidth=1)
#plt.plot(P_evol_15,m2_evol_15,c='g',linewidth=1,linestyle='dashed')
plt.xlabel(r'$P_{\rm orb}\ (\rm hrs)$', fontsize=16)
plt.ylabel(r'$M_{\rm 2}\ (\rm{M}_{\odot})$', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=13, width=1.0)
plt.tick_params(top='on',right='on')


### BPL TESTING ###
'''
m2_test_1 = np.linspace(0.063,0,1000)
q_test_1 = m2_test_1/0.811
b_test_1 = 0.1372
c_test_1 = 0.1087

porb_test_1 = ((c_test_1/(0.2478*(0.064**b_test_1)))**(3.0/2.0))*\
    (m2_test_1**(((3.0/2.0)*b_test_1)-(1.0/2.0)))*\
    ((((q_test_1**(1.0/3.0))*((1+q_test_1)**(1.0/3.0)))/((0.6*(q_test_1**(2.0/3.0)))+np.log(1+(q_test_1**(1.0/3.0)))))**(-3.0/2.0))


m2_test_2 = np.linspace(0.063,0.2,1000)
q_test_2 = m2_test_2/0.811
b_test_2 = 0.6343
c_test_2 = 0.2254

porb_test_2 = ((c_test_2/(0.2478*(0.2**b_test_2)))**(3.0/2.0))*\
    (m2_test_2**(((3.0/2.0)*b_test_2)-(1.0/2.0)))*\
    ((((q_test_2**(1.0/3.0))*((1+q_test_2)**(1.0/3.0)))/((0.6*(q_test_2**(2.0/3.0)))+np.log(1+(q_test_2**(1.0/3.0)))))**(-3.0/2.0))

plt.plot(porb_test_1,m2_test_1,c='r',linewidth=1,alpha=0.8)
plt.plot(porb_test_2,m2_test_2,c='r',linewidth=1,alpha=0.8)
#plt.plot(P_k11_ds,m2_k11_ds,c='r',linewidth=1,alpha=0.8)
'''

### P_MIN CALCULATION ###

porb_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [6],skiprows=0)  
porb_all = np.concatenate((p_orb*60,p_orb_b*24*60,p_orb_c*24*60,porb_eclipsers*24*60))

porb_min = []
for i in range (0,len(porb_all)):
    if porb_all[i] >= 76.0 and porb_all[i] <= 82.0:
        porb_min.append(porb_all[i])
        
porb_min = np.array(porb_min)
      
      
s = np.std(porb_min)
m = np.mean(porb_min)

print m, s

mu, std = norm.fit(porb_min)

print mu, std


title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)     

def chisqfunc(a):
    chisq = np.sum(((porb_min - a)**2.0) / (0**2.0 + 1.656**2.0))
    red_chisq = (chisq / (len(porb_min)-1))
    #print chisq
    print red_chisq
    return chisq

x0 = 1

#a = 79.7886766 #0.22
#result = chisqfunc(a)

result = opt.minimize(chisqfunc,x0)
a = result.x
print a

'''
76 - 82 mins
#a = 79.57 +- 0.22 # Error from delta(chisq) = 1
#sigma = 1.656
#FWHM = 2.355*sigma = 3.90
'''


# New period minimum (from SDSS Gaussian spike distribution)
plt.axvline(1.378,linestyle='dashed',color='r',linewidth=1,alpha=0.5) #82.7 mins
plt.axvspan(1.332,1.425,color='r',alpha=0.05) #79.94 - 85.47 mins (FWHM = 5.53)

# New period minimum (from SH + eclipser systems between 76.0 and 82.0 mins)
#plt.axvspan(1.267,1.367,color='b',alpha=0.05) #76 - 82 mins
#plt.axvspan(1.2935,1.3585,color='b',alpha=0.05) #77.62 - 81.52 mins (FWHM = 3.90)
#plt.axvline(1.326,linestyle='dashed',color='b',linewidth=1,alpha=0.3) #79.57 mins

# Mbounce
#plt.axhline(0.063,linestyle='dashed',color='b',linewidth=1,alpha=0.5)

# Existing period minimum
#plt.axvline(1.3626,linestyle='dashed',color='k',linewidth=1,alpha=0.5) #K11
#plt.axvspan(1.3476,1.3776,color='k',alpha=0.05) #K11
#plt.errorbar(1.373,0.024,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1.5,alpha=0.8) #G09
#plt.axvspan(1.325,1.421,color='k',alpha=0.05) #G09
plt.arrow(1.373,0.024,0.0475,0,width=0.0003,head_width=0.002,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09
plt.arrow(1.373,0.024,-0.0475,0,width=0.0003,head_width=0.002,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09
#plt.arrow(1.373,0.035,0.0475,0,width=0.0003,head_width=0.003,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09
#plt.arrow(1.373,0.035,-0.0475,0,width=0.0003,head_width=0.003,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09

plt.subplots_adjust(bottom=0.10, top=0.98, left=0.10, right=0.99)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("m2vsP_curr.pdf")
plt.show()

