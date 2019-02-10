# -*- coding: utf-8 -*-
"""
DFT of sinc and square function
"""

from numpy import sinc,linspace,angle,arange
from scipy.fftpack import fft
import matplotlib.pyplot as plt

fs=int(input('sampling rate of sinc:'))

n1=arange(0,5,1/fs)
x1=sinc(n1)
N1=len(n1)
X1k=fft(x1,N1)

plt.stem(n1,x1)
plt.title('sinc input')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.show()

plt.stem(n1*fs,abs(X1k))
plt.title('Frequency domain representation')
plt.xlabel('K')
plt.ylabel('X(K)')
plt.show()

plt.stem(n1*fs,angle(X1k))
plt.title('Phase response')
plt.xlabel('Phase')
plt.ylabel('<X(K)')
plt.show()

