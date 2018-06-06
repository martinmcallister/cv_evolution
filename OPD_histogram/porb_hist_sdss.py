import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn
import scipy.optimize as opt
from astropy import units as u

porb_kato_days = np.loadtxt('../Superhumpers/superhumpers_kato_esh.dat',dtype=float,usecols = [0]) 
porb_kato_days_err = np.loadtxt('../Superhumpers/superhumpers_kato_esh.dat',dtype=float,usecols = [1])

porb_ecl_days = np.loadtxt('porb_eclipsers.dat',dtype=float,usecols = [0]) 
porb_ecl_days_err = np.loadtxt('porb_eclipsers.dat',dtype=float,usecols = [1])

porb_g09_days = np.loadtxt('porb_g09.dat',dtype=float,usecols = [0]) 
porb_g09_days_err = np.loadtxt('porb_g09.dat',dtype=float,usecols = [1])

porb_g09_new_days = np.loadtxt('porb_g09_new.dat',dtype=float,usecols = [0]) 
porb_g09_new_days_err = np.loadtxt('porb_g09_new.dat',dtype=float,usecols = [1])
 
 
porb_g09_mins = porb_g09_days*24*60
#porb_g09_mins_err = porb_g09_mins*(porb_g09_days_err/porb_g09_days)

porb_g09_new_mins = porb_g09_new_days*24*60

porb_sdss_all = np.concatenate((porb_g09_mins,porb_g09_new_mins))
porb_g09 = porb_g09_mins
porb_new_no_esh = porb_g09_new_mins[0:67]
porb_sdss_no_esh = np.concatenate((porb_g09_mins,porb_g09_new_mins[0:67]))
porb_sdss_esh = porb_g09_new_mins[67:]

porb_sdss_new = np.concatenate((porb_g09_mins[0:49],porb_g09_new_mins[0:23]))
porb_sdss_new_g09 = porb_g09_mins[0:49]
porb_sdss_old = np.concatenate((porb_g09_mins[49:],porb_g09_new_mins[23:]))


# G09 sample = 82 systems < porb=130 mins
# New SDSS (no esh) = 67 systems < porb=130 mins
#New SDSS (esh) = 31 systems < porb=130 mins



seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

### HISTOGRAM ###


bins = np.arange(63,131,2)
bins_2 = np.arange(70,96,0.1)
#bins = np.arange(66,134,4)
#bins_2 = np.arange(66,134,4)


### CUMULATIVE PLOT ###

values_g09, base_g09 = np.histogram(porb_sdss_new_g09, bins=100000)
values_new, base_new = np.histogram(porb_sdss_new, bins=100000)
pspike_gauss = np.random.normal(82.7,2.35,10000)
values_gauss, base_gauss = np.histogram(pspike_gauss, bins=100000)
#evaluate the cumulative
cumulative_g09 = np.cumsum(values_g09)
cumulative_new = np.cumsum(values_new)
cumulative_gauss = np.cumsum(values_gauss)


# ESH work
'''
mwd = np.random.normal(0.81,0.13,len(porb_sdss_no_esh))
density = 107.0/(porb_sdss_no_esh/60.0)**2.0 * u.g * u.cm**-3.0
R0 = 1.0*u.R_sun
M0 = u.M_sun
m_92 = 3.0*M0/1.07/np.pi/density/R0**3.0
m2 = m_92.decompose()**(1.0/0.92)
q = m2/mwd
superhump_mask = q < 0.095
# Mask of q < 0.095 found to be able to replicate distribution reasonably well

plt.hist(porb_sdss_esh,bins=bins,alpha=0.5)
plt.hist(porb_sdss_no_esh[superhump_mask],bins=bins,alpha=0.5)
plt.show()
'''

porb_spike = []
for i in range (0,len(porb_sdss_new)):
    if porb_sdss_no_esh[i] >= 77 and porb_sdss_no_esh[i] <= 87:
        porb_spike.append(porb_sdss_no_esh[i])
        
