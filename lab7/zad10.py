import numpy as np

a = np.arange(81).reshape(9,9)
print ("1\n\n",a)
b=a.reshape(27,3)
print("2\n\n",b)
c=a.reshape(3,27)
print("3\n\n",c)
d=a.reshape(81,1)
print("4\n\n",d)
e=a.reshape(1,81)
print("5\n\n",e)
#mamy tylko tak mozlliwosc z powodu array size
#cannot reshape array of size 81 into shape (8,8)