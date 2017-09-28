import numpy as np
import matplotlib.pyplot as plt

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

plt.rcParams['xtick.major.pad']='15'
plt.rcParams['ytick.major.pad']='10'

#plt.scatter(P,m2,marker='o',color='k',s=20)
#plt.errorbar(P,m2,yerr=m2_err,ls='none',color='k',capsize=3)



#plt.scatter(0.0739089282*24,0.10,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0739089282*24,0.10,yerr=0.01,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0739089282*24,0.10,'  IY UMa(Steeghs03)',color='b',size=12,alpha=0.5)

#plt.scatter(0.0739089282*24,0.138,marker='o',color='g',s=20)
#plt.errorbar(0.0739089282*24,0.138,yerr=[[0.007],[0.008]],ls='none',color='g',capsize=3)
#plt.text(0.0739089282*24,0.138,'  IY UMa_kg5(ave_GPs)',color='g',size=12)

#plt.scatter(0.0739089282*24,0.143,marker='o',color='r',s=20)
#plt.errorbar(0.0739089282*24,0.143,yerr=[[0.003],[0.008]],ls='none',color='r',capsize=3)
#plt.text(0.0739089282*24,0.143,'  IY UMa_kg5(ave_noGPs)',color='r',size=12)

#plt.scatter(0.0739089282*24,0.132,marker='o',color='g',s=20)
#plt.errorbar(0.0739089282*24,0.132,yerr=[[0.015],[0.005]],ls='none',color='g',capsize=3)
#plt.text(0.0739089282*24,0.132,'  IY UMa_kg5(ind_GPs)',color='g',size=12)#

#plt.scatter(0.0739089282*24,0.149,marker='o',color='r',s=20)
#plt.errorbar(0.0739089282*24,0.149,yerr=[[0.004],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0739089282*24,0.149,'  IY UMa_kg5(ind_noGPs)',color='r',size=12)

plt.scatter(0.0739089282*24,0.120,marker='o',color='g',s=20)
plt.errorbar(0.0739089282*24,0.120,yerr=[[0.008],[0.008]],ls='none',color='g',capsize=3)
plt.text(0.0739089282*24,0.120,'  IY UMa(GPs)',color='g',size=12)

#plt.scatter(0.0739089282*24,0.150,marker='o',color='r',s=20)
#plt.errorbar(0.0739089282*24,0.150,yerr=[[0.004],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0739089282*24,0.150,'  IY UMa(noGPs)',color='r',size=12)



#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.083,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.083,yerr=0.003,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0744992631*24,0.083,'  Z Cha(Wood86)',color='b',size=12,alpha=0.5)

#From Wood&Horne90
#plt.scatter(0.0744992631*24,0.099,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0744992631*24,0.099,yerr=0.007,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0744992631*24,0.095,'  Z Cha(WH90)',color='b',size=12,alpha=0.5)

#plt.scatter(0.0744992631*24,0.1551,marker='o',color='r',s=20)
#plt.errorbar(0.0744992631*24,0.1551,yerr=[[0.0019],[0.0011]],ls='none',color='r',capsize=3)
#plt.text(0.0744992631*24,0.1551,'  Z Cha_g(noGPs)',color='r',size=12)

#plt.scatter(0.0744992631*24,0.130,marker='o',color='g',s=20)
#plt.errorbar(0.0744992631*24,0.130,yerr=[[0.002],[0.015]],ls='none',color='g',capsize=3)
#plt.text(0.0744992631*24,0.130,'  Z Cha_g(GPs)',color='g',size=12)

#plt.scatter(0.0744992631*24,0.1416,marker='o',color='r',s=20)
#plt.errorbar(0.0744992631*24,0.1416,yerr=[[0.0009],[0.0013]],ls='none',color='r',capsize=3)
#plt.text(0.0744992631*24,0.1416,'  Z Cha(noGPs)',color='r',size=12)

plt.scatter(0.0744992631*24,0.127,marker='o',color='g',s=20)
plt.errorbar(0.0744992631*24,0.127,yerr=[[0.003],[0.006]],ls='none',color='g',capsize=3)
plt.text(0.0744992631*24,0.131,'  Z Cha(GPs)',color='g',size=12)



