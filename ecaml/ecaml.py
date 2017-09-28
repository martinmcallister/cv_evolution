import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from scipy import optimize as opt
import seaborn

# Functions required for plotting dynamical unstable regions from Schreiber 16
# Fully conservative case
def psi_conv(q, m2):
    a = np.log(1.0+q**(1.0/3.0))
    b = 0.5*(q**(1.0/3.0)/(1.0+q**(1.0/3.0)))
    c = 0.6*q**(2.0/3.0) + np.log(1.0+q**(1.0/3.0))
    return (2.0/3.0)*((a-b)/c)*(1.0+q) + 2.0*(q-1.0)

# Classical non-conservative case
def psi_class(q, m2):
    a = np.log(1.0+q**(1.0/3.0))
    b = 0.5*(q**(1.0/3.0)/(1.0+q**(1.0/3.0)))
    c = 0.6*q**(2.0/3.0) + np.log(1.0+q**(1.0/3.0))
    return (2.0/3.0)*((a-b)/c) + 2.0*q/(1.0+1.0/q) + 1.0/(1.0+1.0/q) - 2.0

# ecaml
def psi_ecaml(q, m2):
    m1 = m2/q
    nu = 0.35/m1
    a = np.log(1.0+q**(1.0/3.0))
    b = 0.5*(q**(1.0/3.0)/(1.0+q**(1.0/3.0)))
    c = 0.6*q**(2.0/3.0) + np.log(1.0+q**(1.0/3.0))
    return (2.0/3.0)*((a-b)/c) + 2.0*nu + 1.0/(1.0+1.0/q) - 2.0

def politano96(m2):
    return 4.488*(m2-0.4342)**1.364 - 1.0/3.0

def qcrit(func):
    m2v = np.linspace(0.01, 0.80, 1000)
    qcrit = []
    for m2 in m2v:
        psi_ad = -1.0/3.0 if m2 < 0.4342 else politano96(m2)
        fitfunc = lambda x: func(x, m2) - psi_ad
        qcritcand = opt.newton(fitfunc, 0.7)
        qcrit.append(qcritcand)
    return m2v, np.array(qcrit)

# By eye from graph in Schreiber 16
#m2 = [0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65]
#q = [0.0,0.08,0.16,0.23,0.31,0.38,0.44,0.50,0.57,0.67,0.79,0.95,1.13,1.35]

# Chandrasekhar limit
m2_chand = np.arange(0,1.4,0.001)
q_chand = m2_chand/1.44

m2_av_mwd = np.arange(0,1.4,0.001)
q_av_mwd = m2_av_mwd/0.812
#q_av_mwd = m2_av_mwd/0.75

m2_conv, qc_conv = qcrit(psi_conv)
m2_class, qc_class = qcrit(psi_class)
m2_ecaml, qc_ecaml = qcrit(psi_ecaml)

#produce plot

seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

#plt.rcParams['xtick.major.pad']='15'
#plt.rcParams['ytick.major.pad']='10'

#plt.axis([0,1.201,0,1.201])
#plt.axis([0.1,1.1,0.1,1.401])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([0.04,1.4])
ax.set_xticks([0.04,0.06,0.08,0.1,0.2,0.4,0.6,0.8,1.0,1.2,1.4])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_yscale('log')
ax.set_ylim([0.04,1.4])
ax.set_yticks([0.04,0.06,0.08,0.1,0.2,0.4,0.6,0.8,1.0,1.2,1.4])
ax.get_yaxis().set_major_formatter(ScalarFormatter())
ax.minorticks_off()


############ PHL 1445 paper ##############


#plt.scatter(0.064,0.087,marker='o',color='k',s=10)
#plt.errorbar(0.064,0.087,xerr=0.006,yerr=0.004,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.064,0.087,'  PHL 1445_paper',color='k',size=12)


############ DONE (with GPs) ##############


