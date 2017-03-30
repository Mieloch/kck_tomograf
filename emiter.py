from math import floor, sqrt, ceil, sin, cos, radians
import numpy as np
import copy


class Emiter:
    def __init__(self, s_x, s_y, e_x, e_y):
        self.s_x = int(s_x)
        self.s_y = int(s_y)
        self.e_x = int(e_x)
        self.e_y = int(e_y)


class EmiterFrame:
    emiters = []

    def __init__(self, working_space, emitersCount):
        self.size = int(round(working_space.source_d() * 1.25, 0))
        center_x, center_y = working_space.center_x_y()
        self.center_x = center_x
        self.center_y = center_y
        if emitersCount is None:
            self.emitersCount = self.size
        else:
            self.emitersCount = emitersCount
        self.__set_up_ermiters()

    def with_angle(self, angle):
        # print("rotate emiters. Angle = ", angle, "Point= ", self.center_x, ", ", self.center_y)
        theta = radians(angle)
        emiters_copy = self.__copy_emiters()
        for emiter in emiters_copy:
            self.rotate_emiter(emiter, theta)
            # print("x= ", emiter.s_x, "y = ", emiter.s_y)
        return emiters_copy

    def rotate_emiter(self, emiter, theta):

        s_x, s_y = self.rotate_point(emiter.s_x, emiter.s_y, theta)
        emiter.s_x = int((round(s_x, 0)))
        emiter.s_y = int((round(s_y, 0)))
        e_x, e_y = self.rotate_point(emiter.e_x, emiter.e_y, theta)
        emiter.e_x = int((round(e_x, 0)))
        emiter.e_y = int((round(e_y, 0)))

    def rotate_point(self, x, y, theta):
        f = cos(theta)
        sin1 = sin(theta)
        px = f * (x - self.center_x) - sin1 * (y - self.center_y) + self.center_x
        py = sin1 * (x - self.center_x) + f * (y - self.center_y) + self.center_y
        return px, py

    def get(self):
        return self.emiters

    def __copy_emiters(self):
        result = []
        for emiter in self.emiters:
            result.append(copy.copy(emiter))
        return result;

    def __set_up_ermiters(self):
        print("set up emiters")
        s_y = int(round(self.center_y + self.size / 2, 0))
        s_x = int(round(self.center_x - self.size / 2, 0))
        e_x = s_x
        e_y = s_y - self.size
        stop_x = int(round(self.center_x + self.size / 2, 0))
        emiters_s_x = np.linspace(s_x, stop_x, self.emitersCount)
        for i in emiters_s_x:
            emiter = Emiter(s_x, s_y, e_x, e_y)
            s_x = int(round(i, 0))
            e_x = s_x
            # print("s_x= ", emiter.s_x, "s_y = ", emiter.s_y,"e_x= ", emiter.e_x, "e_y = ", emiter.e_y)
            self.emiters.append(emiter)
