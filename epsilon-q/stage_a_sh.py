import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import scipy.optimize as opt

'''p_orb = np.loadtxt('stage_a_sh.dat',dtype=float,usecols = [0])
p_orb_err = np.loadtxt('stage_a_sh.dat',dtype=float,usecols = [1])
p_sh = np.loadtxt('stage_a_sh.dat',dtype=float,usecols = [2])
p_sh_err = np.loadtxt('stage_a_sh.dat',dtype=float,usecols = [3])

ep_ast = 1 - (p_orb/p_sh)
ep_ast_err = (p_orb/p_sh)*np.sqrt((p_orb_err/p_orb)**2+(p_sh_err/p_sh)**2)

#for i in range(len(ep_ast)):
    #print ep_ast[i]
    #print ep_ast_err[i]

q = -0.0016 + 2.60*ep_ast + 3.33*(ep_ast**2) + 79.0*(ep_ast**3)
q_err = np.sqrt(((2.60*ep_ast_err)**2)+((2*3.33*ep_ast*ep_ast_err)**2)+((3*79.0*(ep_ast**2)*ep_ast_err)**2))

for i in range(len(q)):
    #print q[i]
    print q_err[i]
'''

# 2010
plt.scatter(0.199,0.15,marker='o',color='k',s=20)
plt.errorbar(0.199,0.15,xerr=0.023,yerr=0.01,ls='none',color='k',capsize=3)
#plt.text(0.199,0.15,'  HT Cas',color='k',size=12)

# 2001
plt.scatter(0.0785,0.092,marker='o',color='k',s=20)
plt.errorbar(0.0785,0.092,xerr=0.0026,yerr=0.008,ls='none',color='k',capsize=3)
#plt.text(0.0785,0.092,'  WZ Sge',color='k',size=12)

# 2008
plt.scatter(0.191,0.118,marker='o',color='k',s=20)
plt.errorbar(0.191,0.118,xerr=0.008,yerr=0.003,ls='none',color='k',capsize=3)
#plt.text(0.191,0.118,'  XZ Eri',color='k',size=12)

#2000
plt.scatter(0.100,0.144,marker='o',color='k',s=20)
plt.errorbar(0.100,0.144,xerr=0.005,yerr=[[0.001],[0.009]],ls='none',color='k',capsize=3)
#plt.text(0.100,0.144,'  IY UMa',color='k',size=12)

#2009
plt.scatter(0.120,0.144,marker='o',color='k',s=20)
plt.errorbar(0.120,0.144,xerr=0.005,yerr=[[0.001],[0.009]],ls='none',color='k',capsize=3)
#plt.text(0.120,0.144,'  IY UMa',color='k',size=12)

#2014
plt.scatter(0.227,0.189,marker='o',color='k',s=20)
plt.errorbar(0.227,0.189,xerr=0.010,yerr=0.004,ls='none',color='k',capsize=3)
#plt.text(0.227,0.189,'  Z Cha',color='k',size=12)

#2008
plt.scatter(0.107,0.172,marker='o',color='k',s=20)
plt.errorbar(0.107,0.172,xerr=0.005,yerr=[[0.007],[0.002]],ls='none',color='k',capsize=3)
#plt.text(0.107,0.172,'  DV UMa',color='k',size=12)

#2007
plt.scatter(0.117,0.1115,marker='o',color='k',s=20)
plt.errorbar(0.117,0.1115,xerr=0.003,yerr=0.0016,ls='none',color='k',capsize=3)
#plt.text(0.117,0.1115,'  SDSS 1227',color='k',size=12)

#2011 
plt.scatter(0.1693,0.248,marker='o',color='k',s=20)
plt.errorbar(0.1693,0.248,xerr= 0.0027,yerr=0.005,ls='none',color='k',capsize=3)
#plt.text(0.1693,0.248,'  SDSS 1702',color='k',size=12)

#2012
plt.scatter(0.227,0.182,marker='o',color='k',s=20)
plt.errorbar(0.227,0.182,xerr=0.003,yerr=[[0.004],[0.009]],ls='none',color='k',capsize=3)
#plt.text(0.227,0.182,'  SDSS 0901',color='k',size=12)

#2015
plt.scatter(0.0844,0.095,marker='o',color='k',s=20)
plt.errorbar(0.0844,0.095,xerr=0.0008,yerr=[[0.004],[0.003]],ls='none',color='k',capsize=3)
#plt.text(0.0844,0.095,'  SSS100615',color='k',size=12)

q_e = np.arange(0,0.3,0.001)
q_sh = np.arange(0,0.3,0.001)
plt.plot(q_e,q_sh,linestyle='dashed',color='r',linewidth=1)
plt.axis([0,0.3,0,0.3])
plt.xlabel(r'q (from sh)')
plt.ylabel(r'q (from ecl)')
plt.show()