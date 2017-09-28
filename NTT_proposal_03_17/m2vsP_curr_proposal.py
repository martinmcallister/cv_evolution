import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import math

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
#plt.axis([1.2,2.2001,0.01,0.23001])
#plt.axis([1.0,3.001,0.02,0.401])
#plt.axis([1.1,1.6,0.03,0.11])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([1.0, 6.0])
ax.set_xticks([1,2,3,4,5,6])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_yscale('log')
ax.set_ylim([0.03, 0.8])
ax.set_yticks([0.04,0.06,0.08,0.2,0.4,0.6,0.8])
ax.get_yaxis().set_major_formatter(ScalarFormatter())

#plt.scatter(P,m2,marker='o',color='k',s=20)
#plt.errorbar(P,m2,yerr=m2_err,ls='none',color='k',capsize=3)

#plt.scatter(0.0529848884*24,0.064,marker='o',color='k',s=20)
#plt.errorbar(0.0529848884*24,0.064,yerr=0.005,ls='none',color='k',capsize=3)
#plt.text(0.0529848884*24,0.063,'  PHL 1445',color='k',size=12)

plt.scatter(0.0529848884*24,0.071,marker='o',color='k',s=20)
plt.errorbar(0.0529848884*24,0.071,yerr=[[0.005],[0.009]],ls='none',color='k',capsize=3)
#plt.text(0.0529848884*24,0.071,'  PHL 1445(GPs)',color='k',size=12)



############ DONE (with GPs) ##############


plt.scatter(0.060310649*24,0.109,marker='o',color='g',s=20)
plt.errorbar(0.060310649*24,0.109,yerr=[[0.013],[0.012]],ls='none',color='g',capsize=3)
#plt.text(0.060310649*24,0.109,'  ASASSN-14ag(GPs)',color='g',size=12)


plt.scatter(0.0739089282*24,0.141,marker='o',color='g',s=20)
plt.errorbar(0.0739089282*24,0.141,yerr=[[0.007],[0.007]],ls='none',color='g',capsize=3)
#plt.text(0.0739089282*24,0.141,'  IY UMa(GPs)',color='g',size=12)

#plt.scatter(0.0739089282*24,0.132,marker='o',color='g',s=20)
#plt.errorbar(0.0739089282*24,0.132,yerr=[[0.015],[0.005]],ls='none',color='g',capsize=3)
#plt.text(0.0739089282*24,0.132,'  IY UMa_kg5(GPs)',color='g',size=12)


plt.scatter(0.0744992631*24,0.152,marker='o',color='g',s=20)
plt.errorbar(0.0744992631*24,0.152,yerr=[[0.005],[0.006]],ls='none',color='g',capsize=3)
#plt.text(0.0744992631*24,0.152,'  Z Cha(GPs)',color='g',size=12)

#plt.scatter(0.0744992631*24,0.130,marker='o',color='g',s=20)
#plt.errorbar(0.0744992631*24,0.130,yerr=[[0.002],[0.015]],ls='none',color='g',capsize=3)
#plt.text(0.0744992631*24,0.130,'  Z Cha_g(GPs)',color='g',size=12)


plt.scatter(0.059578970*24,0.081,marker='o',color='g',s=20)
plt.errorbar(0.059578970*24,0.081,yerr=[[0.005],[0.005]],ls='none',color='g',capsize=3)
#plt.text(0.059578970*24,0.081,'  CSS080623(GPs)',color='g',size=12)


plt.scatter(0.0778805320*24,0.138,marker='o',color='g',s=20)
plt.errorbar(0.0778805320*24,0.138,yerr=[[0.007],[0.007]],ls='none',color='g',capsize=3)
#plt.text(0.0778805320*24,0.138,'  SDSS 0901(GPs)',color='g',size=12)


plt.scatter(0.0858526521*24,0.187,marker='o',color='k',s=20)
plt.errorbar(0.0858526521*24,0.187,yerr=[[0.012],[0.003]],ls='none',color='k',capsize=3)
#plt.text(0.0858526521*24,0.187,'  DV UMa(GPs)',color='k',size=12)

