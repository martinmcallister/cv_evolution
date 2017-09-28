import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import scipy.optimize as opt

#input wd mass and period for system
'''mwd,mwd_err = raw_input("WD mass and error in solar masses: ").split()
mwd = float(mwd)
mwd_err = float(mwd_err)

P = raw_input("System period in days: ")
P = float(P)*24'''

#produce plot

#plt.rcParams['xtick.major.pad']='15'
#plt.rcParams['ytick.major.pad']='10'

#plt.axis([1,2.2001,0.4,1.2001])
#plt.axis([0.5,5.0001,0.5,1.2001])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([1.0, 6.0])
ax.set_xticks([1,2,3,4,5,6])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_ylim([0.5, 1.2])
ax.set_yticks([0.6,0.8,1.0,1.2])
ax.get_yaxis().set_major_formatter(ScalarFormatter())

#plt.scatter(P,m2,marker='o',color='k',s=20)
#plt.errorbar(P,m2,yerr=m2_err,ls='none',color='k',capsize=3)


############ DONE ##############


#plt.scatter(0.0627919557*24,0.807,marker='o',color='r',s=20)
#plt.errorbar(0.0627919557*24,0.807,yerr=[[0.014],[0.013]],ls='none',color='r',capsize=3)
#plt.text(0.0627919557*24,0.807,'  SDSS1057(noGPs)',color='r',size=12)

plt.scatter(0.0627919557*24,0.800,marker='o',color='g',s=20)
plt.errorbar(0.0627919557*24,0.800,yerr=[[0.016],[0.015]],ls='none',color='g',capsize=3)
#plt.text(0.0627919557*24,0.800,'  SDSS1057(GPs)',color='g',size=12)

#plt.scatter(0.0587045*24,0.874,marker='o',color='r',s=20)
#plt.errorbar(0.0587045*24,0.874,yerr=[[0.024],[0.019]],ls='none',color='r',capsize=3)
#plt.text(0.0587045*24,0.874,'  SSS100615(noGPs)',color='r',size=12)

plt.scatter(0.0587045*24,0.88,marker='o',color='g',s=20)
plt.errorbar(0.0587045*24,0.88,yerr=[[0.03],[0.03]],ls='none',color='g',capsize=3)
#plt.text(0.0587045*24,0.88,'  SSS100615(GPs)',color='g',size=12)

#plt.scatter(0.060310649*24,0.722,marker='o',color='r',s=20)
#plt.errorbar(0.060310649*24,0.722,yerr=[[0.011],[0.017]],ls='none',color='r',capsize=3)
#plt.text(0.060310649*24,0.722,'  ASASSN-14ag(noGPs)',color='r',size=12)

plt.scatter(0.060310649*24,0.67,marker='o',color='g',s=20)
plt.errorbar(0.060310649*24,0.67,yerr=[[0.04],[0.04]],ls='none',color='g',capsize=3)
#plt.text(0.060310649*24,0.67,'  ASASSN-14ag(GPs)',color='g',size=12)

#plt.scatter(0.0660508707*24,1.024,marker='o',color='r',s=20)
#plt.errorbar(0.0660508707*24,1.024,yerr=[[0.024],[0.024]],ls='none',color='r',capsize=3)
#plt.text(0.0660508707*24,1.024,'  CSS110113(noGPs)',color='r',size=12)

plt.scatter(0.0660508707*24,1.00,marker='o',color='g',s=20)
plt.errorbar(0.0660508707*24,1.00,yerr=[[0.01],[0.03]],ls='none',color='g',capsize=3)
#plt.text(0.0660508707*24,1.00,'  CSS110113(GPs)',color='g',size=12)

#plt.scatter(0.059578970*24,0.752,marker='o',color='r',s=20)
#plt.errorbar(0.059578970*24,0.752,yerr=[[0.014],[0.019]],ls='none',color='r',capsize=3)
#plt.text(0.059578970*24,0.752,'  CSS080623(noGPs)',color='r',size=12)

plt.scatter(0.059578970*24,0.710,marker='o',color='g',s=20)
plt.errorbar(0.059578970*24,0.710,yerr=[[0.019],[0.018]],ls='none',color='g',capsize=3)
#plt.text(0.059578970*24,0.710,'  CSS080623(GPs)',color='g',size=12)

