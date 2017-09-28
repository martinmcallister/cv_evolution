import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn

#input donor mass and period for system
'''m2,m2_err = raw_input("Donor mass and error in solar masses: ").split()
m2 = float(m2)
m2_err = float(m2_err)

P = raw_input("System period in days: ")
P = float(P)*24'''

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
#plt.axis([1.2,2.3001,0,0.21001])
plt.axis([1.0,1.7,0.02,0.12])


'''fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([1.0, 7.0])
ax.set_xticks([1,2,3,4,5,6,7])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_yscale('log')
ax.set_ylim([0.03, 0.9])
ax.set_yticks([0.04,0.06,0.08,0.2,0.4,0.6,0.8])
ax.get_yaxis().set_major_formatter(ScalarFormatter())'''

#plt.scatter(P,m2,marker='o',color='k',s=20)
#plt.errorbar(P,m2,yerr=m2_err,ls='none',color='k',capsize=None)

plt.scatter(0.0529848884*24,0.064,marker='o',color='k',s=15)
plt.errorbar(0.0529848884*24,0.064,yerr=0.006,ls='none',color='k',capsize=None,linewidth=1)
plt.text(0.0529848884*24,0.065,'  PHL 1445',color='k',size=10)

#(6 ecl fit)
#plt.scatter(0.0529848884*24,0.061,marker='o',color='k',s=15)
#plt.errorbar(0.0529848884*24,0.061,yerr=[[0.008],[0.005]],ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0529848884*24,0.062,'  PHL 1445 (GPs)',color='k',size=10)

#(10 ecl fit)
#plt.scatter(0.0529848884*24,0.071,marker='o',color='g',s=15)
#plt.errorbar(0.0529848884*24,0.071,yerr=[[0.005],[0.009]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0529848884*24,0.071,'  PHL 1445 (GPs)',color='g',size=10)



############ DONE (with GPs) ##############


#plt.scatter(0.060310649*24,0.093,marker='o',color='g',s=20)
#plt.errorbar(0.060310649*24,0.093,yerr=[[0.012],[0.015]],ls='none',color='g',capsize=None)
#plt.text(0.060310649*24,0.095,'  ASASSN-14ag(GPs)',color='g',size=12)


#plt.scatter(0.0739089282*24,0.131,marker='o',color='g',s=20)
#plt.errorbar(0.0739089282*24,0.131,yerr=[[0.006],[0.008]],ls='none',color='g',capsize=None)
#plt.text(0.0739089282*24,0.131,'  IY UMa(GPs)',color='g',size=12)

#plt.scatter(0.0739089282*24,0.132,marker='o',color='g',s=20)
#plt.errorbar(0.0739089282*24,0.132,yerr=[[0.015],[0.005]],ls='none',color='g',capsize=None)
#plt.text(0.0739089282*24,0.132,'  IY UMa_kg5(GPs)',color='g',size=12)


#plt.scatter(0.0744992631*24,0.134,marker='o',color='g',s=20)
#plt.errorbar(0.0744992631*24,0.134,yerr=[[0.006],[0.004]],ls='none',color='g',capsize=None)
#plt.text(0.0744992631*24,0.135,'  Z Cha(GPs)',color='g',size=12)

#plt.scatter(0.0744992631*24,0.130,marker='o',color='g',s=20)
#plt.errorbar(0.0744992631*24,0.130,yerr=[[0.002],[0.015]],ls='none',color='g',capsize=None)
#plt.text(0.0744992631*24,0.130,'  Z Cha_g(GPs)',color='g',size=12)


#plt.scatter(0.059578970*24,0.079,marker='o',color='g',s=20)
#plt.errorbar(0.059578970*24,0.079,yerr=[[0.003],[0.007]],ls='none',color='g',capsize=None)
#plt.text(0.059578970*24,0.079,'  CSS080623(GPs)',color='g',size=12)


#plt.scatter(0.0778805320*24,0.133,marker='o',color='g',s=20)
#plt.errorbar(0.0778805320*24,0.133,yerr=[[0.005],[0.015]],ls='none',color='g',capsize=None)
#plt.text(0.0778805320*24,0.133,'  SDSS 0901(GPs)',color='g',size=12)


