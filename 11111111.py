import numpy as np
a = np.array([[1,2,3]])
b = np.array([[5,6,7]])
new_=np.vstack((a, b))
print(np.transpose(new_))