import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,19,20)

plt.plot(x,1/x, linestyle='dotted',marker = '>',color='g',markersize=5, label='f(x)=1/x')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) dla x [1, 20]')
plt.legend()
plt.axis([0,20,0,1])
plt.show()