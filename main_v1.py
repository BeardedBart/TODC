# NOTE first steps of creating an alghoritm
import numpy as np
import json

stages = int()


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
    '''Calculate drag of wheels on the take-off'''
    return WD*(M/1000)


def speed_data(V, stages):
    speeds = np.linspace(0, V, int(stages)+1)
    # add mean value at stage feature
    i, mean_s = 0, []
    while not i == len(speeds) - 1:
        val = (speeds[i] + speeds[i+1])/2
        mean_s += val
        print(val)
        i += 1
    return speeds, mean_s


def first_stage():
    None


def nth_stage():
    None


if __name__ == '__main__':
    stages = input("How many stages? ")
    data = load_config()
    speeds = speed_data(data[1], stages)
    print(speeds)