#plt.scatter(0.059578970*24,0.101,marker='o',color='r',s=20)
#plt.errorbar(0.059578970*24,0.101,yerr=[[0.004],[0.007]],ls='none',color='r',capsize=3)
#plt.text(0.059578970*24,0.101,'  CSS080623(noGPs)',color='r',size=12)

plt.scatter(0.059578970*24,0.085,marker='o',color='g',s=20)
plt.errorbar(0.059578970*24,0.085,yerr=[[0.005],[0.005]],ls='none',color='g',capsize=3)
plt.text(0.059578970*24,0.076,'  CSS080623(GPs)',color='g',size=12)

#plt.scatter(0.059578970*24,0.099,marker='o',color='r',s=20)
#plt.errorbar(0.059578970*24,0.099,yerr=[[0.006],[0.007]],ls='none',color='r',capsize=3)
#plt.text(0.059578970*24,0.099,'  CSS080623_g(noGPs)',color='r',size=12)

#plt.scatter(0.059578970*24,0.084,marker='o',color='g',s=20)
#plt.errorbar(0.059578970*24,0.084,yerr=[[0.011],[0.014]],ls='none',color='g',capsize=3)
#plt.text(0.059578970*24,0.084,'  CSS080623_g(GPs)',color='g',size=12)



#plt.scatter(0.0778805320*24,0.166,marker='o',color='r',s=20)
#plt.errorbar(0.0778805320*24,0.166,yerr=[[0.010],[0.004]],ls='none',color='r',capsize=3)
#plt.text(0.0778805320*24,0.166,'  SDSS 0901(noGPs)',color='r',size=12)

plt.scatter(0.0778805320*24,0.126,marker='o',color='g',s=20)
plt.errorbar(0.0778805320*24,0.126,yerr=[[0.004],[0.019]],ls='none',color='g',capsize=3)
plt.text(0.0778805320*24,0.126,'  SDSS 0901(GPs)',color='g',size=12)

#plt.scatter(0.0778805320*24,0.163,marker='o',color='r',s=20)
#plt.errorbar(0.0778805320*24,0.163,yerr=[[0.008],[0.006]],ls='none',color='r',capsize=3)
#plt.text(0.0778805320*24,0.163,'  SDSS 0901_g(noGPs)',color='r',size=12)

#plt.scatter(0.0778805320*24,0.152,marker='o',color='g',s=20)
#plt.errorbar(0.0778805320*24,0.152,yerr=[[0.013],[0.012]],ls='none',color='g',capsize=3)
#plt.text(0.0778805320*24,0.152,'  SDSS 0901_g(GPs)',color='g',size=12)



#plt.scatter(0.0858526521*24,0.196,marker='o',color='r',s=20)
#plt.errorbar(0.0858526521*24,0.196,yerr=[[0.008],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.0858526521*24,0.196,'  DV UMa(noGPs)',color='r',size=12)

plt.scatter(0.0858526521*24,0.161,marker='o',color='g',s=20)
plt.errorbar(0.0858526521*24,0.161,yerr=[[0.010],[0.011]],ls='none',color='g',capsize=3)
plt.text(0.0858526521*24,0.161,'  DV UMa(GPs)',color='g',size=12)

#plt.scatter(0.0858526521*24,0.192,marker='o',color='r',s=20)
#plt.errorbar(0.0858526521*24,0.192,yerr=[[0.003],[0.006]],ls='none',color='r',capsize=3)
#plt.text(0.0858526521*24,0.192,'  DV UMa_g(ave_noGPs)',color='r',size=12)

#plt.scatter(0.0858526521*24,0.188,marker='o',color='g',s=20)
#plt.errorbar(0.0858526521*24,0.188,yerr=[[0.008],[0.010]],ls='none',color='g',capsize=3)
#plt.text(0.0858526521*24,0.188,'  DV UMa_g(ave_GPs)',color='g',size=12)

#plt.scatter(0.0858526521*24,0.191,marker='o',color='r',s=20)
#plt.errorbar(0.0858526521*24,0.191,yerr=[[0.004],[0.010]],ls='none',color='r',capsize=3)
#plt.text(0.0858526521*24,0.191,'  DV UMa_g(ing_noGPs)',color='r',size=12)

#plt.scatter(0.0858526521*24,0.151,marker='o',color='g',s=20)
#plt.errorbar(0.0858526521*24,0.151,yerr=[[0.007],[0.016]],ls='none',color='g',capsize=3)
#plt.text(0.0858526521*24,0.151,'  DV UMa_g(ind_GPs)',color='g',size=12)



