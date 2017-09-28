import numpy as np
from scipy import optimize as opt


def psi_conv(q, m2):
    a = np.log(1.0+q**(1.0/30.))
    b = 0.5*(q**(1.0/3.0)/(1.0+q**(1.0/3.0)))
    c = 0.6*q**(2.0/3.0) + np.log(1.0+q**(1.0/3.0))
    return (2.0/3.0)*((a-b)/c)*(1.0+q) + 2.0*(q-1.0)


def psi_class(q, m2):
    a = np.log(1.0+q**(1.0/3.0))
    b = 0.5*(q**(1.0/3.0)/(1+q**(1.0/3.0)))
    c = 0.6*q**(2.0/3.0) + np.log(1.0+q**(1.0/3.0))
    return (2.0/3.0)*((a-b)/c) + 2.0*q/(1.0+1.0/q) + 1.0/(1.0+1.0/q) - 2.0


def psi_caml(q, m2):
    m1 = m2/q
    nu = 0.35/m1
    a = np.log(1.0+q**(1.0/3.0))
    b = 0.5*(q**(1.0/3.0)/(1.0+q**(1.0/3.0)))
    c = 0.6*q**(2.0/3.0) + np.log(1.0+q**(1.0/3.0))
    return (2.0/3.0)*((a-b)/c) + 2.0*nu + 1.0/(1.0+1.0/q) - 2.0


def politano96(m2):
    return 4.488*(m2-0.4342)**1.364 - 1.0/3.0


def qcrit(func):
    m2v = np.linspace(0.001, 0.8, 100)
    qcrit = []
    for m2 in m2v:
        psi_ad = -1.0/3.0 if m2 < 0.4342 else politano96(m2)
        fitfunc = lambda x: func(x, m2) - psi_ad
        qcritcand = opt.newton(fitfunc, 0.7)
        if m2/qcritcand > 1.44:
            qcrit.append(m2/1.44)
        else:
            qcrit.append(qcritcand)
    return m2v, np.array(qcrit)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    m2, qc = qcrit(psi_conv)
    plt.plot(m2, qc, label='conservative')
    m2, qc = qcrit(psi_class)
    plt.plot(m2, qc, label='non-conservative')
    m2, qc = qcrit(psi_caml)
    plt.plot(m2, qc, label='CAML')
    plt.legend()
    plt.xlabel('M2')
    plt.ylabel('q')
    plt.show()