#plt.scatter(0.0858526521*24,0.172,marker='o',color='g',s=20)
#plt.errorbar(0.0858526521*24,0.172,yerr=[[0.013],[0.012]],ls='none',color='g',capsize=None)
#plt.text(0.0858526521*24,0.172,'  DV UMa(GPs)',color='g',size=12)

#plt.scatter(0.0858526521*24,0.173,marker='o',color='g',s=20)
#plt.errorbar(0.0858526521*24,0.173,yerr=[[0.010],[0.012]],ls='none',color='g',capsize=None)
#plt.text(0.0858526521*24,0.173,'  DV UMa_g(GPs)',color='g',size=12)


#plt.scatter(0.088940717*24,0.166,marker='o',color='g',s=20)
#plt.errorbar(0.088940717*24,0.166,yerr=[[0.005],[0.010]],ls='none',color='g',capsize=None)
#plt.text(0.088940717*24,0.166,'  CTCV 1300(GPs)',color='g',size=12)

#plt.scatter(0.088940717*24,0.168,marker='o',color='g',s=20)
#plt.errorbar(0.088940717*24,0.168,yerr=[[0.007],[0.009]],ls='none',color='g',capsize=None)
#plt.text(0.088940717*24,0.168,'  CTCV 1300_g(GPs)',color='g',size=12)


#plt.scatter(0.0631209221*24,0.093,marker='o',color='g',s=20)
#plt.errorbar(0.0631209221*24,0.093,yerr=[[0.006],[0.003]],ls='none',color='g',capsize=None)
#plt.text(0.0631209221*24,0.093,'  OY Car(GPs)',color='g',size=12)

#plt.scatter(0.0631209221*24,0.086,marker='o',color='g',s=20)
#plt.errorbar(0.0631209221*24,0.086,yerr=[[0.006],[0.006]],ls='none',color='g',capsize=None)
#plt.text(0.0631209221*24,0.086,'  OY Car_g(GPs)',color='g',size=12)


#plt.scatter(0.065769292*24,0.126,marker='o',color='g',s=20)
#plt.errorbar(0.065769292*24,0.126,yerr=[[0.005],[0.011]],ls='none',color='g',capsize=None)
#plt.text(0.065769292*24,0.126,'  SSS130413(GPs)',color='g',size=12)


#plt.scatter(0.0660508707*24,0.096,marker='o',color='g',s=20)
#plt.errorbar(0.0660508707*24,0.096,yerr=[[0.010],[0.006]],ls='none',color='g',capsize=None)
#plt.text(0.0660508707*24,0.096,'  CSS110113(GPs)',color='g',size=12)


#plt.scatter(0.0587045*24,0.086,marker='o',color='g',s=20)
#plt.errorbar(0.0587045*24,0.086,yerr=[[0.004],[0.004]],ls='none',color='g',capsize=None)
#plt.text(0.0587045*24,0.086,'  SSS100615(GPs)',color='g',size=12)


#plt.scatter(0.0677497026*24,0.092,marker='o',color='g',s=20)
#plt.errorbar(0.0677497026*24,0.092,yerr=[[0.011],[0.018]],ls='none',color='g',capsize=None)
#plt.text(0.0677497026*24,0.092,'  SDSS 1152(GPs)',color='g',size=12)


#plt.scatter(0.0627919557*24,0.0436,marker='o',color='g',s=20)
#plt.errorbar(0.0627919557*24,0.0436,yerr=[[0.0017],[0.0025]],ls='none',color='g',capsize=None)
#plt.text(0.0627919557*24,0.0436,'  SDSS1057',color='g',size=12)


#plt.scatter(0.185912957*24,0.42,marker='o',color='g',s=20)
#plt.errorbar(0.185912957*24,0.42,yerr=[[0.06],[0.09]],ls='none',color='g',capsize=None)
#plt.text(0.185912957*24,0.42,'  SDSS 1006(GPs)',color='g',size=12)


#plt.scatter(0.1754424023*24,0.350,marker='o',color='g',s=20)
#plt.errorbar(0.1754424023*24,0.350,yerr=[[0.031],[0.025]],ls='none',color='g',capsize=None)
#plt.text(0.1754424023*24,0.350,'  GY Cnc(GPs)',color='g',size=12)


