# N point DFT


"""N point DFT using Fast Fourier Transform"""

import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

xn=[1,2,3,4]

N=int(input('how many point dft:'))

Xk=fft(xn,N)

plt.stem(xn)
plt.title('DFT seq')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()


B=np.absolute(Xk)

# Expected values

#10.          7.25447565  2.82842712  2.71525008  2.          2.71525008
#2.82842712  7.25447565


plt.stem(B)
print(B)
plt.title('magnitude')
plt.xlabel('K')
plt.ylabel('X(K)')
plt.show()

C=np.angle(Xk)
plt.stem(C)
print(C)

#Expected values
# 0.         -1.62792505  2.35619449 -0.47535306  3.14159265  0.47535306
#-2.35619449  1.62792505
