import matplotlib.pyplot as plt
import numpy as np
from random import uniform
fig, ax = plt.subplots()

A = ( (4, 0), 
      (3, 2) ) #�����s��
N = 20
T = 10000

epsilon = 0.2

x = [0.0]

for t in range(T):
    if x[t] / N > uniform(0, 1): #true=�s����I�ׂ�l�������_�ōs���u�P�v������Ă���.
        if epsilon > uniform(0, 1): #true=�ˑR�ψك��[�h,false=�ʏ�̗������胂�[�h
            if 0.5 > uniform(0, 1):
                x.append(x[t])
            else:
                x.append(x[t] - 1)
        else:
            x.append(x[t] - 1 + (np.dot(A, (N - x[t], x[t] - 1))).argmax()) #��������F�����������ꍇ�͎Ⴂ�ԍ��̍s�����̗p
    else:                        #false=�s����I�ׂ�l�������_�ōs���u�O�v������Ă���.
        if epsilon > uniform(0, 1):
            if 0.5 > uniform(0, 1):
                x.append(x[t])
            else:
                x.append(x[t] + 1)
        else:
            x.append(x[t] + (np.dot(A, (N - x[t] - 1, x[t]))).argmax())
ax.plot(x, 'r-')
plt.show()
        
            

