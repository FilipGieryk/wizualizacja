import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris.data', names=['sepal length','sepal width','1','2','3'])
c=np.random.randint(0,50,150)

x = df['sepal length']
y = df['sepal width']
s=abs(x-y)
print(s)
plt.scatter(x, y, c=c,s=s)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()