#plt.scatter(0.0529848884*24,0.73,marker='o',color='k',s=20)
#plt.errorbar(0.0529848884*24,0.73,yerr=0.03,ls='none',color='k',capsize=3)
#plt.text(0.0529848884*24,0.73,'  PHL 1445_M15',color='k',size=12)

plt.scatter(0.0529848884*24,0.77,marker='o',color='k',s=20)
plt.errorbar(0.0529848884*24,0.77,yerr=[[0.02],[0.03]],ls='none',color='k',capsize=3)
#plt.text(0.0529848884*24,0.77,'  PHL 1445(GPs)',color='k',size=12)

#plt.scatter(0.0778805320*24,0.801,marker='o',color='r',s=20)
#plt.errorbar(0.0778805320*24,0.801,yerr=[[0.026],[0.019]],ls='none',color='r',capsize=3)
#plt.text(0.0778805320*24,0.801,'  SDSS 0901(noGPs)',color='r',size=12)

plt.scatter(0.0778805320*24,0.752,marker='o',color='g',s=20)
plt.errorbar(0.0778805320*24,0.752,yerr=[[0.018],[0.024]],ls='none',color='g',capsize=3)
#plt.text(0.0778805320*24,0.752,'  SDSS 0901(GPs)',color='g',size=12)

plt.scatter(0.185912957*24,0.82,marker='o',color='g',s=20)
plt.errorbar(0.185912957*24,0.82,yerr=[[0.11],[0.12]],ls='none',color='g',capsize=3)
#plt.text(0.185912957*24,0.82,'  SDSS 1006(GPs)',color='g',size=12)

#plt.scatter(0.0739089282*24,0.961,marker='o',color='r',s=20)
#plt.errorbar(0.0739089282*24,0.961,yerr=[[0.024],[0.013]],ls='none',color='r',capsize=3)
#plt.text(0.0739089282*24,0.961,'  IY UMa(noGPs)',color='r',size=12)

plt.scatter(0.0739089282*24,0.955,marker='o',color='g',s=20)
plt.errorbar(0.0739089282*24,0.955,yerr=[[0.028],[0.013]],ls='none',color='g',capsize=3)
#plt.text(0.0739089282*24,0.955,'  IY UMa(GPs)',color='g',size=12)

#plt.scatter(0.065769292*24,0.904,marker='o',color='r',s=20)
#plt.errorbar(0.065769292*24,0.904,yerr=[[0.018],[0.010]],ls='none',color='r',capsize=3)
#plt.text(0.065769292*24,0.904,'  SSS130413(noGPs)',color='r',size=12)

plt.scatter(0.065769292*24,0.84,marker='o',color='g',s=20)
plt.errorbar(0.065769292*24,0.84,yerr=[[0.04],[0.02]],ls='none',color='g',capsize=3)
#plt.text(0.065769292*24,0.84,'  SSS130413(GPs)',color='g',size=12)

#plt.scatter(0.0744992631*24,0.779,marker='o',color='r',s=20)
#plt.errorbar(0.074499315*24,0.779,yerr=[[0.003],[0.007]],ls='none',color='r',capsize=3)
#plt.text(0.074499315*24,0.779,'  Z Cha(noGPs)',color='r',size=12)

plt.scatter(0.0744992631*24,0.803,marker='o',color='g',s=20)
plt.errorbar(0.074499315*24,0.803,yerr=[[0.014],[0.014]],ls='none',color='g',capsize=3)
#plt.text(0.074499315*24,0.803,'  Z Cha(GPs)',color='g',size=12)

#plt.scatter(0.0858526521*24,1.098,marker='o',color='r',s=20)
#plt.errorbar(0.0858526521*24,1.098,yerr=[[0.021],[0.017]],ls='none',color='r',capsize=3)
#plt.text(0.0858526521*24,1.098,'  DV UMa(noGPs)',color='r',size=12)

