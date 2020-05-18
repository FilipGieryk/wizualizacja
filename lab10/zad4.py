import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,30,0.1)
s = np.sin(x)
c= np.cos(x)

plt.plot(x,s+2,'-b', label = 'sin(x)')
plt.plot (x,-s,'-',color='orange', label= 'cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x), sin(x)')
plt.legend(loc=6)
plt.show()