#plt.scatter(0.0858526521*24,0.173,marker='o',color='g',s=20)
#plt.errorbar(0.0858526521*24,0.173,yerr=[[0.010],[0.012]],ls='none',color='g',capsize=3)
#plt.text(0.0858526521*24,0.173,'  DV UMa_g(GPs)',color='g',size=12)


plt.scatter(0.088940717*24,0.166,marker='o',color='k',s=20)
plt.errorbar(0.088940717*24,0.166,yerr=[[0.003],[0.006]],ls='none',color='k',capsize=3)
#plt.text(0.088940717*24,0.166,'  CTCV 1300(GPs)',color='k',size=12)

#plt.scatter(0.088940717*24,0.173,marker='o',color='g',s=20)
#plt.errorbar(0.088940717*24,0.173,yerr=[[0.008],[0.005]],ls='none',color='g',capsize=3)
#plt.text(0.088940717*24,0.173,'  CTCV 1300_g(GPs)',color='g',size=12)


plt.scatter(0.0631209221*24,0.093,marker='o',color='g',s=20)
plt.errorbar(0.0631209221*24,0.093,yerr=[[0.001],[0.003]],ls='none',color='g',capsize=3)
#plt.text(0.0631209221*24,0.093,'  OY Car(GPs)',color='g',size=12)


plt.scatter(0.065769292*24,0.140,marker='o',color='g',s=20)
plt.errorbar(0.065769292*24,0.140,yerr=[[0.008],[0.012]],ls='none',color='g',capsize=3)
#plt.text(0.065769292*24,0.140,'  SSS130413(GPs)',color='g',size=12)


plt.scatter(0.0660508707*24,0.105,marker='o',color='g',s=20)
plt.errorbar(0.0660508707*24,0.105,yerr=[[0.006],[0.008]],ls='none',color='g',capsize=3)
#plt.text(0.0660508707*24,0.105,'  CSS110113(GPs)',color='g',size=12)


plt.scatter(0.0587045*24,0.083,marker='o',color='g',s=20)
plt.errorbar(0.0587045*24,0.083,yerr=[[0.004],[0.006]],ls='none',color='g',capsize=3)
#plt.text(0.0587045*24,0.083,'  SSS100615(GPs)',color='g',size=12)


plt.scatter(0.0677497026*24,0.094,marker='o',color='k',s=20)
plt.errorbar(0.0677497026*24,0.094,yerr=[[0.009],[0.016]],ls='none',color='k',capsize=3)
#plt.text(0.0677497026*24,0.094,'  SDSS 1152(GPs)',color='k',size=12)


plt.scatter(0.0627919557*24,0.0436,marker='o',color='g',s=20)
plt.errorbar(0.0627919557*24,0.0436,yerr=[[0.0017],[0.0025]],ls='none',color='g',capsize=3)
#plt.text(0.0627919557*24,0.0436,'  SDSS1057(GPs)',color='g',size=12)


plt.scatter(0.185912957*24,0.37,marker='o',color='g',s=20)
plt.errorbar(0.185912957*24,0.37,yerr=[[0.06],[0.06]],ls='none',color='g',capsize=3)
#plt.text(0.185912957*24,0.37,'  SDSS 1006(GPs)',color='g',size=12)


plt.scatter(0.1754424023*24,0.394,marker='o',color='g',s=20)
plt.errorbar(0.1754424023*24,0.394,yerr=[[0.022],[0.016]],ls='none',color='g',capsize=3)
#plt.text(0.1754424023*24,0.394,'  GY Cnc(GPs)',color='g',size=12)


plt.scatter(0.0854185080*24,0.176,marker='o',color='g',s=20)
plt.errorbar(0.0854185080*24,0.176,yerr=[[0.018],[0.007]],ls='none',color='g',capsize=3)
#plt.text(0.0854185080*24,0.176,'  V713 Cep(GPs)',color='g',size=12)


plt.scatter(0.0568412623*24,0.061,marker='o',color='k',s=20)
plt.errorbar(0.0568412623*24,0.061,yerr=[[0.003],[0.004]],ls='none',color='k',capsize=3)
#plt.text(0.0568412623*24,0.061,'  SDSS 1501(GPs)',color='k',size=12)