#plt.scatter(0.0854185080*24,0.168,marker='o',color='g',s=20)
#plt.errorbar(0.0854185080*24,0.168,yerr=[[0.003],[0.032]],ls='none',color='g',capsize=None)
#plt.text(0.0854185080*24,0.168,'  V713 Cep(GPs)',color='g',size=12)


#plt.scatter(0.0568412623*24,0.061,marker='o',color='g',s=20)
#plt.errorbar(0.0568412623*24,0.061,yerr=[[0.002],[0.006]],ls='none',color='g',capsize=None)
#plt.text(0.0568412623*24,0.061,'  SDSS 1501(GPs)',color='g',size=12)


'''plt.scatter(0.0719308073*24,0.129,marker='o',color='g',s=20)
plt.errorbar(0.0719308073*24,0.129,yerr=[[0.007],[0.008]],ls='none',color='g',capsize=None)
plt.text(0.0719308073*24,0.129,'  OGLE 82',color='g',size=12)

plt.scatter(0.0932914*24,0.155,marker='o',color='g',s=20)
plt.errorbar(0.0932914*24,0.155,yerr=[[0.014],[0.026]],ls='none',color='g',capsize=None)
plt.text(0.0932914*24,0.155,'  ASASSN-15pb(GPs)',color='g',size=12)

plt.scatter(0.0715286*24,0.182,marker='o',color='g',s=20)
plt.errorbar(0.0715286*24,0.182,yerr=[[0.024],[0.016]],ls='none',color='g',capsize=None)
plt.text(0.0715286*24,0.182,'  MASOT0014(GPs)',color='g',size=12)'''



######### IN LITERATURE ################

# HIGH_TIME RESOLUTION ECLIPSE MODELLING (Last 15 years)

#plt.scatter(0.059578970*24,0.098,marker='o',color='k',s=20,alpha=0.25)
#plt.errorbar(0.059578970*24,0.098,yerr=0.003,ls='none',color='k',capsize=None,alpha=0.25)
#plt.text(0.059578970*24,0.095,'  CSS080623',color='k',size=12,alpha=0.25)

#plt.scatter(0.0778805320*24,0.161,marker='o',color='k',s=20,alpha=0.25)
#plt.errorbar(0.0778805320*24,0.161,yerr=0.007,ls='none',color='k',capsize=None,alpha=0.25)
#plt.text(0.0778805320*24,0.162,'  SDSS 0901',color='k',size=12,alpha=0.25)

#plt.scatter(0.088940717*24,0.177,marker='o',color='k',s=20)
#plt.errorbar(0.088940717*24,0.177,yerr=0.021,ls='none',color='k',capsize=None)
#plt.text(0.088940717*24,0.177,'  CTCV J1300-3052',color='k',size=12)

#plt.scatter(0.0677497026*24,0.087,marker='o',color='k',s=20)
#plt.errorbar(0.0677497026*24,0.087,yerr=0.006,ls='none',color='k',capsize=None)
#plt.text(0.0677497026*24,0.087,'  SDSS 1152',color='k',size=12)

#plt.scatter(0.0858526521*24,0.196,marker='o',color='k',s=20)
#plt.errorbar(0.0858526521*24,0.196,yerr=0.005,ls='none',color='k',capsize=None)
#plt.text(0.0858526521*24,0.196,'  DV UMa',color='k',size=12)

#plt.scatter(0.0568412623*24,0.077,marker='o',color='k',s=20)
#plt.errorbar(0.0568412623*24,0.077,yerr=0.010,ls='none',color='k',capsize=None)
#plt.text(0.0568412623*24,0.074,'  SDSS 1501',color='k',size=12)

plt.scatter(0.054240679*24,0.0571,marker='o',color='k',s=15)
plt.errorbar(0.054240679*24,0.0571,yerr=0.0007,ls='none',color='k',capsize=None,linewidth=1)
plt.text(0.054240679*24,0.0570,'  SDSS\n  1433',color='k',size=10)

#plt.scatter(0.054240679*24,0.0635,marker='o',color='g',s=20)
#plt.errorbar(0.054240679*24,0.0635,yerr=[[0.0013],[0.0019]],ls='none',color='g',capsize=None)
#plt.text(0.054240679*24,0.0635,'  SDSS 1433',color='g',size=12)

