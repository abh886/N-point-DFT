# -*- coding: utf-8 -*-
"""
Calculating DFT without FFT function
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

xn = [1,-1,2,3,4]
N = 8
pp = fft(xn,n=8)
for ix in range(len(xn)):
    if len(xn)<N:
        xn.append((N-len(xn))*0)

for k in range(0,N):
    yn=0
    o=[]
    for n in range(0,N):
        yn = yn + np.sum(xn[n] * np.exp(-1j*2*np.pi*k*n/N))
        o.append(yn)

# for p in range(len(o)):
#     ab=0
#     a=[]
#     for q in range(0,N-1):
#         ab = ()
#         a.append(ab)

        
plt.stem(xn,use_line_collection = True)
plt.title('input sequence')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()

plt.stem(np.abs(o),use_line_collection = True)
plt.title('DFT seq')
plt.xlabel('K')
plt.ylabel('Amplitude')
plt.show()