plt.scatter(0.0858526521*24,1.09,marker='o',color='k',s=20)
plt.errorbar(0.0858526521*24,1.09,yerr=[[0.03],[0.03]],ls='none',color='k',capsize=3)
#plt.text(0.0858526521*24,1.09,'  DV UMa(GPs)',color='k',size=12)

#plt.scatter(0.088940717*24,0.711,marker='o',color='r',s=20)
#plt.errorbar(0.088940717*24,0.711,yerr=[[0.006],[0.010]],ls='none',color='r',capsize=3)
#plt.text(0.088940717*24,0.711,'  CTCV 1300(noGPs)',color='r',size=12)

plt.scatter(0.088940717*24,0.717,marker='o',color='k',s=20)
plt.errorbar(0.088940717*24,0.717,yerr=[[0.016],[0.018]],ls='none',color='k',capsize=3)
#plt.text(0.088940717*24,0.717,'  CTCV 1300(GPs)',color='k',size=12)

#plt.scatter(0.0631209221*24,0.834,marker='o',color='r',s=20)
#plt.errorbar(0.0631209221*24,0.834,yerr=[[0.007],[0.006]],ls='none',color='r',capsize=3)
#plt.text(0.0631209221*24,0.834,'  OY Car(noGPs)',color='r',size=12)

plt.scatter(0.0631209221*24,0.882,marker='o',color='g',s=20)
plt.errorbar(0.0631209221*24,0.882,yerr=[[0.015],[0.011]],ls='none',color='g',capsize=3)
#plt.text(0.0631209221*24,0.882,'  OY Car(GPs)',color='g',size=12)

plt.scatter(0.1754424023*24,0.881,marker='o',color='g',s=20)
plt.errorbar(0.1754424023*24,0.881,yerr=[[0.017],[0.015]],ls='none',color='g',capsize=3)
#plt.text(0.1754424023*24,0.881,'  GY Cnc(GPs)',color='g',size=12)

#plt.scatter(0.0677497026*24,0.58,marker='o',color='r',s=20)
#plt.errorbar(0.0677497026*24,0.58,yerr=[[0.03],[0.03]],ls='none',color='r',capsize=3)
#plt.text(0.0677497026*24,0.58,'  SDSS 1152(noGPs)',color='r',size=12)

plt.scatter(0.0677497026*24,0.62,marker='o',color='k',s=20)
plt.errorbar(0.0677497026*24,0.62,yerr=[[0.03],[0.04]],ls='none',color='k',capsize=3)
#plt.text(0.0677497026*24,0.62,'  SDSS 1152(GPs)',color='k',size=12)

plt.scatter(0.0854185080*24,0.703,marker='o',color='g',s=20)
plt.errorbar(0.0854185080*24,0.703,yerr=[[0.015],[0.012]],ls='none',color='g',capsize=3)
#plt.text(0.0854185080*24,0.703,'  V713 Cep(GPs)',color='g',size=12)

#plt.scatter(0.0568412623*24,0.681,marker='o',color='r',s=20)
#plt.errorbar(0.0568412623*24,0.681,yerr=[[0.015],[0.014]],ls='none',color='r',capsize=3)
#plt.text(0.0568412623*24,0.681,'  SDSS 1501(noGPs)',color='r',size=12)

plt.scatter(0.0568412623*24,0.723,marker='o',color='k',s=20)
plt.errorbar(0.0568412623*24,0.723,yerr=[[0.013],[0.017]],ls='none',color='k',capsize=3)
#plt.text(0.0568412623*24,0.723,'  SDSS 1501(GPs)',color='k',size=12)


plt.scatter(0.0719308073*24,0.83,marker='o',color='orange',s=20)
plt.errorbar(0.0719308073*24,0.83,yerr=[[0.04],[0.04]],ls='none',color='orange',capsize=3)
#plt.text(0.0719308073*24,0.83,'  OGLE 82',color='orange',size=12)

plt.scatter(0.0932914*24,0.75,marker='o',color='orange',s=20)
plt.errorbar(0.0932914*24,0.75,yerr=[[0.03],[0.04]],ls='none',color='orange',capsize=3)
#plt.text(0.0932914*24,0.75,'  ASASSN-15pb(GPs)',color='orange',size=12)