#plt.scatter(0.088940717*24,0.174,marker='o',color='r',s=20)
#plt.errorbar(0.088940717*24,0.174,yerr=[[0.003],[0.003]],ls='none',color='r',capsize=3)
#plt.text(0.088940717*24,0.174,'  CTCV 1300(noGPs)',color='r',size=12)

plt.scatter(0.088940717*24,0.169,marker='o',color='g',s=20)
plt.errorbar(0.088940717*24,0.169,yerr=[[0.003],[0.008]],ls='none',color='g',capsize=3)
plt.text(0.088940717*24,0.169,'  CTCV 1300(GPs)',color='g',size=12)

#plt.scatter(0.088940717*24,0.188,marker='o',color='r',s=20)
#plt.errorbar(0.088940717*24,0.188,yerr=[[0.003],[0.004]],ls='none',color='r',capsize=3)
#plt.text(0.088940717*24,0.188,'  CTCV 1300_g(noGPs)',color='r',size=12)

#plt.scatter(0.088940717*24,0.168,marker='o',color='g',s=20)
#plt.errorbar(0.088940717*24,0.168,yerr=[[0.007],[0.009]],ls='none',color='g',capsize=3)
#plt.text(0.088940717*24,0.168,'  CTCV 1300_g(GPs)',color='g',size=12)

#plt.scatter(0.088940717*24,0.198,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.088940717*24,0.198,yerr=[[0.029],[0.029]],ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.088940717*24,0.198,'  CTCV 1300(S12)',color='b',size=12,alpha=0.5)

#plt.scatter(0.088940717*24,0.177,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.088940717*24,0.177,yerr=0.021,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.088940717*24,0.177,'  CTCV 1300(S11)',color='b',size=12,alpha=0.5)



plt.scatter(0.0631209221*24,0.087,marker='o',color='g',s=20)
plt.errorbar(0.0631209221*24,0.087,yerr=[[0.006],[0.010]],ls='none',color='g',capsize=3)
plt.text(0.0631209221*24,0.087,'  OY Car(GPs)',color='g',size=12)

#plt.scatter(0.0631209221*24,0.1070,marker='o',color='r',s=20)
#plt.errorbar(0.0631209221*24,0.1070,yerr=[[0.0007],[0.0011]],ls='none',color='r',capsize=3)
#plt.text(0.0631209221*24,0.1070,'  OY Car(noGPs)',color='r',size=12)

#plt.scatter(0.0631209221*24,0.1072,marker='o',color='r',s=20)
#plt.errorbar(0.0631209221*24,0.1072,yerr=[[0.0009],[0.0009]],ls='none',color='r',capsize=3)
#plt.text(0.0631209221*24,0.1072,'  OY Car_g(noGPs)',color='r',size=12)

#plt.scatter(0.0631209221*24,0.080,marker='o',color='g',s=20)
#plt.errorbar(0.0631209221*24,0.080,yerr=[[0.002],[0.014]],ls='none',color='g',capsize=3)
#plt.text(0.0631209221*24,0.080,'  OY Car_g(GPs)',color='g',size=12)

#From Littlefair08
#plt.scatter(0.0631209221*24,0.086,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0631209221*24,0.086,yerr=0.005,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0631209221*24,0.086,'  OY Car(L08)',color='b',size=12,alpha=0.5)

#From Wood&Horne90
#plt.scatter(0.0631209221*24,0.082,marker='o',color='b',s=20,alpha=0.5)
#plt.errorbar(0.0631209221*24,0.082,yerr=0.004,ls='none',color='b',capsize=3,alpha=0.5)
#plt.text(0.0631209221*24,0.082,'  OY Car(WH90)',color='b',size=12,alpha=0.5)


######  OTHER  #######


plt.scatter(0.0627919557*24,0.0440,marker='o',color='purple',s=20)
plt.errorbar(0.0627919557*24,0.0440,yerr=[[0.0017],[0.0015]],ls='none',color='purple',capsize=3)
plt.text(0.0627919557*24,0.0440,'  SDSS1057',color='purple',size=12)

