import numpy as np
from math import sin, pi, radians, ceil, cos


def ramp(n, t, m):
    output = []
    for i in range(0, ceil((n) / 2)):
        value = 0
        if i == 0:
            value = t
        elif i % 2 == 0:
            value = 0
        elif i % 2 != 0:
            value = -1 / ((i * pi * m) ** 2)
        output.append(value)
    test = output[::-1]
    test = test[0:len(test) - 1]
    app = np.append(test, output)
    return app


def ramp2(n):
    output = []
    for i in range(0, ceil((n) / 2)):
        value = 0
        if i == 0:
            value = 1
        elif i % 2 == 0:
            value = 0
        elif i % 2 != 0:
            value = ((- 4) / (pi ** 2)) / (i ** 2)
        output.append(value)
    test = output[::-1]
    test = test[0:len(test) - 1]
    app = np.append(test, output)
    return app


def ram_lak(n, T):
    output = []
    for i in np.linspace(0.1, 2, 50):
        x = ((sin(T * i) / T * i) + (cos(T * i) - 1) / ((T * i) ** 2))
        output.append(((T ** 2) / 4 * pi ** 2) * x)
    return output


def shepp_logan(n, F):
    output = []
    for i in np.linspace(0.1, 2, 50):
        upper = 2 * F
        lower = pi * (sin(i) * pi / 2 * F)
        output.append(upper / lower)
    return output


def filter_sinogram(sinogram):
    filtered_sinogram = np.zeros(sinogram.shape)
    n = sinogram.shape[0]
    ramp_filter = ramp2(n/2)
    for i, column in enumerate(sinogram.T):
        conv = np.convolve(column, ramp_filter, mode="same")
        filtered_sinogram[:, i] = conv
    min = filtered_sinogram.min()
    filtered_sinogram = filtered_sinogram[:,:] + abs(min)
    max = filtered_sinogram.max()
    filtered_sinogram = filtered_sinogram[:, :] * 1 / max
    return filtered_sinogram
