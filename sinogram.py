import numpy as np
from functools import reduce
from math import sin, pi, radians


class Sinogram:
    def __init__(self, angle_count, emiter_count):
        self.img = np.zeros((emiter_count, angle_count))

    def weakness_function(self, value):
        if value > 0:
            return 1

    def radon_value(self, angle, emiter_no, ray_values):
        value = reduce((lambda x, y: x + y), ray_values)
        self.img[emiter_no, angle] = value