plt.scatter(0.071,0.093,marker='o',color='g',s=10)
plt.errorbar(0.071,0.093,xerr=[[0.005],[0.009]],yerr=[[0.006],[0.007]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.071,0.093,'  PHL 1445 (10 ecl)',color='g',size=12)

#plt.scatter(0.061,0.084,marker='o',color='g',s=10)
#plt.errorbar(0.061,0.084,xerr=[[0.008],[0.005]],yerr=[[0.009],[0.004]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.061,0.084,'  PHL 1445 (6 ecl)',color='g',size=12)

plt.scatter(0.109,0.161,marker='o',color='g',s=10)
plt.errorbar(0.109,0.161,xerr=[[0.013],[0.012]],yerr=[[0.013],[0.012]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.109,0.161,'  ASASSN-14ag',color='g',size=12)

plt.scatter(0.141,0.146,marker='o',color='g',s=10)
plt.errorbar(0.141,0.146,xerr=[[0.007],[0.007]],yerr=[[0.001],[0.009]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.141,0.146,'  IY UMa',color='g',size=12)

plt.scatter(0.152,0.189,marker='o',color='g',s=10)
plt.errorbar(0.152,0.189,xerr=[[0.005],[0.006]],yerr=[[0.004],[0.004]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.152,0.189,'  Z Cha',color='g',size=12)

plt.scatter(0.081,0.114,marker='o',color='g',s=10)
plt.errorbar(0.081,0.114,xerr=[[0.005],[0.005]],yerr=[[0.005],[0.005]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.081,0.114,'  CSS080623',color='g',size=12)

plt.scatter(0.138,0.182,marker='o',color='g',s=10)
plt.errorbar(0.138,0.182,xerr=[[0.007],[0.007]],yerr=[[0.004],[0.009]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.138,0.182,'  SDSS 0901',color='g',size=12)

plt.scatter(0.187,0.172,marker='o',color='g',s=10)
plt.errorbar(0.187,0.172,xerr=[[0.012],[0.003]],yerr=[[0.007],[0.002]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.187,0.172,'  DV UMa',color='g',size=12)

plt.scatter(0.166,0.233,marker='o',color='g',s=10)
plt.errorbar(0.166,0.233,xerr=[[0.003],[0.006]],yerr=[[0.004],[0.004]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.166,0.233,'  CTCV 1300',color='g',size=12)

plt.scatter(0.093,0.1065,marker='o',color='g',s=10)
plt.errorbar(0.093,0.1065,xerr=[[0.004],[0.001]],yerr=[[0.0029],[0.0009]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.093,0.1065,'  OY Car',color='g',size=12)

plt.scatter(0.140,0.169,marker='o',color='g',s=10)
plt.errorbar(0.140,0.169,xerr=[[0.008],[0.012]],yerr=[[0.006],[0.011]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.140,0.152,'  SSS130413',color='g',size=12)

plt.scatter(0.105,0.105,marker='o',color='g',s=10)
plt.errorbar(0.105,0.105,xerr=[[0.006],[0.008]],yerr=[[0.005],[0.006]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.105,0.105,'  CSS110113',color='g',size=12)

plt.scatter(0.083,0.095,marker='o',color='g',s=10)
plt.errorbar(0.083,0.095,xerr=[[0.004],[0.006]],yerr=[[0.004],[0.003]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.083,0.095,'  SSS100615',color='g',size=12)

plt.scatter(0.094,0.153,marker='o',color='g',s=10)
plt.errorbar(0.094,0.153,xerr=[[0.009],[0.016]],yerr=[[0.010],[0.015]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.094,0.153,'  SDSS 1152',color='g',size=12)

plt.scatter(0.0436,0.0546,marker='o',color='g',s=10)
plt.errorbar(0.0436,0.0546,xerr=[[0.0017],[0.0025]],yerr=[[0.0017],[0.0022]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.0436,0.0546,'  SDSS1057',color='g',size=12)

plt.scatter(0.37,0.46,marker='o',color='g',s=10)
plt.errorbar(0.37,0.46,xerr=[[0.06],[0.06]],yerr=[[0.04],[0.03]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.37,0.46,'  SDSS 1006',color='g',size=12)

plt.scatter(0.394,0.448,marker='o',color='g',s=10)
plt.errorbar(0.394,0.448,xerr=[[0.022],[0.016]],yerr=[[0.021],[0.014]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.394,0.448,'  GY Cnc',color='g',size=12)

plt.scatter(0.176,0.246,marker='o',color='g',s=10)
plt.errorbar(0.176,0.246,xerr=[[0.018],[0.007]],yerr=[[0.014],[0.006]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.176,0.246,'  V713 Cep',color='g',size=12)

plt.scatter(0.061,0.084,marker='o',color='g',s=10)
plt.errorbar(0.061,0.084,xerr=[[0.003],[0.004]],yerr=[[0.003],[0.004]],ls='none',color='g',capsize=3,linewidth=1)
#plt.text(0.061,0.084,'  SDSS 1501',color='g',size=12)


######### IN LITERATURE ################


# HIGH_TIME RESOLUTION ECLIPSE MODELLING (circles)

'''
# Systems from Savoury 11 that have been revisited

#plt.scatter(0.098,,marker='o',color='k',s=10,alpha=0.25)
#plt.errorbar(0.098,,xerr=0.003,yerr=,ls='none',color='k',capsize=3,linewidth=1,alpha=0.25)
#plt.text(0.095,,'  CSS080623',color='k',size=12,alpha=0.25)

#plt.scatter(0.161,,marker='o',color='k',s=10,alpha=0.25)
#plt.errorbar(0.161,,xerr=0.007,yerr=,ls='none',color='k',capsize=3,linewidth=1,alpha=0.25)
#plt.text(0.162,,'  SDSS 0901',color='k',size=12,alpha=0.25)

#plt.scatter(0.177,0.240,marker='o',color='k',s=10)
#plt.errorbar(0.177,0.240,xerr=0.021,yerr=0.021,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.177,0.240,'  CTCV J1300-3052',color='k',size=12)

#plt.scatter(0.087,0.155,marker='o',color='k',s=10)
#plt.errorbar(0.087,0.155,xerr=0.006,yerr=0.006,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.087,0.155,'  SDSS 1152',color='k',size=12)

#plt.scatter(0.196,0.1778,marker='o',color='k',s=10)
#plt.errorbar(0.196,0.1778,xerr=0.005,yerr=0.0022,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.196,0.1778,'  DV UMa',color='k',size=12)

#plt.scatter(0.077,0.101,marker='o',color='k',s=10)
#plt.errorbar(0.077,0.101,xerr=0.010,yerr=0.010,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.074,0.101,'  SDSS 1501',color='k',size=12)
'''

# Systems from Savoury 11

plt.scatter(0.0571,0.0661,marker='o',color='k',s=10)
plt.errorbar(0.0571,0.0661,xerr=0.0007,yerr=0.0007,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.0571,0.0661,'  SDSS 1433',color='k',size=12)

plt.scatter(0.0575,0.0647,marker='o',color='k',s=10)
plt.errorbar(0.0575,0.0647,xerr=0.002,yerr=0.0018,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.0551,0.0647,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0475,0.0571,marker='o',color='k',s=10)
plt.errorbar(0.0475,0.0571,xerr=0.0012,yerr=0.0010,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.0457,0.0571,'  SDSS 1035',color='k',size=12)

plt.scatter(0.101,0.1097,marker='o',color='k',s=10)
plt.errorbar(0.101,0.1097,xerr=0.003,yerr=0.0008,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.103,0.1097,' CTCV J2354-4700',color='k',size=12)

plt.scatter(0.099,0.113,marker='o',color='k',s=10)
plt.errorbar(0.099,0.113,xerr=0.004,yerr=0.004,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.098,0.113,'  SDSS 0903',color='k',size=12)

plt.scatter(0.0889,0.1115,marker='o',color='k',s=10)
plt.errorbar(0.0889,0.1115,xerr=0.0025,yerr=0.0016,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.0889,0.1115,'  SDSS 1227',color='k',size=12)

plt.scatter(0.091,0.118,marker='o',color='k',s=10)
plt.errorbar(0.091,0.118,xerr=0.004,yerr=0.003,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.092,0.118,'  XZ Eri',color='k',size=12)

plt.scatter(0.0781,0.1099,marker='o',color='k',s=10)
plt.errorbar(0.0781,0.1099,xerr=0.0008,yerr=0.0007,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.0781,0.1099,'  SDSS 1502',color='k',size=12)

plt.scatter(0.1157,0.1641,marker='o',color='k',s=10)
plt.errorbar(0.1157,0.1641,xerr=0.0022,yerr=0.0013,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.1157,0.1641,'  OU Vir',color='k',size=12)

plt.scatter(0.223,0.248,marker='o',color='k',s=10)
plt.errorbar(0.223,0.248,xerr=0.010,yerr=0.005,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.223,0.248,'  SDSS 1702',color='k',size=12)

'''
# Systems from other sources that have been revisited

# From Southworth09
#plt.scatter(0.40,0.51,marker='o',color='k',s=10)
#plt.errorbar(0.40,0.51,xerr=0.10,yerr=0.08,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.40,0.51,'  SDSS 1006_S09',color='k',size=12)
'''

# Other systems

#From Shafter03
plt.scatter(0.53,0.75,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.53,0.75,xerr=0.01,yerr=0.05,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.53,0.75,'  EX Dra_S03',color='b',size=12,alpha=0.3)

#From Littlefair14 (UCAM data)
plt.scatter(0.39,0.570,marker='o',color='k',s=10)
plt.errorbar(0.39,0.570,xerr=0.04,yerr=0.011,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.39,0.570,'  KIS J1927_L14',color='k',size=12)

#From Copperwheat10 (UCAM data)
plt.scatter(0.55,0.48,marker='o',color='k',s=10)
plt.errorbar(0.55,0.48,xerr=0.02,yerr=0.01,ls='none',color='k',capsize=3,linewidth=1)
#plt.text(0.55,0.48,'  IP Peg_C10',color='k',size=12)

#From Miszalski16 (Mass overestimated due to bug in code)
plt.scatter(0.28,0.236,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.28,0.236,xerr=0.03,yerr=0.006,ls='none',color='k',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.28,0.236,'  CSS111003_M16',color='k',size=12,alpha=0.3)

#From Rodriguez-Gil15 (eclipse modelling)
plt.scatter(0.47,0.54,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.47,0.54,xerr=0.05,yerr=0.03,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.47,0.54,'  HS 0220+0603_RG15',color='b',size=12,alpha=0.3)

#From Hernandez17 (eclipse modelling) (in agreement with RV study of echevarria)
plt.scatter(0.58,0.80,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.58,0.80,xerr=0.06,yerr=0.02,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.58,0.80,'  1RXS J064434.5+334451_H17',color='b',size=12,alpha=0.3)

#From Tovmassian14 (eclipse modelling) # VIOLATES ECAML MODEL (no errors included -- 20% errors used)
plt.scatter(0.28,0.47,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.28,0.47,xerr=0.05,yerr=0.09,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.28,0.47,'  SDSS0756+0858_T14',color='b',size=12,alpha=0.3)


# CONTACT PHASE TIMING (squares)

'''
# Systems that have been revisited

#From Steeghs03 (timing)
#plt.scatter(0.10,0.125,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.10,0.125,xerr=0.01,yerr=0.008,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.10,0.125,'  IY UMa_S03',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.083,0.149,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.083,0.149,xerr=0.003,yerr=0.004,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.083,0.149,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Littlefair08 (Revised from Wood & Horne 1990)
#plt.scatter(0.086,0.102,marker='s',color='b',s=10)
#plt.errorbar(0.086,0.102,xerr=0.005,yerr=0.003,ls='none',color='b',capsize=3,linewidth=1)
#plt.text(0.086,0.102,'  OY Car_L08',color='b',size=12)
'''


#From Horne91 (timing)
plt.scatter(0.09,0.15,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.09,0.15,xerr=0.02,yerr=0.03,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.09,0.15,' HT Cas_H91',color='b',size=12,alpha=0.3)

#From Baptista98 (timing)
plt.scatter(0.15,0.19,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.15,0.19,xerr=0.03,yerr=0.03,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.15,0.19,'  V2051 Oph_B98',color='b',size=12,alpha=0.3)

#From Borges&Baptista98 (timing)
plt.scatter(0.092,0.125,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.092,0.125,xerr=0.016,yerr=0.015,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.092,0.125,'  V4140 Sgr_BB98',color='b',size=12,alpha=0.3)

#From Baptista00 (timing) (More accurate mass from Shafter03)
#plt.scatter(0.54,0.72,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.54,0.72,xerr=0.10,0yerr=0.06,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.54,0.72,'  EX Dra_B00',color='b',size=12,alpha=0.3)

#From Araujo-Betancour03 & Patterson05 (timing & q from epsilon)
plt.scatter(0.21,0.28,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.21,0.28,xerr=0.03,yerr=0.04,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.21,0.28,'  DW UMa_AB03',color='b',size=12,alpha=0.3)

#From Baptista04 (timing)
plt.scatter(0.20,0.30,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.20,0.30,xerr=0.07,yerr=0.07,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.20,0.30,'  UU Aqr_B04',color='b',size=12,alpha=0.3)


# RADIAL VELOCITY (triangles)

'''
# Systems that have been revisited

#From Wade&Horne88 (RV) **Note: Used low value of q (0.149) from Wood86** 
#plt.scatter(0.125,0.149,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.125,0.149,xerr=0.014,yerr=0.004,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.125,0.149,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
#plt.scatter(0.33,0.41,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.33,0.41,xerr=0.07,yerr=0.04,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.33,0.41,'  GY Cnc_T00',color='b',size=12,alpha=0.3)
'''

#From Echevarria16 (RV)
plt.scatter(0.10,0.13,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.10,0.13,xerr=0.02,yerr=0.02,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.10,0.13,'  EX Hya_E16',color='b',size=12,alpha=0.3)

#From HernandezSantisteban17 (RV)
#plt.scatter(0.78,0.96,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.78,0.96,xerr=0.04,yerr=0.05,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.78,0.96,'  1RXS J064434.5+334451_H17',color='b',size=12,alpha=0.3)

#From Echevarria07 (RV)
plt.scatter(0.42,0.35,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.42,0.35,xerr=0.04,yerr=0.05,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.42,0.35,'  U Gem_E07',color='b',size=12,alpha=0.3)

#From Horne93 (RV) # VIOLATES ECAML MODEL
plt.scatter(0.40,0.66,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.40,0.66,xerr=0.05,yerr=0.04,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.40,0.66,'  DQ Her_H93',color='b',size=12,alpha=0.3)

#From Thoroughgood05 (RV)
plt.scatter(0.52,0.83,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.52,0.83,xerr=0.06,yerr=0.05,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.52,0.83,'  V347 Pup_T05',color='b',size=12,alpha=0.3)

#From Arenas00 (RV)
plt.scatter(0.29,0.24,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.29,0.24,xerr=0.04,yerr=0.05,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.29,0.24,'  V603 Aql_A00',color='b',size=12,alpha=0.3)

#From Rodriguez-Gil01 (RV)
plt.scatter(0.20,0.31,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.20,0.31,xerr=0.04,yerr=0.06,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.20,0.31,'  V348 Pup_RG01',color='b',size=12,alpha=0.3)

#From Steeghs01+07 (wd mass from gravitational redshift (S07) & q from RV (S01))
plt.scatter(0.049,0.057,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.049,0.057,xerr=0.015,yerr=0.018,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.049,0.057,'  WZ Sge_S01/07',color='b',size=12,alpha=0.3)

#From Echevarria08 (RV) -- Not included as expected to have evolved secondary
#plt.scatter(0.37,0.60,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.37,0.60,xerr=0.04,yerr=0.08,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.37,0.60,'  AE Aqr_E08',color='b',size=12,alpha=0.3)

#From Welsh07 (RV)
plt.scatter(0.77,0.77,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.77,0.77,xerr=0.08,yerr=0.04,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.77,0.77,'  EM Cyg_W07',color='b',size=12,alpha=0.3)

#From Thoroughgood04 (RV)
plt.scatter(0.77,1.02,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.77,1.02,xerr=0.05,yerr=0.04,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(0.77,1.02,'  AC Cnc_T04',color='b',size=12,alpha=0.3)

#From Thoroughgood04 (RV) -- Not used in other M2 and R2 plots as M2 too large
plt.scatter(1.06,1.17,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(1.06,1.17,xerr=0.11,yerr=0.07,ls='none',color='b',capsize=3,linewidth=1,alpha=0.3)
#plt.text(1.06,1.17,'  V363 Aur_T04',color='b',size=12,alpha=0.3)



plt.plot(m2_chand,q_chand,c='k',linewidth=1,alpha=0.5)
plt.plot(m2_av_mwd,q_av_mwd,linestyle='dashed',color='k',linewidth=1,alpha=0.5)

plt.plot(m2_ecaml,qc_ecaml,c='k',linewidth=1,alpha=0.5)

plt.fill_between(m2_chand, 0, q_chand, color='k', alpha=0.2)#, hatch='x')
plt.fill_between(m2_ecaml, 100, qc_ecaml, color='k', alpha=0.2)#, hatch='x')

#plt.plot(m2_cons_1,q_cons_1,c='k',linewidth=1,alpha=0.5)
#plt.plot(m2_cons_2,q_cons_2,c='k',linewidth=1,alpha=0.5)

plt.xlabel(r'$M_{2}\ (\rm{M}_{\odot}$)', fontsize=14)
plt.ylabel(r'$q = M_{2}/M_{1}$', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10, width=1.0)
plt.tick_params(top='on',right='on')


plt.subplots_adjust(bottom=0.09, top=0.98, left=0.08, right=0.98)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("ecaml.pdf")
plt.show()
