#Levi Peachey-Stoner
#Fall 2021

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3.1415,3.1415,1000)

y = np.sin(5*x)+np.cos(11*x)


fig = plt.figure()
ax = fig.add_subplot(1, 3, 1)
plt.title('Y(t) = sin(5t)+cos(11t)')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'r')

ax = fig.add_subplot(1, 3, 2)
plt.title('0.05 Second Moving Average Window')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

def runningmean(m, N):
    cumsum = np.cumsum(np.insert(m, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

xx = runningmean(x,50)
yy = runningmean(y,50)

plt.plot(xx,yy, 'b')

ax = fig.add_subplot(1, 3, 3)
plt.title('0.1 Second Moving Average Window')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

xx = runningmean(x,100)
yy = runningmean(y,100)

plt.plot(xx,yy, 'g')


plt.show()