plt.scatter(0.0719308073*24,0.129,marker='o',color='orange',s=20)
plt.errorbar(0.0719308073*24,0.129,yerr=[[0.007],[0.008]],ls='none',color='orange',capsize=3)
#plt.text(0.0719308073*24,0.129,'  OGLE 82',color=orange',size=12)

plt.scatter(0.074326968*24,0.128,marker='o',color='orange',s=20)
plt.errorbar(0.074326968*24,0.128,yerr=[[0.008],[0.006]],ls='none',color='orange',capsize=3)
#plt.text(0.074326968*24,0.128,'  ASASSN-14hq(GPs)',color='orange',size=12)

plt.scatter(0.09328967*24,0.165,marker='o',color='orange',s=20)
plt.errorbar(0.09328967*24,0.165,yerr=[[0.015],[0.018]],ls='none',color='orange',capsize=3)
#plt.text(0.09328967*24,0.165,'  ASASSN-15pb(GPs)',color='orange',size=12)

plt.scatter(0.0715286*24,0.182,marker='o',color='orange',s=20)
plt.errorbar(0.0715286*24,0.182,yerr=[[0.024],[0.016]],ls='none',color='orange',capsize=3)
#plt.text(0.0715286*24,0.182,'  MASOT0014(GPs)',color='orange',size=12)

plt.scatter(0.07461448*24,0.102,marker='o',color='orange',s=20)
plt.errorbar(0.07461448*24,0.102,yerr=[[0.008],[0.009]],ls='none',color='orange',capsize=3)
#plt.text(0.07461448*24,0.102,'  AY For(GPs)',color='orange',size=12)

'''
plt.scatter(0.0583110901*24,0.095,marker='o',color='g',s=20)
plt.errorbar(0.0583110901*24,0.095,yerr=0.005,ls='none',color='g',capsize=3)
#plt.text(0.0583110901*24,0.095,'  SDSS0748',color='g',size=12)

plt.scatter(0.059073543*24,0.089,marker='o',color='g',s=20)
plt.errorbar(0.059073543*24,0.089,yerr=[[0.004],[0.005]],ls='none',color='g',capsize=3)
#plt.text(0.059073543*24,0.089,'      SDSS 0903',color='g',size=12)

plt.scatter(0.0570067*24,0.05198,marker='o',color='g',s=20)
plt.errorbar(0.0570067*24,0.05198,yerr=[[0.0017],[0.0029]],ls='none',color='g',capsize=3)
#plt.text(0.0570067*24,0.05198,'  SDSS 1035',color='g',size=12)

plt.scatter(0.054240679*24,0.0635,marker='o',color='g',s=20)
plt.errorbar(0.054240679*24,0.0635,yerr=[[0.0013],[0.0019]],ls='none',color='g',capsize=3)
#plt.text(0.054240679*24,0.0635,'  SDSS 1433',color='g',size=12)
'''

######### IN LITERATURE ################

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
#plt.scatter(0.209937*24,0.53,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.209937*24,0.53,yerr=0.01,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.209937*24,0.53,'  EX Dra',color='b',size=12,alpha=0.3)

# From Southworth09
#plt.scatter(0.185912957*24,0.40,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.185912957*24,0.40,yerr=0.10,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.185912957*24,0.40,'  SDSS 1006',color='b',size=12,alpha=0.3)

#From Littlefair14
plt.scatter(0.1653077*24,0.39,marker='o',color='k',s=20)
plt.errorbar(0.1653077*24,0.39,yerr=0.04,ls='none',color='k',capsize=3)
#plt.text(0.1653077*24,0.39,'  KIS J1927',color='k',size=12)

#From Copperwheat10
plt.scatter(0.1582061029*24,0.55,marker='o',color='k',s=20)
plt.errorbar(0.1582061029*24,0.55,yerr=0.02,ls='none',color='k',capsize=3)
#plt.text(0.1582061029*24,0.55,'  IP Peg',color='k',size=12)