plt.scatter(0.04625828*24,0.0575,marker='o',color='k',s=15)
plt.errorbar(0.04625828*24,0.0575,yerr=0.002,ls='none',color='k',capsize=None,linewidth=1)
plt.text(0.04625828*24,0.0510,'  SDSS\n  1507',color='k',size=10)

plt.scatter(0.0570067*24,0.0475,marker='o',color='k',s=15)
plt.errorbar(0.0570067*24,0.0475,yerr=0.0012,ls='none',color='k',capsize=None,linewidth=1)
plt.text(0.0570067*24,0.0410,'  SDSS\n  1035',color='k',size=10)

#plt.scatter(0.0570067*24,0.05198,marker='o',color='g',s=20)
#plt.errorbar(0.0570067*24,0.05198,yerr=[[0.0017],[0.0029]],ls='none',color='g',capsize=None)
#plt.text(0.0570067*24,0.05198,'  SDSS 1035',color='g',size=12)

#plt.scatter(0.065550270*24,0.101,marker='o',color='k',s=20)
#plt.errorbar(0.065550270*24,0.101,yerr=0.003,ls='none',color='k',capsize=None)
#plt.text(0.065550270*24,0.103,' CTCV J2354-4700',color='k',size=12)

#plt.scatter(0.059073543*24,0.099,marker='o',color='k',s=20)
#plt.errorbar(0.059073543*24,0.099,yerr=0.004,ls='none',color='k',capsize=None)
#plt.text(0.059073543*24,0.098,'      SDSS 0903',color='k',size=12)

#plt.scatter(0.059073543*24,0.089,marker='o',color='g',s=20)
#plt.errorbar(0.059073543*24,0.089,yerr=[[0.004],[0.005]],ls='none',color='g',capsize=None)
#plt.text(0.059073543*24,0.089,'      SDSS 0903',color='g',size=12)

#plt.scatter(0.062959041*24,0.0889,marker='o',color='k',s=20)
#plt.errorbar(0.062959041*24,0.0889,yerr=0.0025,ls='none',color='k',capsize=None)
#plt.text(0.062959041*24,0.0889,'  SDSS 1227',color='k',size=12)

#plt.scatter(0.061159491*24,0.091,marker='o',color='k',s=20)
#plt.errorbar(0.061159491*24,0.091,yerr=0.004,ls='none',color='k',capsize=None)
#plt.text(0.061159491*24,0.092,'  XZ Eri',color='k',size=12)

#plt.scatter(0.05890961*24,0.0781,marker='o',color='k',s=20)
#plt.errorbar(0.05890961*24,0.0781,yerr=0.0008,ls='none',color='k',capsize=None)
#plt.text(0.05890961*24,0.0781,'  SDSS 1502',color='k',size=12)

#plt.scatter(0.072706113*24,0.1157,marker='o',color='k',s=20)
#plt.errorbar(0.072706113*24,0.1157,yerr=0.0022,ls='none',color='k',capsize=None)
#plt.text(0.072706113*24,0.1157,'  OU Vir',color='k',size=12)

#plt.scatter(0.10008215*24,0.223,marker='o',color='k',s=20)
#plt.errorbar(0.10008215*24,0.223,yerr=0.010,ls='none',color='k',capsize=None)
#plt.text(0.10008215*24,0.223,'  SDSS 1702',color='k',size=12)

#From Littlefair08
#plt.scatter(0.063121*24,0.086,marker='o',color='k',s=20)
#plt.errorbar(0.063121*24,0.086,yerr=0.005,ls='none',color='k',capsize=None)
#plt.text(0.063121*24,0.086,'  OY Car',color='k',size=12)

#From Shafter03
#plt.scatter(0.209937*24,0.53,marker='o',color='b',s=20)
#plt.errorbar(0.209937*24,0.53,yerr=0.01,ls='none',color='b',capsize=None)
#plt.text(0.209937*24,0.53,'  EX Dra',color='b',size=12)

