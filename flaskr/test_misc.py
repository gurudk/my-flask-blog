import numpy as np
import time

import matplotlib.cm
print(matplotlib.cm.cmap_d.keys())

dict = {}
arr = np.zeros((100, 2))
arr[0, 0] = 1
print(arr)
print(arr.size)
print(time.time())