#From Miszalski16 (Mass overestimated due to bug in code)
#plt.scatter(0.120971374*24,0.28,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,0.28,yerr=[[0.03],[0.03]],ls='none',color='k',capsize=3)
#plt.text(0.120971374*24,0.28,'  CSS111003',color='k',size=12)

#From Miszalski16 (Revised value from Stu)
#plt.scatter(0.120971374*24,,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,,yerr=[[],[]],ls='none',color='k',capsize=3)
#plt.text(0.120971374*24,,'  CSS111003',color='k',size=12)

#From Rodriguez-Gil15 (Eclipse modelling)
#plt.scatter(0.149207696*24,0.47,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.149207696*24,0.47,yerr=0.05,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.149207696*24,0.47,'  HS 0220+0603',color='b',size=12,alpha=0.3)

# OTHER - below gap

'''#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.198,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.088940717*24,0.198,yerr=[[0.029],[0.029]],ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.088940717*24,0.198,'  CTCV 1300',color='b',size=12,alpha=0.3)

#From Steeghs03 (timing)
#plt.scatter(0.0739089282*24,0.10,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0739089282*24,0.10,yerr=0.01,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0739089282*24,0.10,'  IY UMa',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
#plt.scatter(0.0744992631*24,0.125,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.125,yerr=0.014,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0744992631*24,0.125,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.083,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.083,yerr=0.003,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0744992631*24,0.083,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Wood&Horne90 (eclipse modelling)
#plt.scatter(0.0631209221*24,0.082,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.082,yerr=0.004,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0631209221*24,0.082,'  OY Car_H90',color='b',size=12,alpha=0.3)


#From Horne91 (eclipse modelling)
plt.scatter(0.0736471745*24,0.09,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.0736471745*24,0.09,yerr=0.02,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0736471745*24,0.09,' HT Cas ',color='b',size=12,alpha=0.3)

#From Baptista98 (timing)
plt.scatter(0.06242785751*24,0.15,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.06242785751*24,0.15,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.06242785751*24,0.15,'  V2051 Oph',color='b',size=12,alpha=0.3)

#From Steeghs07 (wd mass from gravitational redshift & q from RV)
plt.scatter(0.056688*24,0.078,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.056688*24,0.078,yerr=0.006,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.056688*24,0.078,'  WZ Sge',color='b',size=12,alpha=0.3)

#From Echevarria16 (RV)
plt.scatter(0.068233843*24,0.10,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.068233843*24,0.10,yerr=0.02,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.068233843*24,0.10,'  EX Hya',color='b',size=12,alpha=0.3)

#From Borges&Baptista05 (timing)
plt.scatter(0.0614296757*24,0.092,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.0614296757*24,0.092,yerr=0.016,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0614296757*24,0.092,'  V4140 Sgr',color='b',size=12,alpha=0.3)

#From Smith06 (wd mass from gravitational redshift & q from epsilon) -- don't use
#plt.scatter(0.074271*24,0.11,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.074271*24,0.11,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.074271*24,0.11,'  VW Hyi',color='b',size=12,alpha=0.3)

#From Yakin10 (RV & md from porb) -- don't use
#plt.scatter(0.070037*24,0.14,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.070037*24,0.14,yerr=0.02,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.070037*24,0.14,'  1RXS J180834.7+101041',color='b',size=12,alpha=0.3)

#From Mason&Howell05 (RV) (Error bars not given in paper) -- don't use
#plt.scatter(0.07460*24,0.17,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.07460*24,0.17,yerr=0.05,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.07460*24,0.17,'  AY For',color='b',size=12,alpha=0.3)
'''

# OTHER - above gap


