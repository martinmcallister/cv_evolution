import math

def R2_calc(P_orb,M2):
    return 0.2377*((P_orb*24)**(2.0/3.0))*(M2**(1.0/3.0))
    
def R2_err_calc(P_orb,P_orb_err,M2,M2_err,R2):
    return R2*math.sqrt(((2.0/3.0)*(P_orb_err/P_orb))**2+((1.0/3.0)*(M2_err/M2))**2)

P_orb = input ("Porb(d): ")
P_orb_err = input ("Porb_err: ")
M2 = input ("M2: ")
M2_err = input ("M2_err: ")
R2 = R2_calc(P_orb,M2)
R2_err = R2_err_calc(P_orb,P_orb_err,M2,M2_err,R2)

print "R2: ", R2
print "R2_err: ", R2_err
