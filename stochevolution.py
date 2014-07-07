import matplotlib.pyplot as plt
import numpy as np
from random import uniform
fig, ax = plt.subplots()

class random: #変異モードの行動変化
    def __init__(self, current_action):
        if current_action == 0:
            self.choice = (0.5 < uniform(0, 1)) * 1.0 + (0.5 >= uniform(0, 1)) * 0.0
        elif current_action == 1:
            self.choice = (0.5 < uniform(0, 1)) * (-1.0) + (0.5 >= uniform(0, 1)) * 0.0
        else:
            self.choice = 0.0

class judge: #通常の利得判断モードの行動変化
    def __init__(self, current_action):
        if current_action == 0:
            self.choice = (np.dot(A, (N - x[t] - 1, x[t]))).argmax()
        elif current_action == 1:
            self.choice = -1.0 + (np.dot(A, (N - x[t] - 1, x[t]))).argmax()
        else:
            self.choice = 0.0
            
A = ( (4, 0), 
      (3, 2) ) #利得行列
N = 20
T = 10000

epsilon = 0.2

x = [0.0]

for t in range(T):
    current_action = x[t] / N > uniform(0, 1) #2x2の場合は行動が０か１なので、falseとtrueに対応させる。3x3にしたときはここを直す。
    
    if epsilon > uniform(0, 1): #trueだとrandom(変異モード）,falseだとjudge(通常の利得判断モード)。
        mode = random(current_action)
    else:
        mode = judge(current_action)
    x.append(x[t] + mode.choice)
        
ax.plot(x, 'r-')
plt.show()