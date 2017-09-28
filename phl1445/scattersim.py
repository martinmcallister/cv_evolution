import numpy as np
import matplotlib.pyplot as plt

ncond1 = 0
ncond2 = 0
i = 0


for i in range(0,100000):
    samples = np.random.normal(size=6)
    print samples
    x = 0
    y = 0
    if samples[0] < -1.5:
        x += 1
    if samples[1] < -1.5:
        x += 1 
    if samples[2] < -1.5:
        x += 1 
    if samples[3] < -1.5:
        x += 1
    if samples[4] < -1.5:
        x += 1
    if samples[5] < -1.5:
        x += 1
    if samples[0] < -2.3:
        y += 1
    if samples[1] < -2.3:
        y += 1
    if samples[2] < -2.3:
        y += 1
    if samples[3] < -2.3:
        y += 1
    if samples[4] < -2.3:
        y += 1
    if samples[5] < -2.3:
        y += 1
    if x >= 2:
        ncond1 += 1
    if y >= 1:
        ncond2 += 1
    i += 1

print ncond1
print ncond2


