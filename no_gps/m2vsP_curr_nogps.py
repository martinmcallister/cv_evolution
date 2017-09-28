import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

#input donor mass and period for system
'''m2,m2_err = raw_input("Donor mass and error in solar masses: ").split()
m2 = float(m2)
m2_err = float(m2_err)

P = raw_input("System period in days: ")
P = float(P)*24'''

#input optimal and original CV model tracks from Knigge et al. 2011
m2_optimal = np.loadtxt('knigge11_optimal.dat',dtype=float,usecols = [0],skiprows=4)
P_optimal = np.loadtxt('knigge11_optimal.dat',dtype=float,usecols = [1],skiprows=4)
m2_standard = np.loadtxt('knigge11_standard.dat',dtype=float,usecols = [1],skiprows=4)
P_standard = np.loadtxt('knigge11_standard.dat',dtype=float,usecols = [2],skiprows=4)

#input BD donor track from Kolb & Baraffe 1999
m2_BD_1 = np.loadtxt('KolbBaraffe99_BD.dat',dtype=float,usecols = [2])
P_BD_1 = np.loadtxt('KolbBaraffe99_BD.dat',dtype=float,usecols = [18])

#input BD donor tracks from Baraffe (Priv. comm)
m2_BD_2 = np.loadtxt('Baraffe_t2gyr.dat',dtype=float,usecols = [2])
P_BD_2 = np.loadtxt('Baraffe_t2gyr.dat',dtype=float,usecols = [18])
m2_BD_3 = np.loadtxt('Baraffe_t1gyr.dat',dtype=float,usecols = [2])
P_BD_3 = np.loadtxt('Baraffe_t1gyr.dat',dtype=float,usecols = [18])
m2_BD_4 = np.loadtxt('Baraffe_t600myr.dat',dtype=float,usecols = [2])
P_BD_4 = np.loadtxt('Baraffe_t600myr.dat',dtype=float,usecols = [18])

#input evolved donor tracks from thorstensen et al. 2002
m2_evol_12 = np.loadtxt('thorstensen02_evol1.2.dat',dtype=float,usecols = [1])
P_evol_12 = np.loadtxt('thorstensen02_evol1.2.dat',dtype=float,usecols = [0])
m2_evol_15 = np.loadtxt('thorstensen02_evol1.5.dat',dtype=float,usecols = [1])
P_evol_15 = np.loadtxt('thorstensen02_evol1.5.dat',dtype=float,usecols = [0])

#produce plot

#plt.rcParams['xtick.major.pad']='15'
#plt.rcParams['ytick.major.pad']='10'

#plt.axis([1,1.7001,0,0.15001])
#plt.axis([1.2,2.2001,0,0.21001])
#plt.axis([1.3,2.21,0,0.231])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([1.0, 7.0])
ax.set_xticks([1,2,3,4,5,6,7])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_yscale('log')
ax.set_ylim([0.03, 0.9])
ax.set_yticks([0.04,0.06,0.08,0.2,0.4,0.6,0.8])
ax.get_yaxis().set_major_formatter(ScalarFormatter())

#plt.scatter(P,m2,marker='o',color='k',s=20)
#plt.errorbar(P,m2,yerr=m2_err,ls='none',color='k',capsize=3)


plt.scatter(0.0529848884*24,0.064,marker='o',color='k',s=20)
plt.errorbar(0.0529848884*24,0.064,yerr=0.006,ls='none',color='k',capsize=3)
#plt.text(0.0529848884*24,0.063,'  PHL 1445',color='k',size=12)


############ DONE (without GPs) ##############


