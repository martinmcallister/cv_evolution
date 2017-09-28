import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn

porb_kato_days = np.loadtxt('Superhumpers/superhumpers_kato_esh.dat',dtype=float,usecols = [0]) 
porb_kato_days_err = np.loadtxt('Superhumpers/superhumpers_kato_esh.dat',dtype=float,usecols = [1])

porb_ecl_days = np.loadtxt('porb_eclipsers.dat',dtype=float,usecols = [0]) 
porb_ecl_days_err = np.loadtxt('porb_eclipsers.dat',dtype=float,usecols = [1])

porb_g09_days = np.loadtxt('porb_g09.dat',dtype=float,usecols = [0]) 
porb_g09_days_err = np.loadtxt('porb_g09.dat',dtype=float,usecols = [1])
 

porb_kato_mins = porb_kato_days*24*60
porb_kato_mins_err = porb_kato_mins*(porb_kato_days_err/porb_kato_days)

porb_ecl_mins = porb_ecl_days*24*60
#porb_ecl_mins_err = porb_ecl_mins*(porb_ecl_days_err/porb_ecl_days)

porb_g09_mins = porb_g09_days*24*60
#porb_g09_mins_err = porb_g09_mins*(porb_g09_days_err/porb_g09_days)

porb_all_mins = np.concatenate((porb_kato_mins,porb_ecl_mins,porb_g09_mins[0:40]))
no_esh = porb_kato_mins[0:158]
esh = porb_kato_mins[158:]

# G09 sample = 97 systems < porb=130 mins
# This sample = 300 systems < porb=130 mins (205 from Kato papers, 40 from G09 and 55 from data archive)

# This sample has >3x more systems


### HISTOGRAM ###


bins = np.arange(66,134,1)
bins_2 = np.arange(74,86,0.1)
#bins = np.arange(66,134,4)
#bins_2 = np.arange(66,134,4)


### CUMULATIVE PLOT ###

values, base = np.histogram(esh, bins=100000)
#evaluate the cumulative
cumulative = np.cumsum(values)



esh_spike = []
for i in range (0,len(esh)):
    if esh[i] >= 75.0 and esh[i] <= 84:
        esh_spike.append(esh[i])
        
esh_spike = np.array(esh_spike)

s = np.std(esh_spike)
m = np.mean(esh_spike)

print m, s

mu, std = norm.fit(esh_spike)

p = norm.pdf(bins_2, mu, std)


seaborn.set(style='ticks')
seaborn.set_style({"xtick.direction": "in","ytick.direction": "in"})

fig, ax1 = plt.subplots()
plt.hist(porb_all_mins,bins=bins,align='mid',color='r',edgecolor='none',alpha=0.7)
plt.hist(esh,bins=bins,align='mid',color='b',edgecolor='none',alpha=0.7)
#plt.axvspan(79.55,85.25,color='g',alpha=0.2) #G09
#plt.errorbar(82.4,1.5,xerr=2.85,ls='none',color='k',capsize=5,linewidth=2.5,alpha=0.6) #G09

#plt.arrow(82.4,1.5,2.85,0,width=0.1,head_width=0.6,head_length=0.01,color='k',linewidth=0.5,alpha=0.8) #G09
#plt.arrow(82.4,1.5,-2.85,0,width=0.1,head_width=0.6,head_length=0.01,color='k',linewidth=0.5,alpha=0.8) #G09
#plt.axvspan(77.95,81.25,color='g',alpha=0.3) 
#plt.axvline(77.95,color='g',alpha=1,linewidth=1.5,linestyle='dashed')
#plt.axvline(81.25,color='g',alpha=1,linewidth=1.5,linestyle='dashed')
#plt.axvline(76.0,color='orange',alpha=1,linewidth=1.5,linestyle='dashed')

ax1.set_xlim([66,130])
#ax1.set_ylim([0,60])
ax1.set_xticks(np.arange(66,130.1,4))
#ax1.set_yticks(np.arange(0,60.1,5))
ax1.set_xlabel(r'$P_{\rm orb}$ (mins)', fontsize=15)
ax1.set_ylabel(r'$N_{\rm sys}$', fontsize=15)

ax1.plot(bins_2, p*60, 'k', linewidth=1)

#ax2 = ax1.twinx()
#ax2.set_xlim([66,130])
# plot the cumulative function
#ax2.plot(base[:-1], cumulative/67.0, c='b',alpha=1,linewidth=1.2)
#ax2.set_ylabel(r'$N_{\rm sys}$ / $\Sigma(N_{\rm sys})$', fontsize=15)
#ax2.set_ylim([0,1])

plt.subplots_adjust(bottom=0.09, top=0.985, left=0.07, right=0.925)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.savefig("porb_hist.pdf")
plt.show()
 