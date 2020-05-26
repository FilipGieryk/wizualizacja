import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure( figsize =( 8 , 3 ))
ax1 = plt.gca (projection = '3d' )

_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top,color = 'g', shade = True,alpha = 0.2,edgecolor = 'r',zsort = 'average')
ax1.set_title('Wykres zacieniony')
plt.show()