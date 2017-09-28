import math

def eps_calc(P_orb,P_sh):
    return (P_sh - P_orb)/P_orb
    
def eps_err_calc(P_orb,P_orb_err,P_sh,P_sh_err,epsilon):
    return epsilon*math.sqrt((math.sqrt(P_sh_err**2+P_orb_err**2)/(P_sh-P_orb))**2+(P_orb_err/P_orb)**2)

P_orb = input ("Porb: ")
P_orb_err = input ("Porb_err: ")
P_sh = input ("Psh: ")
P_sh_err = input ("Psh_err: ")
epsilon = eps_calc(P_orb,P_sh)
epsilon_err = eps_err_calc(P_orb,P_orb_err,P_sh,P_sh_err,epsilon)

print "Epsilon: ", epsilon
print "Epsilon_err: ", epsilon_err