'''#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.1754424023*24,0.33,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.1754424023*24,0.33,yerr=0.07,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.1754424023*24,0.33,'  GY Cnc',color='b',size=12,alpha=0.3)

#From Baptista00 (timing) 
#plt.scatter(0.209937*24,0.54,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.209937*24,0.54,yerr=0.10,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.209937*24,0.54,'  EX Dra',color='b',size=12,alpha=0.3)


#From Araujo-Betancour03 & Patterson05 (timing & q from epsilon)
plt.scatter(0.136606499*24,0.21,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.136606499*24,0.21,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.136606499*24,0.21,'  DW UMa',color='b',size=12,alpha=0.3)

#From Baptista04 (timing)
plt.scatter(0.163580429*24,0.20,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.163580429*24,0.20,yerr=0.07,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.163580429*24,0.20,'  UU Aqr',color='b',size=12,alpha=0.3)

#From Echevarria07 (RV)
plt.scatter(0.176906*24,0.42,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.176906*24,0.42,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.176906*24,0.42,'  U Gem',color='b',size=12,alpha=0.3)

#From Horne93 (RV)
plt.scatter(0.1936209*24,0.40,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.1936209*24,0.40,yerr=0.05,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.1936209*24,0.40,'  DQ Her',color='b',size=12,alpha=0.3)

#From Thoroughgood05 (RV)
plt.scatter(0.231936060*24,0.52,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.231936060*24,0.52,yerr=0.06,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.231936060*24,0.52,'  V347 Pup',color='b',size=12,alpha=0.3)

#From HernandezSantisteban17 (RV)
plt.scatter(0.26937446*24,0.78,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.26937446*24,0.78,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.26937446*24,0.78,'  1RXS J064434.5+334451',color='b',size=12,alpha=0.3)

'''

mwd_k11 = 0.75
# Values from MwdvsP_curr.py
mwd_new = 0.808
mwd_new_err = 0.019
mwd_int_dis = 0.12

ep_q_intercept_k06 = 0.114
ep_q_intercept_k06_err = 0.005
ep_q_gradient_k06 = 3.97
ep_q_gradient_k06_err = 0.41
# Values from epsilon-q_relation.py
ep_q_intercept_b = 0.120
#ep_q_intercept_b = 0.114
ep_q_intercept_b_err = 0.003
ep_q_gradient_b = 4.3
ep_q_gradient_b_err = 0.3
ep_q_int_dis_b = 0.013
ep_q_intercept_c = 0.137
#ep_q_intercept_c = 0.114
ep_q_intercept_c_err = 0.004
ep_q_gradient_c = 4.7
ep_q_gradient_c_err = 0.5
ep_q_int_dis_c = 0.012

#apply a shift to m2 values from P05+Knigge06 (method 1)
p_orb = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [0])
m2_sh = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [1])
m2_err_sh = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [2])
r2_sh = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [3])
r2_err_sh = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [4])
ep_sh = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [5])
ep_err_sh = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [6])
mwd_pat = np.loadtxt('superhumpers_p05.dat',dtype=float,usecols = [7])

m2_sh_shift = mwd_new*((m2_sh/mwd_k11)+(ep_q_intercept_b-ep_q_intercept_k06))
#m2_sh_shift = mwd_new*((m2_sh/mwd_k11)+(ep_q_intercept_c-ep_q_intercept_k06))
#m2_optimal_shift = mwd_new*((m2_optimal/mwd_k11)+(ep_q_intercept_new-ep_q_intercept_k06))

#calculate new q from just porb and psh from Kato papers (method 2)
p_orb_b = np.loadtxt('superhumpers_kato_b.dat',dtype=float,usecols = [0])
p_orb_b_err = np.loadtxt('superhumpers_kato_b.dat',dtype=float,usecols = [1])
p_sh_b = np.loadtxt('superhumpers_kato_b.dat',dtype=float,usecols = [2])
p_sh_b_err = np.loadtxt('superhumpers_kato_b.dat',dtype=float,usecols = [3])

p_orb_c = np.loadtxt('superhumpers_kato_c.dat',dtype=float,usecols = [0])
p_orb_c_err = np.loadtxt('superhumpers_kato_c.dat',dtype=float,usecols = [1])
p_sh_c = np.loadtxt('superhumpers_kato_c.dat',dtype=float,usecols = [2])
p_sh_c_err = np.loadtxt('superhumpers_kato_c.dat',dtype=float,usecols = [3])

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

