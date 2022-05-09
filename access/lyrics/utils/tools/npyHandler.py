import numpy as np


def approximate(d):
    unit = 0.5
    # 将音节长度的最小单元由0.25改成0.5
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
    # data_T[5] = np.round(data_T[5])

    # 更改处理休止符的代码
    for i in range(20):
        for j in range(data_T[5][i].shape[0]):
            if data_T[5][i][j] < 1.0:
                data_T[5][i][j] = 0
            elif data_T[5][i][j] < 1.8:
                data_T[5][i][j] = 1
            else:
                data_T[5][i][j] = np.round(data_T[5][i][j])

    for pitch in range(0, len(data_T[4])):
        for sentence in range(0, len(data_T[4][pitch])):
            data_T[4][pitch][sentence] = approximate(data_T[4][pitch][sentence])

    data = data_T.T
    return data