plt.scatter(0.0715286*24,0.95,marker='o',color='orange',s=20)
plt.errorbar(0.0715286*24,0.95,yerr=[[0.07],[0.05]],ls='none',color='orange',capsize=3)
#plt.text(0.0715286*24,0.95,'  MASOT0014(GPs)',color='orange',size=12)

plt.scatter(0.074326968*24,0.724,marker='o',color='orange',s=20)
plt.errorbar(0.074326968*24,0.724,yerr=[[0.023],[0.016]],ls='none',color='orange',capsize=3)
#plt.text(0.074326968*24,0.724,'  ASASSN-14hq(GPs)',color='orange',size=12)

plt.scatter(0.07461448*24,0.78,marker='o',color='orange',s=20)
plt.errorbar(0.07461448*24,0.78,yerr=[[0.04],[0.02]],ls='none',color='orange',capsize=3)
#plt.text(0.07461448*24,0.78,'  AY For(GPs)',color='orange',size=12)



############## TEST FITS #################


#plt.scatter(0.06242785751*24,0.86,marker='o',color='orange',s=20)
#plt.errorbar(0.06242785751*24,0.86,yerr=[[0.07],[0.03]],ls='none',color='orange',capsize=3)
#plt.text(0.06242785751*24,0.86,'  V2051 Oph',color='orange',size=12)

#plt.scatter(0.0736471745*24,0.74,marker='o',color='orange',s=20)
#plt.errorbar(0.0736471745*24,0.74  ,yerr=0.07,ls='none',color='orange',capsize=3)
#plt.text(0.0736471745*24,0.74,' HT Cas ',color='orange',size=12)


############## IN LITERATURE ################

# HIGH-TIME RESOLUTION ECLIPSE MODELLING (Last 15 years)

#plt.scatter(0.059578970*24,0.699,marker='o',color='k',s=20,alpha=0.25)
#plt.errorbar(0.059578970*24,0.699,yerr=0.016,ls='none',color='k',capsize=3,alpha=0.25)
#plt.text(0.059578970*24,0.699,'  CSS080623',color='k',size=12,alpha=0.25)

#plt.scatter(0.0778805320*24,0.800,marker='o',color='k',s=20,alpha=0.25)
#plt.errorbar(0.0778805320*24,0.800,yerr=0.025,ls='none',color='k',capsize=3,alpha=0.25)
#plt.text(0.0778805320*24,0.800,'  SDSS 0901',color='k',size=12,alpha=0.25)

plt.scatter(0.054240679*24,0.865,marker='o',color='k',s=20)
plt.errorbar(0.054240679*24,0.865,yerr=0.005,ls='none',color='k',capsize=3)
#plt.text(0.054240679*24,0.865,'  SDSS 1433',color='k',size=12)

plt.scatter(0.04625828*24,0.892,marker='o',color='k',s=20)
plt.errorbar(0.04625828*24,0.892,yerr=0.008,ls='none',color='k',capsize=3)
#plt.text(0.04625828*24,0.892,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0570067*24,0.835,marker='o',color='k',s=20)
plt.errorbar(0.0570067*24,0.835,yerr=0.009,ls='none',color='k',capsize=3)
#plt.text(0.0570067*24,0.835,'  SDSS 1035',color='k',size=12)

plt.scatter(0.065550270*24,0.94,marker='o',color='k',s=20)
plt.errorbar(0.065550270*24,0.94,yerr=0.03,ls='none',color='k',capsize=3)
#plt.text(0.065550270*24,0.94,' CTCV J2354-4700',color='k',size=12)

#plt.scatter(0.0677497026*24,0.560,marker='o',color='k',s=20)
#plt.errorbar(0.0677497026*24,0.560,yerr=0.028,ls='none',color='k',capsize=3)
#plt.text(0.0677497026*24,0.560,'  SDSS 1152',color='k',size=12,alpha=0.25)

plt.scatter(0.059073543*24,0.872,marker='o',color='k',s=20)
plt.errorbar(0.059073543*24,0.872,yerr=0.011,ls='none',color='k',capsize=3)
#plt.text(0.059073543*24,0.872,'  SDSS 0903',color='k',size=12)