'''
for i in range(len(p_orb)):
    #plt.scatter(p_orb[i],m2_sh_shift[i],marker='o',color='k',s=20,alpha=0.2)
    #plt.errorbar(p_orb[i],m2_sh_shift[i],yerr=m2_err_sh[i],ls='none',color='k',capsize=3,alpha=0.15)
    #plt.scatter(p_orb[i],m2_new[i],marker='o',color='k',s=20,alpha=0.2)
    #plt.errorbar(p_orb[i],m2_new[i],yerr=m2_err_sh[i],ls='none',color='k',capsize=3,alpha=0.15)
   
    plt.scatter(p_orb[i],m2_pat[i],marker='o',color='k',s=20,alpha=0.2)
    plt.errorbar(p_orb[i],m2_pat[i],yerr=m2_pat_err[i],ls='none',color='k',capsize=3,alpha=0.15)

for i in range(len(p_orb_b)):   
    plt.scatter(p_orb_b[i]*24,m2_b[i],marker='o',color='k',s=20,alpha=0.2)
    plt.errorbar(p_orb_b[i]*24,m2_b[i],yerr=m2_b_err[i],ls='none',color='k',capsize=3,alpha=0.15)
    
for i in range(len(p_orb_c)):  
    plt.scatter(p_orb_c[i]*24,m2_c[i],marker='o',color='k',s=20,alpha=0.2)
    plt.errorbar(p_orb_c[i]*24,m2_c[i],yerr=m2_c_err[i],ls='none',color='k',capsize=3,alpha=0.15)
'''

#plt.plot(P_optimal*1.064,m2_optimal*1.1,c='r',linewidth=1) # m=0.22
#plt.plot(P_optimal*1.048,m2_optimal*1.075,c='r',linewidth=1) # m=0.215
#plt.plot(P_optimal*1.032,m2_optimal*1.05,c='r',linewidth=1) # m=0.21
#plt.plot(P_optimal*1.016,m2_optimal*1.025,c='r',linewidth=1) # m=0.205
#plt.plot(P_standard*1.016,m2_standard*1.025,c='k',linewidth=1) # m=0.205
#plt.plot(P_optimal*0.983,m2_optimal*0.975,c='r',linewidth=1) # m=0.195
#plt.plot(P_standard*0.983,m2_standard*0.975,c='k',linewidth=1) # m=0.195
#plt.plot(P_optimal*0.982,m2_optimal*1.07,c='r',linewidth=1)
plt.plot(P_optimal,m2_optimal,c='r',linewidth=1)#,linestyle='dashed',alpha=0.5)
#plt.plot(P_standard+(0.3/P_standard**5),m2_standard,c='k',linewidth=1,linestyle='dashed')
#plt.plot(P_standard,m2_standard,c='k',linewidth=1)
#plt.plot(P_BD_1,m2_BD_1,c='b',linewidth=1)
#plt.plot(P_BD_2,m2_BD_2,c='b',linestyle='--',linewidth=1)
#plt.plot(P_BD_3,m2_BD_3,c='b',linestyle='-.',linewidth=1)
#plt.plot(P_BD_4,m2_BD_4,c='b',linestyle=':',linewidth=1)
#plt.plot(P_evol_12,m2_evol_12,c='g',linewidth=1)
#plt.plot(P_evol_15,m2_evol_15,c='g',linestyle='dashed')
plt.xlabel(r'P$_{\rm orb}$ (hrs)', fontsize=15)
plt.ylabel(r'M$_{\rm d}$ (M$_{\odot}$)', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15, width=1.0)
#plt.axvline(1.3626,linestyle='dashed',color='k',linewidth=1,alpha=0.5)
#plt.axvspan(1.3476,1.3776,color='k',alpha=0.1)
#plt.errorbar(1.373,0.035,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1,alpha=0.5)
#plt.errorbar(1.373,0.061,xerr=0.048,ls='none',color='r',capsize=5,linewidth=1,alpha=0.5)
#plt.errorbar(1.373,0.106,xerr=0.048,ls='none',color='k',capsize=5,linewidth=1,alpha=0.5)
#plt.axvline(1.373,linestyle='dashed',color='gray')

plt.subplots_adjust(bottom=0.1, top=0.95, left=0.1, right=0.95)
for axis in ['top','bottom','left','right']:
 plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.savefig("m2vsP_curr_gps.pdf")
plt.show()
