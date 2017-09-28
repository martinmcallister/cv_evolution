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

plt.axis([0,0.08,0,0.4])


### Patterson et al. 2005 ###
'''
plt.scatter(0.0047,0.037,marker='o',color='k',s=12)
plt.errorbar(0.0047,0.037,xerr=0.0009,yerr=0.007,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0047,0.037,'  KV UMa',color='k',size=12)

plt.scatter(0.0330,0.15,marker='o',color='k',s=12)
plt.errorbar(0.0330,0.15,xerr=0.0030,yerr=0.01,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0330,0.15,'  HT Cas',color='k',size=12)

plt.scatter(0.030,0.19,marker='o',color='k',s=12)
plt.errorbar(0.030,0.19,xerr=0.002,yerr=0.03,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.030,0.19,'  V2051 Oph',color='k',size=12)

plt.scatter(0.0644,0.28,marker='o',color='k',s=12)
plt.errorbar(0.0644,0.28,xerr=0.0020,yerr=0.04,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0644,0.28,'  DW UMa',color='k',size=12)

plt.scatter(0.0702,0.30,marker='o',color='k',s=12)
plt.errorbar(0.0702,0.30,xerr=0.0019,yerr=0.07,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0702,0.30,'  UU Aqr',color='k',size=12)

plt.scatter(0.0939,0.38,marker='o',color='k',s=12)
plt.errorbar(0.0939,0.38,xerr=0.0015,yerr=0.02,uplims=True,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0939,0.38,'  BB Dor',color='k',size=12)

plt.scatter(0.0092,0.050,marker='o',color='k',s=12)
plt.errorbar(0.0092,0.050,xerr=0.0008,yerr=0.015,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0092,0.050,'  WZ Sge',color='k',size=12)

# Altered slightly in K06
plt.scatter(0.0270,0.111,marker='o',color='k',s=12)
plt.errorbar(0.0270,0.111,xerr=0.0015,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0270,0.111,'  XZ Eri',color='k',size=12)

plt.scatter(0.0260,0.125,marker='o',color='k',s=12)
plt.errorbar(0.0260,0.125,xerr=0.0010,yerr=0.008,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0260,0.125,'  IY UMa',color='k',size=12)

plt.scatter(0.0364,0.145,marker='o',color='k',s=12)
plt.errorbar(0.0364,0.145,xerr=0.0009,yerr=0.015,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0364,0.145,'  Z Cha',color='k',size=12)

# Altered slightly in K06
plt.scatter(0.0343,0.152,marker='o',color='k',s=12)
plt.errorbar(0.0343,0.152,xerr=0.0010,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0343,0.152,'  DV UMa',color='k',size=12)

plt.scatter(0.0326,0.175,marker='o',color='k',s=12)
plt.errorbar(0.0326,0.175,xerr=0.0015,yerr=0.025,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0326,0.175,'  OU Vir',color='k',size=12)


### Updated (C) ###

# epsilon = C (K09), porb from Wagner et al. 2001
#plt.scatter(0.00265,0.037,marker='o',color='b',s=12,alpha=0.3)
#plt.errorbar(0.00265,0.037,xerr=0.00018,yerr=0.007,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.00265,0.037,'  KV UMa',color='b',size=12,alpha=0.3)

# epsilon = C (2016), q from Horne91 (timing)
plt.scatter(0.03040,0.15,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.03040,0.15,xerr=0.00007,yerr=0.01,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.03040,0.15,'  HT Cas',color='b',size=12,alpha=0.3)

# epsilon = C (2015), q from Baptista98 (timing)
plt.scatter(0.0275,0.19,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.0275,0.19,xerr=0.0007,yerr=0.03,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0275,0.19,'  V2051 Oph',color='b',size=12,alpha=0.3)

# q from Araujo-Betancour03 & Patterson05 (timing & epsilon)
#plt.scatter(0.0644,0.28,marker='s',color='b',s=12,alpha=0.3)
#plt.errorbar(0.0644,0.28,xerr=0.0020,yerr=0.04,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0644,0.28,'  DW UMa',color='b',size=12,alpha=0.3)

# Porb from Baptista08, Psh from Patterson05, q from Baptista04 (timing)
#plt.scatter(0.0690,0.30,marker='s',color='b',s=12,alpha=0.3)
#plt.errorbar(0.0690,0.30,xerr=0.0011,yerr=0.07,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0690,0.30,'  UU Aqr',color='b',size=12,alpha=0.3)

#New epsilon from Rodriguez-Gil12
#plt.scatter(0.0593,0.38,marker='o',color='b',s=12,alpha=0.3)
#plt.errorbar(0.0593,0.38,xerr=0.0005,yerr=0.02,uplims=True,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0593,0.38,'  BB Dor',color='b',size=12,alpha=0.3)

# epsilon = C (2007), q from Savoury11
plt.scatter(0.0244,0.118,marker='o',color='k',s=12)
plt.errorbar(0.0244,0.118,xerr=0.0019,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0244,0.118,'  XZ Eri',color='k',size=12)

# epsilon = C (2009)
plt.scatter(0.02463,0.144,marker='o',color='g',s=12)
plt.errorbar(0.02463,0.144,xerr=0.00026,yerr=[[0.001],[0.009]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.02463,0.144,'  IY UMa',color='g',size=12)

# epsilon = C (2014)
plt.scatter(0.0329,0.189,marker='o',color='g',s=12)
plt.errorbar(0.0329,0.189,xerr=0.0003,yerr=0.004,ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0329,0.189,'  Z Cha',color='g',size=12)

# epsilon = C (1997)
plt.scatter(0.0298,0.172,marker='o',color='g',s=12)
plt.errorbar(0.0298,0.172,xerr=0.0004,yerr=[[0.007],[0.002]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0298,0.172,'  DV UMa',color='g',size=12)

### Additional (C) ###

# epsilon = C (2016)
plt.scatter(0.0209,0.106,marker='o',color='g',s=12)
plt.errorbar(0.0209,0.106,xerr=0.0008,yerr=[[0.003],[0.001]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0209,0.106,'  OY Car',color='g',size=12)

# epsilon = C (2009), q from Savoury11
plt.scatter(0.0210,0.1099,marker='o',color='k',s=12)
plt.errorbar(0.0210,0.1099,xerr=0.0003,yerr=0.0007,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0210,0.1099,'  SDSS 1502',color='k',size=12)

# epsilon = C (2007), q from Savoury11
plt.scatter(0.0229,0.1115,marker='o',color='k',s=12)
plt.errorbar(0.0229,0.1115,xerr=0.0007,yerr=0.0016,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0229,0.1115,'  SDSS 1227',color='k',size=12)

# epsilon = C (2010), q from Savoury11
plt.scatter(0.0169,0.113,marker='o',color='k',s=12)
plt.errorbar(0.0169,0.113,xerr=0.0008,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0169,0.113,'  SDSS 0903',color='k',size=12)

# epsilon = C (2017)
plt.scatter(0.03195,0.153,marker='o',color='g',s=12)
plt.errorbar(0.03195,0.153,xerr=0.00028,yerr=[[0.011],[0.015]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.03195,0.153,'  SDSS 1152',color='g',size=12)

# epsilon = C (2011)
plt.scatter(0.0190,0.105,marker='o',color='g',s=12)
plt.errorbar(0.0190,0.105,xerr=0.0007,yerr=[[0.005],[0.006]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0190,0.105,'  CSS110113',color='g',size=12)

# epsilon = C (2012)
plt.scatter(0.0365,0.182,marker='o',color='g',s=12)
plt.errorbar(0.0365,0.182,xerr=0.0013,yerr=[[0.004],[0.009]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0365,0.182,'  SDSS 0901',color='g',size=12)

# epsilon = C (2015)
plt.scatter(0.026,0.152,marker='o',color='g',s=12)
plt.errorbar(0.026,0.152,xerr=0.004,yerr=[[0.002],[0.014]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.026,0.152,'  SSS130413',color='g',size=12)

# epsilon = C (2004), q from Borges&Baptista05 (timing)
plt.scatter(0.0271,0.125,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.0271,0.125,xerr=0.0011,yerr=0.015,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0271,0.125,'  V4140 Sgr',color='b',size=12,alpha=0.3)
'''

