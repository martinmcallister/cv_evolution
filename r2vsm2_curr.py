import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math
import scipy.optimize as opt
import seaborn

#input updated semi-empirical broken-power-law donor sequence from Knigge et al. 2011
P_k11_ds = np.loadtxt('Knigge11/knigge11_don_seq.dat',dtype=float,usecols = [0],skiprows=3)
m2_k11_ds = np.loadtxt('Knigge11/knigge11_don_seq.dat',dtype=float,usecols = [1],skiprows=3)
r2_k11_ds = np.loadtxt('Knigge11/knigge11_don_seq.dat',dtype=float,usecols = [2],skiprows=3)
m2_k11_evo_std = np.loadtxt('Knigge11/knigge11_evo_track_std.dat',dtype=float,usecols = [0],skiprows=3)
r2_k11_evo_std = np.loadtxt('Knigge11/knigge11_evo_track_std.dat',dtype=float,usecols = [1],skiprows=3)
P_k11_evo_std = np.loadtxt('Knigge11/knigge11_evo_track_std.dat',dtype=float,usecols = [2],skiprows=3)
m2_k11_evo_opt = np.loadtxt('Knigge11/knigge11_evo_track_opt.dat',dtype=float,usecols = [0],skiprows=3)
r2_k11_evo_opt = np.loadtxt('Knigge11/knigge11_evo_track_opt.dat',dtype=float,usecols = [1],skiprows=3)
P_k11_evo_opt = np.loadtxt('Knigge11/knigge11_evo_track_opt.dat',dtype=float,usecols = [2],skiprows=3)
zeta_k11_evo_opt = np.loadtxt('Knigge11/knigge11_evo_track_opt.dat',dtype=float,usecols = [7],skiprows=3)

#produce plot

seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

#plt.rcParams['xtick.major.pad']='15'
#plt.rcParams['ytick.major.pad']='10'

#plt.axis([1,1.7001,0,0.15001])
#plt.axis([0.02,0.2,0.08,0.3])
#plt.axis([1.0,3.001,0.02,0.301])
#plt.axis([1.1,1.6,0.03,0.11])

#plt.axis([0.01,0.2,0.08,0.260])
#plt.tick_params(top='on',right='on')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([0.02, 0.9])
ax.set_xticks([0.02,0.04,0.06,0.08,0.10,0.2,0.4,0.6,0.8])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_yscale('log')
ax.set_ylim([0.08, 0.9])
ax.set_yticks([0.08,0.1,0.2,0.4,0.6,0.8])
ax.get_yaxis().set_major_formatter(ScalarFormatter())
ax.minorticks_off()


############# PHL 1445 paper ##############


#plt.scatter(0.064,0.109,marker='o',color='k',s=10)
#plt.errorbar(0.064,0.109,xerr=0.005,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.063,0.109,'  PHL 1445',color='k',size=12)


############ DONE (with GPs) ##############


