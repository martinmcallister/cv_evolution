import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math
import seaborn

#input optimal and original CV model tracks from Knigge et al. 2011
m2_optimal = np.loadtxt('Knigge11/knigge11_optimal.dat',dtype=float,usecols = [0],skiprows=4)
P_optimal = np.loadtxt('Knigge11/knigge11_optimal.dat',dtype=float,usecols = [1],skiprows=4)
m2_standard = np.loadtxt('Knigge11/knigge11_standard.dat',dtype=float,usecols = [1],skiprows=4)
P_standard = np.loadtxt('Knigge11/knigge11_standard.dat',dtype=float,usecols = [2],skiprows=4)

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

#plt.axis([1,1.7001,0,0.15001])
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


# HIGH_TIME RESOLUTION ECLIPSE MODELLING (circles)

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

plt.scatter(0.0677497026*24,0.087,marker='o',color='k',s=10)
plt.errorbar(0.0677497026*24,0.087,yerr=0.006,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0677497026*24,0.087,'  SDSS 1152',color='k',size=12)

plt.scatter(0.059073543*24,0.099,marker='o',color='k',s=10)
plt.errorbar(0.059073543*24,0.099,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.059073543*24,0.098,'   SDSS 0903',color='k',size=12)

plt.scatter(0.062959041*24,0.0889,marker='o',color='k',s=10)
plt.errorbar(0.062959041*24,0.0889,yerr=0.0025,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.062959041*24,0.0889,'  SDSS 1227',color='k',size=12)

plt.scatter(0.061159491*24,0.091,marker='o',color='k',s=10)
plt.errorbar(0.061159491*24,0.091,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.061159491*24,0.092,'  XZ Eri',color='k',size=12)

plt.scatter(0.05890961*24,0.0781,marker='o',color='k',s=10)
plt.errorbar(0.05890961*24,0.0781,yerr=0.0008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.05890961*24,0.0781,'  SDSS 1502',color='k',size=12)

plt.scatter(0.0568412623*24,0.077,marker='o',color='k',s=10)
plt.errorbar(0.0568412623*24,0.077,yerr=0.010,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0568412623*24,0.074,'  SDSS 1501',color='k',size=12)

plt.scatter(0.088940717*24,0.177,marker='o',color='k',s=10)
plt.errorbar(0.088940717*24,0.177,yerr=0.021,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.088940717*24,0.177,'  CTCV J1300-3052',color='k',size=12)

plt.scatter(0.072706113*24,0.1157,marker='o',color='k',s=10)
plt.errorbar(0.072706113*24,0.1157,yerr=0.0022,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.072706113*24,0.1157,'  OU Vir',color='k',size=12)

plt.scatter(0.0858526521*24,0.196,marker='o',color='k',s=10)
plt.errorbar(0.0858526521*24,0.196,yerr=0.005,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0858526521*24,0.196,'  DV UMa',color='k',size=12)

plt.scatter(0.10008215*24,0.223,marker='o',color='k',s=10)
plt.errorbar(0.10008215*24,0.223,yerr=0.010,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.10008215*24,0.223,'  SDSS 1702',color='k',size=12)

# Other systems

#From Shafter03
plt.scatter(0.209937*24,0.53,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.209937*24,0.53,yerr=0.01,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.209937*24,0.53,'  EX Dra_S03',color='b',size=12,alpha=0.3)

# From Southworth09
plt.scatter(0.185912957*24,0.40,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.185912957*24,0.40,yerr=0.10,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.185912957*24,0.40,'  SDSS 1006_S09',color='b',size=12,alpha=0.3)

#From Copperwheat10 (UCAM data)
plt.scatter(0.1582061029*24,0.55,marker='o',color='k',s=10)
plt.errorbar(0.1582061029*24,0.55,yerr=0.02,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.1582061029*24,0.55,'  IP Peg_C10',color='b',size=12)


# CONTACT PHASE TIMING (squares)

#From Steeghs03 (timing)
plt.scatter(0.0739089282*24,0.10,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0739089282*24,0.10,yerr=0.01,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0739089282*24,0.10,'  IY UMa_S03',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.083,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.083,yerr=0.003,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0744992631*24,0.083,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Horne91 (timing)
plt.scatter(0.0736471745*24,0.09,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0736471745*24,0.09,yerr=0.02,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0736471745*24,0.09,' HT Cas_H91',color='b',size=12,alpha=0.3)

#From Littlefair08 (Revised from Wood & Horne 1990)
plt.scatter(0.0631209221*24,0.086,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0631209221*24,0.086,yerr=0.005,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0631209221*24,0.086,'  OY Car_L08',color='b',size=12,alpha=0.3)

#From Wood&Horne90 (timing)
#plt.scatter(0.0631209221*24,0.082,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.082,yerr=0.004,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0631209221*24,0.082,'  OY Car_H90',color='b',size=12,alpha=0.3)

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


#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.198,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.088940717*24,0.198,yerr=[[0.029],[0.029]],ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.088940717*24,0.198,'  CTCV 1300_S12',color='b',size=12,alpha=0.3)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
plt.scatter(0.1754424023*24,0.33,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.1754424023*24,0.33,yerr=0.07,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.1754424023*24,0.33,'  GY Cnc_T00',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
plt.scatter(0.0744992631*24,0.125,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.0744992631*24,0.125,yerr=0.014,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0744992631*24,0.125,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

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


# SUPERHUMPERS

p_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [0])
m2_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [1])
m2_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [2])
r2_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [3])
r2_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [3])

for i in range(len(p_sh)):
    plt.scatter(p_sh[i],m2_sh[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(p_sh[i],m2_sh[i],yerr=m2_err_sh[i],ls='none',color='k',capsize=None,alpha=0.15)

plt.plot(P_optimal,m2_optimal,c='r',linewidth=1,alpha=0.8)
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


# Existing period minimum
plt.axvline(1.3626,linestyle='dashed',color='k',linewidth=1,alpha=0.5) #K11
plt.axvspan(1.3476,1.3776,color='k',alpha=0.05) #K11
#plt.errorbar(1.373,0.024,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1.5,alpha=0.8) #G09
#plt.axvspan(1.325,1.421,color='k',alpha=0.05) #G09
plt.arrow(1.373,0.024,0.0475,0,width=0.0003,head_width=0.002,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09
plt.arrow(1.373,0.024,-0.0475,0,width=0.0003,head_width=0.002,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09


plt.subplots_adjust(bottom=0.10, top=0.98, left=0.10, right=0.99)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("m2vsP_init.pdf")
plt.show()
