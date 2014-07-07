import matplotlib.pyplot as plt
import numpy as np
from random import uniform
fig, ax = plt.subplots()

A = ( (4, 0), 
      (3, 2) ) #利得行列
N = 20
T = 10000

epsilon = 0.2

x = [0.0]

for t in range(T):
    if x[t] / N > uniform(0, 1): #true=行動を選べる人が今時点で行動「１」を取っていた.
        if epsilon > uniform(0, 1): #true=突然変異モード,false=通常の利得判定モード
            if 0.5 > uniform(0, 1):
                x.append(x[t])
            else:
                x.append(x[t] - 1)
        else:
            x.append(x[t] - 1 + (np.dot(A, (N - x[t], x[t] - 1))).argmax()) #利得判定：利得が同じ場合は若い番号の行動を採用
    else:                        #false=行動を選べる人が今時点で行動「０」を取っていた.
        if epsilon > uniform(0, 1):
            if 0.5 > uniform(0, 1):
                x.append(x[t])
            else:
                x.append(x[t] + 1)
        else:
            x.append(x[t] + (np.dot(A, (N - x[t] - 1, x[t]))).argmax())
ax.plot(x, 'r-')
plt.show()
        
            