plt.scatter(0.071,0.113,marker='o',color='g',s=10)
plt.errorbar(0.071,0.113,xerr=[[0.005],[0.009]],yerr=[[0.003],[0.004]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.071,0.113,'  PHL 1445 (10 ecl)',color='g',size=12)

#plt.scatter(0.061,0.108,marker='o',color='g',s=10)
#plt.errorbar(0.061,0.108,xerr=[[0.008],[0.005]],yerr=[[0.005],[0.002]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.061,0.108,'  PHL 1445 (6 ecl)',color='g',size=12)

plt.scatter(0.109,0.142,marker='o',color='g',s=10)
plt.errorbar(0.109,0.142,xerr=[[0.013],[0.012]],yerr=[[0.007],[0.004]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.109,0.142,'  ASASSN-14ag',color='g',size=12)

plt.scatter(0.141,0.1770,marker='o',color='g',s=10)
plt.errorbar(0.141,0.1770,xerr=[[0.007],[0.007]],yerr=[[0.0029],[0.0027]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.141,0.1770,'  IY UMa',color='g',size=12)

plt.scatter(0.152,0.1820,marker='o',color='g',s=10)
plt.errorbar(0.152,0.1820,xerr=[[0.005],[0.006]],yerr=[[0.0019],[0.0021]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.152,0.1820,'  Z Cha',color='g',size=12)

plt.scatter(0.081,0.1275,marker='o',color='g',s=10)
plt.errorbar(0.081,0.1275,xerr=[[0.005],[0.005]],yerr=[[0.0024],[0.0024]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.081,0.1275,'  CSS080623',color='g',size=12)

plt.scatter(0.138,0.182,marker='o',color='g',s=10)
plt.errorbar(0.138,0.182,xerr=[[0.007],[0.007]],yerr=[[0.003],[0.003]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.138,0.182,'  SDSS 0901',color='g',size=12)

plt.scatter(0.187,0.215,marker='o',color='g',s=10)
plt.errorbar(0.187,0.215,xerr=[[0.012],[0.003]],yerr=[[0.005],[0.001]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.187,0.215,'  DV UMa',color='g',size=12)

plt.scatter(0.166,0.2111,marker='o',color='g',s=10)
plt.errorbar(0.166,0.2111,xerr=[[0.003],[0.006]],yerr=[[0.0014],[0.0025]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.166,0.2111,'  CTCV 1300',color='g',size=12)

plt.scatter(0.093,0.1388,marker='o',color='g',s=10)
plt.errorbar(0.093,0.1388,xerr=[[0.001],[0.003]],yerr=[[0.0003],[0.0018]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.093,0.1388,'  OY Car',color='g',size=12)

plt.scatter(0.140,0.163,marker='o',color='g',s=10)
plt.errorbar(0.140,0.163,xerr=[[0.008],[0.012]],yerr=[[0.003],[0.004]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.140,0.163,'  SSS130413',color='g',size=12)

plt.scatter(0.105,0.149,marker='o',color='g',s=10)
plt.errorbar(0.105,0.149,xerr=[[0.006],[0.008]],yerr=[[0.003],[0.004]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.105,0.149,'  CSS110113',color='g',size=12)

plt.scatter(0.083,0.1276,marker='o',color='g',s=10)
plt.errorbar(0.083,0.1276,xerr=[[0.004],[0.006]],yerr=[[0.0024],[0.0028]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.083,0.1276,'  SSS100615',color='g',size=12)

plt.scatter(0.094,0.147,marker='o',color='g',s=10)
plt.errorbar(0.094,0.147,xerr=[[0.009],[0.016]],yerr=[[0.006],[0.007]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.094,0.147,'  SDSS 1152',color='g',size=12)

plt.scatter(0.0436,0.1086,marker='o',color='g',s=10)
plt.errorbar(0.0436,0.1086,xerr=[[0.0017],[0.0025]],yerr=[[0.0015],[0.0019]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0436,0.1086,'  SDSS1057',color='g',size=12)

plt.scatter(0.37,0.457,marker='o',color='g',s=10)
plt.errorbar(0.37,0.457,xerr=[[0.06],[0.06]],yerr=[[0.026],[0.022]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.37,0.457,'  SDSS 1006',color='g',size=12)

plt.scatter(0.394,0.446,marker='o',color='g',s=10)
plt.errorbar(0.394,0.446,xerr=[[0.022],[0.016]],yerr=[[0.009],[0.006]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.394,0.446,'  GY Cnc',color='g',size=12)

plt.scatter(0.176,0.208,marker='o',color='g',s=10)
plt.errorbar(0.176,0.208,xerr=[[0.018],[0.007]],yerr=[[0.005],[0.002]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.176,0.208,'  V713 Cep',color='g',size=12)

plt.scatter(0.061,0.1129,marker='o',color='g',s=10)
plt.errorbar(0.061,0.1129,xerr=[[0.003],[0.004]],yerr=[[0.0016],[0.0025]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.061,0.1129,'  SDSS 1501',color='g',size=12)


######### IN LITERATURE ################


# HIGH TIME RESOLUTION ECLIPSE MODELLING (circles)

'''
# Systems from Savoury 11 that have been revisited

#plt.scatter(0.098,0.1382,marker='o',color='k',s=10,alpha=0.25)
#plt.errorbar(0.098,0.1382,xerr=0.003,yerr=0.0014,ls='none',color='k',capsize=None,linewidth=1,alpha=0.25)
#plt.text(0.095,0.1382,'  CSS080623',color='k',size=12,alpha=0.25)

#plt.scatter(0.161,0.1949,marker='o',color='k',s=10,alpha=0.25)
#plt.errorbar(0.161,0.1949,xerr=0.007,yerr=0.0028,ls='none',color='k',capsize=None,linewidth=1,alpha=0.25)
#plt.text(0.162,0.1949,'  SDSS 0901',color='k',size=12,alpha=0.25)

#plt.scatter(0.177,0.215,marker='o',color='k',s=10)
#plt.errorbar(0.177,0.215,xerr=0.021,yerr=0.008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.177,0.215,'  CTCV J1300-3052',color='k',size=12)

#plt.scatter(0.087,0.142,marker='o',color='k',s=10)
#plt.errorbar(0.087,0.142,xerr=0.006,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.087,0.142,'  SDSS 1152',color='k',size=12)

#plt.scatter(0.196,0.2176,marker='o',color='k',s=10)
#plt.errorbar(0.196,0.2176,xerr=0.005,yerr=0.0018,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.196,0.2176,'  DV UMa',color='k',size=12)

#plt.scatter(0.077,0.122,marker='o',color='k',s=10)
#plt.errorbar(0.077,0.122,xerr=0.010,yerr=0.005,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.074,0.122,'  SDSS 1501',color='k',size=12)
'''

# Systems from Savoury 11

plt.scatter(0.0571,0.1074,marker='o',color='k',s=10)
plt.errorbar(0.0571,0.1074,xerr=0.0007,yerr=0.0004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0571,0.1074,'  SDSS 1433',color='k',size=12)

plt.scatter(0.0575,0.0969,marker='o',color='k',s=10)
plt.errorbar(0.0575,0.0969,xerr=0.0020,yerr=0.0011,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0551,0.0969,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0475,0.1047,marker='o',color='k',s=10)
plt.errorbar(0.0475,0.1047,xerr=0.0012,yerr=0.0008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0457,0.1047,'  SDSS 1035',color='k',size=12)

plt.scatter(0.101,0.1463,marker='o',color='k',s=10)
plt.errorbar(0.101,0.1463,xerr=0.003,yerr=0.0016,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.103,0.1463,' CTCV J2354-4700',color='k',size=12)

plt.scatter(0.099,0.1358,marker='o',color='k',s=10)
plt.errorbar(0.099,0.1358,xerr=0.004,yerr=0.0020,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.098,0.1358,'  SDSS 0903',color='k',size=12)

plt.scatter(0.0889,0.1365,marker='o',color='k',s=10)
plt.errorbar(0.0889,0.1365,xerr=0.0025,yerr=0.0013,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0889,0.1365,'  SDSS 1227',color='k',size=12)

plt.scatter(0.091,0.1350,marker='o',color='k',s=10)
plt.errorbar(0.091,0.1350,xerr=0.004,yerr=0.0018,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.092,0.1350,'  XZ Eri',color='k',size=12)

plt.scatter(0.0781,0.1241,marker='o',color='k',s=10)
plt.errorbar(0.0781,0.1241,xerr=0.0008,yerr=0.0003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0781,0.1241,'  SDSS 1502',color='k',size=12)

plt.scatter(0.1157,0.1634,marker='o',color='k',s=10)
plt.errorbar(0.1157,0.1634,xerr=0.0022,yerr=0.0010,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.1157,0.1634,'  OU Vir',color='k',size=12)

plt.scatter(0.223,0.252,marker='o',color='k',s=10)
plt.errorbar(0.223,0.252,xerr=0.010,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(,0.223,0.252,'  SDSS 1702',color='k',size=12)

'''
# Systems from other sources that have been revisited

# From Southworth09
#plt.scatter(0.40,0.47,marker='o',color='b',s=10,alpha=0.3)
#plt.errorbar(0.40,0.47,xerr=0.10,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.40,0.47,'  SDSS 1006_S09',color='b',size=12,alpha=0.3)

'''

# Other systems

#From Shafter03
plt.scatter(0.53,0.565,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.53,0.565,xerr=0.01,yerr=0.004,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.53,0.565,'  EX Dra_S03',color='b',size=12,alpha=0.3)

#From Littlefair14 (UCAM data)
plt.scatter(0.39,0.432,marker='o',color='k',s=10)
plt.errorbar(0.39,0.432,xerr=0.04,yerr=0.015,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.39,0.432,'  KIS J1927_L14',color='k',size=12)

#From Copperwheat10 (UCAM data)
plt.scatter(0.55,0.466,marker='o',color='k',s=10)
plt.errorbar(0.55,0.466,xerr=0.02,yerr=0.006,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.55,0.466,'  IP Peg_C10',color='k',size=12)

#From Miszalski16 (Mass overestimated due to bug in code)
plt.scatter(0.28,0.314,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.28,0.314,xerr=[[0.03],[0.03]],yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.28,0.314,'  CSS111003_M16',color='b',size=12,alpha=0.3)

#From Rodriguez-Gil15 (eclipse modelling)
plt.scatter(0.47,0.427,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.47,0.427,xerr=0.05,yerr=0.015,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.47,0.427,'  HS 0220+0603_RG15',color='b',size=12,alpha=0.3)

#From Hernandez17 (eclipse modelling) (in agreement with RV study of echevarria)
plt.scatter(0.58,0.690,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.58,0.690,xerr=0.06,yerr=0.024,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.58,0.690,'  1RXS J064434.5+334451_H17',color='b',size=12,alpha=0.3)

#From Tovmassian14 (eclipse modelling) (no errors included -- 20% errors used)
plt.scatter(0.28,0.338,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.28,0.338,xerr=0.05,yerr=0.020,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.28,0.338,'  SDSS0756+0858_T14',color='b',size=12,alpha=0.3)


# CONTACT PHASE TIMING (squares)

'''
# Systems that have been revisited

#From Steeghs03 (timing)
#plt.scatter(0.10,0.158,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.10,0.158,xerr=0.01,yerr=0.005,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.10,0.158,'  IY UMa_S03',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.083,0.1489,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.083,0.1489,xerr=0.003,yerr=0.0018,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.083,0.1489,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Littlefair08 (Revised from Wood & Horne 1990)
#plt.scatter(0.086,0.1354,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.086,0.1354,xerr=0.005,yerr=0.0026,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.086,0.1354,'  OY Car_L08',color='b',size=12,alpha=0.3)
'''

#From Horne91 (timing)
plt.scatter(0.09,0.152,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.09,0.152,xerr=0.02,yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.09,0.152,' HT Cas_H91',color='b',size=12,alpha=0.3)

#From Baptista98 (timing)
plt.scatter(0.15,0.161,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.15,0.161,xerr=0.03,yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.15,0.161,'  V2051 Oph_B98',color='b',size=12,alpha=0.3)

#From Borges&Baptista05 (timing) 
plt.scatter(0.092,0.136,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.092,0.136,xerr=0.016,yerr=0.008,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.092,0.136,'  V4140 Sgr_BB05',color='b',size=12,alpha=0.3)

#From Baptista00 (timing) (More accurate mass from Shafter03)
#plt.scatter(0.54,0.57,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.54,0.57,xerr=0.10,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.54,0.57,'  EX Dra_B00',color='b',size=12,alpha=0.3)

#From Araujo-Betancour03 & Patterson05 (timing & q from epsilon)
plt.scatter(0.21,0.304,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.21,0.304,xerr=0.03,yerr=0.014,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.21,0.304,'  DW UMa_AB03',color='b',size=12,alpha=0.3)

#From Baptista04 (timing)
plt.scatter(0.20,0.34,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.20,0.34,xerr=0.07,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.20,0.34,'  UU Aqr_B04',color='b',size=12,alpha=0.3)


# RADIAL VELOCITY (triangles)

'''
# Systems that have been revisited

#From Savoury12 (RV)
#plt.scatter(0.198,0.224,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.198,0.224,xerr=[[0.029],[0.029]],yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.198,0.224,'  CTCV 1300_S12',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
#plt.scatter(0.125,0.171,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.125,0.171,xerr=0.014,yerr=0.006,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.125,0.171,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.33,0.42,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.33,0.42,xerr=0.07,yerr=0.03,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.33,0.42,'  GY Cnc_T00',color='b',size=12,alpha=0.3)
'''

#From Echevarria16 (RV)
plt.scatter(0.10,0.150,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.10,0.150,xerr=0.02,yerr=0.010,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.10,0.150,'  EX Hya_E16',color='b',size=12,alpha=0.3)

#From HernandezSantisteban17 (RV) (seems an outlier as other studies favour Hernandez17)
#plt.scatter(0.78,0.769,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.78,0.769,xerr=0.04,yerr=0.013,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.78,0.769,'  1RXS J064434.5+334451_HS17',color='b',size=12,alpha=0.3)

#From Echevarria07 (RV)
plt.scatter(0.42,0.456,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.42,0.456,xerr=0.04,yerr=0.014,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.42,0.456,'  U Gem_E07',color='b',size=12,alpha=0.3)

#From Horne93 (RV)
plt.scatter(0.40,0.485,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.40,0.485,xerr=0.05,yerr=0.020,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.40,0.485,'  DQ Her_H93',color='b',size=12,alpha=0.3)

#From Thoroughgood05 (RV)
plt.scatter(0.52,0.603,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.52,0.603,xerr=0.06,yerr=0.023,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.52,0.603,'  V347 Pup_T05',color='b',size=12,alpha=0.3)

#From Arenas00 (RV)
plt.scatter(0.29,0.341,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.29,0.341,xerr=0.04,yerr=0.016,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.29,0.341,'  V603 Aql_A00',color='b',size=12,alpha=0.3)

#From Rodriguez-Gil01 (RV)
plt.scatter(0.20,0.246,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.20,0.246,xerr=0.04,yerr=0.016,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.20,0.246,'  V348 Pup_RG01,color='b',size=12,alpha=0.3)

#From Steeghs01+07 (wd mass from gravitational redshift (S07) & q from RV (S01))
plt.scatter(0.049,0.105,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.049,0.105,xerr=0.015,yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.049,0.105,'  WZ Sge_S01/07',color='b',size=12,alpha=0.3)

#From Echevarria08 (RV) -- Not included as expected to have evolved secondary
#plt.scatter(0.37,0.780,marker='^',color='r',s=10,alpha=0.3)
#plt.errorbar(0.37,0.780,xerr=0.04,yerr=0.028,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.37,0.780,'  AE Aqr_E08',color='b',size=12,alpha=0.3)

#From Welsh07 (RV)
plt.scatter(0.77,0.797,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.77,0.797,xerr=0.08,yerr=0.028,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.77,0.797,'  EM Cyg_W07',color='b',size=12,alpha=0.3)

#From Thoroughgood04 (RV)
plt.scatter(0.77,0.827,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.77,0.827,xerr=0.05,yerr=0.018,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.77,0.827,'  AC Cnc_T04',color='b',size=12,alpha=0.3)



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

r2_b = 0.2478 * ((p_orb_b*24)**(2.0/3.0)) * (m2_b**(1.0/3.0)) * \
        (((q_b**(1.0/3.0))*((1+q_b)**(1.0/3.0)))/((0.6*(q_b**(2.0/3.0)))+np.log(1+(q_b**(1.0/3.0)))))
r2_c = 0.2478 * ((p_orb_c*24)**(2.0/3.0)) * (m2_c**(1.0/3.0)) * \
        (((q_c**(1.0/3.0))*((1+q_c)**(1.0/3.0)))/((0.6*(q_c**(2.0/3.0)))+np.log(1+(q_c**(1.0/3.0)))))
r2_pat = 0.2478 * ((p_orb)**(2.0/3.0)) * (m2_pat**(1.0/3.0)) * \
        (((q_pat**(1.0/3.0))*((1+q_pat)**(1.0/3.0)))/((0.6*(q_pat**(2.0/3.0)))+np.log(1+(q_pat**(1.0/3.0)))))

## NEED TO INCORPORATE q ERRORS ##
r2_b_err = r2_b*np.sqrt(((2.0/3.0)*(p_orb_b_err/p_orb_b))**2.0+((1.0/3.0)*(m2_b_err/m2_b))**2.0)
r2_c_err = r2_c*np.sqrt(((2.0/3.0)*(p_orb_c_err/p_orb_c))**2.0+((1.0/3.0)*(m2_c_err/m2_c))**2.0)
r2_pat_err = r2_pat*((1.0/3.0)*(m2_pat_err/m2_pat))


m2_superhumpers = np.concatenate((m2_b,m2_c,m2_pat))
m2_err_superhumpers = np.concatenate((m2_b_err,m2_c_err,m2_pat_err))
r2_superhumpers = np.concatenate((r2_b,r2_c,r2_pat))
r2_err_superhumpers = np.concatenate((r2_b_err,r2_c_err,r2_pat_err))
q_superhumpers = np.concatenate((q_b,q_c,q_pat))
q_err_superhumpers = np.concatenate((q_b_err,q_c_err,q_pat_err))
porb_superhumpers = np.concatenate((p_orb_b,p_orb_c,p_orb/24.0))

# Create text file with superhumper data
#superhumpers = np.array([m2_superhumpers,m2_err_superhumpers,r2_superhumpers,r2_err_superhumpers,q_superhumpers,q_err_superhumpers,porb_superhumpers])
#superhumpers = np.transpose(superhumpers)
#np.savetxt('r2m2_superhumpers.txt',superhumpers)


for i in range(len(p_orb)):
    plt.scatter(m2_pat[i],r2_pat[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(m2_pat[i],r2_pat[i],xerr=m2_pat_err[i],yerr=r2_pat_err[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)

for i in range(len(p_orb_b)):   
    plt.scatter(m2_b[i],r2_b[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(m2_b[i],r2_b[i],xerr=m2_b_err[i],yerr=r2_b_err[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)
for i in range(len(p_orb_c)):  
    plt.scatter(m2_c[i],r2_c[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(m2_c[i],r2_c[i],xerr=m2_c_err[i],yerr=r2_c_err[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)



# Updated broken law donor sequence from K11
m2_1 = np.linspace(0,0.069,1000)
r2_1 = 0.118*((m2_1/0.069)**0.30)
m2_2 = np.linspace(0.069,0.20,1000)
r2_2 = 0.225*((m2_2/0.2)**0.61)
r2_3 = np.linspace(0.225,0.293,1000)
m2_3 = 0.2*(r2_3**0.0)
m2_4 = np.linspace(0.2,0.9,1000)
r2_4 = 0.293*((m2_4/0.2)**0.69)

#plt.plot(m2_1,r2_1,c='k',linewidth=1,alpha=0.8)
#plt.plot(m2_2,r2_2,c='k',linewidth=1,alpha=0.8)
#plt.plot(m2_3,r2_3,c='k',linewidth=1,alpha=0.8)
#plt.plot(m2_4,r2_4,c='k',linewidth=1,alpha=0.8)

# New fit
# Mbounce = 0.063 (pmin = 76 mins)
#m2_1 = np.linspace(0,0.063,1000)
#r2_1 = 0.1087 *((m2_1/0.063)**0.1372)
#m2_2 = np.linspace(0.063,0.200,1000)
#r2_2 = 0.2254*((m2_2/0.2)**0.6344)
# Mbounce = 0.064 (pmin = 76 mins)
#m2_1 = np.linspace(0,0.064,1000)
#r2_1 = 0.1092 *((m2_1/0.064)**0.1497)
#m2_2 = np.linspace(0.064,0.200,1000)
#r2_2 = 0.2254*((m2_2/0.2)**0.6344)
# Mbounce = 0.0633 (pmin = 76.3 mins)
m2_1 = np.linspace(0,0.0636,1000)
r2_1 = 0.1091*((m2_1/0.0633)**0.1524)
m2_2 = np.linspace(0.0637,0.200,1000)
r2_2 = 0.2254*((m2_2/0.2)**0.6361)
r2_3 = np.linspace(0.225,0.293,1000)
m2_3 = 0.2*(r2_3**0.0)
m2_4 = np.linspace(0.2,0.9,1000)
r2_4 = 0.2926*((m2_4/0.2)**0.6859)

#plt.plot(m2_1,r2_1,c='r',linewidth=1,alpha=0.8)
#plt.plot(m2_2,r2_2,c='r',linewidth=1,alpha=0.8)
#plt.plot(m2_3,r2_3,c='r',linewidth=1,alpha=0.8)
#plt.plot(m2_4,r2_4,c='r',linewidth=1,alpha=0.8)

# Used for working out mbounce value + error
'''
porb_pmin_1 = np.linspace(1.3733,1.3733,1000) #82.4 mins
porb_pmin_2 = np.linspace(1.329,1.329,1000) #79.75 mins  # ACTUALLY 80.20 MINS!!
porb_pmin_3 = np.linspace(1.2917,1.2917,1000) #77.5 mins  # ACTUALLY 77.95 MINS!!
porb_pmin_4 = np.linspace(1.2667,1.2667,1000) #76.0 mins
m2_pmin = np.linspace(0.0,0.2,1000)
q_pmin = m2_pmin/mwd_new
r2_pmin_1 = 0.2478 * (porb_pmin_1**(2.0/3.0)) * (m2_pmin**(1.0/3.0)) * \
        (((q_pmin**(1.0/3.0))*((1+q_pmin)**(1.0/3.0)))/((0.6*(q_pmin**(2.0/3.0)))+np.log(1+(q_pmin**(1.0/3.0)))))
r2_pmin_2 = 0.2478 * (porb_pmin_2**(2.0/3.0)) * (m2_pmin**(1.0/3.0)) * \
        (((q_pmin**(1.0/3.0))*((1+q_pmin)**(1.0/3.0)))/((0.6*(q_pmin**(2.0/3.0)))+np.log(1+(q_pmin**(1.0/3.0)))))
r2_pmin_3 = 0.2478 * (porb_pmin_3**(2.0/3.0)) * (m2_pmin**(1.0/3.0)) * \
        (((q_pmin**(1.0/3.0))*((1+q_pmin)**(1.0/3.0)))/((0.6*(q_pmin**(2.0/3.0)))+np.log(1+(q_pmin**(1.0/3.0)))))
r2_pmin_4 = 0.2478 * (porb_pmin_4**(2.0/3.0)) * (m2_pmin**(1.0/3.0)) * \
        (((q_pmin**(1.0/3.0))*((1+q_pmin)**(1.0/3.0)))/((0.6*(q_pmin**(2.0/3.0)))+np.log(1+(q_pmin**(1.0/3.0)))))

plt.plot(m2_pmin,r2_pmin_1,c='k',linewidth=1,linestyle='dashed',alpha=0.8)
plt.plot(m2_pmin,r2_pmin_2,c='r',linewidth=1,linestyle='dashed',alpha=0.8)
plt.plot(m2_pmin,r2_pmin_3,c='r',linewidth=1,linestyle='dashed',alpha=0.8)
plt.plot(m2_pmin,r2_pmin_4,c='r',linewidth=1,linestyle='dashed',alpha=0.8)
plt.scatter(0.06,0.1105,c='b') #m2=0.06,m1=0.812,pmin=79.75 mins
plt.scatter(0.065,0.1134,c='g')  #m2=0.065,m1=0.812,pmin=79.75 mins
plt.scatter(0.07,0.1161,c='r')  #m2=0.07,m1=0.812,pmin=79.75 mins
plt.scatter(0.075,0.1187,c='y')  #m2=0.075,m1=0.812,pmin=79.75 mins
plt.scatter(0.08,0.1212,c='orange')  #m2=0.08,m1=0.812,pmin=79.75 mins

plt.scatter(0.064,0.1092,c='r')  #m2=0.064,m1=0.811,pmin=76.0 mins
plt.scatter(0.065,0.1098,c='g')  #m2=0.065,m1=0.811,pmin=76.0 mins
'''

# BPL fitting -- see Knigge 2006 + 2011 for details

m2_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [0],skiprows=0)
m2_err_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [1],skiprows=0)
r2_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [2],skiprows=0)
r2_err_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [3],skiprows=0)
q_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [4],skiprows=0)
q_err_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [5],skiprows=0)
porb_eclipsers = np.loadtxt('m2_r2_curr.dat',dtype=float,usecols = [6],skiprows=0)  


m2_all_systems = np.concatenate([m2_superhumpers,m2_eclipsers])
m2_err_all_systems = np.concatenate([m2_err_superhumpers,m2_err_eclipsers])
r2_all_systems = np.concatenate([r2_superhumpers,r2_eclipsers])
r2_err_all_systems = np.concatenate([r2_err_superhumpers,r2_err_eclipsers])
q_all_systems = np.concatenate([q_superhumpers,q_eclipsers])
q_err_all_systems = np.concatenate([q_err_superhumpers,q_err_eclipsers])
porb_all_systems = np.concatenate([porb_superhumpers,porb_eclipsers])

'''
r2_all_systems = 0.2478 * ((porb_all_systems*24)**(2.0/3.0)) * (m2_all_systems**(1.0/3.0)) * \
        (((q_all_systems**(1.0/3.0))*((1+q_all_systems)**(1.0/3.0)))/((0.6*(q_all_systems**(2.0/3.0)))+np.log(1+(q_all_systems**(1.0/3.0)))))
for i in range(len(porb_all_systems)):
     plt.scatter(m2_all_systems[i],r2_all_systems[i],marker='o',color='k',s=10,alpha=0.2)
'''

all_systems = np.array([m2_all_systems, m2_err_all_systems, r2_all_systems, r2_err_all_systems,q_all_systems,q_err_all_systems,porb_all_systems])
all_systems = np.transpose(all_systems)


# long period systems
m_conv = 0.2        #K06 (Msun)
m_conv_err = 0.02   #K06 (Msun)
p_gap_upper = 3.18  #K06 (hrs)
p_gap_upper_err = 0.04  #K06 (hrs)
r_above_pg = 0.2926  #from m_conv, p_gap_upper and mwd=0.811

all_systems_select = []
for i in range (0,len(all_systems)):
    if all_systems[i][2] >= r_above_pg:
        all_systems_select.append(all_systems[i])
        
all_systems_select = np.transpose(all_systems_select)
#print all_systems_select[0]
'''
def chisqfunc_longp(b):
    delta = ((2.0/3.0)*np.log10(all_systems_select[6]*24)) - ((2.0/3.0)*np.log10(p_gap_upper)) + \
        (((1.0/3.0)-b)*np.log10(all_systems_select[0])) - (((1.0/3.0)-b)*np.log10(m_conv))
    sigma_stat = (1.0/3.0)*(0.434*(all_systems_select[1]/all_systems_select[0]))
    sigma_int = 0.04
    sigma_sys_squared = (4.0/9.0)*(0.434*(p_gap_upper_err/p_gap_upper))**2 + (((1.0/3.0)-b)**2)*(0.434*(m_conv_err/m_conv))**2
    #chisq = np.sum((delta**2.0)/((sigma_stat**2.0)+(sigma_int**2.0)))
    #red_chisq = chisq / (len(all_systems_select[0])-1)
    
    chisq_alt = np.sum((delta**2.0)/((sigma_stat**2.0)+(sigma_int**2.0))) - \
        ((np.sum((delta*np.sqrt(sigma_sys_squared))/((sigma_stat**2.0)+(sigma_int**2.0)))**2) / \
        (1 + np.sum(sigma_sys_squared/((sigma_stat**2.0)+(sigma_int**2.0)))))
    red_chisq_alt = chisq_alt / (len(all_systems_select[0])-1)
    
    #print red_chisq
    #return chisq
    print red_chisq_alt
    #print chisq_alt
    return chisq_alt
    
x0 = 0.5

#b = 0.6359127 #0.05
#result = chisqfunc_longp(b)

result = opt.minimize(chisqfunc_longp,x0)
b = result.x
print b
print len(all_systems_select[0])
'''

# short period systems
m_bounce = 0.0633
m_conv = 0.2        #K06 (Msun)
m_conv_err = 0.02       #K06 (Msun)
p_gap_lower = 2.15  #K06 (hrs)
p_gap_lower_err = 0.03  #K06 (hrs)
r_below_pg = 0.2254  #from m_conv, p_gap_lower and mwd=0.812

#m_bounce = 0.063
#m_conv = 0.2        #K06 (Msun)
#m_conv_err = 0.02       #K06 (Msun)
#p_gap_lower = 2.15  #K06 (hrs)
#p_gap_lower_err = 0.03  #K06 (hrs)
#r_below_pg = 0.2254  #from m_conv, p_gap_lower and mwd=0.811


all_systems_select = []
for i in range (0,len(all_systems)):
    if all_systems[i][0] >= m_bounce and all_systems[i][2] <= r_below_pg:
        all_systems_select.append(all_systems[i])
        
all_systems_select = np.transpose(all_systems_select)
#print all_systems_select[0]
'''
def chisqfunc_shortp(b):
    delta = ((2.0/3.0)*np.log10(all_systems_select[6]*24)) - ((2.0/3.0)*np.log10(p_gap_lower)) + \
        (((1.0/3.0)-b)*np.log10(all_systems_select[0])) - (((1.0/3.0)-b)*np.log10(m_conv))
    sigma_stat = (1.0/3.0)*(0.434*(all_systems_select[1]/all_systems_select[0]))
    #sigma_int = 0.00
    sigma_int = 0.0051
    sigma_sys_squared = (4.0/9.0)*(0.434*(p_gap_lower_err/p_gap_lower))**2 + (((1.0/3.0)-b)**2)*(0.434*(m_conv_err/m_conv))**2
    #chisq = np.sum((delta**2.0)/((sigma_stat**2.0)+(sigma_int**2.0)))
    #red_chisq = chisq / (len(all_systems_select[0])-1)
    
    chisq_alt = np.sum((delta**2.0)/((sigma_stat**2.0)+(sigma_int**2.0))) - \
        ((np.sum((delta*np.sqrt(sigma_sys_squared))/((sigma_stat**2.0)+(sigma_int**2.0)))**2) / \
        (1 + np.sum(sigma_sys_squared/((sigma_stat**2.0)+(sigma_int**2.0)))))
    red_chisq_alt = chisq_alt / (len(all_systems_select[0])-1)
    
    #print red_chisq
    #return chisq
    print red_chisq_alt
    #print chisq_alt
    return chisq_alt
    
x0 = 0.5

#b = 0.63608055 #0.0
#result = chisqfunc_shortp(b)

result = opt.minimize(chisqfunc_shortp,x0)
b = result.x
print b
print len(all_systems_select[0])

'''
# period bounce systems
p_min = 76.3           # from this work (mins)
p_min_err = 1.0        #
m_bounce = 0.0633       #
m_bounce_err = 0.005    # rough value
r_below_pmin = 0.1091   #from m_bounce, p = 76.3 mins and mwd=0.812


#p_min = 76.0           # from this work (mins)
#p_min_err = 2.25        #
#m_bounce = 0.063        #
#m_bounce_err = 0.005    # rough value
#r_below_pmin = 0.1087   #from m_bounce, p = 76.0 mins and mwd=0.811


all_systems_select = []
for i in range (0,len(all_systems)):
    if all_systems[i][0] <= m_bounce:
        all_systems_select.append(all_systems[i])
        
all_systems_select = np.transpose(all_systems_select)
#print all_systems_select[0]

def chisqfunc_pbouncers(b):
    delta = ((2.0/3.0)*np.log10(all_systems_select[6]*24)) - ((2.0/3.0)*np.log10(p_min/60.0)) + \
        (((1.0/3.0)-b)*np.log10(all_systems_select[0])) - (((1.0/3.0)-b)*np.log10(m_bounce))
    sigma_stat = (1.0/3.0)*(0.434*(all_systems_select[1]/all_systems_select[0]))
    sigma_int = 0.00
    sigma_sys_squared = (4.0/9.0)*(0.434*(p_min_err/p_min))**2 + (((1.0/3.0)-b)**2)*(0.434*(m_bounce_err/m_bounce))**2
    chisq = np.sum((delta**2.0)/((sigma_stat**2.0)+(sigma_int**2.0)))
    red_chisq = chisq / (len(all_systems_select[0])-1)
    
    #chisq_alt = np.sum((delta**2.0)/((sigma_stat**2.0)+(sigma_int**2.0))) - \
    #    ((np.sum((delta*np.sqrt(sigma_sys_squared))/((sigma_stat**2.0)+(sigma_int**2.0)))**2) / \
    #    (1 + np.sum(sigma_sys_squared/((sigma_stat**2.0)+(sigma_int**2.0)))))
    #red_chisq_alt = chisq_alt / (len(all_systems_select[0])-1)
    
    print red_chisq
    #print chisq
    return chisq
    #print red_chisq_alt
    #return chisq_alt
    
x0 = 0.5

#b = 0.17041327 #0.018
#result = chisqfunc_pbouncers(b)

result = opt.minimize(chisqfunc_pbouncers,x0)
b = result.x
print b
print len(all_systems_select[0])


'''
#plt.plot(m2_k11_ds,r2_k11_ds,c='k',linewidth=1)
#plt.plot(m2_k11_evo_opt*1.1,r2_k11_evo_opt*1.076,c='r',linewidth=1) # m2=0.22
#plt.plot(m2_k11_evo_opt*1.075,r2_k11_evo_opt*1.057,c='r',linewidth=1) # m2=0.215
#plt.plot(m2_k11_evo_opt*1.05,r2_k11_evo_opt*1.038,c='r',linewidth=1) # m2=0.21
#plt.plot(m2_k11_evo_opt*1.025,r2_k11_evo_opt*1.019,c='r',linewidth=1) # m2=0.205
#plt.plot(m2_k11_evo_opt*0.975,r2_k11_evo_opt*0.981,c='r',linewidth=1) # m2=0.195
'''

plt.plot(m2_k11_evo_opt,r2_k11_evo_opt,c='r',linewidth=1,alpha=0.8)#,linestyle='dashed',alpha=0.5)
plt.plot(m2_k11_evo_std,r2_k11_evo_std,c='k',linewidth=1,alpha=0.8)#,linestyle='dashed')    

plt.xlabel(r'$M_{2}\ (\rm{M}_{\odot})$', fontsize=16)
plt.ylabel(r'$R_{2}\ (\rm{R}_{\odot})$', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=13, width=1.0)
plt.tick_params(top='on',right='on')

# Period gap
#plt.axhspan(0.2254,0.2926,xmin=0.59,xmax=0.70,color='k',alpha=0.05)

#plt.axvline(1.363,linestyle='dashed',color='k',linewidth=1,alpha=0.5)
#plt.axvspan(1.348,1.378,color='k',alpha=0.1)
#plt.scatter(1.373,0.1175,marker='o',color='w',s=25)
#plt.errorbar(1.373,0.035,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1,alpha=0.5)
#plt.errorbar(1.373,0.061,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1,alpha=0.5)
#plt.errorbar(1.373,0.106,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1,alpha=0.5)
#plt.axvline(1.373,linestyle='dashed',color='gray')

plt.subplots_adjust(bottom=0.10, top=0.98, left=0.10, right=0.99)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("r2vsm2_curr.pdf")
plt.show()
