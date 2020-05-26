import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

fig=plt.figure()
ax = fig.add_subplot(121,projection='3d')
z1 = 5 * np.random.random(20)
x1 = np.cos(z1)
y1 = np.cos(z1)
ax.scatter(x1,y1,z1, color= 'r')


ax = fig.add_subplot(122, projection='3d')

z = np.linspace(0,5 , 5)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, 'g')




plt.show()