plt.scatter(0.062959041*24,0.796,marker='o',color='k',s=20)
plt.errorbar(0.062959041*24,0.796,yerr=0.018,ls='none',color='k',capsize=3)
#plt.text(0.062959041*24,0.796,'  SDSS 1227',color='k',size=12)

plt.scatter(0.061159491*24,0.769,marker='o',color='k',s=20)
plt.errorbar(0.061159491*24,0.769,yerr=0.017,ls='none',color='k',capsize=3)
#plt.text(0.061159491*24,0.769,'  XZ Eri',color='k',size=12)

plt.scatter(0.05890961*24,0.709,marker='o',color='k',s=20)
plt.errorbar(0.05890961*24,0.709,yerr=0.004,ls='none',color='k',capsize=3)
#plt.text(0.05890961*24,0.709,'  SDSS 1502',color='k',size=12)

#plt.scatter(0.0568412623*24,0.767,marker='o',color='k',s=20)
#plt.errorbar(0.0568412623*24,0.767,yerr=0.027,ls='none',color='k',capsize=3)
#plt.text(0.0568412623*24,0.767,'  SDSS 1501',color='k',size=12)

#plt.scatter(0.088940717*24,0.736,marker='o',color='k',s=20)
#plt.errorbar(0.088940717*24,0.736,yerr=0.014,ls='none',color='k',capsize=3)
#plt.text(0.088940717*24,0.736,'  CTCV J1300-3052',color='k',size=12)

plt.scatter(0.072706113*24,0.703,marker='o',color='k',s=20)
plt.errorbar(0.072706113*24,0.703,yerr=0.012,ls='none',color='k',capsize=3)
#plt.text(0.072706113*24,0.703,'  OU Vir',color='k',size=12)

#plt.scatter(0.0858526521*24,1.098,marker='o',color='k',s=20)
#plt.errorbar(0.0858526521*24,1.098,yerr=0.024,ls='none',color='k',capsize=3)
#plt.text(0.0858526521*24,1.098,'  DV UMa',color='k',size=12)

plt.scatter(0.10008215*24,0.91,marker='o',color='k',s=20)
plt.errorbar(0.10008215*24,0.91,yerr=0.03,ls='none',color='k',capsize=3)
#plt.text(0.10008215*24,0.91,'  SDSS 1702',color='k',size=12)

#From Littlefair08
#plt.scatter(0.0631209221*24,0.84,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.84,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0631209221*24,0.84,'  OY Car',color='b',size=12,alpha=0.3)

#From Shafter03
#plt.scatter(0.209937*24,0.71,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.209937*24,0.71,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.209937*24,0.71,'  EX Dra',color='b',size=12,alpha=0.3)

#From Southworth09
#plt.scatter(0.185912957*24,0.78,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.185912957*24,0.78,yerr=0.12,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.185912957*24,0.78,'  SDSS 1006',color='b',size=12,alpha=0.3)

#From Littlefair14
plt.scatter(0.1653077*24,0.69,marker='o',color='k',s=20)
plt.errorbar(0.1653077*24,0.69,yerr=0.07,ls='none',color='k',capsize=3)
#plt.text(0.1653077*24,0.69,'  KIS J1927',color='k',size=12)

#From Copperwheat10
plt.scatter(0.1582061029*24,1.16,marker='o',color='k',s=20)
plt.errorbar(0.1582061029*24,1.16,yerr=0.02,ls='none',color='k',capsize=3)
#plt.text(0.1582061029*24,1.16,'  IP Peg',color='k',size=12)

#From Miszalski16 (Mass overestimated due to bug in code - see Stu for revised value)
#plt.scatter(0.120971374*24,1.18,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,1.18,yerr=[[0.15],[0.07]],ls='none',color='k',capsize=3)
#plt.text(0.120971374*24,1.18,'  CSS111003',color='k',size=12)

#From Miszalski16 (Revised value from Stu)
#plt.scatter(0.120971374*24,,marker='o',color='k',s=20)
#plt.errorbar(0.120971374*24,,yerr=[[],[]],ls='none',color='k',capsize=3)
#plt.text(0.120971374*24,,'  CSS111003',color='k',size=12)

