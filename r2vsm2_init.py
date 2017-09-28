import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math
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
#plt.axis([1.2,2.2001,0.02,0.2001])
#plt.axis([1.0,3.001,0.02,0.301])
#plt.axis([1.1,1.6,0.03,0.11])

#plt.axis([0.02,0.55,0.08,0.5])
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


# HIGH_TIME RESOLUTION ECLIPSE MODELLING (circles)

# Systems from Savoury 11

plt.scatter(0.0571,0.1074,marker='o',color='k',s=10)
plt.errorbar(0.0571,0.1074,xerr=0.0007,yerr=0.0004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0571,0.1074,'  SDSS 1433',color='k',size=12)

plt.scatter(0.0575,0.0969,marker='o',color='k',s=10)
plt.errorbar(0.0575,0.0969,xerr=0.002,yerr=0.0011,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0551,0.0969,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0475,0.1047,marker='o',color='k',s=10)
plt.errorbar(0.0475,0.1047,xerr=0.0012,yerr=0.0008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0457,0.1047,'  SDSS 1035',color='k',size=12)

plt.scatter(0.101,0.1463,marker='o',color='k',s=10)
plt.errorbar(0.101,0.1463,xerr=0.003,yerr=0.0016,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.103,0.1463,' CTCV J2354-4700',color='k',size=12)

plt.scatter(0.087,0.142,marker='o',color='k',s=10)
plt.errorbar(0.087,0.142,xerr=0.006,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.087,0.142,'  SDSS 1152',color='k',size=12)

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

plt.scatter(0.077,0.122,marker='o',color='k',s=10)
plt.errorbar(0.077,0.122,xerr=0.010,yerr=0.005,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.074,0.122,'  SDSS 1501',color='k',size=12)

plt.scatter(0.177,0.215,marker='o',color='k',s=10)
plt.errorbar(0.177,0.215,xerr=0.021,yerr=0.008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.177,0.215,'  CTCV J1300-3052',color='k',size=12)

plt.scatter(0.1157,0.1634,marker='o',color='k',s=10)
plt.errorbar(0.1157,0.1634,xerr=0.0022,yerr=0.0010,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.1157,0.1634,'  OU Vir',color='k',size=12)

plt.scatter(0.196,0.2176,marker='o',color='k',s=10)
plt.errorbar(0.196,0.2176,xerr=0.005,yerr=0.0018,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.196,0.2176,'  DV UMa',color='k',size=12)

plt.scatter(0.223,0.252,marker='o',color='k',s=10)
plt.errorbar(0.223,0.252,xerr=0.010,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(,0.223,0.252,'  SDSS 1702',color='k',size=12)

# Other systems

#From Shafter03
plt.scatter(0.53,0.565,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.53,0.565,xerr=0.01,yerr=0.004,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.53,0.565,'  EX Dra_S03',color='b',size=12,alpha=0.3)

# From Southworth09
plt.scatter(0.40,0.47,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.40,0.47,xerr=0.10,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.40,0.47,'  SDSS 1006_S09',color='b',size=12,alpha=0.3)

#From Copperwheat10 (UCAM data)
plt.scatter(0.55,0.466,marker='o',color='k',s=10)
plt.errorbar(0.55,0.466,xerr=0.02,yerr=0.006,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.55,0.466,'  IP Peg_C10',color='k',size=12)


# CONTACT PHASE TIMING (squares)

#From Steeghs03 (timing)
plt.scatter(0.10,0.158,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.10,0.158,xerr=0.01,yerr=0.005,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.10,0.158,'  IY UMa_S03',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.083,0.1489,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.083,0.1489,xerr=0.003,yerr=0.0018,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.083,0.1489,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Horne91 (timing)
plt.scatter(0.09,0.152,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.09,0.152,xerr=0.02,yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.09,0.152,' HT Cas_H91',color='b',size=12,alpha=0.3)

#From Littlefair08 (Revised from Wood & Horne 1990)
plt.scatter(0.086,0.1354,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.086,0.1354,xerr=0.005,yerr=0.0026,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.086,0.1354,'  OY Car_L08',color='b',size=12,alpha=0.3)

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


#From Savoury12 (RV)
#plt.scatter(0.198,0.224,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.198,0.224,xerr=[[0.029],[0.029]],yerr=0.011,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.198,0.224,'  CTCV 1300_S12',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
plt.scatter(0.125,0.171,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.125,0.171,xerr=0.014,yerr=0.006,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.125,0.171,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
plt.scatter(0.33,0.42,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.33,0.42,xerr=0.07,yerr=0.03,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.33,0.42,'  GY Cnc_T00',color='b',size=12,alpha=0.3)

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
#plt.scatter(0.37,0.780,marker='^',color='b',s=10,alpha=0.3)
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


# SUPERHUMPERS

p_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [0])
m2_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [1])
m2_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [2])
#r2_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [3])
#r2_err_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [4])
m1_sh = np.loadtxt('Superhumpers/superhumpers_p05_init.dat',dtype=float,usecols = [7])

q_sh = m2_sh/m1_sh
r2_sh = 0.2478 * ((p_sh)**(2.0/3.0)) * (m2_sh**(1.0/3.0)) * \
        (((q_sh**(1.0/3.0))*((1+q_sh)**(1.0/3.0)))/((0.6*(q_sh**(2.0/3.0)))+np.log(1+(q_sh**(1.0/3.0)))))

for i in range(len(p_sh)):  
    plt.scatter(m2_sh[i],r2_sh[i],marker='o',color='k',s=10,alpha=0.2)
    #plt.errorbar(m2_sh[i],r2_sh[i],xerr=r2_err_sh[i],yerr=m2_err_sh[i],ls='none',color='k',capsize=None,linewidth=1,alpha=0.15)


# Updated broken law donor sequence from K11
m2_1 = np.linspace(0,0.069,1000)
r2_1 = 0.118*((m2_1/0.069)**0.30)
m2_2 = np.linspace(0.069,0.20,1000)
r2_2 = 0.225*((m2_2/0.2)**0.61)
r2_3 = np.linspace(0.225,0.293,1000)
m2_3 = 0.2*(r2_3**0.0)
m2_4 = np.linspace(0.2,0.9,1000)
r2_4 = 0.293*((m2_4/0.2)**0.69)

plt.plot(m2_1,r2_1,c='k',linewidth=1,alpha=0.8)
plt.plot(m2_2,r2_2,c='k',linewidth=1,alpha=0.8)
plt.plot(m2_3,r2_3,c='k',linewidth=1,alpha=0.8)
plt.plot(m2_4,r2_4,c='k',linewidth=1,alpha=0.8)


#plt.plot(m2_k11_evo_opt,r2_k11_evo_opt,c='r',linewidth=1,alpha=0.8)#,linestyle='dashed',alpha=0.5)
#plt.plot(m2_k11_evo_std,r2_k11_evo_std,c='k',linewidth=1,alpha=0.8)#,linestyle='dashed')    

plt.xlabel(r'$M_{2}\ (\rm{M}_{\odot})$', fontsize=16)
plt.ylabel(r'$R_{2}\ (\rm{R}_{\odot})$', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=13, width=1.0)
plt.tick_params(top='on',right='on')

# Period gap
#plt.axhspan(0.225,0.293,color='k',alpha=0.05)


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
plt.savefig("r2vsm2_init.pdf")
plt.show()
