import numpy as np
a=np.arange(2,11).reshape(3,3)
print(a.min(axis=1))
print(a.min(axis=0))
b=np.arange(5,21).reshape(4,4)
print(b.min(axis=1))
print(b.min(axis=0))