#From Rodriguez-Gil15 (Eclipse modelling)
#plt.scatter(0.149207696*24,0.87,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.149207696*24,0.87,yerr=0.09,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.149207696*24,0.87,'  HS 0220+0603',color='b',size=12,alpha=0.3)


# OTHER - below gap

'''#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.79,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.088940717*24,0.79,yerr=[[0.05],[0.05]],ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.088940717*24,0.79,'  CTCV 1300',color='b',size=12,alpha=0.3)

#From Steeghs03 (timing)
#plt.scatter(0.0739089282*24,0.79,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0739089282*24,0.79,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0739089282*24,0.79,'  IY UMa',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV)
#plt.scatter(0.0744992631*24,0.84,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.84,yerr=0.09,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0744992631*24,0.84,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.0744992631*24,0.56,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0744992631*24,0.56,yerr=0.01,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0744992631*24,0.56,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Wood&Horne90 (eclipse modelling)
#plt.scatter(0.0631209221*24,0.80,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.80,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0631209221*24,0.80,'  OY Car_H91',color='b',size=12,alpha=0.3)


#From Horne91 (eclipse modelling)
plt.scatter(0.0736471745*24,0.61,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.0736471745*24,0.61,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0736471745*24,0.61,' HT Cas ',color='b',size=12,alpha=0.3)

#From Baptista98 (timing)
plt.scatter(0.06242785751*24,0.78,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.06242785751*24,0.78,yerr=0.06,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.06242785751*24,0.78,'  V2051 Oph',color='b',size=12,alpha=0.3)

#From Steeghs07 (wd mass from gravitational redshift & q from RV)
plt.scatter(0.056688*24,0.85,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.056688*24,0.85,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.056688*24,0.85,'  WZ Sge',color='b',size=12,alpha=0.3)

#From Echevarria16 (RV)
plt.scatter(0.068233843*24,0.78,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.068233843*24,0.78,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.068233843*24,0.78,'  EX Hya',color='b',size=12,alpha=0.3)

#From Smith06 (wd mass from gravitational redshift & q from superhump excess) -- only use for mwd
plt.scatter(0.074271*24,0.71,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.074271*24,0.71,yerr=[[0.26],[0.18]],ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.074271*24,0.71,'  VW Hyi',color='b',size=12,alpha=0.3)

#From Borges&Baptista05 (timing)
plt.scatter(0.0614296757*24,0.73,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.0614296757*24,0.73,yerr=0.08,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.0614296757*24,0.73,'  V4140 Sgr',color='b',size=12,alpha=0.3)

#From Yakin10 (RV & md from porb) -- only use for mwd
plt.scatter(0.070037*24,0.80,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.070037*24,0.80,yerr=0.22,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.070037*24,0.80,'  1RXS J180834.7+101041',color='b',size=12,alpha=0.3)

#From Mason&Howell05 (RV) (Error bars not given in paper) -- don't use
#plt.scatter(0.07460*24,0.64,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.07460*24,0.64,yerr=0.10,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.07460*24,0.64,'  AY For',color='b',size=12,alpha=0.3)
'''

# OTHER - above gap

