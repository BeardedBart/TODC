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
    WD = float(initData['wheel_drag'])*(M/1000)
    return T, V, CD, WD, S, M


def drag(cd, V, S, rho=1.2255):
    '''Calculate drag'''
    return 0.5*rho*cd*(V**2)*S


def thrust_corr(T):
    '''Thrust correction'''
    if len(T) == 1:
        return T
    else:
        i = 0
        mean_T = []
        while not i == len(T) - 1:
            val = (float(T[i]) + float(T[i+1]))/2
            mean_T.append(val)
            i += 1
        return mean_T


def true_force(thrust, drag, wheel_drag):  # możliwe że do wywalenia
    return thrust - drag - wheel_drag


def speed_data(V, stages):
    speeds = np.linspace(0, V, int(stages)+1)
    # add mean value at stage feature
    i, mean_s = 0, []
    while not i == len(speeds) - 1:
        val = (speeds[i] + speeds[i+1])/2
        mean_s.append(val)
        i += 1
    print(speeds, mean_s)
    return speeds, mean_s


# Alpha version
def first_stage(data, stage=1):
    T = data[0]
    V = data[1]
    CD = data[2]
    WD = data[3]
    S = data[4]
    M = data[5]
    speeds, mean_s = speed_data(V, stage)
    thrust = thrust_corr(T)
    dg = drag(CD, mean_s[0], S)
    print(dg)

    # true force NOTE: do not misunderstand with feets
    ft = true_force(thrust[0], dg, WD)
    print(ft)

    acc = ft/M      # accelereation
    t = mean_s/acc  # time
    x = (acc * (t**2))/2
    print(acc, t, x)
    return x


def nth_stage():
    """Not yet implemented"""
    None


if __name__ == '__main__':
    stages = input("How many stages? ")
    data = load_config()
    print(first_stage(data))
