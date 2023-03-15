# NOTE first steps of creating an alghoritm
import numpy as np

idx = input("How much steps?: ")

array = np.zeros((4, int(idx)))
array[1, 1] = 1
print(array)