'''
#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.1754424023*24,0.82,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.1754424023*24,0.82,yerr=0.14,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.1754424023*24,0.82,'  GY Cnc',color='b',size=12,alpha=0.3)

#From Baptista00 (timing) 
#plt.scatter(0.209937*24,0.75,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.209937*24,0.75,yerr=0.15,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.209937*24,0.75,'  EX Dra',color='b',size=12,alpha=0.3)


#From Gaensicke06 (spectrophotometric modelling)
plt.scatter(0.128927*24,0.78,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.128927*24,0.78,yerr=[[0.17],[0.12]],ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.128927*24,0.78,'  AM Her',color='b',size=12,alpha=0.3)

#From Araujo-Betancour03 & Patterson05 (timing & q from epsilon)
plt.scatter(0.136606499*24,0.73,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.136606499*24,0.73,yerr=0.03,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.136606499*24,0.73,'  DW UMa',color='b',size=12,alpha=0.3)

#From Baptista04 (timing)
plt.scatter(0.163580429*24,0.67,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.163580429*24,0.67,yerr=0.14,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.163580429*24,0.67,'  UU Aqr',color='b',size=12,alpha=0.3)

#From Echevarria07 (RV)
plt.scatter(0.176906*24,1.20,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.176906*24,1.20,yerr=0.05,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.176906*24,1.20,'  U Gem',color='b',size=12,alpha=0.3)

#From Horne93 (RV)
plt.scatter(0.1936209*24,0.60,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.1936209*24,0.60,yerr=0.07,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.1936209*24,0.60,'  DQ Her',color='b',size=12,alpha=0.3)

#From Thoroughgood05 (RV)
plt.scatter(0.231936060*24,0.63,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.231936060*24,0.63,yerr=0.04,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.231936060*24,0.63,'  V347 Pup',color='b',size=12,alpha=0.3)

#From HernandezSantisteban17 (RV)
plt.scatter(0.26937446*24,0.82,marker='o',color='b',s=20,alpha=0.3)
plt.errorbar(0.26937446*24,0.82,yerr=0.06,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.26937446*24,0.82,'  1RXS J064434.5+334451',color='b',size=12,alpha=0.3)

#From North00 (RV)
#plt.scatter(0.29090912*24,1.12,marker='o',color='b',s=20,alpha=0.3)
#plt.errorbar(0.29090912*24,1.12,yerr=0.08,ls='none',color='b',capsize=3,alpha=0.3)
#plt.text(0.29090912*24,1.12,'  EM Cyg',color='b',size=12,alpha=0.3)
'''




'''plt.scatter(,marker='o',color='k',s=20)
plt.errorbar(,yerr=,ls='none',color='k',capsize=3)
plt.text(,'  ',color='k',size=12)'''

# Linear fit to systems below period gap
mwd = np.loadtxt('mwd.dat',dtype=float,usecols = [0])
mwd_err = np.loadtxt('mwd.dat',dtype=float,usecols = [1])
p = np.loadtxt('mwd.dat',dtype=float,usecols = [2])

'''def chisqfunc((a,b)):
    chisq = np.sum(((mwd - a - b*p*24)**2) / (mwd_err**2 + 0.11**2))
    red_chisq = chisq / (len(mwd)-2)
    print red_chisq
    return chisq
    
x0 = np.array([0.8,0])

result = opt.minimize(chisqfunc,x0)
print result.x
a,b = result.x
'''

def chisqfunc(a):
    chisq = np.sum(((mwd - a)**2) / (mwd_err**2 + 0.12**2))
    red_chisq = (chisq / (len(mwd)-1))
    #print chisq
    print red_chisq
    return chisq

x0 = 1
#a = 0.827980
#result = chisqfunc(a)
'''
a = 0.809 - 0.019 # Error from delta(chisq) = 1
c = chisqfunc(a)
b = 0
sigma = 0.12
'''
result = opt.minimize(chisqfunc,x0)

a = result.x
print a
b = 0


plt.xlabel(r'P$_{\rm orb}$ (hrs)', fontsize=15)
plt.ylabel(r'M$_{\rm wd}$ (M$_{\odot}$)', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15, width=1.0)

# Mean WD field mass (Tremblay et al. 2016)
#plt.axhline(0.621,linestyle='dashed',color='k',linewidth=1)

# Mean CV WD mass below period gap (Knigge 2006)
#plt.axhline(0.73,color='r',linewidth=1)

# Mean CV mass assumed in Knigge 06 + 11
#plt.axhline(0.75,color='k',linewidth=1)

# Mean CV WD mass of Savoury et al. 2011 sample
#plt.axhline(0.81,color='k',linewidth=1)

# Linear fit to eclipse modelled systems
p = np.arange(1,7,0.01)
mwd = a + b*p
#plt.plot(p,mwd,color='r',linewidth=1)

plt.subplots_adjust(bottom=0.1, top=0.95, left=0.1, right=0.95)
for axis in ['top','bottom','left','right']:
 plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.savefig("MwdvsP_curr.pdf")
plt.show()
