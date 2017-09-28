import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import scipy.optimize as opt
import seaborn

#produce plot

seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

#plt.rcParams['xtick.major.pad']='15'
#plt.rcParams['ytick.major.pad']='10'

#plt.axis([1,2.2001,0.4,1.2001])
#plt.tick_params(top='on',right='on')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xscale('log')
ax.set_xlim([1.0, 7.5])
ax.set_xticks([1,2,3,4,5,6,7])
ax.get_xaxis().set_major_formatter(ScalarFormatter())
ax.set_ylim([0.4, 1.4])
ax.set_yticks([0.4,0.6,0.8,1.0,1.2,1.4])
ax.get_yaxis().set_major_formatter(ScalarFormatter())
ax.minorticks_off()


# HIGH_TIME RESOLUTION ECLIPSE MODELLING (circles)

# Systems from Savoury 11

plt.scatter(0.054240679*24,0.865,marker='o',color='k',s=10)
plt.errorbar(0.054240679*24,0.865,yerr=0.005,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.054240679*24,0.865,'  SDSS 1433',color='k',size=12)

plt.scatter(0.04625828*24,0.892,marker='o',color='k',s=10)
plt.errorbar(0.04625828*24,0.892,yerr=0.008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.04625828*24,0.892,'  SDSS 1507',color='k',size=12)

plt.scatter(0.0570067*24,0.835,marker='o',color='k',s=10)
plt.errorbar(0.0570067*24,0.835,yerr=0.009,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0570067*24,0.835,'  SDSS 1035',color='k',size=12)

plt.scatter(0.065550270*24,0.94,marker='o',color='k',s=10)
plt.errorbar(0.065550270*24,0.94,yerr=0.03,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.065550270*24,0.94,' CTCV J2354-4700',color='k',size=12)

plt.scatter(0.0677497026*24,0.560,marker='o',color='k',s=10)
plt.errorbar(0.0677497026*24,0.560,yerr=0.028,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0677497026*24,0.560,'  SDSS 1152',color='k',size=12)

plt.scatter(0.059073543*24,0.872,marker='o',color='k',s=10)
plt.errorbar(0.059073543*24,0.872,yerr=0.011,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.059073543*24,0.872,'  SDSS 0903',color='k',size=12)

plt.scatter(0.062959041*24,0.796,marker='o',color='k',s=10)
plt.errorbar(0.062959041*24,0.796,yerr=0.018,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.062959041*24,0.796,'  SDSS 1227',color='k',size=12)

plt.scatter(0.061159491*24,0.769,marker='o',color='k',s=10)
plt.errorbar(0.061159491*24,0.769,yerr=0.017,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.061159491*24,0.769,'  XZ Eri',color='k',size=12)

plt.scatter(0.05890961*24,0.709,marker='o',color='k',s=10)
plt.errorbar(0.05890961*24,0.709,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.05890961*24,0.709,'  SDSS 1502',color='k',size=12)

plt.scatter(0.0568412623*24,0.767,marker='o',color='k',s=10)
plt.errorbar(0.0568412623*24,0.767,yerr=0.027,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0568412623*24,0.767,'  SDSS 1501',color='k',size=12)

plt.scatter(0.088940717*24,0.736,marker='o',color='k',s=10)
plt.errorbar(0.088940717*24,0.736,yerr=0.014,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.088940717*24,0.736,'  CTCV J1300-3052',color='k',size=12)

plt.scatter(0.072706113*24,0.703,marker='o',color='k',s=10)
plt.errorbar(0.072706113*24,0.703,yerr=0.012,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.072706113*24,0.703,'  OU Vir',color='k',size=12)

plt.scatter(0.0858526521*24,1.098,marker='o',color='k',s=10)
plt.errorbar(0.0858526521*24,1.098,yerr=0.024,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0858526521*24,1.098,'  DV UMa',color='k',size=12)

plt.scatter(0.10008215*24,0.91,marker='o',color='k',s=10)
plt.errorbar(0.10008215*24,0.91,yerr=0.03,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.10008215*24,0.91,'  SDSS 1702',color='k',size=12)

# Other systems

#From Shafter03
plt.scatter(0.209937*24,0.71,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.209937*24,0.71,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.209937*24,0.71,'  EX Dra_S03',color='b',size=12,alpha=0.3)

