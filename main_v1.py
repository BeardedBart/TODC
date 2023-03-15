# NOTE first steps of creating an alghoritm
import numpy as np
import json

# initialize array for calculations
array = np.zeros((4, 2))


def load_config():
    initData = dict()
    with open('config.json', 'r', encoding='utf-8') as f:
        initData = json.load(f)

    T = list(initData['thrust'])
    V = float(initData['stall_speed']) * 1.1
    S = float(initData['wing_area'])
    M = float(initData['mass'])
    CD = float(initData['aerodynamic_drag_coeff'])
    WD = float(initData['wheel_drag'])
    return T, V, CD, WD, S, M


def drag(rho, cd, V, S):
    '''Calculate drag'''
    return 0.5*rho*cd*(V**2)*S


def first_column():
    None


def nth_column():
    None


if __name__ == '__main__':
    data = load_config()
    d = drag(1.225, data[2], data[1], data[4])
    print(d)