### Updated (B) ###

# epsilon = B (K09), porb from Wagner et al. 2001
#plt.scatter(0.00371,0.037,marker='o',color='b',s=12,alpha=0.3)
#plt.errorbar(0.00371,0.037,xerr=0.00018,yerr=0.007,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.00371,0.037,'  KV UMa',color='b',size=12,alpha=0.3)

# epsilon = B (2016), q from Horne91 (timing)
plt.scatter(0.03647,0.15,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.03647,0.15,xerr=0.00007,yerr=0.01,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.03647,0.15,'  HT Cas',color='b',size=12,alpha=0.3)

# epsilon = B (2015), q from Baptista98 (timing)
plt.scatter(0.0365,0.19,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.0365,0.19,xerr=0.0014,yerr=0.03,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0365,0.19,'  V2051 Oph',color='b',size=12,alpha=0.3)

#q from Araujo-Betancour03 & Patterson05 (timing & epsilon)
plt.scatter(0.0643,0.28,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.0643,0.28,xerr=0.0010,yerr=0.04,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0643,0.28,'  DW UMa',color='b',size=12,alpha=0.3)

# Porb from Baptista08, Psh from Patterson05
plt.scatter(0.0690,0.30,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.0690,0.30,xerr=0.0011,yerr=0.07,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0690,0.30,'  UU Aqr',color='b',size=12,alpha=0.3)