# From Southworth09
#plt.scatter(0.185912957*24,0.40,marker='o',color='b',s=20)
#plt.errorbar(0.185912957*24,0.40,yerr=0.10,ls='none',color='b',capsize=None)
#plt.text(0.185912957*24,0.40,'  SDSS 1006',color='b',size=12)

#From Littlefair14
#plt.scatter(0.1653077*24,0.39,marker='o',color='k',s=20)
#plt.errorbar(0.1653077*24,0.39,yerr=0.04,ls='none',color='k',capsize=None)
#plt.text(0.1653077*24,0.39,'  KIS J1927',color='k',size=12)

#From Copperwheat10
#plt.scatter(0.1582061029*24,0.55,marker='o',color='b',s=20)
#plt.errorbar(0.1582061029*24,0.55,yerr=0.02,ls='none',color='b',capsize=None)
#plt.text(0.1582061029*24,0.55,'  IP Peg',color='b',size=12)

#From Miszalski16 (Mass overestimated due to bug in code)
#plt.scatter(0.120971374*24,0.28,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,0.28,yerr=[[0.03],[0.03]],ls='none',color='k',capsize=None)
#plt.text(0.120971374*24,0.28,'  CSS111003',color='k',size=12)

#From Miszalski16 (Revised value from Stu)
#plt.scatter(0.120971374*24,,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,,yerr=[[],[]],ls='none',color='k',capsize=None)
#plt.text(0.120971374*24,,'  CSS111003',color='k',size=12)

#From Rodriguez-Gil15 (Eclipse modelling - polar)
#plt.scatter(0.149207696*24,0.47,marker='o',color='b',s=20)
#plt.errorbar(0.149207696*24,0.47,yerr=0.05,ls='none',color='b',capsize=None)
#plt.text(0.149207696*24,0.47,'  HS 0220+0603',color='b',size=12)

# OTHER

#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.198,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.088940717*24,0.198,yerr=[[0.029],[0.029]],ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.088940717*24,0.198,'  CTCV 1300',color='b',size=12,alpha=0.5)

#From Steeghs03 (timing)
#plt.scatter(0.0739089282*24,0.10,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0739089282*24,0.10,yerr=0.01,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0739089282*24,0.10,'  IY UMa',color='b',size=12,alpha=0.5)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.1754424023*24,0.33,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.1754424023*24,0.33,yerr=0.07,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.1754424023*24,0.33,'  GY Cnc',color='b',size=12,alpha=0.5)

#From Smak07 (RV/timing)  
#plt.scatter(0.0744992631*24,0.186,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.186,yerr=0.030,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0744992631*24,0.186,'  Z Cha_S07',color='b',size=12,alpha=0.5)

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
#plt.scatter(0.0744992631*24,0.125,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.125,yerr=0.014,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0744992631*24,0.125,'  Z Cha_WH88',color='b',size=12,alpha=0.5)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.083,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.083,yerr=0.003,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0744992631*24,0.083,'  Z Cha_W86',color='b',size=12,alpha=0.5)

#From Horne91 (eclipse modelling)
#plt.scatter(0.0736471745*24,0.09,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0736471745*24,0.09,yerr=0.02,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0736471745*24,0.09,' HT Cas ',color='b',size=12,alpha=0.5)

#From Wood&Horne90 (eclipse modelling)
#plt.scatter(0.0631209221*24,0.082,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0631209221*24,0.082,yerr=0.004,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0631209221*24,0.082,'  OY Car_H91',color='b',size=12,alpha=0.5)

#From Baptista98 (timing)
#plt.scatter(0.06242785751*24,0.15,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.06242785751*24,0.15,yerr=0.03,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.06242785751*24,0.15,'  V2051 Oph',color='b',size=12,alpha=0.5)

#From Steeghs07 (wd mass from gravitational redshift & q from RV)
#plt.scatter(0.056688*24,0.078,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.056688*24,0.078,yerr=0.006,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.056688*24,0.078,'  WZ Sge',color='b',size=12,alpha=0.5)

#From Echevarria16 (RV)
#plt.scatter(0.068233843*24,0.10,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.068233843*24,0.10,yerr=0.02,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.068233843*24,0.10,'  EX Hya',color='b',size=12,alpha=0.5)

