# NOTE first steps of creating an alghoritm
import numpy as np

# initialize array for calculations
idx = input("How much steps?: ")
array = np.zeros((4, int(idx)))
array[1, 1] *= 5


def drag(rho, cd, V, S):
    '''Calculate drag'''
    return 0.5*rho*cd*(V**2)*S


D = drag(1.225, 0.1, 10, 2)


def first_column():
    None


def nth_column():
    None


print(array)
