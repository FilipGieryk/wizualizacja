import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot( 111 , projection = '3d' )
n = 10

for c, m, in [( 'r' , 'o'),('g', '^'),('b','<'),('c','>'),('k','1')]:
    xs = randrange(n, 0 , 50 )
    ys = randrange(n, 0 , 50 )
    zs = randrange(n, 0, 50)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()