#From Echevarria07 (RV)
#plt.scatter(0.176906*24,0.42,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.176906*24,0.42,yerr=0.04,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.176906*24,0.42,'  U Gem',color='b',size=12,alpha=0.5)

#From Smith06 (wd mass from gravitational redshift & q from superhump excess)
#plt.scatter(0.074271*24,0.11,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.074271*24,0.11,yerr=0.03,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.074271*24,0.11,'  VW Hyi',color='b',size=12,alpha=0.5)

#From Horne93 (RV)
#plt.scatter(0.1936209*24,0.40,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.1936209*24,0.40,yerr=0.05,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.1936209*24,0.40,'  DQ Her',color='b',size=12,alpha=0.5)

#From Thoroughgood05 (RV)
#plt.scatter(0.231936060*24,0.52,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.231936060*24,0.52,yerr=0.06,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.231936060*24,0.52,'  V347 Pup',color='b',size=12,alpha=0.5)

#From Borges&Baptista98 (timing)
#plt.scatter(0.0614296757*24,0.092,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0614296757*24,0.092,yerr=0.016,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.0614296757*24,0.092,'  V4140 Sgr',color='b',size=12,alpha=0.5)

#From HernandezSantisteban16 (RV)
#plt.scatter(0.26937446*24,0.78,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.26937446*24,0.78,yerr=0.04,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.26937446*24,0.78,'  1RXS J064434.5+334451',color='b',size=12,alpha=0.5)

#From Yakin10 (RV)
#plt.scatter(0.070037*24,0.14,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.070037*24,0.14,yerr=0.02,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.070037*24,0.14,'  1RXS J180834.7+101041',color='b',size=12,alpha=0.5)

#From Baptista00 (timing) 
#plt.scatter(0.209937*24,0.54,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.209937*24,0.54,yerr=0.10,ls='none',color='b',capsize=None,alpha=0.5)
#plt.text(0.209937*24,0.54,'  EX Dra',color='b',size=12,alpha=0.5)



plt.plot(P_optimal,m2_optimal,c='r',linewidth=1.5)
#plt.plot(P_standard,m2_standard,c='r',linestyle='dashed')
plt.plot(P_BD_1,m2_BD_1,c='b',linewidth=1.5)
plt.plot(P_BD_2,m2_BD_2,c='b',linestyle='--',linewidth=1.5)
plt.plot(P_BD_3,m2_BD_3,c='b',linestyle='-.',linewidth=1.5)
plt.plot(P_BD_4,m2_BD_4,c='b',linestyle=':',linewidth=1.5)
plt.plot(P_evol_12,m2_evol_12,c='g',linewidth=1.5)
#plt.plot(P_evol_15,m2_evol_15,c='g',linestyle='dashed')
plt.xlabel(r'$P_{\rm orb}\ (\rm hrs)$', fontsize=16)
plt.ylabel(r'$M_{\rm 2}\ (\rm{M}_{\odot})$', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15, width=1.0)
plt.axvline(1.363,linestyle='dashed',color='k',linewidth=1.5,alpha=0.3)
plt.axvspan(1.348,1.378,color='k',alpha=0.05)
#plt.scatter(1.373,0.1175,marker='o',color='w',s=25)
#plt.errorbar(1.373,0.025,xerr=0.048,ls='none',color='k',linewidth=2)
#plt.errorbar(1.373,0.061,xerr=0.048,ls='none',color='k',linewidth=2)
#plt.errorbar(1.373,0.121,xerr=0.048,ls='none',color='k',linewidth=2)
#plt.errorbar(1.373,0.098,xerr=0.062,ls='none',color='k',linewidth=2)
#plt.errorbar(1.373,0.098,xerr=0.033,ls='none',color='k',linewidth=2)
#plt.axvline(1.373,linestyle='dashed',color='gray')

plt.arrow(1.373,0.025,0.0475,0,width=0.0003,head_width=0.002,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09
plt.arrow(1.373,0.025,-0.0475,0,width=0.0003,head_width=0.002,head_length=0.0002,color='k',linewidth=0.5,alpha=0.8) #G09

plt.subplots_adjust(bottom=0.11, top=0.98, left=0.10, right=0.98)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("m2vsP_phl1445.pdf")
plt.show()
