import numpy as np
from pylab import *
from scipy.stats import norm
import scipy.optimize as opt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn


porb_kato_days = np.loadtxt('Superhumpers/superhumpers_kato.dat',dtype=float,usecols = [0]) 
porb_kato_days_err = np.loadtxt('Superhumpers/superhumpers_kato.dat',dtype=float,usecols = [1])

porb_ecl_days = np.loadtxt('porb_eclipsers.dat',dtype=float,usecols = [0]) 
porb_ecl_days_err = np.loadtxt('porb_eclipsers.dat',dtype=float,usecols = [1])

porb_g09_days = np.loadtxt('porb_g09.dat',dtype=float,usecols = [0]) 
porb_g09_days_err = np.loadtxt('porb_g09.dat',dtype=float,usecols = [1])


porb_kato_mins = porb_kato_days*24*60
porb_kato_mins_err = porb_kato_mins*(porb_kato_days_err/porb_kato_days)

porb_ecl_mins = porb_ecl_days*24*60
porb_ecl_mins_err = porb_ecl_mins*(porb_ecl_days_err/porb_ecl_days)

porb_g09_mins = porb_g09_days*24*60
porb_g09_mins_err = porb_g09_mins*(porb_g09_days_err/porb_g09_days)

porb_all_mins = np.concatenate((porb_kato_mins,porb_ecl_mins,porb_g09_mins))
#print len(porb_all_mins)

# G09 sample = 97 systems < porb=130 mins
# This sample = 300 systems < porb=130 mins (205 from Kato papers, 40 from G09 and 55 from data archive)

# This sample has >3x more systems

porb_spike = []
for i in range (0,len(porb_all_mins)):
    if porb_all_mins[i] >= 76.0 and porb_all_mins[i] <= 84.5:
        porb_spike.append(porb_all_mins[i])
        
porb_spike = np.array(porb_spike)


### HISTOGRAM ###

#bins = np.arange(77,84.5,0.5)
#bins_2 = np.arange(77,84.5,0.5)

bins = np.arange(70,96,1.0)
bins_2 = np.arange(70,96,0.1)

print bins

#bins = np.arange(75,84,1)
#bins_2 = np.arange(75,84,1)

#bins = np.arange(70,130,2)
#bins_2 = np.arange(70,130,2)
#bins = np.arange(66,134,4)
#bins_2 = np.arange(66,134,4)


s = np.std(porb_spike)
m = np.mean(porb_spike)

print m, s

mu, std = norm.fit(porb_spike)

p = norm.pdf(bins_2, mu, std)

title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)


def chisqfunc(a):
    chisq = np.sum(((porb_spike - a)**2.0) / (0**2 + 2.175**2.0))
    red_chisq = (chisq / (len(porb_spike)-1))
    print chisq
    #print red_chisq
    return chisq

x0 = 1

a = 80.55760854 #89.98 #0.23 
result = chisqfunc(a)

#result = opt.minimize(chisqfunc,x0)
#a = result.x
#print a

'''
77 - 84 mins
#a = 80.64 +- 0.19 # Error from delta(chisq) = 1
#sigma = 1.707 +- 0.011
#FWHM = 2.355*sigma = 4.02 +- 0.03

76 - 84.5 mins
#a = 80.55 +- 0.23 # Error from delta(chisq) = 1
#sigma = 2.175 +- 0.012
#FWHM = 2.355*sigma = 5.12 +- 0.03
'''

p_2 = norm.pdf(bins_2, 80.64, 1.707)


### CUMULATIVE PLOT ###

#values, base = np.histogram(porb_all_mins, bins=100000)
#evaluate the cumulative
#cumulative = np.cumsum(values)


seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

fig, ax1 = plt.subplots()
plt.hist(porb_all_mins,bins=bins,align='mid',color='r',edgecolor='none',alpha=0.7)

#plt.axvspan(79.55,85.25,color='g',alpha=0.2) #G09
#plt.errorbar(82.4,1.5,xerr=2.85,ls='none',color='k',capsize=5,linewidth=2.5,alpha=0.6) #G09

#plt.arrow(82.4,3,2.85,0,width=0.2,head_width=1.3,head_length=0.03,color='k',linewidth=0.5,alpha=0.8) #G09
#plt.arrow(82.4,3,-2.85,0,width=0.2,head_width=1.3,head_length=0.03,color='k',linewidth=0.5,alpha=0.8) #G09
#plt.axvspan(77.95,82.45,color='g',alpha=0.3) 
#plt.axvline(77.95,color='g',alpha=1,linewidth=1.5,linestyle='dashed')
#plt.axvline(82.45,color='g',alpha=1,linewidth=1.5,linestyle='dashed')
#plt.axvline(76.0,color='orange',alpha=1,linewidth=1.5,linestyle='dashed')

#ax1.set_xlim([66,130])
ax1.set_xlim([70,95])
#ax1.set_ylim([0,60])
ax1.set_xticks(np.arange(70,96,1))
ax1.set_xlabel(r'$P_{\rm orb}$ (mins)', fontsize=15)
ax1.set_ylabel(r'$N_{\rm sys}$', fontsize=15)



#ax1.plot(xdata, fitfunc(c, xdata))
#ax1.plot(xdata, ydata)

ax2 = ax1.twinx()
ax2.plot(bins_2, p*1.2, 'k', linewidth=1)
#ax2.plot(bins_2, p_2, 'b', linewidth=1)

ax2.set_xlim([70,95])
# plot the cumulative function
#ax2.plot(base[:-1], cumulative/300.0, c='b',alpha=1,linewidth=1.2)
#ax2.set_ylabel(r'$N_{\rm sys}$ / $\Sigma(N_{\rm sys})$', fontsize=15)
ax2.set_ylim([0,0.25])

plt.subplots_adjust(bottom=0.09, top=0.985, left=0.07, right=0.925)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.savefig("porb_hist.pdf")
plt.show()
 