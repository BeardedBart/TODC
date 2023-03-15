# NOTE first steps of creating an alghoritm
import numpy as np
import json

# initialize array for calculations
stages = input("How many stages? ")
# array = np.zeros((4, stages))


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


def wheel_drag(WD, M):
    return WD*(M/1000)


def speed(V, stages):
    speeds = np.linspace(0, V, stages)
    return speeds


def first_stage():
    None


def nth_stage():
    None


if __name__ == '__main__':
    data = load_config()
    d = drag(1.225, data[2], data[1], data[4])
    print(d)