plt.scatter(0.0587045*24,0.074,marker='o',color='purple',s=20)
plt.errorbar(0.0587045*24,0.074,yerr=[[0.004],[0.003]],ls='none',color='purple',capsize=3)
plt.text(0.0587045*24,0.071,'  SSS100615',color='purple',size=12)

#plt.scatter(0.060310649*24,0.0903,marker='o',color='r',s=20)
#plt.errorbar(0.060310649*24,0.0903,yerr=[[0.0020],[0.0023]],ls='none',color='r',capsize=3)
#plt.text(0.060310649*24,0.0925,'  ASASSN-14ag(noGPs)',color='r',size=12)

plt.scatter(0.060310649*24,0.093,marker='o',color='g',s=20)
plt.errorbar(0.060310649*24,0.093,yerr=[[0.012],[0.015]],ls='none',color='g',capsize=3)
plt.text(0.060310649*24,0.095,'  ASASSN-14ag(GPs)',color='g',size=12)

plt.scatter(0.0660508707*24,0.102,marker='o',color='purple',s=20)
plt.errorbar(0.0660508707*24,0.102,yerr=[[0.002],[0.004]],ls='none',color='purple',capsize=3)
plt.text(0.0660508707*24,0.098,'  CSS110113',color='purple',size=12)

plt.scatter(0.0529848884*24,0.064,marker='o',color='k',s=20)
plt.errorbar(0.0529848884*24,0.064,yerr=0.005,ls='none',color='k',capsize=3)
#plt.text(0.0529848884*24,0.063,'  PHL 1445',color='k',size=12)

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

plt.scatter(0.0568412623*24,0.077,marker='o',color='k',s=20)
plt.errorbar(0.0568412623*24,0.077,yerr=0.010,ls='none',color='k',capsize=3)
#plt.text(0.0568412623*24,0.074,'  SDSS 1501',color='k',size=12)

plt.scatter(0.072706113*24,0.1157,marker='o',color='k',s=20)
plt.errorbar(0.072706113*24,0.1157,yerr=0.0022,ls='none',color='k',capsize=3)
#plt.text(0.072706113*24,0.1157,'  OU Vir',color='k',size=12)

plt.scatter(0.0677497026*24,0.087,marker='o',color='k',s=20)#,alpha=0.25)
plt.errorbar(0.0677497026*24,0.087,yerr=0.006,ls='none',color='k',capsize=3)#,alpha=0.25)
#plt.text(0.0677497026*24,0.087,'  SDSS 1152',color='k',size=12,alpha=0.25)


plt.plot(P_optimal,m2_optimal,c='r',linewidth=2)
#plt.plot(P_standard,m2_standard,c='r',linestyle='dashed')
#plt.plot(P_BD_1,m2_BD_1,c='b',linewidth=2)
#plt.plot(P_BD_2,m2_BD_2,c='b',linestyle='--',linewidth=2)
#plt.plot(P_BD_3,m2_BD_3,c='b',linestyle='-.',linewidth=2)
#plt.plot(P_BD_4,m2_BD_4,c='b',linestyle=':',linewidth=2)
#plt.plot(P_evol_12,m2_evol_12,c='g',linewidth=2)
#plt.plot(P_evol_15,m2_evol_15,c='g',linestyle='dashed')
plt.xlabel(r'P$_{\rm orb}$ (hrs)', fontsize=20, labelpad=15)
plt.ylabel(r'M$_{\rm d}$ (M$_{\odot}$)', fontsize=20, labelpad=15)
plt.tick_params(axis='both', which='major', labelsize=18, width=1.5)
#plt.axis([1,1.7001,0,0.15001])
#plt.axis([1,2.3001,0,0.21001])
plt.axis([1.2,2.25,0,0.201])
plt.axvline(1.363,linestyle='dashed',color='k',linewidth=2,alpha=0.5)
#plt.axvspan(1.348,1.378,color='k',alpha=0.1)
#plt.scatter(1.373,0.1175,marker='o',color='w',s=25)
#plt.errorbar(1.373,0.01475,xerr=0.048,ls='none',color='k',capsize=5,linewidth=2,alpha=0.5)
#plt.errorbar(1.373,0.061,xerr=0.048,ls='none',color='k',capsize=5)
#plt.axvline(1.373,linestyle='dashed',color='gray')

plt.subplots_adjust(bottom=0.1, top=0.95, left=0.1, right=0.95)
for axis in ['top','bottom','left','right']:
 plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.show()
