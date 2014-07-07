import matplotlib.pyplot as plt
import numpy as np
from random import uniform
fig, ax = plt.subplots()

class random: #�ψك��[�h�̍s���ω�
    def __init__(self, current_action):
        if current_action == 0:
            self.choice = (0.5 < uniform(0, 1)) * 1.0 + (0.5 >= uniform(0, 1)) * 0.0
        elif current_action == 1:
            self.choice = (0.5 < uniform(0, 1)) * (-1.0) + (0.5 >= uniform(0, 1)) * 0.0
        else:
            self.choice = 0.0

class judge: #�ʏ�̗������f���[�h�̍s���ω�
    def __init__(self, current_action):
        if current_action == 0:
            self.choice = (np.dot(A, (N - x[t] - 1, x[t]))).argmax()
        elif current_action == 1:
            self.choice = -1.0 + (np.dot(A, (N - x[t] - 1, x[t]))).argmax()
        else:
            self.choice = 0.0
            
A = ( (4, 0), 
      (3, 2) ) #�����s��
N = 20
T = 10000

epsilon = 0.2

x = [0.0]

for t in range(T):
    current_action = x[t] / N > uniform(0, 1) #2x2�̏ꍇ�͍s�����O���P�Ȃ̂ŁAfalse��true�ɑΉ�������B3x3�ɂ����Ƃ��͂����𒼂��B
    
    if epsilon > uniform(0, 1): #true����random(�ψك��[�h�j,false����judge(�ʏ�̗������f���[�h)�B
        mode = random(current_action)
    else:
        mode = judge(current_action)
    x.append(x[t] + mode.choice)
        
ax.plot(x, 'r-')
plt.show()