# From Southworth09
plt.scatter(0.185912957*24,0.78,marker='o',color='b',s=10,alpha=0.3)
plt.errorbar(0.185912957*24,0.78,yerr=0.12,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.185912957*24,0.78,'  SDSS 1006_S09',color= b',size=12,alpha=0.3)

#From Copperwheat10 (UCAM data)
plt.scatter(0.1582061029*24,1.16,marker='o',color='k',s=10)
plt.errorbar(0.1582061029*24,1.16,yerr=0.02,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.1582061029*24,1.16,'  IP Peg_C10',color='k',size=12)


# CONTACT PHASE TIMING (squares)


#From Steeghs03 (timing)
plt.scatter(0.0739089282*24,0.79,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0739089282*24,0.79,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0739089282*24,0.79,'  IY UMa_S03',color='b',size=12,alpha=0.3)

#From Wood86 (timing) **Note: Values revised slightly in Wade&Horne88**
#plt.scatter(0.074499*24,0.56,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.074499*24,0.56,yerr=0.10,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.074499*24,0.56,'  Z Cha_W86',color='b',size=12,alpha=0.3)

#From Littlefair08 (Revised from Wood & Horne 1990)
plt.scatter(0.0631209221*24,0.84,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0631209221*24,0.84,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0631209221*24,0.84,'  OY Car_L08',color='b',size=12,alpha=0.3)

#From Wood&Horne90 (timing)
#plt.scatter(0.0631209221*24,0.80,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.0631209221*24,0.80,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0631209221*24,0.80,'  OY Car_WH90',color='b',size=12,alpha=0.3)

#From Horne91 (timing)
plt.scatter(0.0736471745*24,0.61,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0736471745*24,0.61,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0736471745*24,0.61,' HT Cas_H91',color='b',size=12,alpha=0.3)

#From Baptista98 (timing)
plt.scatter(0.06242785751*24,0.78,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.06242785751*24,0.78,yerr=0.06,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.06242785751*24,0.78,'  V2051 Oph_B98',color='b',size=12,alpha=0.3)

#From Borges&Baptista05 (timing)
plt.scatter(0.0614296779*24,0.73,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.0614296779*24,0.73,yerr=0.08,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0614296779*24,0.73,'  V4140 Sgr_BB05',color='b',size=12,alpha=0.3)

#From Baptista00 (timing) (More accurate mass from Shafter03)
#plt.scatter(0.209937*24,0.75,marker='s',color='b',s=10,alpha=0.3)
#plt.errorbar(0.209937*24,0.75,yerr=0.15,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.209937*24,0.75,'  EX Dra_B00',color='b',size=12,alpha=0.3)

#From Araujo-Betancour03 & Patterson05 (timing & q from epsilon)
plt.scatter(0.136606499*24,0.73,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.136606499*24,0.73,yerr=0.03,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.136606499*24,0.73,'  DW UMa_AB03',color='b',size=12,alpha=0.3)

#From Baptista94 (timing)
plt.scatter(0.1638049430*24,0.67,marker='s',color='b',s=10,alpha=0.3)
plt.errorbar(0.1638049430*24,0.67,yerr=0.14,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.1638049430*24,0.67,'  UU Aqr_B94',color='b',size=12,alpha=0.3)


# RADIAL VELOCITY (triangles)


#From Savoury12 (RV)
#plt.scatter(0.088940717*24,0.79,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.088940717*24,0.79,yerr=[[0.05],[0.05]],ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.088940717*24,0.79,'  CTCV 1300_S12',color='b',size=12,alpha=0.3)

#From Wade&Horne88 (RV)
plt.scatter(0.074499*24,0.84,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.074499*24,0.84,yerr=0.09,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.074499*24,0.84,'  Z Cha_WH88',color='b',size=12,alpha=0.3)

#From Thorstensen00 (RV) **Note: Values below are with added correction, not those in abstract**
plt.scatter(0.1754424023*24,0.82,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.1754424023*24,0.82,yerr=0.14,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.1754424023*24,0.82,'  GY Cnc_T00',color='b',size=12,alpha=0.3)

#From Echevarria07 (RV)
plt.scatter(0.17690617*24,1.20,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.17690617*24,1.20,yerr=0.05,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.17690617*24,1.20,'  U Gem_E07',color='b',size=12,alpha=0.3)

#From Hoogerwerf04 -- M1 only -- Very low mass?
#plt.scatter(0.068233843*24,0.49,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.068233843*24,0.49,yerr=0.13,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.068233843*24,0.49,'  EX Hya_H04',color='b',size=12,alpha=0.3)

#From Horne93 (RV)
plt.scatter(0.193620897*24,0.60,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.193620897*24,0.60,yerr=0.07,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.193620897*24,0.60,'  DQ Her_H93',color='b',size=12,alpha=0.3)

#From Thoroughgood05 (RV)
plt.scatter(0.231936060*24,0.63,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.231936060*24,0.63,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.231936060*24,0.63,'  V347 Pup_T05',color='b',size=12,alpha=0.3)

#From Arenas00 (RV)
plt.scatter(0.13820103*24,1.2,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.13820103*24,1.2,yerr=0.2,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.13820103*24,1.2,'  V603 Aql_A00',color='b',size=12,alpha=0.3)

#From Rodriguez-Gil01 (RV)
plt.scatter(0.101838931*24,0.65,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.101838931*24,0.65,yerr=0.13,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.101838931*24,0.65,'  V348 Pup_RG01,color='b',size=12,alpha=0.3)

#From Echevarria08 (RV) -- Not included as expected to have evolved secondary and P > 0.8
#plt.scatter(0.4116554800*24,0.63,marker='^',color='b',s=10,alpha=0.3)
#plt.errorbar(0.4116554800*24,0.63,yerr=0.05,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.4116554800*24,0.63,'  AE Aqr_E08',color='b',size=12,alpha=0.3)

#Welsh07 (RV)
plt.scatter(0.290909*24,1.00,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.290909*24,1.00,yerr=0.12,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.290909*24,1.00,'  EM Cyg_W07',color='b',size=12,alpha=0.3)

#From Thoroughgood04 (RV)
plt.scatter(0.30047747*24,0.76,marker='^',color='b',s=10,alpha=0.3)
plt.errorbar(0.30047747*24,0.76,yerr=0.03,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.30047747*24,0.76,'  AC Cnc_T04',color='b',size=12,alpha=0.3)


# GRAVITATIONAL REDSHIFT (stars)


#From Steeghs01+07 (wd mass from gravitational redshift (S07) & q from RV (S01))
plt.scatter(0.0566878460*24,0.85,marker='*',color='b',s=10,alpha=0.3)
plt.errorbar(0.0566878460*24,0.85,yerr=0.04,ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.0566878460*24,0.85,'  WZ Sge_S01/07',color='b',size=12,alpha=0.3)

#From Smith06 (wd mass from gravitational redshift & q from superhump excess) -- only use for mwd
plt.scatter(0.074271*24,0.71,marker='*',color='b',s=10,alpha=0.3)
plt.errorbar(0.074271*24,0.71,yerr=[[0.26],[0.18]],ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.074271*24,0.71,'  VW Hyi_S06',color='b',size=12,alpha=0.3)


# SPECTROPHOTOMETRIC MODELLING (diamonds)


#From Gaensicke06 (spectrophotometric modelling)
plt.scatter(0.128927*24,0.78,marker='d',color='b',s=10,alpha=0.3)
plt.errorbar(0.128927*24,0.78,yerr=[[0.17],[0.12]],ls='none',color='b',capsize=None,linewidth=1,alpha=0.3)
#plt.text(0.128927*24,0.78,'  AM Her',color='b',size=12,alpha=0.3)


# AVERAGE MASS CALCULATION -- Shouldn't be needed here

'''
# Linear fit to white dwarf masses
mwd = np.loadtxt('mwd_init.dat',dtype=float,usecols = [0])
mwd_err = np.loadtxt('mwd_init.dat',dtype=float,usecols = [1])
p = np.loadtxt('mwd_init.dat',dtype=float,usecols = [2])

def chisqfunc((a,b)):
    chisq = np.sum(((mwd - a - b*p*24)**2) / (mwd_err**2 + 0.127**2))
    red_chisq = chisq / (len(mwd)-2)
    print red_chisq
    return chisq
    
x0 = np.array([0.8,0.1])

result = opt.minimize(chisqfunc,x0)
print result.x
a,b = result.x


def chisqfunc(a):
    chisq = np.sum(((mwd - a)**2) / (mwd_err**2 + 0.125**2))
    red_chisq = (chisq / (len(mwd)-1))
    #print chisq
    print red_chisq
    return chisq

x0 = 1
#a = 0.82797952
#result = chisqfunc(a)


#a = 0.809 - 0.019 # Error from delta(chisq) = 1
#c = chisqfunc(a)
#b = 0
#sigma = 0.13


result = opt.minimize(chisqfunc,x0)

a = result.x
print a
b = 0
'''

plt.xlabel(r'$P_{\rm orb}$ (hrs)', fontsize=16)
plt.ylabel(r'$M_{1} \ (\rm{M}_{\odot}$)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=15, width=1.0)
plt.tick_params(top='on',right='on')

# Mean WD field mass (Tremblay et al. 2016)
plt.axhline(0.621,linestyle='dashed',color='k',linewidth=1,alpha=0.3)

# Mean CV mass measured in Knigge 06 and assumed in both Knigge 06 + 11
plt.axhline(0.75,color='k',linewidth=1,alpha=0.3)

# Mean CV WD mass of Savoury et al. 2011 sample
#plt.axhline(0.81,color='k',linewidth=1,alpha=0.8)

# Mean CV WD mass from Zorotovic 11
plt.axhline(0.82,color='k',linewidth=1,alpha=0.8)
plt.axhspan(0.82-0.03,0.82+0.03,color='k',alpha=0.05)


# Linear fit to white dwarf masses
#p = np.arange(1,8,0.01)
#mwd = a + b*p
#plt.plot(p,mwd,color='r',linewidth=1,alpha=0.8)

plt.subplots_adjust(bottom=0.11, top=0.98, left=0.09, right=0.99)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("m1vsP_init.pdf")
plt.show()