plt.scatter(0.060310649*24,0.111,marker='o',color='r',s=20)
plt.errorbar(0.060310649*24,0.111,yerr=[[0.002],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.060310649*24,0.111,'  ASASSN-14ag(noGPs)',color='r',size=12)


plt.scatter(0.0739089282*24,0.150,marker='o',color='r',s=20)
plt.errorbar(0.0739089282*24,0.150,yerr=[[0.004],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0739089282*24,0.150,'  IY UMa(noGPs)',color='r',size=12)

#plt.scatter(0.0739089282*24,0.149,marker='o',color='r',s=20)
#plt.errorbar(0.0739089282*24,0.149,yerr=[[0.004],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0739089282*24,0.149,'  IY UMa_kg5(noGPs)',color='r',size=12)


plt.scatter(0.0744992631*24,0.1416,marker='o',color='r',s=20)
plt.errorbar(0.0744992631*24,0.1416,yerr=[[0.0009],[0.0013]],ls='none',color='r',capsize=3)
#plt.text(0.0744992631*24,0.1416,'  Z Cha(noGPs)',color='r',size=12)

#plt.scatter(0.0744992631*24,0.1551,marker='o',color='r',s=20)
#plt.errorbar(0.0744992631*24,0.1551,yerr=[[0.0019],[0.0011]],ls='none',color='r',capsize=3)
#plt.text(0.0744992631*24,0.1551,'  Z Cha_g(noGPs)',color='r',size=12)


plt.scatter(0.059578970*24,0.101,marker='o',color='r',s=20)
plt.errorbar(0.059578970*24,0.101,yerr=[[0.004],[0.007]],ls='none',color='r',capsize=3)
#plt.text(0.059578970*24,0.101,'  CSS080623(noGPs)',color='r',size=12)


plt.scatter(0.0778805320*24,0.166,marker='o',color='r',s=20)
plt.errorbar(0.0778805320*24,0.166,yerr=[[0.010],[0.004]],ls='none',color='r',capsize=3)
#plt.text(0.0778805320*24,0.166,'  SDSS 0901(noGPs)',color='r',size=12)


plt.scatter(0.0858526521*24,0.196,marker='o',color='r',s=20)
plt.errorbar(0.0858526521*24,0.196,yerr=[[0.008],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0858526521*24,0.196,'  DV UMa(noGPs)',color='r',size=12)

#plt.scatter(0.0858526521*24,0.191,marker='o',color='r',s=20)
#plt.errorbar(0.0858526521*24,0.191,yerr=[[0.004],[0.010]],ls='none',color='r',capsize=3)
#plt.text(0.0858526521*24,0.191,'  DV UMa_g(noGPs)',color='r',size=12)


plt.scatter(0.088940717*24,0.174,marker='o',color='r',s=20)
plt.errorbar(0.088940717*24,0.174,yerr=[[0.003],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.088940717*24,0.174,'  CTCV 1300(noGPs)',color='r',size=12)

#plt.scatter(0.088940717*24,0.188,marker='o',color='r',s=20)
#plt.errorbar(0.088940717*24,0.188,yerr=[[0.003],[0.004]],ls='none',color='r',capsize=3)
#plt.text(0.088940717*24,0.188,'  CTCV 1300_g(noGPs)',color='r',size=12)


plt.scatter(0.0631209221*24,0.0891,marker='o',color='r',s=20)
plt.errorbar(0.0631209221*24,0.0891,yerr=[[0.0007],[0.0015]],ls='none',color='r',capsize=3)
#plt.text(0.0631209221*24,0.0891,'  OY Car(noGPs)',color='r',size=12)

#plt.scatter(0.0631209221*24,0.1072,marker='o',color='r',s=20)
#plt.errorbar(0.0631209221*24,0.1072,yerr=[[0.0009],[0.0009]],ls='none',color='r',capsize=3)
#plt.text(0.0631209221*24,0.1072,'  OY Car_g(noGPs)',color='r',size=12)


plt.scatter(0.065769292*24,0.148,marker='o',color='r',s=20)
plt.errorbar(0.065769292*24,0.148,yerr=[[0.004],[0.002]],ls='none',color='r',capsize=3)
#plt.text(0.065769292*24,0.148,'  SSS130413(noGPs)',color='r',size=12)


plt.scatter(0.0660508707*24,0.109,marker='o',color='r',s=20)
plt.errorbar(0.0660508707*24,0.109,yerr=[[0.006],[0.008]],ls='none',color='r',capsize=3)
#plt.text(0.0660508707*24,0.109,'  CSS110113(noGPs)',color='r',size=12)


plt.scatter(0.0587045*24,0.074,marker='o',color='r',s=20)
plt.errorbar(0.0587045*24,0.074,yerr=[[0.004],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0587045*24,0.071,'  SSS100615(noGPs)',color='r',size=12)


plt.scatter(0.0677497026*24,0.086,marker='o',color='r',s=20)
plt.errorbar(0.0677497026*24,0.086,yerr=[[0.007],[0.005]],ls='none',color='r',capsize=3)
#plt.text(0.0677497026*24,0.086,'  SDSS 1152(noGPs)',color='r',size=12)


plt.scatter(0.0627919557*24,0.0440,marker='o',color='r',s=20)
plt.errorbar(0.0627919557*24,0.0440,yerr=[[0.0017],[0.0015]],ls='none',color='r',capsize=3)
#plt.text(0.0627919557*24,0.0440,'  SDSS1057(noGPs)',color='r',size=12)


plt.scatter(0.0568412623*24,0.047,marker='o',color='r',s=20)
plt.errorbar(0.0568412623*24,0.047,yerr=[[0.003],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0568412623*24,0.047,'  SDSS 1501(noGPs)',color='r',size=12)


############## IN LITERATURE ################

# HIGH_TIME RESOLUTION ECLIPSE MODELLING (Last 15 years)

#plt.scatter(0.059578970*24,0.098,marker='o',color='k',s=20,alpha=0.25)
#plt.errorbar(0.059578970*24,0.098,yerr=0.003,ls='none',color='k',capsize=3,alpha=0.25)
#plt.text(0.059578970*24,0.095,'  CSS080623',color='k',size=12,alpha=0.25)

#plt.scatter(0.0778805320*24,0.161,marker='o',color='k',s=20,alpha=0.25)
#plt.errorbar(0.0778805320*24,0.161,yerr=0.007,ls='none',color='k',capsize=3,alpha=0.25)
#plt.text(0.0778805320*24,0.162,'  SDSS 0901',color='k',size=12,alpha=0.25)

#plt.scatter(0.088940717*24,0.177,marker='o',color='k',s=20)
#plt.errorbar(0.088940717*24,0.177,yerr=0.021,ls='none',color='k',capsize=3)
#plt.text(0.088940717*24,0.177,'  CTCV J1300-3052',color='k',size=12)

#plt.scatter(0.0677497026*24,0.087,marker='o',color='k',s=20)
#plt.errorbar(0.0677497026*24,0.087,yerr=0.006,ls='none',color='k',capsize=3)
#plt.text(0.0677497026*24,0.087,'  SDSS 1152',color='k',size=12)

#plt.scatter(0.0858526521*24,0.196,marker='o',color='k',s=20)
#plt.errorbar(0.0858526521*24,0.196,yerr=0.005,ls='none',color='k',capsize=3)
#plt.text(0.0858526521*24,0.196,'  DV UMa',color='k',size=12)

#plt.scatter(0.0568412623*24,0.077,marker='o',color='k',s=20)
#plt.errorbar(0.0568412623*24,0.077,yerr=0.010,ls='none',color='k',capsize=3)
#plt.text(0.0568412623*24,0.074,'  SDSS 1501',color='k',size=12)

plt.scatter(0.054240679*24,0.0571,marker='o',color='k',s=20)
plt.errorbar(0.054240679*24,0.0571,yerr=0.0007,ls='none',color='k',capsize=3)
#plt.text(0.054240679*24,0.0571,'  SDSS 1433',color='k',size=12)

plt.scatter(0.04625828*24,0.0575,marker='o',color='k',s=20)
plt.errorbar(0.04625828*24,0.0575,yerr=0.002,ls='none',color='k',capsize=3)
#plt.text(0.04625828*24,0.0551,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0570067*24,0.0475,marker='o',color='k',s=20)
plt.errorbar(0.0570067*24,0.0475,yerr=0.0012,ls='none',color='k',capsize=3)
#plt.text(0.0570067*24,0.0457,'  SDSS 1035',color='k',size=12)

plt.scatter(0.065550270*24,0.101,marker='o',color='k',s=20)
plt.errorbar(0.065550270*24,0.101,yerr=0.003,ls='none',color='k',capsize=3)
#plt.text(0.065550270*24,0.103,' CTCV J2354-4700',color='k',size=12)

plt.scatter(0.059073543*24,0.099,marker='o',color='k',s=20)
plt.errorbar(0.059073543*24,0.099,yerr=0.004,ls='none',color='k',capsize=3)
#plt.text(0.059073543*24,0.098,'      SDSS 0903',color='k',size=12)

plt.scatter(0.062959041*24,0.0889,marker='o',color='k',s=20)
plt.errorbar(0.062959041*24,0.0889,yerr=0.0025,ls='none',color='k',capsize=3)
#plt.text(0.062959041*24,0.0889,'  SDSS 1227',color='k',size=12)

plt.scatter(0.061159491*24,0.091,marker='o',color='k',s=20)
plt.errorbar(0.061159491*24,0.091,yerr=0.004,ls='none',color='k',capsize=3)
#plt.text(0.061159491*24,0.092,'  XZ Eri',color='k',size=12)

plt.scatter(0.05890961*24,0.0781,marker='o',color='k',s=20)
plt.errorbar(0.05890961*24,0.0781,yerr=0.0008,ls='none',color='k',capsize=3)
#plt.text(0.05890961*24,0.0781,'  SDSS 1502',color='k',size=12)

plt.scatter(0.072706113*24,0.1157,marker='o',color='k',s=20)
plt.errorbar(0.072706113*24,0.1157,yerr=0.0022,ls='none',color='k',capsize=3)
#plt.text(0.072706113*24,0.1157,'  OU Vir',color='k',size=12)

plt.scatter(0.10008215*24,0.223,marker='o',color='k',s=20)
plt.errorbar(0.10008215*24,0.223,yerr=0.010,ls='none',color='k',capsize=3)
#plt.text(0.10008215*24,0.223,'  SDSS 1702',color='k',size=12)

#From Littlefair08
#plt.scatter(0.063121*24,0.086,marker='o',color='b',s=20)
#plt.errorbar(0.063121*24,0.086,yerr=0.005,ls='none',color='b',capsize=3)
#plt.text(0.063121*24,0.086,'  OY Car',color='b',size=12)

#From Shafter03
plt.scatter(0.209937*24,0.53,marker='o',color='b',s=20)
plt.errorbar(0.209937*24,0.53,yerr=0.01,ls='none',color='b',capsize=3)
#plt.text(0.209937*24,0.53,'  EX Dra',color='b',size=12)

# From Southworth09
#plt.scatter(0.185912957*24,0.40,marker='o',color='b',s=20)
#plt.errorbar(0.185912957*24,0.40,yerr=0.10,ls='none',color='b',capsize=3)
#plt.text(0.185912957*24,0.40,'  SDSS 1006',color='b',size=12)

#From Littlefair14
plt.scatter(0.1653077*24,0.39,marker='o',color='k',s=20)
plt.errorbar(0.1653077*24,0.39,yerr=0.04,ls='none',color='k',capsize=3)
#plt.text(0.1653077*24,0.39,'  KIS J1927',color='k',size=12)

#From Copperwheat10
plt.scatter(0.1582061029*24,0.55,marker='o',color='b',s=20)
plt.errorbar(0.1582061029*24,0.55,yerr=0.02,ls='none',color='b',capsize=3)
#plt.text(0.1582061029*24,0.55,'  IP Peg',color='b',size=12)

#From Miszalski16 (Mass overestimated due to bug in code)
plt.scatter(0.120971374*24,0.28,marker='o',color='k',s=20)
plt.errorbar(0.120971374*24,0.28,yerr=[[0.03],[0.03]],ls='none',color='k',capsize=3)
#plt.text(0.120971374*24,0.28,'  CSS111003',color='k',size=12)

#From Miszalski16 (Revised value from Stu)
#plt.scatter(0.120971374*24,,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,,yerr=[[],[]],ls='none',color='k',capsize=3)
#plt.text(0.120971374*24,,'  CSS111003',color='k',size=12)

#From Rodriguez-Gil15 (Eclipse modelling)
plt.scatter(0.149207696*24,0.47,marker='o',color='b',s=20)
plt.errorbar(0.149207696*24,0.47,yerr=0.05,ls='none',color='b',capsize=3)
#plt.text(0.149207696*24,0.47,'  HS 0220+0603',color='b',size=12)

# OTHER

#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.198,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.088940717*24,0.198,yerr=[[0.029],[0.029]],ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.088940717*24,0.198,'  CTCV 1300',color='b',size=12,alpha=0.5)

#From Steeghs03 (timing)
#plt.scatter(0.0739089282*24,0.10,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0739089282*24,0.10,yerr=0.01,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0739089282*24,0.10,'  IY UMa',color='b',size=12,alpha=0.5)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.1754424023*24,0.33,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.1754424023*24,0.33,yerr=0.07,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.1754424023*24,0.33,'  GY Cnc',color='b',size=12,alpha=0.5)

#From Smak07 (RV/timing)  
#plt.scatter(0.0744992631*24,0.186,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.186,yerr=0.030,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0744992631*24,0.186,'  Z Cha_S07',color='b',size=12,alpha=0.5)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
#plt.scatter(0.0744992631*24,0.125,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.125,yerr=0.014,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0744992631*24,0.125,'  Z Cha_WH88',color='b',size=12,alpha=0.5)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.083,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.083,yerr=0.003,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0744992631*24,0.083,'  Z Cha_W86',color='b',size=12,alpha=0.5)

#From Horne91 (eclipse modelling)
#plt.scatter(0.0736471745*24,0.09,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0736471745*24,0.09,yerr=0.02,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0736471745*24,0.09,' HT Cas ',color='b',size=12,alpha=0.5)

#From Wood&Horne90 (eclipse modelling)
#plt.scatter(0.0631209221*24,0.082,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0631209221*24,0.082,yerr=0.004,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0631209221*24,0.082,'  OY Car_H91',color='b',size=12,alpha=0.5)

#From Baptista98 (timing)
#plt.scatter(0.06242785751*24,0.15,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.06242785751*24,0.15,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.06242785751*24,0.15,'  V2051 Oph',color='b',size=12,alpha=0.5)

#From Steeghs07 (wd mass from gravitational redshift & q from RV)
#plt.scatter(0.056688*24,0.078,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.056688*24,0.078,yerr=0.006,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.056688*24,0.078,'  WZ Sge',color='b',size=12,alpha=0.5)

#From Echevarria16 (RV)
#plt.scatter(0.068233843*24,0.10,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.068233843*24,0.10,yerr=0.02,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.068233843*24,0.10,'  EX Hya',color='b',size=12,alpha=0.5)

#From Echevarria07 (RV)
#plt.scatter(0.176906*24,0.42,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.176906*24,0.42,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.176906*24,0.42,'  U Gem',color='b',size=12,alpha=0.5)

#From Smith06 (wd mass from gravitational redshift & q from superhump excess)
#plt.scatter(0.074271*24,0.11,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.074271*24,0.11,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.074271*24,0.11,'  VW Hyi',color='b',size=12,alpha=0.5)

#From Horne93 (RV)
#plt.scatter(0.1936209*24,0.40,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.1936209*24,0.40,yerr=0.05,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.1936209*24,0.40,'  DQ Her',color='b',size=12,alpha=0.5)

#From Thoroughgood05 (RV)
#plt.scatter(0.231936060*24,0.52,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.231936060*24,0.52,yerr=0.06,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.231936060*24,0.52,'  V347 Pup',color='b',size=12,alpha=0.5)

#From Borges&Baptista98 (timing)
#plt.scatter(0.0614296757*24,0.092,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0614296757*24,0.092,yerr=0.016,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0614296757*24,0.092,'  V4140 Sgr',color='b',size=12,alpha=0.5)

#From HernandezSantisteban17 (RV)
#plt.scatter(0.26937446*24,0.78,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.26937446*24,0.78,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.26937446*24,0.78,'  1RXS J064434.5+334451',color='b',size=12,alpha=0.5)

#From Yakin10 (RV)
#plt.scatter(0.070037*24,0.14,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.070037*24,0.14,yerr=0.02,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.070037*24,0.14,'  1RXS J180834.7+101041',color='b',size=12,alpha=0.5)

#From Baptista00 (timing) 
#plt.scatter(0.209937*24,0.54,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.209937*24,0.54,yerr=0.10,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.209937*24,0.54,'  EX Dra',color='b',size=12,alpha=0.5)

#From Mason&Howell05 (RV) (Error bars not given in paper)
#plt.scatter(0.07460*24,0.17,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.07460*24,0.17,yerr=0.05,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.07460*24,0.17,'  AY For',color='b',size=12,alpha=0.5)

mwd_k11 = 0.75
mwd_new = 0.75
m2_shift = mwd_new/mwd_k11

plt.plot(P_optimal,m2_optimal*m2_shift,c='r',linewidth=1)
#plt.plot(P_optimal,m2_optimal*1.07,c='r',linewidth=1)
#plt.plot(P_standard,m2_standard,c='r',linestyle='dashed')
#plt.plot(P_BD_1,m2_BD_1,c='b',linewidth=2)
#plt.plot(P_BD_2,m2_BD_2,c='b',linestyle='--',linewidth=2)
#plt.plot(P_BD_3,m2_BD_3,c='b',linestyle='-.',linewidth=2)
#plt.plot(P_BD_4,m2_BD_4,c='b',linestyle=':',linewidth=2)
#plt.plot(P_evol_12,m2_evol_12,c='g',linewidth=2)
#plt.plot(P_evol_15,m2_evol_15,c='g',linestyle='dashed')
plt.xlabel(r'P$_{\rm orb}$ (hrs)', fontsize=15)
plt.ylabel(r'M$_{\rm d}$ (M$_{\odot}$)', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15, width=1.0)
plt.axvline(1.363,linestyle='dashed',color='k',linewidth=1,alpha=0.5)
#plt.axvspan(1.348,1.378,color='k',alpha=0.1)
#plt.scatter(1.373,0.1175,marker='o',color='w',s=25)
#plt.errorbar(1.373,0.01475,xerr=0.048,ls='none',color='k',capsize=5,linewidth=2,alpha=0.5)
#plt.errorbar(1.373,0.061,xerr=0.048,ls='none',color='k',capsize=5)
#plt.axvline(1.373,linestyle='dashed',color='gray')

plt.subplots_adjust(bottom=0.1, top=0.95, left=0.1, right=0.95)
for axis in ['top','bottom','left','right']:
 plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.savefig("m2vsP_curr_nogps.pdf")
plt.show()
