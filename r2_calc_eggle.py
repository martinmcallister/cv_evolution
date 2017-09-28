import math
import numpy as np

def R2_calc(P_orb,M2,q):
    return 0.2478 * ((P_orb*24)**(2.0/3.0)) * (M2**(1.0/3.0)) * \
        (((q**(1.0/3.0))*((1+q)**(1.0/3.0)))/((0.6*(q**(2.0/3.0)))+np.log(1+(q**(1.0/3.0)))))
    
def R2_err_calc(P_orb,P_orb_err,M2,M2_err,R2,q,q_err):
    return R2*np.sqrt(((2.0/3.0)*(P_orb_err/P_orb))**2+((1.0/3.0)*(M2_err/M2))**2)

P_orb = input ("Porb(d): ")
P_orb_err = input ("Porb_err: ")
q = input ("q: ")
q_err = input ("q_err: ")
M2 = input ("M2: ")
M2_err = input ("M2_err: ")
R2 = R2_calc(P_orb,M2,q)
R2_err = R2_err_calc(P_orb,P_orb_err,M2,M2_err,R2,q,q_err)

print "R2: ", R2
print "R2_err: ", R2_err
