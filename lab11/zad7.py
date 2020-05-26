# Projekcja 3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.gca(projection ='3d')
z = np.linspace(0,5 , 5)
x = np.sin(z)
y = np.cos(z)
ax.plot(x, y, z, 'g')

z1 = 5 * np.random.random(20)
x1 = np.cos(z1)
y1 = np.cos(z1)
ax.scatter(x1,y1,z1, color= 'r')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()