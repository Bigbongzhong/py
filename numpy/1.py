import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[3,4,5],[6,7,8]]])
arr1=np.array([[[3,2,1],[6,4,5],[7,8,9]],[[2,1,3],[3,4,5],[8,7,4]]])
print(arr)
plt.plot(arr[0][0],arr[0][1],arr[0][2], label="1st")
plt.plot(arr1[0][1],arr1[1][1],arr1[1][2], label="2nd")
plt.legend()
plt.title("3D plot")
plt.show()
d=np.arange(9).reshape(3,3)
print(d)
for i in np.nditer(arr):
    print(i,end=" ")
print()
c=np.hstack((arr,arr1))
print(c)