porb_spike = np.array(porb_spike)
      
      
s = np.std(porb_spike)
m = np.mean(porb_spike)

print m, s

mu, std = norm.fit(porb_spike)

print mu, std

p = norm.pdf(bins_2, mu, std)

title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)     

def chisqfunc(a):
    chisq = np.sum(((porb_spike - a)**2.0) / (0**2.0 + 2.35**2.0))
    red_chisq = (chisq / (len(porb_spike)-1))
    #print chisq
    print red_chisq
    return chisq

x0 = 1

#a = 82.65457847 #0.0
#result = chisqfunc(a)

result = opt.minimize(chisqfunc,x0)
a = result.x
print a

'''
77 - 87 mins
a = 82.7 +- 0.4 # Error from delta(chisq) = 1
sigma = 2.35 +- 0.04
FWHM = 2.355*sigma = 5.53 +- 0.09
'''

p_2 = norm.pdf(bins_2, 81.2, 1.814)



fig, ax1 = plt.subplots()
plt.hist(porb_sdss_new,bins=bins,align='mid',color='r',edgecolor='none',alpha=0.75)
plt.hist(porb_sdss_new_g09,bins=bins,align='mid',facecolor='k',edgecolor='none',linewidth=1,linestyle='dashed',alpha=0.25)
#plt.hist(porb_new_no_esh,bins=bins,align='mid',color='k',edgecolor='none',alpha=0.25)
#plt.hist(porb_sdss_esh,bins=bins,align='mid',color='b',edgecolor='none',alpha=0.75)
#plt.axvspan(79.55,85.25,color='g',alpha=0.2) #G09
#plt.errorbar(82.4,1.5,xerr=2.85,ls='none',color='k',capsize=5,linewidth=2.5,alpha=0.6) #G09

plt.arrow(82.4,0.3,2.85,0,width=0.05,head_width=0.25,head_length=0.01,color='k',linewidth=0.7,alpha=0.8) #G09
plt.arrow(82.4,0.3,-2.85,0,width=0.05,head_width=0.25,head_length=0.01,color='k',linewidth=0.7,alpha=0.8) #G09
#plt.axvline(80.35,color='g',alpha=0.7,linewidth=1.5,linestyle='dashed')
#plt.axvline(82.825,color='g',alpha=0.7,linewidth=1.5,linestyle='dashed')
#plt.axvline(77.9,color='orange',alpha=0.7,linewidth=1.5,linestyle='dashed')

ax1.set_xlim([65,129])
ax1.set_ylim([0,8])
ax1.tick_params(axis='x', which='major', labelsize=7, width=1.0)
#ax1.set_xticks(np.arange(66,130.1,4))
ax1.set_xticks(np.arange(65,129.1,2))
#ax1.set_yticks(np.arange(0,22.1,2))
ax1.set_xlabel(r'$P_{\rm orb}$ (mins)', fontsize=15)
ax1.set_ylabel(r'$N_{\rm sys}$', fontsize=15)

#ax1.plot(bins_2, p*60, 'k', linewidth=1)

ax2 = ax1.twinx()
#ax2.plot(bins_2, p*2.2, 'k', linewidth=1)
#ax2.plot(bins_2, p_2*2.2, 'b', linewidth=1)
ax2.set_xlim([65,129])
# plot the cumulative function
#ax2.plot(base_g09[:-1], cumulative_g09/49.0, c='g',alpha=1,linewidth=1.2)
ax2.plot(base_new[:-1], cumulative_new/72.0, c='b',alpha=1,linewidth=1.2)
#ax2.plot(base_gauss[:-1], (cumulative_gauss/23300.0)+0.014, c='orange',alpha=1,linewidth=1.2,linestyle='dashed')
ax2.set_ylabel(r'$N_{\rm sys}$ / $\Sigma(N_{\rm sys})$', fontsize=15)
ax2.set_ylim([0,1])

plt.subplots_adjust(bottom=0.09, top=0.985, left=0.07, right=0.925)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.savefig("porb_hist.pdf")
plt.show()
 