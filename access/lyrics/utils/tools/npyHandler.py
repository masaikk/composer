import numpy as np


def approximate(d):
    unit = 0.25
    flag = True
    if d < 0:
        flag = False
        d = -d
    quotient = int(d / unit)
    remainder = d % unit

    if flag:
        if remainder < unit / 2:
            return unit * quotient
        else:
            return unit * (quotient + 1)
    else:
        if remainder < unit / 2:
            return -(unit * quotient)
        else:
            return -(unit * (quotient + 1))


def pre_process_data(data):
    # data = np.load(path, allow_pickle=True)
    # 暂时将处理使用np.abs()

    data_T = data.T
    data_T[3] = np.abs(np.round(data_T[3]))
    data_T[5] = np.abs(np.round(data_T[5]))

    for pitch in range(0, len(data_T[4])):
        for sentence in range(0, len(data_T[4][pitch])):
            data_T[4][pitch][sentence] = approximate(data_T[4][pitch][sentence])

    data = data_T.T
    return data