#New epsilon from Rodriguez-Gil12
#plt.scatter(0.0593,0.38,marker='o',color='b',s=12,alpha=0.3)
#plt.errorbar(0.0593,0.38,xerr=0.0005,yerr=0.02,uplims=True,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0593,0.38,'  BB Dor',color='b',size=12,alpha=0.3)

# epsilon = B (2001), q from Steeghs07
#plt.scatter(0.009105,0.092,marker='^',color='b',s=12,alpha=0.3)
#plt.errorbar(0.009105,0.092,xerr=0.000009,yerr=0.008,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.009105,0.092,'  WZ Sge',color='b',size=12,alpha=0.3)

# epsilon = B (2001), q from Steeghs01
plt.scatter(0.009105,0.057,marker='^',color='b',s=12,alpha=0.3)
plt.errorbar(0.009105,0.057,xerr=0.000009,yerr=0.018,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.009105,0.057,'  WZ Sge',color='b',size=12,alpha=0.3)

# epsilon = B (2007), q from Savoury11
plt.scatter(0.0269,0.118,marker='o',color='k',s=12)
plt.errorbar(0.0269,0.118,xerr=0.0003,yerr=0.003,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0269,0.118,'  XZ Eri',color='k',size=12)

# epsilon = B (2009)
plt.scatter(0.0311,0.144,marker='o',color='g',s=12)
plt.errorbar(0.0311,0.144,xerr=0.0003,yerr=[[0.001],[0.009]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0311,0.144,'  IY UMa',color='g',size=12)

# epsilon = B (2014)
plt.scatter(0.0384,0.189,marker='o',color='g',s=12)
plt.errorbar(0.0384,0.189,xerr=0.0011,yerr=0.004,ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0384,0.189,'  Z Cha',color='g',size=12)

# epsilon = B (1997)
plt.scatter(0.0343,0.172,marker='o',color='g',s=12)
plt.errorbar(0.0343,0.172,xerr=0.0003,yerr=[[0.007],[0.002]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0343,0.172,'  DV UMa',color='g',size=12)

# epsilon = B (2003), q from Savoury11
plt.scatter(0.03034,0.1641,marker='o',color='k',s=12)
plt.errorbar(0.03034,0.1641,xerr=0.00023,yerr=0.0013,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.03034,0.1641,'  OU Vir',color='k',size=12)


### Additional (B) ###

# epsilon = B (2016)
plt.scatter(0.0243,0.106,marker='o',color='g',s=12)
plt.errorbar(0.0243,0.106,xerr=0.0004,yerr=[[0.003],[0.001]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0243,0.106,'  OY Car',color='g',size=12)

# epsilon = B (2009), q from Savoury11
plt.scatter(0.02637,0.1099,marker='o',color='k',s=12)
plt.errorbar(0.02637,0.1099,xerr=0.00022,yerr=0.0007,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.02637,0.1099,'  SDSS 1502',color='k',size=12)

# epsilon = B (2007), q from Savoury11
plt.scatter(0.0261,0.1115,marker='o',color='k',s=12)
plt.errorbar(0.0261,0.1115,xerr=0.0005,yerr=0.0016,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0261,0.1115,'  SDSS 1227',color='k',size=12)

# epsilon = B (2005), q from Savoury11
plt.scatter(0.0498,0.248,marker='o',color='k',s=12)
plt.errorbar(0.0498,0.248,xerr=0.0008,yerr=0.005,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0498,0.248,'  SDSS 1702',color='k',size=12)

# epsilon = B (2010), q from Savoury11
plt.scatter(0.0218,0.113,marker='o',color='k',s=12)
plt.errorbar(0.0218,0.113,xerr=0.0008,yerr=0.004,ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0218,0.113,'  SDSS 0903',color='k',size=12)

# epsilon = B (2017)
plt.scatter(0.0386,0.153,marker='o',color='g',s=12)
plt.errorbar(0.0386,0.153,xerr=0.0006,yerr=[[0.011],[0.015]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0386,0.153,'  SDSS 1152',color='g',size=12)

# epsilon = B (2011)
plt.scatter(0.0232,0.105,marker='o',color='g',s=12)
plt.errorbar(0.0232,0.105,xerr=0.0004,yerr=[[0.005],[0.006]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0232,0.105,'  CSS110113',color='g',size=12)

# epsilon = B (2012)
plt.scatter(0.0412,0.182,marker='o',color='g',s=12)
plt.errorbar(0.0412,0.182,xerr=0.0006,yerr=[[0.004],[0.009]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0412,0.182,'  SDSS 0901',color='g',size=12)

# epsilon = B (2014)
plt.scatter(0.0290,0.161,marker='o',color='g',s=12)
plt.errorbar(0.0290,0.161,xerr=0.0009,yerr=[[0.013],[0.012]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0290,0.161,'  ASASSN-14ag',color='g',size=12)

# epsilon = B (2015)
plt.scatter(0.0173,0.095,marker='o',color='g',s=12)
plt.errorbar(0.0173,0.095,xerr=0.0015,yerr=[[0.004],[0.003]],ls='none',color='g',capsize=None,linewidth=1)
#plt.text(0.0173,0.095,'  SSS100615',color='g',size=12)

# epsilon = B (2004), q from Borges&Baptista05 (timing)
plt.scatter(0.0339,0.125,marker='s',color='b',s=12,alpha=0.3)
plt.errorbar(0.0339,0.125,xerr=0.0007,yerr=0.015,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0339,0.125,'  V4140 Sgr',color='b',size=12,alpha=0.3)

#Excess calculated from Rolfe00, q from Rodriguez-gil01 (no error given -- 20% error used)
plt.scatter(0.0661,0.31,marker='^',color='b',s=12,alpha=0.3)
plt.errorbar(0.0661,0.31,xerr=0.0005,yerr=0.06,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0661,0.31,'  V348 Pup',color='b',size=12,alpha=0.3)

#Porb from Peters06, Psh from Patterson..., q from Arenas00
plt.scatter(0.0627,0.24,marker='^',color='b',s=12,alpha=0.3)
plt.errorbar(0.0627,0.24,xerr=0.0005,yerr=0.05,ls='none',color='b',capsize=None,alpha=0.3,linewidth=1)
#plt.text(0.0627,0.24,'  V603 Aql',color='b',size=12,alpha=0.3)


# Psh = 0.046756(3) - (27-31/03)
#plt.scatter(0.01076,0.0647,marker='o',color='k',s=12)
#plt.errorbar(0.01076,0.0647,xerr=0.00006,yerr=[[0.0018],[0.0018]],ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.01076,0.0647,'  SDSS 1507/OV BOO',color='k',size=12)

# Psh = 0.046851(4) - (1-3/04)
#plt.scatter(0.01281,0.0647,marker='o',color='k',s=12)
#plt.errorbar(0.01281,0.0647,xerr=0.00009,yerr=[[0.0018],[0.0018]],ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.01281,0.0647,'  SDSS 1507/OV BOO',color='k',size=12)

# Psh = 0.046966(2) - just prior to fading (13/04)
#plt.scatter(0.01530,0.0647,marker='o',color='r',s=12)
#plt.errorbar(0.01530,0.0647,xerr=0.00004,yerr=[[0.0018],[0.0018]],ls='none',color='r',capsize=None,linewidth=1)
#plt.text(0.01530,0.0647,'  SDSS 1507/OV BOO',color='r',size=12)

# Psh = 0.04693(4) - fading (15/04)
#plt.scatter(0.0145,0.0647,marker='o',color='r',s=12)
#plt.errorbar(0.0145,0.0647,xerr=0.0009,yerr=[[0.0018],[0.0018]],ls='none',color='r',capsize=None,linewidth=1)
#plt.text(0.0145,0.0647,'  SDSS 1507/OV BOO',color='r',size=12)

# Psh = 0.046894(112) - weighted mean for 27/03-13/04
#plt.scatter(0.0137,0.0647,marker='o',color='k',s=12)
#plt.errorbar(0.0137,0.0647,xerr=0.0011,yerr=[[0.0018],[0.0018]],ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.0137,0.0647,'  SDSS 1507/OV BOO',color='r',size=12)

# Psh = 0.046825(4) - From Patterson pre-print
plt.scatter(0.01225,0.0647,marker='o',color='k',s=12)
plt.errorbar(0.01225,0.0647,xerr=0.00009,yerr=[[0.0018],[0.0018]],ls='none',color='k',capsize=None,linewidth=1)
#plt.text(0.01225,0.0647,'  SDSS 1507/OV BOO',color='r',size=12)


'''
# epsilon = B (2014)
plt.scatter(0.01560,0.01,marker='o',color='r',s=12)
plt.errorbar(0.01560,0.01,xerr=0.00020,ls='none',color='r',capsize=None,linewidth=1)
#plt.text(0.01560,0.01,'  MAS OT 0057',color='g',size=12)

# epsilon = B (2016)
plt.scatter(0.01333,0.01,marker='o',color='r',s=12)
plt.errorbar(0.01333,0.01,xerr=0.00022,ls='none',color='r',capsize=None,linewidth=1)
#plt.text(0.01333,0.01,'  ASASSN-15ux',color='g',size=12)

# epsilon = B (2016)
plt.scatter(0.0461,0.01,marker='o',color='r',s=12)
plt.errorbar(0.0461,0.01,xerr=0.0008,ls='none',color='r',capsize=None,linewidth=1)
#plt.text(0.0461,0.01,'  ASASSN-15sl',color='g',size=12)

# epsilon = B (2012)
plt.scatter(0.0542,0.01,marker='o',color='r',s=12)
plt.errorbar(0.0542,0.01,xerr=0.0011,ls='none',color='r',capsize=None,linewidth=1)
#plt.text(0.0542,0.01,'  TCP J0846',color='g',size=12)
'''

# Fit new linear relation
new_epsilon = np.loadtxt('epsilon-q.dat',dtype=float,usecols = [0])
new_epsilon_err = np.loadtxt('epsilon-q.dat',dtype=float,usecols = [1])
new_q = np.loadtxt('epsilon-q.dat',dtype=float,usecols = [2])
new_q_err = np.loadtxt('epsilon-q.dat',dtype=float,usecols = [3])


def chisqfunc((a,b)):
    chisq = np.sum(((new_q - a - b*(new_epsilon-0.025))**2) / ((new_q_err**2) + (b**2)*(new_epsilon_err**2) + 0.0118**2))
    red_chisq = chisq / (len(new_epsilon)-2)
    print red_chisq
    #print chisq
    return chisq
  
x0 = np.array([0.1,4])

#a = 0.11841631  #0.0
#b = 4.72856594 #0.0
#result = chisqfunc((a,b))

result = opt.minimize(chisqfunc,x0)
print result.x
a,b = result.x
'''
# B superhumps
a = 0.118 + 0.003 # Error from delta(chisq) = 1
b = 4.45 + 0.28     # Error from delta(chisq) = 1
sigma = 0.012 (0.0118)
c = chisqfunc((a,b))

# C superhumps
a = 0.135 + 0.004 # Error from delta(chisq) = 1
b = 5.0 + 0.7     # Error from delta(chisq) = 1
sigma = 0.012 (0.0118)
c = chisqfunc((a,b))
'''
# Plot linear fits from K06 and current data
epsilon = np.arange(0,0.11,0.001)
q_k06 = 0.114 + 3.97*(epsilon-0.025)
q_k06_poserr = 0.114 + 4.38*(epsilon-0.025)
q_k06_negerr = 0.114 + 3.56*(epsilon-0.025)
q = np.arange(0,0.5,0.001)
epsilon_kato09 = (0.16*q) + (0.25*(q**2))
q_kato13 = 0.035 + 3.09*epsilon
new_q_fit = a + b*(epsilon-0.025)
new_q_fit_poserr = a + (b+0.28)*(epsilon-0.025)
new_q_fit_negerr = a + (b-0.28)*(epsilon-0.025)

plt.plot(epsilon,q_k06,color='k',linewidth=1,linestyle='dashed',alpha=0.3)
#plt.fill_between(epsilon,q_k06_negerr,q_k06_poserr,color='k',alpha=0.1)
#plt.plot(epsilon_kato09,q,color='b',linewidth=1)
#plt.plot(epsilon,q_kato13,color='b',linewidth=1)
plt.plot(epsilon,new_q_fit,color='r',linewidth=1)
plt.fill_between(epsilon,new_q_fit_negerr,new_q_fit_poserr,color='r',alpha=0.1)

plt.xlabel(r'$\epsilon = (P_{\rm sh} - P_{\rm orb}) / P_{\rm orb}$ ', fontsize=16)
plt.ylabel(r'$q$ = $M_{2} / M_{1}$', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=14, width=1.0)
plt.tick_params(top='on',right='on')

plt.subplots_adjust(bottom=0.11, top=0.97, left=0.10, right=0.97)
#for axis in ['top','bottom','left','right']:
# plt.subplot(1,1,1).spines[axis].set_linewidth(1.5)
plt.axes().set_aspect('auto')
plt.savefig("epsilon-q.pdf")
plt.show()
